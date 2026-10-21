#!/usr/bin/env python3
"""Compile a typed scientific table to LaTeX/PDF/PNG plus semantic HTML and CSV.

Requires pdflatex with standalone, lmodern, booktabs, array, dcolumn, xcolor
and colortbl; Python requires PyMuPDF. Does not shrink the artwork.
The generated fragment inherits a manuscript's typeface; the standalone preview
uses Latin Modern. Review the actual manuscript placement after integration.
"""
from __future__ import annotations
import argparse
import csv
import html
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

from table_core import FAILURES, MISSING, STATUS, decimal, display_cell, emphasis, formatted, number, precision, rounded, sha256, validate, write_json


def tex(value):
    mapping = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
               "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
               "↑": r"\ensuremath{\uparrow}", "↓": r"\ensuremath{\downarrow}", "±": r"\ensuremath{\pm}",
               "−": r"\ensuremath{-}", "–": "--", "—": "---", "≤": r"\ensuremath{\leq}", "≥": r"\ensuremath{\geq}",
               "×": r"\ensuremath{\times}", "→": r"\ensuremath{\rightarrow}", "·": r"\ensuremath{\cdot}",
               "Δ": r"\ensuremath{\Delta}", "μ": r"\ensuremath{\mu}", "µ": r"\ensuremath{\mu}",
               "σ": r"\ensuremath{\sigma}", "α": r"\ensuremath{\alpha}", "β": r"\ensuremath{\beta}",
               # raised marks at a fixed 6.2 pt: \textsuperscript at 8-9 pt body falls to ~5.5 pt
               "²": r"\raisebox{0.6ex}{\fontsize{6.2}{6.2}\selectfont 2}", "†": r"\raisebox{0.6ex}{\fontsize{6.2}{6.2}\selectfont\dag}",
               "‡": r"\raisebox{0.6ex}{\fontsize{6.2}{6.2}\selectfont\ddag}",
               "✓": r"\ding{51}", "✗": r"\textcolor{TableMuted}{\ding{55}}", "◐": r"\ensuremath{\sim}"}
    return "".join(mapping.get(c, c) for c in str(value))


MISSING_WORDS = {"not_reported": "not reported", "not_applicable": "not applicable", "not_run": "not run",
                 "incomparable": "not comparable"}


def notes(spec):
    """Notes travel with the table: data status first, then definitions, then the emphasis legend."""
    result = []
    if spec["data_status"] in {"synthetic", "illustrative", "schematic"}:
        result.append(spec["data_status"].capitalize() + " data.")
    result += list(spec["notes"])
    if spec.get("ranking", {}).get("axis", "none") != "none":
        result.append(spec["ranking"]["meaning"])
    if spec.get("focus_meaning"):
        result.append(spec["focus_meaning"])
    seen_missing, seen_failures, seen_status = set(), set(), set()
    status_cols = {c["id"] for c in spec["columns"] if c["kind"] == "status"}
    for row in spec["rows"]:
        for cid, cell in row["cells"].items():
            if isinstance(cell, dict):
                if "missing" in cell: seen_missing.add(cell["missing"])
                if "failure" in cell: seen_failures.add(cell["failure"])
            elif cid in status_cols:
                seen_status.add(cell)
    if seen_missing:
        if spec.get("missing_style") == "dash":
            result.append("– = " + MISSING_WORDS[next(iter(seen_missing))] + ".")
        else:
            result.append("; ".join(f"{MISSING[k]} = {MISSING_WORDS[k]}" for k in sorted(seen_missing)) + ".")
    if seen_failures:
        descriptions = {'oom': 'out of memory', 'timeout': 'timeout', 'execution_error': 'execution error'}
        result.append("; ".join(f"{FAILURES[k]} = {descriptions[k]}" for k in sorted(seen_failures)) + " (an outcome, not a score of zero).")
    if seen_status and spec.get("status_style", "symbols") == "symbols":
        words = {"yes": "✓ enabled", "no": "✗ disabled", "partial": "◐ partial", "unknown": "? unknown"}
        result.append(", ".join(words[k] for k in ("yes", "no", "partial", "unknown") if k in seen_status) + ".")
    return result


def column_format(spec, col):
    if col["kind"] == "text":
        align = {"l": r"\raggedright", "r": r"\raggedleft", "c": r"\centering"}[col.get("align", "l")]
        return ">{" + align + r"\arraybackslash}p{" + str(col["width_mm"]) + "mm}"
    if col["kind"] == "number" and col.get("format") != "sci":
        values = [display_cell(col, row, row["cells"][col["id"]], spec) for row in spec["rows"]
                  if isinstance(row["cells"][col["id"]], dict) and "value" in row["cells"][col["id"]] and not row.get("delta")]
        digits = {precision(col, r, r["cells"][col["id"]]) for r in spec["rows"]
                  if isinstance(r["cells"][col["id"]], dict) and "value" in r["cells"][col["id"]] and not r.get("delta")}
        if len({len(v) for v in values}) <= 1 and len(digits) <= 1:
            # equal-width numbers at one precision are already decimal-aligned when centred
            # (tabular lining figures), and centring keeps underlines and bold intact
            return "c"
        before = max([len(x.split(".")[0].replace(",", "")) + x.split(".")[0].count(",") for x in values] + [1])
        after = max([precision(col, row, row["cells"][col["id"]]) for row in spec["rows"]
                     if isinstance(row["cells"][col["id"]], dict) and "value" in row["cells"][col["id"]]] + [0])
        # The extra fractional slot accommodates bold digits without moving the
        # decimal anchor or reducing text size. It is spacing, not extra precision.
        return f"D{{.}}{{\\CSPdot}}{{{before}.{after+1 if after else 0}}}"
    return "c"


def math_number(text):
    """Display string -> math-mode TeX: true minus, grouped thousands, a·10^n."""
    text = text.replace("−", "-").replace(",", "{,}")
    if "·10^" in text:
        mant, exp = text.split("·10^")
        text = mant + r"\cdot 10^{" + exp + "}"
    return text


def numeric_tex(text, bold, under=False):
    # dcolumn splits the cell at "." so every wrapper is applied per side of the point
    parts = math_number(text).split(".")
    if bold:
        parts = [r"\mathbf{" + p + "}" for p in parts]
    if under:
        parts = [r"\underline{" + p + "}" for p in parts]
    if (bold or under) and len(parts) == 2:
        # dcolumn boxes the left half first, so it can switch the separator to a bold/underlined
        # point and the right half switches it back: the point matches the digits around it
        dot = r"\mathbf{.}" if bold else "."
        dot = r"\underline{" + dot + "}" if under else dot
        parts = [r"\gdef\CSPdot{" + dot + "}" + parts[0], parts[1] + r"\gdef\CSPdot{.}"]
    return ".".join(parts)


def cell_tex(spec, col, row, bold, under=False):
    cell = row["cells"][col["id"]]
    if isinstance(cell, dict) and cell.get("spanned"):
        return None
    text = display_cell(col, row, cell, spec)
    if isinstance(cell, dict) and ("missing" in cell or "failure" in cell):
        mark = tex(text) if text == "–" else r"\textit{" + tex(text) + "}"
        return r"\multicolumn{1}{c}{\textcolor{TableMuted}{" + mark + "}}"
    if row.get("delta") and col["kind"] in {"number", "mean_sd", "interval"}:
        # Change rows: colour follows the column's direction (better = green, worse = red);
        # the sign carries the same meaning in greyscale.
        value = decimal(cell["value"])
        good = (value > 0) if col.get("direction") == "max" else (value < 0) if col.get("direction") == "min" else None
        shade = "DeltaUp" if good and rounded(value, precision(col, row, cell)) != 0 else "DeltaDown" if good is False and rounded(value, precision(col, row, cell)) != 0 else "TableMuted"
        content = r"\textcolor{" + shade + "}{$" + math_number(text) + "$}"
        return r"\multicolumn{1}{c}{" + content + "}"
    if col["kind"] == "number":
        content = numeric_tex(text, bold, under)
        if column_format(spec, col) == "c":
            whole = math_number(text)
            whole = r"\mathbf{" + whole + "}" if bold else whole
            content = "$" + (r"\underline{" + whole + "}" if under else whole) + "$"
        if isinstance(cell, dict) and cell.get("span"):
            return r"\multicolumn{" + str(cell["span"]) + "}{c}{$" + numeric_tex(text, bold, under) + "$}"
        return content
    if col["kind"] in {"mean_sd", "interval"}:
        # Compound estimates retain an explicit separator/interval convention.
        # No uncertainty notation is guessed from a parenthetical number.
        digits = precision(col, row, cell)
        lead = math_number(formatted(col, cell['value'], digits, col.get('signed', False)))
        lead = r"\mathbf{" + lead + "}" if bold else lead
        lead = r"\underline{" + lead + "}" if under else lead
        if col['kind'] == 'mean_sd' and col.get("sd_style") == "paren":
            return r"$" + lead + r"$\,{\CSPsmall\textcolor{TableMuted}{(" + number(cell['sd'], digits) + ")}}"
        if col['kind'] == 'mean_sd':
            return r"$" + lead + r"$\,{\CSPsmall$\pm$" + number(cell['sd'], digits) + "}"
        interval = "[" + math_number(number(cell['low'], digits, col.get('signed', False))) + r",\," + math_number(number(cell['high'], digits, col.get('signed', False))) + "]"
        return r"$" + lead + r"$\,{\CSPsmall$" + interval + "$}"
    if col["kind"] == "status":
        return tex(text)
    return tex(text).replace("\n", r"\newline ")


def header_tex(label, bold):
    """First line is the name; further lines (n, unit, direction) are set smaller and muted."""
    lines = label if isinstance(label, list) else str(label).split("\n")
    head = (r"\textbf{" + tex(lines[0]) + "}") if bold else tex(lines[0])
    rest = [r"{\CSPsmall\textcolor{TableMuted}{" + tex(x) + "}}" for x in lines[1:]]
    return r"\shortstack{" + r"\\[-0.15ex] ".join([head] + rest) + "}"


def make_latex(spec, marked, second=frozenset()):
    style = spec["style"]
    cols, rows = spec["columns"], spec["rows"]
    n = len(cols)
    ids = [c["id"] for c in cols]
    groups = spec.get("column_groups", [])
    starts = {ids.index(g["columns"][0]): g for g in groups}
    bold_head = style.get("header_weight", "bold") == "bold"
    setup = [r"\begingroup", r"\fontsize{" + str(style["body_pt"]) + "}{" + str(style.get("leading_pt", style["body_pt"]*1.25)) + r"}\selectfont",
             r"\setlength{\tabcolsep}{" + str(style.get("tabcolsep_pt", 4.0)) + "pt}",
             r"\renewcommand{\arraystretch}{" + str(style.get("arraystretch", 1.2)) + "}",
             # booktabs' own em-based weights, so rules scale with the type (0.8/0.5/0.3 pt at 10 pt)
             r"\setlength{\heavyrulewidth}{.08em}\setlength{\lightrulewidth}{.05em}\setlength{\cmidrulewidth}{.03em}",
             r"\arrayrulecolor{TableRule}", r"\gdef\CSPdot{.}",
             # secondary text (units under headers, SDs, intervals): ~0.86 of body, never below the 7.2 pt floor
             r"\def\CSPsmall{\fontsize{" + str(max(7.2, round(style["body_pt"] * 0.86, 2))) + "}{" + str(max(7.2, round(style["body_pt"] * 0.86, 2)) * 1.1) + r"}\selectfont}"]
    colspec = "".join((r">{\columncolor{FocusFill}}" if c.get("focus") else "") + column_format(spec, c) for c in cols)
    parts = [r"\toprule"]
    if groups:
        cells, i = [], 0
        while i < n:
            if i in starts:
                g = starts[i]; count = len(g["columns"])
                label = r"\textbf{" + tex(g["label"]) + "}" if bold_head else tex(g["label"])
                cells.append(r"\multicolumn{" + str(count) + r"}{c}{" + label + "}")
                i += count
            else:
                cells.append(r"\multicolumn{1}{c}{}")
                i += 1
        parts.append(" & ".join(cells) + r" \\")
        parts.append("".join(r"\cmidrule(lr){" + str(ids.index(g["columns"][0])+1) + "-" + str(ids.index(g["columns"][-1])+1) + "}" for g in groups))
    parts.append(" & ".join(r"\multicolumn{1}{" + ("l" if c["kind"] == "text" and c.get("align", "l") == "l" else "c") + "}{" + header_tex(c["label"], bold_head) + "}" for c in cols) + r" \\")
    parts.append(r"\midrule")
    previous = None
    labels = spec.get("row_group_labels", {})
    banner = style.get("group_style", "banner") == "banner"
    for k, row in enumerate(rows):
        group = row.get("display_group")
        if group != previous and group is not None:
            if previous is not None:
                parts.append(r"\midrule")
            label = labels.get(group, group)
            if not label:
                previous = group
            elif banner:
                parts.append(r"\multicolumn{" + str(n) + r"}{c}{\textit{" + tex(label) + r"}}\\[0.15ex]")
            else:
                parts.append(r"\multicolumn{" + str(n) + r"}{@{}l}{\textit{" + tex(label) + r"}}\\[0.15ex]")
            previous = group
        if row.get("space_before"):
            parts.append(r"\addlinespace[0.6ex]")
        if row.get("rule_before"):
            parts.append(r"\cmidrule(lr){1-" + str(n) + "}")
        if row.get("focus") or (row.get("delta") and style.get("tint_delta_rows", False)):
            parts.append(r"\rowcolor{" + ("FocusFill" if row.get("focus") else "DeltaFill") + "}")
        cells = [cell_tex(spec, c, row, (row['id'], c['id']) in marked, (row['id'], c['id']) in second) for c in cols]
        parts.append(" & ".join(x for x in cells if x is not None) + r" \\")
    parts += [r"\bottomrule"]
    # Natural width by default (top-lab tables keep columns close so groups read as groups);
    # style.fill = true distributes spare width through tabcolsep, never by scaling the type.
    rows_tex = "\n".join(parts)
    measure = r"\sbox{\CSPTableMeasure}{\begin{tabular}{" + colspec + r"}\CSPTableRows\end{tabular}}"
    parts = setup + [r"\ifdefined\CSPTableMeasure\else\newsavebox{\CSPTableMeasure}\fi",
                    r"\def\CSPTableRows{" + rows_tex + "}",
                    measure,
                    r"\ifdim\wd\CSPTableMeasure>\linewidth\PackageError{cs-paper-table}{Table is wider than the target; recompose it}{Split columns, shorten headers, or choose a wider placement. Do not scale down.}\fi"]
    if style.get("fill", False):
        for _ in range(12):
            parts += [r"\setlength{\tabcolsep}{\dimexpr\tabcolsep+(\linewidth-\wd\CSPTableMeasure)/" + str(2*n) + r"\relax}", measure]
    note_text = " ".join(tex(x) for x in notes(spec))
    parts += [r"\noindent\hfill\usebox{\CSPTableMeasure}\hfill\null", r"\par\vspace{1.4mm}",
              r"{\fontsize{" + str(style["note_pt"]) + "}{" + str(style["note_pt"]*1.25) + r"}\selectfont\noindent\textcolor{TableNote}{" + note_text + r"}\par}", r"\endgroup"]
    fragment = "\n".join(parts) + "\n"
    caption = r"\textbf{Table " + str(spec.get("number", 1)) + ". " + tex(spec["title"]) + ".} " + tex(spec["caption"])
    font = {"times": r"\usepackage{newtxtext,newtxmath}", "lmodern": r"\usepackage{lmodern}"}[style.get("font", "times")]
    preamble = r"""\documentclass[border=0pt]{standalone}
\usepackage[T1]{fontenc}
""" + font + r"""
\usepackage{booktabs,array,dcolumn,pifont}
\usepackage[table]{xcolor}
\definecolor{TableRule}{HTML}{000000}
\definecolor{TableMuted}{HTML}{6B7280}
\definecolor{TableNote}{HTML}{374151}
\definecolor{FocusFill}{HTML}{""" + style.get("focus_fill", "EEF3FA") + r"""}
\definecolor{DeltaFill}{HTML}{F6F7F9}
\definecolor{DeltaUp}{HTML}{408C40}
\definecolor{DeltaDown}{HTML}{8C4040}
\begin{document}
"""
    standalone = preamble + r"\begin{minipage}{" + str(style["width_mm"]) + "mm}\n" + r"\vspace*{1mm}" + "\n" + r"\fontsize{" + str(style.get("caption_pt", 9.0)) + "}{" + str(style.get("caption_pt", 9.0)*1.22) + r"}\selectfont" + "\n" + caption + r"\par\vspace{1.6mm}" + "\n" + fragment + r"\vspace*{1mm}\end{minipage}" + "\n" + r"\end{document}" + "\n"
    return standalone, fragment, caption


def make_html(spec, marked):
    e = html.escape
    cols = spec["columns"]
    ids = [c['id'] for c in cols]
    groups = spec.get('column_groups', [])
    prefix = spec['id'] + '-'
    group_for = {cid: prefix+'cg-'+str(i) for i,g in enumerate(groups) for cid in g['columns']}
    header_for = {cid: prefix+'ch-'+str(i) for i,cid in enumerate(ids)}
    starts = {ids.index(g['columns'][0]): (i,g) for i,g in enumerate(groups)}
    parts = ['<!doctype html><html lang="en"><meta charset="utf-8"><title>'+e(spec["title"])+'</title>',
             '<style>body{font-family:"Times New Roman",Georgia,serif;color:#111;margin:2rem auto;max-width:1050px;line-height:1.35}table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums;border-top:1.5px solid #000;border-bottom:1.5px solid #000}caption{text-align:left;margin-bottom:1rem}th,td{padding:.36rem .5rem}thead{border-bottom:1px solid #000}th{text-align:center}td{text-align:right}td.text,th.row{text-align:left}th.row{font-weight:normal}tr.group th{text-align:center;font-weight:normal;font-style:italic;border-top:1px solid #000;padding-top:.5rem}tr.focus{background:#eef3fa}.notes{font-size:.88rem}.status{text-align:center}.num{white-space:nowrap}@media print{body{max-width:none;margin:0}thead{display:table-header-group}tr{break-inside:avoid}}</style>',
             '<table aria-describedby="'+prefix+'notes"><caption><strong>Table '+str(spec.get("number",1))+'. '+e(spec["title"])+'.</strong> '+e(spec["caption"])+ '</caption>']
    i = 0
    while i < len(cols):
        count = len(starts[i][1]['columns']) if i in starts else 1
        parts.append('<colgroup span="'+str(count)+'"></colgroup>')
        i += count
    parts.append('<thead>')
    if groups:
        parts.append('<tr>'); i=0
        while i<len(cols):
            if i in starts:
                gi,g=starts[i]; parts.append('<th scope="colgroup" id="'+prefix+'cg-'+str(gi)+'" colspan="'+str(len(g["columns"]))+'">'+e(g["label"])+'</th>'); i+=len(g["columns"])
            else: parts.append('<th></th>'); i+=1
        parts.append('</tr>')
    parts.append('<tr>'+''.join('<th scope="col" id="'+header_for[c['id']]+'"'+(' headers="'+group_for[c['id']]+'"' if c['id'] in group_for else '')+'>'+('<br>'.join(e(x) for x in c["label"]) if isinstance(c["label"],list) else e(c["label"]).replace('\n','<br>'))+'</th>' for c in cols)+'</tr></thead>')
    previous=None; rowgroup_header=None
    for ri,row in enumerate(spec["rows"]):
        group=row.get("display_group")
        if ri == 0 or group != previous:
            if ri: parts.append('</tbody>')
            parts.append('<tbody>')
            rowgroup_header = prefix+'rg-'+str(ri) if group is not None else None
            if group is not None:
                parts.append('<tr class="group"><th scope="rowgroup" id="'+rowgroup_header+'" colspan="'+str(len(cols))+'">'+e(spec.get("row_group_labels",{}).get(group,group))+'</th></tr>')
            previous=group
        row_header=prefix+'rh-'+str(ri)
        parts.append('<tr'+(' class="focus"' if row.get("focus") else '')+'>')
        for i,col in enumerate(cols):
            cell=row["cells"][col["id"]]
            if isinstance(cell,dict) and cell.get('spanned'): continue
            value=e(display_cell(col,row,cell,spec)).replace('\n','<br>')
            if (row["id"],col["id"]) in marked: value='<strong>'+value+'</strong>'
            span=' colspan="'+str(cell['span'])+'"' if isinstance(cell,dict) and cell.get('span') else ''
            tag='th' if i==0 else 'td'
            cls='row' if i==0 else 'text' if col["kind"]=='text' else 'status' if col["kind"]=='status' else 'num'
            associated=[header_for[col['id']]]
            if col['id'] in group_for: associated.insert(0,group_for[col['id']])
            if rowgroup_header: associated.append(rowgroup_header)
            if i: associated.append(row_header)
            parts.append('<'+tag+span+' class="'+cls+'"'+(' scope="row" id="'+row_header+'"' if i==0 else '')+' headers="'+' '.join(associated)+'">'+value+'</'+tag+'>')
        parts.append('</tr>')
    parts.append('</tbody></table><p class="notes" id="'+prefix+'notes">'+' '.join(e(x) for x in notes(spec))+'</p></html>')
    return '\n'.join(parts)


def audit_pdf(path, spec, log):
    import fitz
    with fitz.open(path) as doc:
        if len(doc)!=1: raise ValueError('The single-table renderer produced multiple pages; split or use a longtable template')
        p=doc[0]; spans=[s for b in p.get_text('dict')['blocks'] for l in b.get('lines',[]) for s in l.get('spans',[]) if s.get('text','').strip()]
        out=[s['text'] for s in spans if s['bbox'][0]<-.25 or s['bbox'][1]<-.25 or s['bbox'][2]>p.rect.width+.25 or s['bbox'][3]>p.rect.height+.25]
        fonts=[]
        for font in p.get_fonts(full=True):
            name,ext,kind,content=doc.extract_font(font[0]); fonts.append({'name':name,'format':ext,'kind':kind,'embedded_bytes':len(content)})
        width=p.rect.width*25.4/72; height=p.rect.height*25.4/72
        # exponents, daggers and other short raised marks are scripts, checked against a lower floor
        body=spec['style']['body_pt']
        scripts=[s for s in spans if s['size']<0.8*body and len(s['text'].strip())<=4 and (s['flags']&1 or s['text'].strip().lstrip('+-−').isdigit() or s['text'].strip() in '†‡*')]
        minimum=min(s['size'] for s in spans if s not in scripts)
        minimum_script=min([s['size'] for s in scripts] or [minimum])
        outside_vector=[]
        for d in p.get_drawings():
            r=d.get('rect')
            if r and (r.x0<-.25 or r.y0<-.25 or r.x1>p.rect.width+.25 or r.y1>p.rect.height+.25):
                outside_vector.append({'bbox_pt':list(r),'type':d.get('type')})
        overfull=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([\d.]+)pt too (?:wide|high)\)',log)]
        report={'width_mm':width,'height_mm':height,'minimum_visible_font_pt':minimum,'text_outside_page':out,
                'fonts':fonts,'raster_image_objects':len(p.get_images()),'overfull_box_pt':overfull,'vector_objects_outside_page':outside_vector,
                'minimum_script_pt':minimum_script,
                'automated_pass':abs(width-spec['style']['width_mm'])<.1 and minimum>=7.1 and minimum_script>=6.0 and not out and not outside_vector and not any(x>.5 for x in overfull) and all(f['embedded_bytes']>0 for f in fonts),
                'scope':'Checks dimensions, fonts, page bounds and TeX overflow; visual and scientific review remain necessary.'}
        p.get_pixmap(matrix=fitz.Matrix(3,3),alpha=False).save(path.with_suffix('.png'))
        p.get_pixmap(matrix=fitz.Matrix(96/72,96/72),alpha=False).save(path.with_name(path.stem+'_96dpi.png'))
        p.get_pixmap(matrix=fitz.Matrix(2,2),colorspace=fitz.csGRAY,alpha=False).save(path.with_name(path.stem+'_gray.png'))
        report['extracted_text']=p.get_text()
    return report


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('spec',type=Path);parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--source-only',action='store_true',help='Write editable source/data without claiming a compiled or reviewed PDF')
    args=parser.parse_args()
    spec=validate(json.loads(args.spec.read_text())); second=set(); marked,rank_audit=emphasis(spec,second)
    out=args.out.expanduser().resolve();skill_root=Path(__file__).resolve().parents[1]
    if out==skill_root or skill_root in out.parents:parser.error('--out must be outside the installed skill')
    out.mkdir(parents=True,exist_ok=True);stem=spec['id']
    compiled_suffixes=['.pdf','.png','_96dpi.png','_gray.png','_compile.txt','_checks.json']
    if args.source_only and any((out/(stem+s)).exists() for s in compiled_suffixes):
        parser.error('--source-only requires a directory without this table\'s previous compiled outputs. Choose a fresh --out directory or compile the updated table; existing files have not been changed.')
    texdoc,fragment,caption=make_latex(spec,marked,second)
    (out/(stem+'.tex')).write_text(texdoc)
    (out/(stem+'_body.tex')).write_text(fragment)
    (out/(stem+'_caption.tex')).write_text(caption+'\n')
    (out/(stem+'.html')).write_text(make_html(spec,marked))
    write_json(out/(stem+'_spec.json'),spec)
    write_json(out/(stem+'_emphasis.json'),rank_audit)
    with (out/(stem+'.csv')).open('w',newline='') as h:
        w=csv.writer(h);w.writerow(['row_id']+[c['id'] for c in spec['columns']])
        for row in spec['rows']:w.writerow([row['id']]+[display_cell(c,row,row['cells'][c['id']],spec) for c in spec['columns']])
    report=None
    if not args.source_only:
        executable=shutil.which('pdflatex')
        if not executable:raise RuntimeError('pdflatex is required; --source-only exports uncompiled source explicitly')
        proc=subprocess.run([executable,'-no-shell-escape','-interaction=nonstopmode','-halt-on-error',stem+'.tex'],cwd=out,capture_output=True,text=True)
        (out/(stem+'_compile.txt')).write_text(proc.stdout+proc.stderr)
        if proc.returncode:raise RuntimeError('LaTeX compilation failed; inspect '+str(out/(stem+'_compile.txt')))
        report=audit_pdf(out/(stem+'.pdf'),spec,proc.stdout+proc.stderr)
        write_json(out/(stem+'_checks.json'),report)
        if not report['automated_pass']:raise RuntimeError('Recompose the table; export checks failed: '+json.dumps({k:v for k,v in report.items() if k!='extracted_text'}))
    export_suffixes=['.tex','_body.tex','_caption.tex','.html','_spec.json','_emphasis.json','.csv']
    if not args.source_only: export_suffixes += compiled_suffixes
    write_json(out/(stem+'_provenance.json'),{'input_path':str(args.spec.resolve()),'input_sha256':sha256(args.spec),
        'source_sha256':{p.name:sha256(p) for p in [Path(__file__),Path(__file__).with_name('table_core.py')]},
        'data_status':spec['data_status'],'provenance':spec['provenance'],'emphasis':rank_audit,
        'exports':{stem+s:sha256(out/(stem+s)) for s in export_suffixes},
        'compiled':not args.source_only,'visual_review':'Required after rendering; automation alone is not visual approval.'})
    print(json.dumps({'out':str(out),'id':stem,'compiled':not args.source_only,'dimensions_mm':[report['width_mm'],report['height_mm']] if report else None},indent=2))


if __name__=='__main__':main()
