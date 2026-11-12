# LaTeX production and accessible companions

Use these recipes when integrating a generated table into a manuscript or implementing a structure beyond the bundled renderer.
Keep the data and emphasis contract unchanged when changing the typesetting system.

## Contents

- [Integrate the generated body](#integrate-the-generated-body)
- [Rules and grouping with booktabs](#rules-and-grouping-with-booktabs)
- [Decimal alignment with dcolumn](#decimal-alignment-with-dcolumn)
- [Optional siunitx path](#optional-siunitx-path)
- [Small tables, stacked cells and legends](#small-tables-stacked-cells-and-legends)
- [Notes, long text, and multiple pages](#notes-long-text-and-multiple-pages)
- [Font, width, and compilation constraints](#font-width-and-compilation-constraints)
- [Semantic HTML and reusable data](#semantic-html-and-reusable-data)
- [Production verification](#production-verification)
- [Primary documentation](#primary-documentation)

## Integrate the generated body

The renderer writes a standalone document, an editable `_body.tex`, and a `_caption.tex` preview fragment.
Use the body inside the manuscript's own float; it includes the table's notes and locally scoped formatting.
It defines its own colours with `\providecolor`, so the manuscript needs only the packages; define a colour of the same name in the preamble to override one (for example `FocusFill` to match the paper's accent).
Use the manuscript class's font configuration rather than importing the standalone preview's Times (`newtx`) choice.

```latex
% Preamble: merge with packages already loaded by the manuscript.
\usepackage{booktabs,array,dcolumn,pifont}
\usepackage[table]{xcolor}

% In a two-column manuscript, table* is the full-width float.
\begin{table*}[t]
  \centering
  \caption{Controlled comparison under a shared evaluation budget.
    State the task, split, and scope here.}
  \label{tab:controlled-comparison}
  \input{tables/experiment_body.tex}
\end{table*}
```

Replace the caption with the actual specification text; the snippet is a structural example.
Use `table` for an ordinary one-column placement and `table*` only where the class supports the intended full-width placement.
Follow the class's float policy; a placement hint does not guarantee a particular page or position.
The supplied `_caption.tex` already contains a standalone “Table N” prefix; do not put that prefix inside `\caption` and duplicate the class's numbering.
Keep `\label` after `\caption` and refer to the manuscript's resulting label.
Do not paste the standalone `\documentclass`, `\begin{document}`, or minipage wrapper into the manuscript.
If the manuscript already loads `xcolor`, merge compatible table-color support into its preamble rather than blindly loading it again with conflicting options.

The generated body uses local `\linewidth` to check its natural width and distribute spare padding.
Generate it for the actual placement width and inspect it again in that placement.
Do not wrap the body in an extra box with a smaller `\linewidth` and assume the standalone audit still applies.
Do not include a rendered PDF at an arbitrary smaller width as a shortcut: this scales all text, rules, and notes.

## Rules and grouping with booktabs

Use `\toprule`, `\midrule`, and `\bottomrule` for the table's main hierarchy.
Use `\cmidrule(lr){a-b}` under a column spanner; trim adjacent partial rules so separate groups remain visibly separate.
Use `\addlinespace` for a semantic break that does not need another line.
The package supplies rule spacing and different rule weights; its formal-table guidance discourages vertical and double rules.
Its documented compatibility includes `longtable` and `colortbl`; these facts do not establish compatibility with every document class or tagging configuration. See [BT].

**Defaults in this skill:** booktabs' own em-based widths, `\heavyrulewidth=.08em`, `\lightrulewidth=.05em`, `\cmidrulewidth=.03em`, so the rules scale with the table's type (0.68 / 0.43 / 0.26 pt at 8.5 pt).
These values are our production choices, not a company or publisher standard.
Use the manuscript's approved convention when it differs.
Do not insert a `\midrule` after every numeric row; reserve separators for meaningful boundaries.
If a prose matrix needs a vertical boundary, use a deliberately designed alternative and inspect it instead of treating the default booktabs recipe as mandatory.

The following hand-authored example uses original illustrative numbers only:

```latex
\begin{table}[t]
\centering
\caption{Illustrative layout only; these are not measured results.}
\label{tab:illustrative-layout}
\begingroup
\fontsize{8.5}{10.6}\selectfont
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{@{}lD{.}{.}{2.2}D{.}{.}{3.2}@{}}
\toprule
& \multicolumn{2}{c}{Shared evaluation setting} \\
\cmidrule(lr){2-3}
Method & \multicolumn{1}{c}{Success (\%) $\uparrow$}
       & \multicolumn{1}{c}{Latency (ms) $\downarrow$} \\
\midrule
Reference & 71.2 & 128.0 \\
Variant   & \mbox{\boldmath$72$}.\mbox{\boldmath$4$} & \mbox{\boldmath$119$}.\mbox{\boldmath$5$} \\
\bottomrule
\end{tabular}
\par\smallskip
\noindent Bold marks the preferred value in each column of this
illustrative pair; no statistical inference is implied.
\endgroup
\end{table}
```

Fit the chosen class at native size before reusing even a small recipe.
If its natural width exceeds the column, shorten/wrap headers, change placement, or split it.

## Decimal alignment with dcolumn

The bundled renderer uses `D{input separator}{output separator}{format}` for plain numbers.
`D{.}{.}{3.1}` reserves a model with three digits before and one after the decimal; it does not calculate rounding.
`dcolumn` sets digits in math mode and uses `array`; verify that the manuscript's math digits match its text design.
Override the numeric column for a text header or status with `\multicolumn{1}{c}{...}`.
The manual documents both decimal-place and left/right-width forms; a negative format allows unrestricted decimal places but may create excessive width. See [DC].

Format numeric values upstream, using the declared precision and tie rule.
Keep the decimal separator visible to `D` when adding bold: bold each side of the point separately. `\mathbf` changes digits only, leaving the point, a thousands comma and the minus sign at regular weight; the renderer therefore uses `\mbox{\boldmath$…$}` per side and switches the output separator to a bold point for that cell.
Do not surround the entire decimal string with a macro that hides that split without testing the result.
The renderer reserves extra alignment room for bold digits; that space is not extra displayed precision.
Use `\multicolumn{1}{c}{\textit{OOM}}` for an observed failure and explain it in notes.
Do not place OOM, an uncertainty interval, or a capability string in a plain numeric parser as if it were a number.
For `mean ± SD` and estimate-with-interval cells, the bundled renderer uses a consistently formatted composite cell rather than decimal-aligning every internal component.
Use separate estimate/uncertainty columns or a reviewed numeric package setup if internal alignment becomes important.

## Optional siunitx path

Use `siunitx` when the manuscript already uses it or when number/unit formatting and compound alignment justify the dependency.
The default renderer does not require it and does not emit `S` columns.
The v3 manual defines `S` numerical columns, `table-format` as a spacing model, uncertainty display modes, and alignment controls for exponents, comparators, and uncertainties. See [SI], §§3.9 and 4.13.

```latex
% Alternative hand-authored numeric columns, not an additional requirement.
\usepackage{siunitx}
\begin{tabular}{@{}l S[table-format=3.2]@{}}
\toprule
Configuration & {Illustrative value} \\
\midrule
A & 12.30 \\
B & 9.40 \\
\bottomrule
\end{tabular}
```

Reserve enough model width for signs, exponents, bold glyphs, and note markers that actually occur.
Use protected text headers/status entries and the installed version's documented options for font weight.
Do not assume an old `siunitx` configuration from another paper remains valid in the installed version.
Its ability to parse uncertainty does not determine whether the input is SD, SE, or a CI; that meaning still belongs in the contract and caption.
Keep one authoritative rounding step; disable or match downstream automatic rounding rather than creating different PDF and CSV values.
Render a bold value, a negative value, an interval/status, and the widest number before adopting a custom setup.

## Small tables, stacked cells and legends

Patterns from the award-paper studies that the bundled renderer does not emit. Each keeps the table at the paper's one table size.

```latex
% A table of five or fewer columns beside its paragraph (5 of 9 ML award papers), at natural width.
\usepackage{wrapfig}
\begin{wraptable}{r}{0pt}   % 0pt: use the natural width of the contents
  \centering\small
  \input{tables/small_body.tex}
  \caption{Short title. One sentence.}
\end{wraptable}

% Two small tables side by side under a full-width one (TRELLIS.2).
\begin{table*}[t]
  \begin{minipage}[t]{0.48\linewidth}\centering
    \caption{Left title.}\input{tables/left_body.tex}
  \end{minipage}\hfill
  \begin{minipage}[t]{0.48\linewidth}\centering
    \caption{Right title.}\input{tables/right_body.tex}
  \end{minipage}
\end{table*}

% A share over its raw count, the count small and grey (SSH client signatures, Table 2).
\newcommand{\sharecount}[2]{\shortstack[r]{#1\%\\[-0.2ex]{\footnotesize\textcolor{TableMuted}{#2}}}}
RSA & \sharecount{61.53}{5,660,641} & \sharecount{79.44}{4,595,059} \\

% A block label merged across its rows instead of a banner row: saves a line per block in a single column.
\usepackage{multirow}
\multirow{4}{*}{\textbf{16k}} & Baseline & 72.3 \\
                              & Cache    & 72.3 \\

% A legend that shows the tint it defines (Lost in Conversation, Table 1; ChordEdit, Table 1).
Shading: \colorbox[HTML]{F2C1C1}{\strut points lost} against the single-turn score.
```

`wraptable` needs a few lines of text on both sides and fails next to floats, lists and section breaks; check the page.
Generate a body for the width it will actually occupy (`style.width_mm`): the fragment refuses a placement narrower than its natural width.
Feature matrices with ●/◐/○ (`status_style: "circles"`) need `\usepackage[nointegrals]{wasysym}` in the manuscript.
For inferential statistics (HCI), prefer the tests in prose; if tabulated, print estimates with star superscripts, key the stars in the caption, group predictors by rules and put fit statistics after a final rule.

## Notes, long text, and multiple pages

Choose the environment for the required behavior rather than stacking packages indiscriminately.

| Need | Suitable path | Constraint to respect |
|---|---|---|
| Short single-page numeric table | Generated `tabular` body inside `table`/`table*` | The renderer is a one-page table producer; it does not paginate rows |
| Table-width caption and structured notes | `threeparttable` around caption, tabular, and tablenotes | It is not itself a float; place it inside a permitted float when needed [TP] |
| Wrapping descriptive columns | `p{width}` or `tabularx` with `X` columns | `X` allocates paragraph-like width; it is not numeric decimal alignment [TX] |
| Table extending over pages | Manuscript-native `longtable` | It changes the output routine and does not work on ordinary `twocolumn` pages [LT] |
| Many nested groups or irregular cells | Explicit custom LaTeX plus semantic HTML | Keep every header relationship and ranking scope auditable |

For ordinary tables, keep caption above and notes below unless the venue specifies otherwise.
With `threeparttable`, note markers such as `\tnote{a}` refer to explicitly authored `\item[a]` entries in `tablenotes`; do not expect automatic table-note numbering.
Its notes and caption follow the table body's width; keep notes concise enough for that width. See [TP].
Do not wrap the generated body in a second notes environment without removing or adapting its existing notes.
Avoid ordinary page footnotes as a substitute for table-local protocol notes when the association would be lost.
`threeparttable` is a single-table notes mechanism, not a multipage layout solution; check any separate multipage extension against the manuscript.

For a prose-heavy table, use ragged-right paragraph columns and deliberate line breaks rather than compressed justified text.
For `p{...}` columns, `>{\raggedright\arraybackslash}` retains convenient row endings.
For `tabularx`, give only the intended prose columns flexible `X` widths and retain predictable numeric columns.
Do not assume wrapping alone fixes a long unbreakable identifier; supply a meaningful break point or a documented short label.

For `longtable`, author the first-page head, continued head, footer, and final footer explicitly.
Repeat units and leaf headers on every continued page; place breaks between scientific groups when possible.
Use the documented `\endfirsthead`, `\endhead`, `\endfoot`, and `\endlastfoot` divisions. See [LT], §1.
Do not place a multipage table inside a nonbreaking float or minipage and expect it to split.
For a two-column paper, use a permitted one-column appendix section, split tables, or the venue's documented multipage mechanism.
Compile until widths stabilize and inspect the actual page breaks; do not claim the one-page renderer validated this custom path.
For a long catalogue (a rubric, a taxonomy), give each record a short ID in a narrow first column so the text and other tables can cite it, and separate records by space rather than rules.
For a hierarchy, set the parent label once in a merged cell (`\multirow`) and tint alternate leaf rows very lightly (`\rowcolor[HTML]{F7F7F7}`) so a wrapped record is not read as two; do not let a merged cell straddle a page break.

## Font, width, and compilation constraints

Inherit the manuscript's text and math typefaces; the preview uses Times (newtx) only for portable standalone rendering.
Aim for 8–9 pt body text and legible notes at the final placement.
The bundled specification rejects configured body/notes below 7.2 pt; retain that threshold when creating custom source unless an explicit manuscript requirement justifies a reviewed alternative.
PDF-extracted font sizes are slightly different from nominal TeX points, so inspect both the configured size and the audit's measurement tolerance.
Do not use `\resizebox`, `\scalebox`, or a reduced `\includegraphics` width to evade the threshold.

Read width from the actual template; `\linewidth` is local and can change inside a list, minipage, or column.
Use `\typeout{TABLE-COLUMN-WIDTH=\the\columnwidth}` and an analogous `\textwidth`/`\linewidth` line in a temporary manuscript build if needed.
Convert units deliberately; do not assume every CS template uses the same column width.
Reallocate prose width, wrap labels, reduce excess padding, split panels, or choose a wider allowed float before reducing type.
The bundled body expands spare padding after measuring its natural width; it does not geometrically scale the artwork.

The bundled standalone path uses `pdflatex` with `standalone`, `newtx` (or `lmodern`), `booktabs`, `array`, `dcolumn`, `pifont`, `xcolor`, and `colortbl` support.
Do not assume arbitrary Unicode, CJK, or a manuscript-specific font works through that path.
Use the manuscript's configured XeLaTeX/LuaLaTeX or other supported route for such text, and check glyph coverage and embedded fonts.
Keep user content as text and escape LaTeX special characters; do not accidentally interpret a dataset label as executable TeX.
Use `--source-only` only for an honest uncompiled source export when the compilation environment is unavailable.
A failed width/validation gate calls for a fix, not a source-only claim of completed production.

## Semantic HTML and reusable data

Provide an actual HTML `<table>` with a `<caption>`, header cells, and row labels; an image of the table is insufficient for structural navigation.
Use `scope="col"` and `scope="row"` for simple leaf associations.
Define column groups with `<colgroup>` before using `scope="colgroup"`; define row groups with separate `<tbody>` sections when appropriate. See [WAI-I].
For complicated nested/irregular headers, give headers stable IDs and list the relevant row, leaf, spanner, and group IDs in each data cell's `headers` attribute. See [WAI-M].
Do not rely on a visually spanning cell alone to establish an assistive-technology association.
Keep all notes visible and associated with the table; use words to preserve the meaning of color or emphasis.
Check the linearized reading order and repeated names, particularly after splitting or transposing a table.

Ship the display CSV for convenient inspection and the typed specification/raw data for reproducibility.
A flattened display CSV can contain `±`, interval brackets, status codes, and rounded strings; it is not a substitute for raw numerical fields.
Keep units, denominator definitions, comparison groups, missing/failure reasons, and provenance in the specification or a companion data dictionary.
If exporting a raw CSV, use separate columns for estimate, SD/SE or endpoints, status, unit, and relevant setup IDs.
Do not drop “not reported” and “OOM” into the same empty CSV cell.
Do not claim HTML/CSV companions, vector text, or a visually correct PDF imply PDF/UA conformance; tagged-PDF production requires its own supported workflow and verification.

## Production verification

Compile in the standalone path, then compile the real manuscript placement.
Check dimensions, embedded fonts, overflow, clipping, missing glyphs, and unexpected rasterization.
Inspect native-size and grayscale previews; compare the displayed numbers and emphasis with the typed data and `_emphasis.json`.
Check the longest row label, widest numeric value, signs, status tokens, interval endpoints, and all note markers.
Verify that bolding does not disturb decimal alignment and that focus fill covers the intended cells consistently.
After editing layout code, regenerate every companion from the same authoritative specification rather than manually diverging the CSV or HTML.
Report which outputs were compiled and visually inspected; keep the editable source and data with the final artifact.

## Primary documentation

These are package-author/project and W3C references, inspected 2026-10-21; confirm the installed package version before adopting version-specific options.

- **[BT]** Simon Fear, [Publication quality tables in LaTeX](https://tug.ctan.org/macros/latex/contrib/booktabs/booktabs.pdf), booktabs v1.61803398, revised 2020-01-12; §§2–4, printed pp. 3–6.
- **[DC]** David Carlisle / LaTeX Project, [The dcolumn package](https://tug.ctan.org/macros/latex/required/tools/dcolumn.pdf), v1.06, 2025-10-21; printed pp. 1–2.
- **[SI]** Joseph Wright, [siunitx: A comprehensive (SI) units package](https://mirrors.ctan.org/macros/latex/contrib/siunitx/siunitx.pdf), v3.6.4, 2026-10-12; §§3.9, 4.13, and 10.14.
- **[TP]** Donald Arseneau, [The threeparttable package](https://tug.ctan.org/macros/latex/contrib/threeparttable/threeparttable.pdf), documentation dated 2010-03-05; pp. 1–2; see also the [official package entry](https://ctan.org/pkg/threeparttable).
- **[LT]** David Carlisle / LaTeX Project, [The longtable package](https://tug.ctan.org/macros/latex/required/tools/longtable.pdf), v4.27, 2026-01-28; §1; [official entry and output-routine restrictions](https://ctan.org/pkg/longtable).
- **[TX]** LaTeX Project, [tabularx official package entry](https://ctan.org/pkg/tabularx), v2.12a, 2023-12-11; description of the `X` column.
- **[WAI-I]** W3C Web Accessibility Initiative, [Tables with Irregular Headers](https://www.w3.org/WAI/tutorials/tables/irregular/), two-tier and row/column-group examples.
- **[WAI-M]** W3C Web Accessibility Initiative, [Tables with Multi-Level Headers](https://www.w3.org/WAI/tutorials/tables/multi-level/), explicit `id`/`headers` associations and table simplification.

[BT]: https://tug.ctan.org/macros/latex/contrib/booktabs/booktabs.pdf
[DC]: https://tug.ctan.org/macros/latex/required/tools/dcolumn.pdf
[SI]: https://mirrors.ctan.org/macros/latex/contrib/siunitx/siunitx.pdf
[TP]: https://tug.ctan.org/macros/latex/contrib/threeparttable/threeparttable.pdf
[LT]: https://ctan.org/pkg/longtable
[TX]: https://ctan.org/pkg/tabularx
[WAI-I]: https://www.w3.org/WAI/tutorials/tables/irregular/
[WAI-M]: https://www.w3.org/WAI/tutorials/tables/multi-level/
