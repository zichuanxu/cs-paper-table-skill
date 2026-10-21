#!/usr/bin/env python3
"""Search the portable table evidence corpus using the Python standard library.

Examples (run from the skill directory):
  python scripts/search_corpus.py --company DeepSeek --year 2026 --query tie --limit 2
  python scripts/search_corpus.py --company Tencent --query "uncertainty timing" --limit 1
  python scripts/search_corpus.py --company Google --query memory --format json

Filters combine with AND; repeated companies or years combine with OR. A query
requires all its case-insensitive words/quoted phrases. JSON output retains the
complete matching records, with measured / observed / recommended evidence apart.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shlex
import sys
import unicodedata


ALIASES = {
    "谷歌": "google", "谷歌深度思维": "google", "deepmind": "google",
    "微软": "microsoft", "msr": "microsoft", "微软研究院": "microsoft",
    "英伟达": "nvidia", "腾讯": "tencent", "混元": "tencent", "hunyuan": "tencent",
    "阿里": "alibaba", "阿里巴巴": "alibaba", "通义": "alibaba", "通义千问": "alibaba",
    "千问": "alibaba", "qwen": "alibaba", "深度求索": "deepseek", "脸书": "meta", "fair": "meta",
}


def normalize(value: object) -> str:
    return unicodedata.normalize("NFKC", str(value)).casefold()


def values(value: object) -> list[str]:
    if isinstance(value, dict):
        return [text for key, item in value.items() if key not in {"evidence_type", "evidence_kind", "kind"}
                for text in values(item)]
    if isinstance(value, list):
        return [text for item in value for text in values(item)]
    return [] if value is None else [str(value)]


def query_parts(query: str, parser: argparse.ArgumentParser) -> list[str]:
    try:
        return [normalize(word) for word in shlex.split(query) if word.strip()]
    except ValueError as error:
        parser.error(f"Invalid --query quoting: {error}")
        return []


def query_score(table: dict, terms: list[str]) -> int | None:
    weighted = [
        (8, " ".join(str(table.get(key, "")) for key in ("id", "paper_title", "role", "anchor"))),
        (5, " ".join(values(table["recommended"]))),
        (3, " ".join(values(table["observed"]))),
        (1, " ".join(values(table["measured"]))),
        (1, " ".join(str(table.get(key, "")) for key in ("company", "year", "version"))),
    ]
    weighted = [(weight, normalize(text)) for weight, text in weighted]
    if any(not any(term in text for _, text in weighted) for term in terms):
        return None
    return sum(weight * min(text.count(term), 5) for term in terms for weight, text in weighted)


def representative_fonts(measured: dict) -> list[dict]:
    fonts = measured.get("fonts", measured.get("visible_table_font_summary", measured.get("font_summary", [])))
    return sorted((font for font in fonts if font.get("visibility_class", "visible") == "visible"),
                  key=lambda font: -font.get("character_count", 0))[:2]


def rule_summary(measured: dict) -> tuple[str, list[float]]:
    if "horizontal_rule_widths_pt" in measured:
        return "long horizontal candidates", sorted(set(measured["horizontal_rule_widths_pt"]))
    if "long_horizontal_rule_objects" in measured:
        return "long horizontal candidates", sorted({obj["stroke_width_pt"] for obj in measured["long_horizontal_rule_objects"]
                                                      if obj.get("stroke_width_pt") is not None})
    return "all selected strokes (may include underlines)", sorted({obj["width_pt"] for obj in measured.get("stroke_widths_pt", [])})


def render_markdown(matches: list[dict], total: int, terms: list[str]) -> str:
    lines = [f"# Table evidence: {len(matches)} shown / {total} matched", ""]
    if not matches:
        lines += ["No matching table evidence. Try a broader company name or fewer query terms.", ""]
    for table in matches:
        lines += [f"## {table['paper_id']} · {table['anchor']} · PDF p. {table['page_1based']}", "",
                  f"**{table['company']} · {table['year']} · {table['role']}**", "",
                  f"Source: [{table['paper_title']}]({table['source_page_url']}) — {table['version']}", "",
                  f"PDF SHA256: `{table['pdf_sha256']}`", "",
                  f"Coordinates (pt, top-left of unrotated page): crop `{table['coordinates']['display_crop_bbox_pt']}`; "
                  f"body `{table['coordinates']['table_body_bbox_pt']}`.", ""]
        candidates = [(sum(term in normalize(" ".join(values(value))) for term in terms), position, key, value)
                      for position, (key, value) in enumerate(table["observed"].items())]
        candidates.sort(key=lambda item: (-item[0], item[1]))
        lines += ["**Observed**", ""]
        for _, _, label, value in candidates[:3]:
            lines.append(f"- {label.replace('_', ' ')}: {' '.join(values(value))}")
        fonts = representative_fonts(table["measured"])
        label, widths = rule_summary(table["measured"])
        lines += ["", "**Measured**", "",
                  "- Largest text contributions by character count: " + "; ".join(f"`{f['font']}` {f['size_pt']:g} pt" for f in fonts) + ".",
                  f"- Stroke widths ({label}): {', '.join(f'{width:g}' for width in widths) or 'not available'} pt.",
                  "- Nominal PDF properties; these are not recommended production sizes or source TeX settings.", "",
                  "**Recommended**", ""]
        lines += [f"- {lesson}" for lesson in table["recommended"]["lessons"]]
        lines += ["", "**Cautions**", ""]
        lines += [f"- {caution}" for caution in table["recommended"]["cautions"]]
        lines += ["", "Full record ID: `" + table["id"] + "` in `references/source-index.json`.", "",
                  "Measurement records: " + "; ".join("`" + path + "`" for path in table["measurement_method"]["measurement_records"]) + ".", ""]
    return "\n".join(lines)


def positive_int(value: str) -> int:
    try:
        result = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("must be an integer") from error
    if result < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--company", action="append", default=[], help="Case-insensitive company/alias substring; repeat for OR")
    parser.add_argument("--year", action="append", type=positive_int, default=[], help="First-publication/report year; repeat for OR")
    parser.add_argument("--query", default="", help="All case-insensitive words or quoted phrases must match the table evidence")
    parser.add_argument("--limit", type=positive_int, default=5, help="Maximum returned tables (default 5)")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--index", type=Path, default=Path(__file__).resolve().parents[1] / "references" / "source-index.json")
    args = parser.parse_args()
    terms = query_parts(args.query, parser)
    companies = [ALIASES.get(normalize(name), normalize(name)) for name in args.company]
    try:
        index = json.loads(args.index.read_text(encoding="utf-8"))
        if not isinstance(index.get("tables"), list) or not isinstance(index.get("papers"), list):
            raise ValueError("Expected a source index with papers[] and tables[]")
        paper_lookup = {paper["id"]: paper for paper in index["papers"]}
        ranked = []
        for position, table in enumerate(index["tables"]):
            if companies and not any(company in normalize(table["company"]) for company in companies):
                continue
            if args.year and table["year"] not in args.year:
                continue
            score = query_score(table, terms)
            if score is not None:
                ranked.append((score, position, table))
        ranked.sort(key=lambda item: (-item[0], item[1]))
        matches = [table for _, _, table in ranked[:args.limit]]
        if args.format == "json":
            payload = {"schema_version": "1.0.0", "filters": {"company": args.company, "year": args.year, "query": args.query, "limit": args.limit},
                       "matched": len(ranked), "returned": len(matches),
                       "evidence_taxonomy": index["evidence_taxonomy"],
                       "results": [{**table, "paper": paper_lookup[table["paper_id"]]} for table in matches]}
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(render_markdown(matches, len(ranked), terms))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Corpus search failed: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
