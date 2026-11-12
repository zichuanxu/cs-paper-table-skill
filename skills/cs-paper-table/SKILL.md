---
name: cs-paper-table
description: Design, redesign, repair and typeset tables for computer-science research papers - benchmark and leaderboard tables, ablations, efficiency and scaling comparisons, dataset statistics, capability and feature matrices, robustness (degradation) tables and long text tables. Use when the user asks to make a table from results, improve or redesign a table from a paper, fix LaTeX table formatting, or fit a table into a one- or two-column venue template. Applies principles distilled from about 190 inspected tables in 50 papers (AI-lab reports and 2025-2026 award papers from NeurIPS, ICML, ICLR, CVPR, ICCV, ACL, EMNLP, OSDI, SOSP, NSDI, USENIX Security, S&P, CCS, VLDB, SIGMOD, PLDI and CHI) and a 95-table measurement corpus, while preserving scientific comparability, uncertainty, missingness and provenance. Exports editable LaTeX, vector PDF, preview PNG, semantic HTML and CSV. Not for ordinary spreadsheets or scientific plots.
---

# CS Paper Table

Make the table's scientific comparison easy to read and hard to misread. Typography, grouping and emphasis are part of the argument.

## The eight principles

Decide from these; the detailed rules, the evidence for each and the renderer field that implements it are in [table-craft.md](references/table-craft.md). Read it before styling.

1. **One table answers one question.** Put the compared numbers next to each other, down a column, in a stated order.
2. **The reader never computes.** Print direction, unit, n, the reference and the margin.
3. **Space and alignment before ink.** Rules only at real boundaries; a fill for one declared role.
4. **Emphasis is a budget.** One mark per meaning, every mark defined beside the table. Undefined bold is the most common defect in award papers.
5. **Secondary information recedes but stays readable.** Uncertainty, units and counts are smaller or muted, never below the size floor.
6. **Comparability is visible.** Comparable rows share a block whose banner names the condition; the rest is separated or marked. Missing, failed and censored results are values.
7. **Design at the final size, in the venue's template.** One table size per paper; recompose, never scale.
8. **One paper, one system.** The same row order, precision, marks and hue meanings in every table.

## 1. Establish the table contract

1. Read the data and the manuscript context. Preserve values, identifiers, metric definitions and conditions. From a screenshot or PDF, transcribe and verify every cell before ranking anything; mark unresolved entries instead of guessing.
2. Write the one question the table answers and a one-sentence claim the evidence supports. That sentence becomes the caption.
3. Record metric direction, units, denominators, evaluation version, budgets, hardware and workload where relevant. State which rows or columns are comparable.
4. Declare the uncertainty type, sampling unit, repetition count and method. Distinguish SD, SE, CI, quantiles and deltas; do not infer them from `±`, parentheses or a subscript.
5. Choose the emphasis policy (best within a scope, threshold, focal method, reference row) with its ties and eligibility.
6. Find the venue template, its column width and table type size. Without one, assume a reversible draft placement and say so. Label synthetic data in the caption and metadata.

Read [scientific-contract.md](references/scientific-contract.md) before constructing ranks, aggregates, uncertainty or ablation deltas. Use `NR`, `NA`, `NT`, `NC`, bounds (`> 180`) and observed failures (OOM, TO) deliberately; never replace them with zero.

## 2. Choose the structure

| Reader's question | Structure | Renderer support | Constraint |
|---|---|---|---|
| Which method is best, by how much? | Method rows; metric spanners; one block per budget or protocol; a "Δ vs. best baseline" row | `ranking`, `row.delta`, `focus` | Rank only within a comparable scope |
| What does each component contribute? | Full system first, then removals with a change column or as signed delta rows | `status`, `column.delta`, `row.delta` | One reference; say independent or cumulative |
| What does it cost? | Metrics as rows with a unit-and-direction column; conditions as bands | `ranking.axis: "row"`, `group_style: "band"`, failures | Fix hardware, batch and timing boundaries |
| How much is lost under a harder condition? | Reference block unshaded, other blocks shaded by the drop | `heat.reference` | State the scale; raw values stay printed |
| Where is performance high or low across a matrix? | Heat shading on one shared scale | `column.heat`, `header_fill` | One quantity, one direction per hue |
| What does each system support? | Feature matrix with ✓/✗ or ●/◐/○ and a legend | `status_style`, `status_colors`, `group_rules` | Unknown is not no |
| What is in the data? | Text columns, aligned counts, the unit beside them | `thousands`, typed missing values | No total across unlike units |
| Long catalogue, taxonomy, codebook | Wrapping text, record IDs, repeated headers | manuscript-native | Keep records together across pages |

Use [design-guide.md](references/design-guide.md) for structure and fitting decisions and [latex-recipes.md](references/latex-recipes.md) for manuscript integration, wrapped and side-by-side tables, multipage tables and anything beyond the renderer. Follow the community conventions in table-craft.md: a systems or HCI table is not an ML leaderboard.

For a measured precedent, search the corpus instead of reading it:

```bash
python /path/to/cs-paper-table/scripts/search_corpus.py --query ablation --limit 5
python /path/to/cs-paper-table/scripts/search_corpus.py --company DeepSeek --year 2026 --limit 4
```

[craft-study.md](references/craft-study.md) holds what each of the 50 visually studied papers does well and badly; [evidence-atlas.md](references/evidence-atlas.md) and `references/*.csv` hold the 54-paper measurement corpus. Distinguish **observed**, **measured** and **recommended** statements, and do not claim to have inspected unlisted tables.

## 3. Produce editable output

Write a typed JSON spec ([spec-schema.md](references/spec-schema.md)) and render it. The spec is the input contract, not a licence to invent data or comparability.

```bash
python /path/to/cs-paper-table/scripts/render_table.py \
  /path/to/cs-paper-table/assets/specs/benchmark.json --out /absolute/workdir/table-output
```

Start from the closest example in `assets/specs/`: `benchmark`, `ablation`, `efficiency`, `budget_comparison` (single column), `registry`, `capability`, `robustness` (shaded by drop from a reference), and the five transcribed redesigns in `redesigns/`. `scripts/build_examples.py --out DIR --render` regenerates the four examples that have constructed raw data.

Write output outside the installed skill. The renderer needs Python with PyMuPDF and `pdflatex` with `standalone`, `newtx` (or `lmodern`), `booktabs`, `array`, `dcolumn`, `pifont`, `xcolor` and `colortbl` (`wasysym` only for ●/◐/○). With no LaTeX, use `--source-only` and say the PDF was not compiled.

Each table comes out as `.tex`, `_body.tex`, `_caption.tex`, PDF, PNG (216 dpi, 96 dpi, greyscale), HTML, CSV, the typed spec, `_emphasis.json`, `_checks.json` and provenance hashes. Put `_body.tex` inside the manuscript's own float; it carries its notes and defines its own colours. Then compile the manuscript and look at that placement: a standalone preview does not prove a fit in an unseen template.

The renderer refuses, rather than repairs: text under 7.2 pt, a table wider than its target, emphasis without a stated meaning, a tint without a meaning, heat without a declared domain, rank tints combined with another fill, and captions or notes that narrate how the table was made. It does not infer significance, guess a metric's direction, or rank incompatible scopes in one cell. Use manuscript-native LaTeX for non-Latin text, nested panels, merged row labels, stacked cells and multipage tables, under the same contract and review.

To examine a table in another PDF:

```bash
python /path/to/cs-paper-table/scripts/inspect_table_pdf.py paper.pdf \
  --page 12 --bbox 60 140 550 430 --out /absolute/workdir/table-inspection
```

Read the crop visually. Object extraction measures fonts, sizes, colours and strokes; it cannot tell what an underline or an arrow means.

## 4. Verify and deliver

1. **Content.** Reconcile every cell with the data; recompute deltas, shares and aggregates; audit ties, directions and scope exclusions in `_emphasis.json`.
2. **Five-second review.** Open the PNG at final size and answer the seven questions at the end of table-craft.md; then look closer for wrapped headers, alignment, glyphs, fills and clipping, and check the greyscale preview.
3. **Automated checks are evidence, not approval.** `_checks.json` covers fonts, width, bounds and overflow. Fix a failure by recomposing, never by weakening the check. After changing the renderer, run `python scripts/test_render.py`.
4. **Deliver** the PDF/PNG with the LaTeX, the spec and a short account of the design choices and any unresolved scientific facts. Say which outputs were compiled and looked at.

Stop when the requested table is correct and passes. Do not claim a redesign "beats" its source in general; name the specific gains in readability and verifiability.
