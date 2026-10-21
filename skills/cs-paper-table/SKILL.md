---
name: cs-paper-table
description: Design, analyze, repair, and produce publication-ready computer science research tables from data, manuscript tables, or AI research-paper references. Use for benchmark and leaderboard tables, controlled or cumulative ablations, efficiency and scaling comparisons, dataset statistics, capability matrices, long text tables, and LaTeX table formatting. Apply measured lessons from 54 recent major-tech AI papers and 95 visually inspected tables, plus a 13-paper visual-craft study (DeepSeek-V3, Qwen2.5, Llama 3, Gemini 1.5, GPT-4, Phi-4, Nemotron-4, DINOv2 and others), to typography, color, rules, layout, grouping, precision, and emphasis while preserving scientific comparability, uncertainty, missingness, and provenance. Export editable LaTeX, vector PDF, preview PNG, semantic HTML, and data; do not use this skill for ordinary spreadsheets or scientific plots.
---

# CS Paper Table

Make the table's scientific comparison easy to read and hard to misinterpret. Treat typography and grouping as part of the argument. Use the bundled research as evidence for particular design choices, not as a universal corporate style or a ranking of prestigious papers.

**Craft first.** Read [table-craft.md](references/table-craft.md) before styling: what 13 top-lab papers do in their typeset tables (restraint, booktabs weights, two-line headers, banner row groups, bold best within a scope, muted deltas and uncertainty, short captions with notes underneath) and the renderer defaults that implement it. Its redesign protocol and the two worked redesigns (`assets/specs/redesigns/`) show how to beat an existing table without changing a value.

## Establish the table contract

1. Read the supplied data and manuscript context. Preserve values, source identifiers, metric definitions and experimental conditions. If only a screenshot is available, transcribe and verify every cell before ranking anything; mark unresolved entries instead of guessing.
2. Identify the reader's task: compare models, explain an ablation, audit resource costs, describe data, or inspect coverage. Write a one-sentence intended claim that the available evidence actually supports.
3. Record metric direction, units, denominators, evaluation version, model/configuration identity, training/inference budgets, hardware and workload where relevant. Specify which rows or columns are comparable. Keep incompatible groups visually separate.
4. Declare uncertainty type, sampling unit, repetition count and estimation method. Distinguish SD, SE, CI, quantiles, deltas and gaps to a reference. Do not infer these from `±`, parentheses, a subscript, or a paper's ambiguous legend.
5. Choose an explicit emphasis policy: structural headers, focal method, within-scope rank, reference row, or significance supported by an appropriate analysis. Define ties and eligibility. Do not treat bold, underline or color as self-explanatory.
6. Set final manuscript width and font requirements. Infer a reversible draft placement if none is supplied; ask only for unknown scientific facts that materially affect correctness. Label synthetic demonstration data prominently in both caption and exported metadata.

Read [scientific-contract.md](references/scientific-contract.md) before constructing ranks, aggregates, uncertainty, or ablation deltas. Use `NR`, `NA`, `NT`, `NC`, and observed execution outcomes deliberately; never replace them with zero.

## Select evidence and a table structure

Search the inspected corpus by purpose or source rather than reading the entire archive:

```bash
python /path/to/cs-paper-table/scripts/search_corpus.py --query ablation --limit 5
python /path/to/cs-paper-table/scripts/search_corpus.py --company DeepSeek --year 2026 --limit 4
```

Use [evidence-atlas.md](references/evidence-atlas.md) for study scope and representative anchors. Use [source-index.json](references/source-index.json), [paper-corpus.csv](references/paper-corpus.csv) and [table-corpus.csv](references/table-corpus.csv) when exact versions, table numbers, pages, PDF hashes, or measurements matter. Follow its links to detailed evidence only as needed. Distinguish **observed**, **measured**, and **recommended** statements. Do not claim to have inspected unlisted tables or infer a source's LaTeX implementation from a rendered PDF.

| Reader task | Starting structure | Scientific constraint |
|---|---|---|
| Dense benchmark | Method stub; grouped metric headers; separate protocol/budget row blocks | Rank only within eligible comparison scopes; keep aggregate weights explicit |
| Independent ablation | Configuration matrix plus estimate and paired delta | Define one reference and retain paired sampling units |
| Cumulative ablation | Ordered configuration states or stages | Label dependencies; adjacent changes are conditional increments |
| Efficiency | Metrics as rows when directions/units differ; setup above or in notes | Fix hardware, precision, batch, sequence lengths and timing boundaries |
| Dataset registry | Text columns plus aligned split counts and unit of observation | Preserve versions, zeros, missing states and heterogeneous count units |
| Capability / taxonomy | Grouped categorical columns with a symbol or word legend | Separate no, unknown, unsupported and not tested; avoid false numeric ranks |
| Long catalog / examples | Wrapping text columns; repeated headers for multipage output | Keep records together and avoid losing header associations |

Use [design-guide.md](references/design-guide.md) for specific layout and style decisions. Use [latex-recipes.md](references/latex-recipes.md) for manuscript integration, multipage tables, and alternatives beyond the bundled renderer.

## Design at the final physical size

- Inherit the manuscript's typeface. The standalone preview uses Times (newtx), the most common CS venue face; it is only a portable specimen. Keep typography consistent with the paper's mathematics and caption style.
- Start at 8–9 pt body type for a dense full-width table. Keep the bundled renderer's 7.2 pt authoring floor; it is a design guard, not a conference rule. Shorten or wrap headers, remove repeated units, transpose, split panels, or move detail to an appendix before reducing type.
- Align text stubs left and simple numeric columns on the decimal point. Retain meaningful trailing zeros. Format percentages, counts, latency and memory at justified precision instead of applying one decimal policy to the entire table.
- Use header spanners and trimmed group rules to make related metrics visible. Use whitespace and a light hierarchy of horizontal rules. Add a vertical separator only if a specific association would otherwise be ambiguous; avoid default spreadsheet grids.
- Use two-line headers: a bold name, then a smaller muted line for n, unit, shots or direction (`Latency` / `ms ↓`). Show uncertainty and intervals as smaller secondary text, deltas as signed values coloured by improvement after the metric's direction, binary states as ✓/✗, counts with thousands separators and FLOPs as `a·10^n`. Keep the source's precision when transcribing (`precision: "reported"`).
- Keep the caption to a bold title and one or two sentences; put definitions, the emphasis legend and data status in the notes, in two or three lines.
- Use dark text, a white background, and at most one or two semantic accent roles. Treat pale fills as opaque specified colors unless transparency is actually measured. State whether a fill marks a reference, a focal row, a condition or an effect; preserve meaning in grayscale and through labels.
- Keep bold sparse and explicit. Add second-place underlining (`ranking.runner_up`) only when the notes say what it means, and never highlight all cells in a focal row as winners. Apply any source-inspired convention only after explaining its meaning in this table.
- Put the caption and notes in the manuscript's required positions. Make the caption identify the comparison and protocol; put uncertainty, emphasis, missing-value and exception definitions close enough to travel with the table.

## Produce editable output

Use the typed JSON renderer for the supported structures. Read [spec-schema.md](references/spec-schema.md); the JSON specification is the input contract, not an excuse to invent data or comparability.

```bash
# Compile an existing specimen at its declared physical width.
python /path/to/cs-paper-table/scripts/render_table.py \
  /path/to/cs-paper-table/assets/specs/benchmark.json \
  --out /absolute/workdir/table-output

# Real-table redesigns: Transformer Table 2 and Harness² Table 1 (transcribed, reported values).
python /path/to/cs-paper-table/scripts/render_table.py \
  /path/to/cs-paper-table/assets/specs/redesigns/harness2_t1.json --out /absolute/workdir/h2

# Rebuild all four specimens and their constructed raw data.
python /path/to/cs-paper-table/scripts/build_examples.py \
  --out /absolute/workdir/table-examples --render
```

Write output outside the installed skill. The renderer requires Python with PyMuPDF and `pdflatex` with `standalone`, `newtx` (or `lmodern` with `style.font`), `booktabs`, `array`, `dcolumn`, `pifont`, `xcolor`, and `colortbl`. The example builder additionally requires NumPy. Use `--source-only` when LaTeX is unavailable, and clearly say that the PDF was not compiled.

Keep `.tex`, `_body.tex`, `_caption.tex`, the typed JSON, raw inputs, CSV, semantic HTML and provenance together. The standalone PDF is vector output; PNG is a review preview. Integrate the body and caption fragments into the real manuscript, then compile and inspect that placement again. Do not claim that a standalone preview proves compatibility with an unseen conference template. Use manuscript-native LaTeX for unsupported structures, Chinese or other non-Latin text, nested panels, special cells and multipage tables; preserve the same data contract and review gates.

The renderer supports column or row ranking, explicit scopes, exclusions, rounded/raw/tolerance ties, an optional underlined runner-up, mean ± SD or mean (SD), estimate with interval, ✓/✗ status, signed delta rows, cells spanning columns, scientific notation, thousands separators, reported per-value precision, focus rows or columns, typed missingness (codes or a single dash) and observed failure outcomes. It intentionally does not infer statistical significance, compute second-place semantics, guess unknown metric directions, or rank multiple incompatible scopes in one cell. Use custom code when needed and save the decisions and calculations.

To examine another PDF table, use:

```bash
python /path/to/cs-paper-table/scripts/inspect_table_pdf.py paper.pdf \
  --page 12 --bbox 60 140 550 430 --out /absolute/workdir/table-inspection
```

Read the resulting crop visually. PDF object extraction can measure font resources, nominal sizes, colors and strokes; it cannot establish the intended semantics of an underline, arrow or missing marker. Keep source artwork as research material, not as a template asset to redistribute.

## Verify and deliver

1. **Verify content.** Reconcile cells with the data, check denominators and aggregate weights, recalculate deltas, and audit ties and metric directions. Confirm scope exclusions and the interpretation of every special marker. Retain raw data and source versions.
2. **Compile and inspect.** Open the rendered PNG/PDF at intended size and at a closer view. Check wrapped headers, alignment, glyphs, row fills, line weights, spacing, caption/notes, clipping, and visible winner marks. Inspect grayscale where color carries structure.
3. **Use automated checks as evidence, not approval.** Inspect `_checks.json` for font embedding, width, text bounds and TeX overflow, and `_emphasis.json` for eligible scopes and marked cells. An automated pass does not prove good layout, complete accessibility or correct science. Fix a failed check by recomposing the table, not by silently weakening it.
4. **Finish with the editable source.** Deliver the requested PDF/PNG plus the LaTeX, input data/specification and a concise explanation of design choices and any unresolved scientific facts. Offer semantic HTML/CSV alongside untagged PDF when useful. State which outputs were compiled and visually reviewed.

Stop after the requested artifacts are correct and the relevant gates pass. Do not enlarge the study or rerun unrelated tests merely to increase a paper count. Do not promise that a table objectively “beats” every source; identify the specific improvements in readability, verifiability and editing.
