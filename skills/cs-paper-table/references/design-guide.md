# Table design: evidence and decisions

Use this reference to choose a table structure and its final-size typography.
Use [scientific-contract.md](scientific-contract.md) to decide what may be compared or emphasized and [latex-recipes.md](latex-recipes.md) to implement the result.

## Contents

- [Evidence boundaries](#evidence-boundaries)
- [Observed and measured examples](#observed-and-measured-examples)
- [Choose a table type](#choose-a-table-type)
- [Recommended typography and geometry](#recommended-typography-and-geometry)
- [Fit one or two manuscript columns](#fit-one-or-two-manuscript-columns)
- [Caption, notes, and reading order](#caption-notes-and-reading-order)
- [Color and accessible alternatives](#color-and-accessible-alternatives)
- [Visual acceptance checks](#visual-acceptance-checks)

## Evidence boundaries

Distinguish three kinds of statement throughout the work:

| Label | What it establishes | What it does not establish |
|---|---|---|
| **Observed** | A visible layout or an explicit meaning in the inspected source caption/text | The LaTeX commands that produced it; an unstated statistical meaning |
| **Measured** | A selected PDF text/vector object's nominal font size, color, position, or stroke width | An author-specified TeX setting, universal body size, or perceptual legibility |
| **Recommended** | A design choice made by this skill for a new table | A rule imposed by an author, company, conference, or publisher |

All page references below are physical, 1-based PDF pages; printed folios may differ.
The cited arXiv URLs identify inspected versions; the official system-card URL identifies the dated report described in its row.
Font measurements below are selected visible body spans, not a claim that every glyph has that size.
PDF points and TeX points differ slightly; do not derive a manuscript font command by copying a measured decimal verbatim.
Treat these heterogeneous papers and reports as examples of design decisions, not evidence of a company house style.
Do not reproduce their table artwork or substitute their numbers into the skill's original demonstrations.

## Observed and measured examples

This ledger is descriptive. Apply the recommendations in subsequent sections after checking the new table's purpose.

| Source and exact anchor | Measured properties | Observed design and interpretation |
|---|---|---|
| [GPT-6 Astra System Card](https://deploymentsafety.openai.com/gpt-6-astra/gpt-6-astra.pdf), official cover dated 2026-09-03; Table 1, p. 11 | OpenAISans regular/semibold 9.775 PDF pt; neutral fill `#F3F3F1`; rules about 0.857/0.535 pt | Wrapped category stub, neutral alternating bands, three-decimal rates; an entire focal-model column is semibold. Focal emphasis is not a per-row winner computation. |
| [HealthBench: Evaluating Large Language Models Towards Improved Human Health](https://arxiv.org/pdf/2505.08775v1), v1; Table 5, p. 17 | CMR/CMMI 9.963 PDF pt; black text; rules 0.797/0.498 pt | Left-aligned theme names, right-aligned numbers, multiline headers. Counts, scores, and percentiles have different precision; no winner decoration. |
| [PaperBench: Evaluating AI's Ability to Replicate AI Research](https://arxiv.org/pdf/2504.01848v3), v3; Table 2, p. 5 | Principal Nimbus Roman spans 8.966 PDF pt; alternating fill `#F9F9F9` | Wide, wrapping bibliographic stub and variable-height rows. Italics identify titles; integer rubric-node counts are metadata, not performance. |
| [AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors](https://arxiv.org/pdf/2602.22755v4), v4; Table 1, p. 14 | Principal Nimbus Roman spans 9.963 PDF pt | Prose taxonomy with a thin vertical boundary between label and explanation and thin row separators. A sparse-rule numeric recipe is not the only defensible structure. |
| [Fara-7B: An Efficient Agentic Model for Computer Use](https://arxiv.org/pdf/2511.19663v1), v1; Table 4, p. 9 | URW Palladio body spans 8.966 PDF pt | Indented change labels expose a cumulative sequence. The caption identifies it as cumulative; there is no automatic bold winner. |
| [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/pdf/2605.23904v2), v2; Tables 1 and 3, pp. 7–8 | Table 1 main spans 7.970 PDF pt; delta annotations 5.978 pt. Table 3 principal spans about 8.998 pt | Table 1 separates best, runner-up, focal row, and signed delta. Table 3 uses tint for defaults and bold for within-component ranking. These marks have different jobs. |
| [Gemma 3 Technical Report](https://arxiv.org/pdf/2503.19786v1), v1; Table 6, p. 6 | XCharter Roman body spans 8.966 PDF pt; rule widths 0.868/0.542/0.325 pt | Four family spanners organize eleven model columns. Horizontal family rules and benchmark groups establish hierarchy without score bolding or fill. |
| [Fast Byte Latent Transformer](https://arxiv.org/pdf/2605.08044v1), v1; Table 1, p. 14 | Serif SFRM1000 scores 9.963 PDF pt; OptimisticDisp bold labels 8.767 pt | Bold sans-serif labels coexist with serif scores. Three rules and generous whitespace suffice; the quality table alone does not quantify the speed claim. |
| [SAM 3: Segment Anything with Concepts](https://arxiv.org/pdf/2511.16719v1), v1; Tables 8 and 9, p. 10 | Consult the source-specific measurement record before reusing sizes | Underline in Table 8 identifies a main metric, not runner-up. Table 9 uses four independent ablation panels and explicitly warns against comparisons across them. |
| [Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](https://arxiv.org/pdf/2601.16163v1), v1; Table 1, p. 8 | Main spans 5.383 PDF pt; pale-yellow fill `#FFF9AE`; green citation text `#76B900` | A paired narrow layout carries useful trial/seed notes but very small type. Citation color does not encode quality; the proposed row and leading scores have separate emphasis. |
| [DeepSeek-OCR 2: Visual Causal Flow](https://arxiv.org/pdf/2601.20552v1), v1; Table 1, p. 9 | URW Palladio main spans 8.966 PDF pt; blue delta text `#0000FF`, separate blue links `#1976D2` | Metric-specific two/three-decimal values, resource qualifiers, and selected vertical boundaries. An apparent direction inconsistency needs investigation, not automatic color propagation. |
| [Qwen3-ASR Technical Report](https://arxiv.org/pdf/2601.21337v1), v1; Tables 1–2, pp. 4–5 | Main spans about 6.750 PDF pt in Table 1 and 8.462 pt in Table 2 | Wrapping language inventories and grouped concurrency sweeps require different structures. Table 2 mixes integer milliseconds, two-decimal throughput, and five-decimal real-time factors. |
| [HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/pdf/2604.14268v1), v1; Tables 7 and 14, pp. 27, 37 | Table 7 main spans 7.970 PDF pt, fills `#FFE5E5`/`#E5E5FF`; Table 14 main spans 6.447 pt | Red/blue fill identifies baseline/selected setting, not a universal quality scale. OOM records feasibility failure. Selection prioritizes user study despite disagreement among metrics. |

Preserve useful structure while improving weaknesses: do not reproduce tiny notes, unexplained marks, ambiguous units, or an apparent metric-direction error merely because they occur in a source.
Do not infer absence of uncertainty from a tidy score matrix; distinguish “not displayed” from “not measured.”

## Choose a table type

Choose the scientific question before choosing colors or fonts.
Use the fewest header levels that make every cell's meaning unambiguous.

| Type | Choose it when | Structure to build | Primary failure to prevent |
|---|---|---|---|
| **Grouped benchmark** | Several systems share outcomes, with meaningful budget/protocol cohorts | Method stub; visible setup fields; metric-family spanners; one comparison cohort per block | Ranking across different budgets, prompting, datasets, or metric directions |
| **Controlled ablation** | The question is what changes under defined interventions | Full reference; component-status columns; explicit independent/cumulative/joint labels; outcome and paired delta | Presenting sequential additions as independent component effects |
| **Efficiency and capacity** | Quality, latency, throughput, memory, or feasibility must be read together | Setup blocks; unit/direction per metric; explicit hardware/workload; typed failure outcomes | Calling the fastest multi-device setting most efficient, or treating OOM as zero |
| **Capability/configuration matrix** | Rows describe supported modes, training stages, or enabled components | Text labels plus Yes/No/Partial/Unknown or configuration values; qualification column | Treating support as measured quality; replacing Unknown with No |
| **Dataset/coverage register** | Readers need scope, split membership, units, or provenance | Wide wrapping descriptions; integer counts; unit-of-observation and version/split fields | Adding unlike count units, or equating coverage with evaluation quality |
| **Estimate and effect panel** | Uncertainty or paired changes are the central evidence | Estimate and explicitly named SD/SE/CI; reference and effect units; separate incomparable panels | Confusing dispersion, uncertainty of a mean, quantiles, and deltas |

### Orientation and grouping

- Put methods on rows when readers scan one metric across many systems.
- Put metrics on rows when many quantities need individual units/directions and only a few systems are compared.
- Put configuration fields before outcome fields; make the conditions visible before the result.
- Keep `display_group` and scientific comparison scope independent. Visual proximity is not permission to rank.
- Use one spanner tier plus leaf labels by default. For three-level headers, split panels or implement an explicitly reviewed custom table.
- Keep abbreviated leaf labels meaningful outside their spanner: “Latency (ms)” survives copying better than “Value.”
- Repeat essential conditions in each panel when panels may be cited or exported separately.
- Use whitespace or a light separator to introduce a block; use a short textual block label when the change is scientific.

### Type-specific decisions

For a benchmark, make “best within the matched 16k budget” possible to read directly from the block heading and note.
For an ablation, place the full reference before removals and specify whether every removal starts from that reference.
For a capacity sweep, keep concurrency, precision, device count, and context length attached to every result block.
For a capability matrix, prefer words over unlabelled check/cross glyphs; explain the scope of Partial.
For a register, allocate width to long descriptions rather than making prose into a field of small abbreviations.
For an estimate panel, align the estimate consistently and reserve room for the full interval; do not shrink the interval to a footnote-sized suffix.
If six or more fields are merely experimental setup, consider a small setup table plus a result table linked by stable configuration IDs.

## Recommended typography and geometry

The values below are **our starting recommendations**, not measured corpus averages or external submission requirements.
The manuscript class and the venue's explicit instructions take precedence.

| Property | Starting choice | Adaptation rule |
|---|---|---|
| Typeface | Inherit manuscript text and mathematics fonts | Do not impose a company font. The standalone preview's Times (newtx) is only a preview choice. |
| Body type | Aim for 8–9 pt at final placement | Prefer the manuscript's normal table size when larger; never shrink a finished graphic to obtain a fit. |
| Minimum configured type | 7.2 pt for body and notes in the bundled renderer | This is a rejection threshold, not a target. Recompose if important content needs smaller type. |
| Notes | About 7.6–8.2 pt, remaining readable at native page size | Essential protocol details must not become tiny superscripts or footnotes. |
| Caption | Inherit venue caption styling; standalone preview starts at 9 pt | The manuscript supplies caption numbering and spacing. |
| Leading | About 1.2–1.3 times type size | Increase for wrapped prose; inspect accents, math, and interval brackets. |
| `\tabcolsep` | 2.5–4 pt; renderer starts at 3 pt | Reduce unnecessary padding before reducing type, but retain separation between adjacent numbers. |
| `\arraystretch` | About 1.10–1.25 | Use the upper end for mixed prose/status cells; avoid mechanical expansion of every row. |
| Horizontal rules | Outer 0.75 pt; header/group 0.45 pt; partial 0.30 pt | These are renderer defaults. Keep the outer/header/group hierarchy visible in grayscale. |
| Group gap | Roughly 0.4–0.8 ex in addition to rule spacing | Use a gap instead of a rule when the boundary is already clear. |
| Focus fill | One pale neutral or muted accent, e.g. `#EEF3FA` | Label the reference/default/selected role explicitly; do not imply winning. |
| Numeric precision | Declare per metric | Use the same decimals within a comparable quantity, while preserving integers and meaningful bounds. |

### Alignment

Left-align names, prose, and multiword descriptors.
Align plain numeric columns on the decimal point; right alignment is acceptable for integers and uniform numeric strings.
Center categorical states and short headers when their associations remain clear.
Do not claim that visually centered source values prove use of `siunitx` or `dcolumn`.
Align composite estimates as a consistent unit or provide dedicated estimate/interval columns.
Keep minus signs, comparison signs, units, and note markers from shifting the decimal anchor.
Preserve trailing zeros when the declared precision requires them.
Avoid inserting thousands separators only in some rows of the same numeric field.

### Hierarchy and rules

Start with top, header, and bottom rules; add partial rules under spanners.
Add a body rule only when it marks a real cohort, subtotal, or section transition.
Use a group label and a small gap to prevent a dense stack of rules.
Avoid vertical rules in the default numerical recipe; consider a carefully justified boundary for prose association or complex categorical structure.
Do not mix a full grid with the booktabs spacing recipe without inspecting the intersections.
Do not use heavy boxing, alternating saturation, and winner bolding simultaneously to solve the same tracking problem.
Reserve bold for header hierarchy and one declared data role; avoid bolding an entire final row merely because it is “ours.”

## Fit one or two manuscript columns

Read the actual `\columnwidth`, `\textwidth`, and local `\linewidth` from the manuscript.
Use 80–90 mm for a one-column and 170–180 mm for a two-column trial only when the real template is unavailable; record the assumption.
Do not treat these trial widths as conference requirements.
Measure at the intended placement; a full-width preview cannot validate a one-column inclusion.

Apply this sequence when the table is too wide:

1. Remove redundant words and move repeated units into headers.
2. Wrap descriptive headers into two or three lines; keep ordinary reading orientation.
3. Allocate stub/prose widths by content and reduce excess cell padding.
4. Separate incomparable cohorts or independent experiments into panels with repeated headers.
5. Transpose only when it improves the reading task without hiding per-metric units/directions.
6. Use a full-width `table*` placement if the manuscript permits it.
7. Move detailed secondary results into a readable appendix table with a precise cross-reference.

If it remains too wide, split the table. Do not use `\resizebox`, `\scalebox`, or an undersized included PDF to defeat the type-size gate.
For a tall table, use repeated headers in a suitable multipage appendix or split at scientific group boundaries.
Avoid side-by-side panels when either requires unreadable type; the Cosmos Policy Table 1 example above is a caution, not a target.
Keep panel widths comparable when readers are expected to compare the same columns.

## Caption, notes, and reading order

Use this default order unless the venue requires another placement:

1. Caption title naming the question, followed by population/task, setting, and scope.
2. Group headers, leaf headers with units/direction, then the data body.
3. General interpretation note: aggregation, uncertainty definition, repetition/sampling unit.
4. Specific notes in marker order: protocol deviations, data origin, exclusions, missing/failure definitions.
5. Emphasis key: eligible scope, ties, and the meaning of any fill/underline/colored annotation.

Move a definition into the header when readers need it for every cell; leave long qualifications in notes.
Keep only notes that change how a cell is read. Procedure belongs in the methods text and `provenance`, not in a
note: "The 18 held-out definitions, in three draws of six fixed before any model call" reads better as "The 18
held-out definitions in three draws of six". No tool names for how the table was made, no mark-placement
mechanics, no disclaimers that change no reading; `table_core.validate` rejects these phrases.
Do not make readers infer whether parentheses denote a delta, SD, or reference value.
State the denominator or weighting for an aggregate, and explain any omitted results.
Use literal descriptive note markers when possible; a star is not a significance claim unless a test and threshold are actually specified.
Place source citations near externally reported data or its explicit note.
Let the manuscript's caption command supply “Table N”; do not duplicate a standalone preview prefix.
Keep caption and notes with the table and ensure every panel is independently interpretable.

## Color and accessible alternatives

Treat color as a redundant cue; also name the reference, default, selected setting, or signed change in text.
This follows the [W3C explanation of WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html), which requires a visible alternative when meaning depends on color.
Prefer black or near-black numbers over a pale fill; check grayscale output and normal screen size.
Never map a positive raw delta to “good” before consulting metric direction: a positive error-rate delta is deterioration.
Do not map unlike score ranges to one shared heat scale, or normalize columns without explaining the transformation.
Do not treat link blue, citation green, low-opacity text, or baseline fill as a numerical color scale.
Avoid a heatmap unless magnitude patterns are a real reading task; retain exact printed numbers and a defined scale if one is used.
Provide semantic HTML and a machine-readable CSV/JSON companion for reuse; keep group labels, units, status reasons, and emphasis meaning in those alternatives.
The alternatives supplement the PDF and do not by themselves certify PDF accessibility.

## Visual acceptance checks

Inspect the complete page at intended placement and the table at native size, not only a magnified crop.
Confirm that every header, note marker, minus sign, interval endpoint, and status label is legible.
Check that decimal anchors survive bold values and that fills do not fragment across intercolumn space.
Check that a wrapped row cannot be mistaken for two observations and that group separators do not split a label from its values.
Compare color and grayscale versions; the intended reading must survive both.
Verify that the smallest meaningful text meets the configured minimum, including qualifiers and notes.
After manuscript integration, repeat the size/overflow check because fonts, caption layout, and available width may change.
Accept the visual design only after the separate scientific contract also passes.
