> Portable evidence notes. Source PDFs and images are not bundled. Measurement paths below are relative to this directory; consult [measurement-method.md](measurement-method.md) for scope and reproduction.

# Table-design research: OpenAI, Anthropic, Microsoft

Inspected on 2026-10-21: **18 distinct primary-source papers/reports, 33 table anchors**. Six papers per company. All counted tables were visually opened as rendered PDF pages/crops and measured at selected body regions. Seventeen papers came from the prior figure corpus; one is an additional official report. This does **not** claim table inspection of all prior 120 papers.

## Method and evidence boundaries

Primary-source PDFs were browsed/verified, downloaded and rendered with PyMuPDF. The full table-plus-caption crop and a separate body-only measurement region are recorded for every anchor. Coordinates are PDF points on the unrotated physical page, origin at top left. The page number is the physical 1-based PDF page, which can differ from the printed folio. Font sizes, color objects and stroke widths are measured nominal PDF properties. Alignment, wrapping and spacing descriptions are visual judgments. Design lessons are recommendations and are not claimed as properties of a company or conference.

Crops and source PDFs are research intermediates only. No source artwork should be distributed in the new skill. Keep bibliographic references, measured property summaries and original design guidance. No conference-acceptance or house-style status is inferred.

The downloaded Natural Emergent Misalignment report was text-screened, not counted as a table inspection: no actual numbered source-table anchor was selected; a table mention in an example transcript was excluded. The Claude Sonnet 5 system card is the documented substitute. Its cover is dated 2026-06-30; the CDN document identity and hash are preserved instead of assuming a publication date from a search result.

## Cross-source synthesis

### Start from the scientific role, not a single visual theme.

Offer distinct recipes for descriptive statistics, coverage catalogs, configuration matrices, benchmark comparisons, cumulative ablations and efficiency trade-offs.

Evidence: healthbench Table 1; paperbench Table 2; phi-vision Table 2; fara Table 4; fara Table 10.

### Bold, underline and color have independent and sometimes opposite semantics.

Require an emphasis declaration: purpose, grouping scope, metric direction, ties, and whether color means default, focal method, baseline, signed delta or simple row tracking. Do not infer meaning from appearance.

Evidence: astra Table 1; openai-controllability Table 2; skillopt Table 1; skillopt Table 3; phi-mini Table 7.

### Comparability is nested in settings, datasets, budgets, units and aggregation.

Store comparison groups with each numeric result. Rank only inside a group whose benchmark, protocol, split, budget and metric are genuinely aligned.

Evidence: swe-lancer Table 1; gpt-oss Table 3; sonnet5-system Table 4.1.1.A; phi-vision Table 6; skillopt Table 1.

### Missingness is typed evidence.

Distinguish unavailable, unsupported, not applicable, omitted environment, censored rank, failed run and lower bound. Never silently convert these to zero or use one dash for incompatible statuses.

Evidence: hidden-objectives Table 2; magma Table 2; phi-mini Table 3; sonnet5-system Table 4.1.1.A.

### Sparse rules are common, but vertical lines and full grids occur for defensible purposes.

Default to strong hierarchy with few rules; add boundaries when prose association, semantic column groups or long report headers need them. Avoid a universal ban on vertical rules.

Evidence: healthbench Table 5; auditbench Table 1; hidden-objectives Table 2; reasoning-faithfulness Table 1; sonnet5-system Table 4.1.1.A.

### Precision follows the quantity.

Specify per-column units and precision; keep means/errors commensurate; retain integer counts. Disclose rounding and distinguish uncertainty, delta and ratios.

Evidence: healthbench Table 5; gpt-oss Table 3; fara Table 10; skillopt Table 6.

### Native-size readability is a separate acceptance gate from PDF validity.

Do not copy the smallest measured fonts. Split, transpose, move notes, shorten labels with a key, or widen the table before reducing type. Inspect at intended final width and at native page scale.

Evidence: skillopt Table 1; magma Table 7; phi-mini Table 3; phi-mini Table 7.

### Captions often carry essential measurement semantics.

Require metric units/direction, comparison scope, uncertainty definition, aggregation, exceptions, missingness and emphasis key when they are not already explicit in headers/notes.

Evidence: openai-controllability Table 2; swe-lancer Table 1; hidden-objectives Table 2; anthropic-aar Table 3; skillopt Table 6.

### No defensible single corporate house style emerges from these heterogeneous publication artifacts.

Borrow task-level layout patterns, not brand-specific colors/fonts or claims that a style is universal across a company or a conference.

Evidence: astra Table 1; gpt-oss Table 3; sonnet5-system Table 4.1.1.A; auditbench Table 1; magma Table 7; phi-vision Table 2.

## Source inventory

| Company | Papers | Table anchors |
|---|---:|---:|
| OpenAI | 6 | 10 |
| Anthropic | 6 | 9 |
| Microsoft Research | 6 | 14 |

## Per-paper and per-table evidence

### GPT-6 Astra System Card

- ID: `astra`; company grouping: OpenAI; year: 2026.
- Source: https://deploymentsafety.openai.com/gpt-6-astra/gpt-6-astra.pdf
- Version: Official PDF; cover dated 2026-09-03; retrieved 2026-10-21
- Affiliation evidence: PDF title page names OpenAI; downloaded from the official OpenAI deployment-safety domain.
- SHA-256: `77ff1e8aaf7018c7d7bbe347c374cd74188387ceca91f1ef637ccc59ea930895`

#### Table 1 — Safety benchmark comparison

Anchor: physical PDF page 11; full crop `[68, 384, 544, 561]`; body measurement crop `[70, 404, 542, 560]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/astra-table-1.json`

**Measured PDF properties:** OpenAISans-Regular 9.775 pt (276 selected characters); OpenAISans-Semibold 9.775 pt (48 selected characters). Selected stroke widths: 0.857, 0.535 pt. Vector fill colors: #F3F3F1, #FFFFFF. Text colors: #000000.

- **Headers:** One header tier; a long row label wraps to two lines.
- **Row groups:** Eight safety categories; alternating neutral row bands.
- **Column groups:** Four model columns beside a descriptive stub.
- **Alignment:** Left-aligned category text; centered model labels and numeric values.
- **Precision:** All rates shown to three decimals, retaining trailing zeroes.
- **Missingness:** None in this region.
- **Emphasis:** Every value in the focal model column is semibold; this is focal-column emphasis, not a universal evidence-based winner legend.
- **Rules:** Top, header, and bottom horizontal rules; no vertical rules.
- **Spacing, visual estimate:** Compact rows; wrapping expands the affected category row without shrinking all text.
- **Caption/notes:** Short caption above; improvement direction is explicit. The preceding page text cautions about evaluation changes across system-card releases.
- **Comparability:** Compare the same category across models within this evaluation snapshot; category difficulty and cross-release measurement changes preclude casual pooled ranking.

**Design lessons:** Allow a declared focal-model emphasis rule separate from best-value highlighting. Use neutral bands when long row labels increase horizontal tracking effort.

**Cautions:** Do not interpret a bold column as statistical superiority.

### Reasoning Models Struggle to Control their Chains of Thought

- ID: `openai-controllability`; company grouping: OpenAI; year: 2026.
- Source: https://arxiv.org/pdf/2603.05706v1
- Version: v1
- Affiliation evidence: PDF page 1 identifies four OpenAI coauthors alongside NYU, UCL, UPenn and MATS affiliations; collaborative paper, not exclusive corporate authorship.
- SHA-256: `0739b5d4b8da2d1b9956216e7111ceaa1625d232ec137cc6cd3cf8658eaafb0f`

#### Table 2 — Grouped safety behavior comparison with uncertainty

Anchor: physical PDF page 29; full crop `[106, 269, 506, 488]`; body measurement crop `[151, 314, 459, 486]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/openai-controllability-table-2.json`

**Measured PDF properties:** NimbusRomNo9L-Medi 9.963 pt (143 selected characters); NimbusRomNo9L-Regu 9.963 pt (113 selected characters); CMR10 9.963 pt (95 selected characters); CMMI10 9.963 pt (46 selected characters). Selected stroke widths: 0.797, 0.498 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** One tier for model and three controllability categories.
- **Row groups:** Models form the body; a ruled count row summarizes category maxima.
- **Column groups:** Three category scores use the same mean-plus-error notation.
- **Alignment:** Left stub, visually centered numeric composites; every mean and error uses aligned decimal precision.
- **Precision:** Means and displayed standard errors use one decimal.
- **Missingness:** None.
- **Emphasis:** Caption explicitly bolds the highest score in each model row, including a tie, while explaining that lower controllability is safer.
- **Rules:** Three main horizontal rules plus a rule above the summary; no vertical grid.
- **Spacing, visual estimate:** Compact single-line rows; summary separated from observations by a clear rule.
- **Caption/notes:** Caption above defines equal weighting of category/dataset pairs, one standard error, and row-wise maximum emphasis.
- **Comparability:** Within-row emphasis asks which category is most controllable; it is not a winner ranking of models. Summary counts can exceed row count when ties count in more than one category.

**Design lessons:** Store emphasis scope and emphasis objective independently of metric direction. State error-bar meaning in the caption.

**Cautions:** Do not equate largest with safest or best; do not discard tied maxima.

### HealthBench: Evaluating Large Language Models Towards Improved Human Health

- ID: `healthbench`; company grouping: OpenAI; year: 2025.
- Source: https://arxiv.org/pdf/2505.08775v1
- Version: v1
- Affiliation evidence: PDF page 1 places OpenAI below the author list.
- SHA-256: `f61c53f6bde84a3964531efe04a75389f9bba9e70a35b4012c871c9ec0b512f3`

#### Table 1 — Dataset descriptive statistics

Anchor: physical PDF page 4; full crop `[350, 279, 542, 456]`; body measurement crop `[365, 333, 522, 455]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/healthbench-table-1.json`

**Measured PDF properties:** CMR10 9.963 pt (134 selected characters). Selected stroke widths: 0.797, 0.498 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** One tier for three measurement columns.
- **Row groups:** Distribution landmarks and mean appear as named rows.
- **Column groups:** Character count, turn count, and rubric-criterion count have distinct units.
- **Alignment:** Left statistic names; right-aligned numbers with visible decimal alignment.
- **Precision:** One decimal is retained even for integer-valued count summaries.
- **Missingness:** None.
- **Emphasis:** No winner emphasis or colored cells.
- **Rules:** Three horizontal rules, no vertical rules.
- **Spacing, visual estimate:** A small table fits beside explanatory prose; short column names retain readable body type.
- **Caption/notes:** Multi-line caption above describes the summarized quantities.
- **Comparability:** Columns describe different units; rows are summaries, not competing methods.

**Design lessons:** Use a compact descriptive-statistics recipe without performance emphasis. Preserve precision consistently when distribution summaries include means.

**Cautions:** Do not rank counts from different units or bold maxima automatically.

#### Table 5 — Human/model grader comparison with sample counts

Anchor: physical PDF page 17; full crop `[70, 71, 542, 248]`; body measurement crop `[82, 112, 530, 246]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/healthbench-table-5.json`

**Measured PDF properties:** CMR10 9.963 pt (350 selected characters); CMMI10 9.963 pt (8 selected characters). Selected stroke widths: 0.797, 0.498 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** One logical header tier, with several labels wrapped over three lines.
- **Row groups:** Seven evaluation themes, no shaded sections.
- **Column groups:** Sample count, weighted physician score, model score, and model percentile are separate columns.
- **Alignment:** Long theme labels align left; numeric columns align right, making their differing precision legible.
- **Precision:** Integer sample sizes; three-decimal score columns; one-decimal percentile.
- **Missingness:** None.
- **Emphasis:** No cell ranking or highlight; headers are regular-weight text.
- **Rules:** Three horizontal rules, no vertical grid.
- **Spacing, visual estimate:** Header height absorbs descriptive labels rather than forcing tiny abbreviations.
- **Caption/notes:** Caption above defines weighting, score and percentile; a complementary plot follows, outside the table.
- **Comparability:** Compare physician/model scores within each theme. Percentile is a different quantity from the score and must not be included in the same numeric ranking.

**Design lessons:** Give each numeric column its own unit and precision. Make sample-size and weighting context visible beside scores.

**Cautions:** A percentile and an absolute metric are not commensurate just because both are numeric.

### PaperBench: Evaluating AI's Ability to Replicate AI Research

- ID: `paperbench`; company grouping: OpenAI; year: 2025.
- Source: https://arxiv.org/pdf/2504.01848v3
- Version: v3
- Affiliation evidence: PDF page 1 identifies OpenAI below the author list.
- SHA-256: `2f58f1a6581af9d99432422dccf3cf61f5c263377c1e4550e7333c4a22d7184d`

#### Table 2 — Dataset/paper coverage catalog

Anchor: physical PDF page 5; full crop `[54, 75, 547, 460]`; body measurement crop `[55, 85, 546, 458]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/paperbench-table-2.json`

**Measured PDF properties:** NimbusRomNo9L-ReguItal 8.966 pt (694 selected characters); NimbusRomNo9L-Regu 8.966 pt (591 selected characters); NimbusRomNo9L-ReguItal 9.146 pt (341 selected characters); NimbusRomNo9L-ReguItal 8.787 pt (76 selected characters). Selected stroke widths: 0.797, 0.498 pt. Vector fill colors: #F9F9F9, #FFFFFF. Text colors: #000000.

- **Headers:** One tier for source work, selection class, topic and rubric-node count.
- **Row groups:** Twenty catalog entries; faint alternating bands.
- **Column groups:** A wide bibliographic stub and three narrower metadata columns.
- **Alignment:** Titles and topics align left and wrap; selection labels and integer counts form narrow columns.
- **Precision:** Integer node counts.
- **Missingness:** None.
- **Emphasis:** Titles are italic; header labels bold; no winner highlight.
- **Rules:** Top, header and bottom rules, without vertical boundaries.
- **Spacing, visual estimate:** Most width belongs to titles; variable-height rows accommodate long text. The table spans the full two-column page width.
- **Caption/notes:** Caption above links the coverage catalog to a separate rubric-count table.
- **Comparability:** This is a coverage index, not a model leaderboard. Node counts describe rubric size, not model capability.

**Design lessons:** Give descriptive columns width according to their information load. Use subtle zebra bands for variable-height catalogs.

**Cautions:** Do not impose performance ranking semantics on coverage metadata.

#### Table 4 — Compact benchmark score with standard error

Anchor: physical PDF page 7; full crop `[306, 145, 546, 264]`; body measurement crop `[340, 178, 506, 262]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/paperbench-table-4.json`

**Measured PDF properties:** NimbusRomNo9L-Regu 7.173 pt (35 selected characters); CMR9 8.966 pt (26 selected characters); NimbusRomNo9L-Medi 7.173 pt (24 selected characters); NimbusRomNo9L-Regu 8.966 pt (17 selected characters). Selected stroke widths: 0.797, 0.498 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** One tier for model and benchmark score.
- **Row groups:** Six model rows.
- **Column groups:** Single numeric result column.
- **Alignment:** Left-aligned small-cap model labels; centered mean-plus-error cells.
- **Precision:** One decimal for mean and standard error.
- **Missingness:** None.
- **Emphasis:** One model name is bold; its numeric cell is not visually bold.
- **Rules:** Three horizontal rules, no vertical rules.
- **Spacing, visual estimate:** A narrow table occupies one paper column; no decorative cell background.
- **Caption/notes:** Caption above states percent units, the agent setup, and one standard error of the mean.
- **Comparability:** Results share the stated scaffold; different scaffolds are presented in separate neighboring tables rather than silently merged.

**Design lessons:** Use a two-column recipe for a single outcome with uncertainty. Keep scaffold changes visible in separate panels or fields.

**Cautions:** Model-label emphasis and numeric winner emphasis are distinct operations.

### SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?

- ID: `swe-lancer`; company grouping: OpenAI; year: 2025.
- Source: https://arxiv.org/pdf/2502.12115v4
- Version: v4
- Affiliation evidence: PDF page 1 affiliation footnote identifies OpenAI.
- SHA-256: `5592089e626e52af27222a144f65ef8e2748e4f8a2ab3cba29df82366a48a5c8`

#### Table 1 — Benchmark performance, earnings and configuration matrix

Anchor: physical PDF page 7; full crop `[54, 75, 543, 440]`; body measurement crop `[55, 130, 542, 439]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/swe-lancer-table-1.json`

**Measured PDF properties:** NimbusRomNo9L-Regu 9.679 pt (1088 selected characters). Selected stroke widths: 0.484, 0.774, 0.290 pt. Vector fill colors: #CCFFCC, #E5E5FF. Text colors: #000000.

- **Headers:** One tier across model, tool availability, split, reasoning setting and three outcomes.
- **Row groups:** Ruled blocks separate tool ablation, task families, full/selected splits, and combined totals.
- **Column groups:** Configuration fields precede outcome columns.
- **Alignment:** Model labels align left; settings and numerical outcomes are visually centered.
- **Precision:** Rates use one decimal plus percent sign; monetary outcomes are rounded to thousands and include denominator totals.
- **Missingness:** N/A occurs for configurations where a tool or reasoning setting does not apply; not a zero score.
- **Emphasis:** Green rows identify baseline task-family results; pale blue rows identify combined-split totals. Caption declares these meanings. No general winner bolding.
- **Rules:** Top/header/bottom rules plus block separators and a double separation before combined totals; no vertical grid.
- **Spacing, visual estimate:** Tight single-line rows carry a large number of conditions; short split labels repeat explicitly.
- **Caption/notes:** Long caption above defines splits, rounding, denominators and the row-color meanings.
- **Comparability:** Compare only rows matched on split, task family, tool condition and reasoning setting. Aggregate earnings and pass rates do not measure the same thing.

**Design lessons:** Place all material evaluation settings before the result columns. Use semantic row colors only with a written key.

**Cautions:** Coloring the baseline is not a claim that it is best; rounded earnings cannot support exact recomputation of rates.

#### Table 2 — Task-type breakdown with denominators

Anchor: physical PDF page 9; full crop `[54, 75, 543, 171]`; body measurement crop `[56, 85, 541, 170]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/swe-lancer-table-2.json`

**Measured PDF properties:** NimbusRomNo9L-Regu 9.418 pt (279 selected characters). Selected stroke widths: 0.753, 0.283, 0.471 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** Two tiers: two task families each span repeated model-result columns and a sample count.
- **Row groups:** Four task categories.
- **Column groups:** Symmetric task-family groups, each with three model rates and n.
- **Alignment:** Left task labels; centered rates and counts; grouped rules align precisely with each family.
- **Precision:** One-decimal percentages and integer counts.
- **Missingness:** None.
- **Emphasis:** No bolding or color, allowing the small denominators to remain visible.
- **Rules:** Top, header and bottom rules plus partial rules below the two group headers; no vertical grid.
- **Spacing, visual estimate:** Wide stub accommodates category names; compact repeated numeric columns reduce header repetition.
- **Caption/notes:** Short caption above states the selected dataset split and task-type breakdown.
- **Comparability:** Subgroup rates have unequal n. Rates from very small groups should not receive the same evidential weight as rates from large groups.

**Design lessons:** Attach the denominator to each comparison block. Use spanning headers for repeated measurement structures.

**Cautions:** Do not infer statistical significance or equal reliability from formatted percentages alone.

### gpt-oss-120b & gpt-oss-20b Model Card

- ID: `gpt-oss`; company grouping: OpenAI; year: 2025.
- Source: https://arxiv.org/pdf/2508.10925v1
- Version: v1
- Affiliation evidence: PDF title page identifies OpenAI.
- SHA-256: `8839e1efdf835be08ad1d60bfa99c8c4fdde15c7ef49eda6a8b910575fb699a0`

#### Table 3 — Multi-metric benchmark matrix across reasoning levels

Anchor: physical PDF page 11; full crop `[99, 140, 493, 508]`; body measurement crop `[101, 163, 492, 507]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/gpt-oss-table-3.json`

**Measured PDF properties:** SFRM1000 9.963 pt (753 selected characters); SFBX1000 9.963 pt (156 selected characters). Selected stroke widths: 0.398, 0.542, 0.868 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** Two tiers: model families span three reasoning levels.
- **Row groups:** Accuracy, score and Elo sections are explicitly separated; the lower-level header repeats in each section.
- **Column groups:** Two model blocks, each with low/medium/high settings.
- **Alignment:** Left benchmark names; centered numbers and settings.
- **Precision:** One decimal for percentages; integers for Elo.
- **Missingness:** None.
- **Emphasis:** Bold is structural: group labels, section headers and subheaders. Numeric results remain regular.
- **Rules:** Horizontal section rules; thin vertical separators after the stub and between model groups.
- **Spacing, visual estimate:** Compact rows but repeated subheaders preserve context after metric changes.
- **Caption/notes:** Caption above identifies benchmark and reasoning-level evaluation.
- **Comparability:** Compare models/settings within a benchmark. Accuracy, score and Elo are different scales and are not one pooled numeric series.

**Design lessons:** Repeat leaf headers when a long matrix changes metric scale. Make metric families explicit, preserving their own precision.

**Cautions:** Do not rank or average Elo together with percentages; never infer winner semantics from structural bold.

#### Table 4 — Safety rate matrix with long category labels

Anchor: physical PDF page 13; full crop `[56, 252, 539, 541]`; body measurement crop `[103, 277, 491, 497]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/gpt-oss-table-4.json`

**Measured PDF properties:** SFRM1000 9.963 pt (336 selected characters); SFBX1000 9.963 pt (50 selected characters); SFRM0700 6.974 pt (1 selected characters). Selected stroke widths: 0.542, 0.868 pt. Vector fill colors: none. Text colors: #000000, #0000FF.

- **Headers:** One tier for category and four models.
- **Row groups:** Individual safety categories; row separators appear throughout.
- **Column groups:** Four comparable rate columns.
- **Alignment:** Left category labels with multi-line wrapping; numbers align at the first line of tall rows.
- **Precision:** Three-decimal rates with trailing zeroes.
- **Missingness:** None.
- **Emphasis:** Bold headers only; no heat map or winner bolding.
- **Rules:** Top/bottom heavier rules plus a horizontal separator for every category; no vertical grid.
- **Spacing, visual estimate:** Row height follows wrapped label content. The chosen narrow stub causes conspicuous line breaks.
- **Caption/notes:** Caption above; a superscript category footnote resolves an aggregate definition below the table.
- **Comparability:** Compare same-category rates across models, retaining the aggregate category definition.

**Design lessons:** Use row separators when multi-line labels would otherwise make alignment ambiguous. Keep aggregate definitions attached to the relevant row.

**Cautions:** The source stub is heavily wrapped; a new design should first consider a wider stub rather than copy the wrap pattern.

### AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors

- ID: `auditbench`; company grouping: Anthropic; year: 2026.
- Source: https://arxiv.org/pdf/2602.22755v4
- Version: v4
- Affiliation evidence: PDF page 1 identifies Anthropic and the Anthropic Fellows Program alongside MATS and University of Freiburg; collaborative paper.
- SHA-256: `1d123f568cb93028d9af6d3829ba8403836c678d07aa0d2e80dfdc8e3b28a80d`

#### Table 1 — Behavior taxonomy

Anchor: physical PDF page 14; full crop `[106, 106, 506, 416]`; body measurement crop `[107, 107, 505, 380]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/auditbench-table-1.json`

**Measured PDF properties:** NimbusRomNo9L-Regu 9.963 pt (666 selected characters); NimbusRomNo9L-Regu 10.162 pt (287 selected characters); NimbusRomNo9L-Regu 9.793 pt (66 selected characters); NimbusRomNo9L-Regu 10.042 pt (62 selected characters). Selected stroke widths: 0.398 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** One tier for behavior name and description.
- **Row groups:** Fourteen named behaviors; no higher-order grouping.
- **Column groups:** Narrow name column and wide prose description column.
- **Alignment:** All text left aligned; descriptions wrap to variable-height rows.
- **Precision:** Not numeric.
- **Missingness:** No missing cells.
- **Emphasis:** Bold header only; black text throughout.
- **Rules:** Thin horizontal lines for each row and one vertical boundary between label and description; no full outer box.
- **Spacing, visual estimate:** Very compact prose rows; wrapped lines justify to the column in places.
- **Caption/notes:** Caption below identifies the taxonomy and scope.
- **Comparability:** This table defines categories; it contains no outcomes or ranking.

**Design lessons:** Use a taxonomy layout that prioritizes row association over numeric conventions. A single vertical divider can be useful for adjacent prose columns.

**Cautions:** Do not turn every table into a benchmark matrix or infer a corporate style from this single taxonomy.

### Automated Researchers Can Reliably Mitigate Alignment Failures

- ID: `anthropic-aar`; company grouping: Anthropic; year: 2026.
- Source: https://www-cdn.anthropic.com/7b1c44894e980876479947dcdd40716278aeeffd/automated-alignment-researchers-august-2026.pdf
- Version: official-2026-08-28
- Affiliation evidence: PDF page 1 identifies Anthropic and its Fellows Program alongside UC Berkeley; official Anthropic CDN source.
- SHA-256: `a4d6b53eb486b9335f0652a3675c1a08ccdde056df62345d3740c6c2c621fbb6`

#### Table 2 — Evaluation-suite and generalization coverage matrix

Anchor: physical PDF page 21; full crop `[106, 70, 506, 551]`; body measurement crop `[121, 99, 492, 550]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/anthropic-aar-table-2.json`

**Measured PDF properties:** NimbusRomNo9L-Regu 8.966 pt (1624 selected characters); NimbusRomNo9L-Medi 8.966 pt (67 selected characters); NimbusRomNo9L-Regu 8.895 pt (53 selected characters); NimbusRomNo9L-Regu 8.940 pt (31 selected characters). Selected stroke widths: 0.797, 0.498 pt. Vector fill colors: #F9F9F9, #FFFFFF. Text colors: #000000, #15317E.

- **Headers:** One logical tier with wrapped prose headers.
- **Row groups:** Ten alignment-failure rows, softly zebra-banded.
- **Column groups:** Failure, optimization benchmarks, held-out benchmark and generalization description.
- **Alignment:** Left/top-aligned prose with citations embedded in cells.
- **Precision:** Not numeric.
- **Missingness:** No empty-result code; task coverage is described in text.
- **Emphasis:** Bold header and blue citation links; gray bands distinguish rows, not quality.
- **Rules:** Three horizontal rules; no vertical grid.
- **Spacing, visual estimate:** Variable-height rows and long citations make a wide prose column essential.
- **Caption/notes:** Caption above defines optimization versus held-out roles.
- **Comparability:** Optimization and held-out benchmarks have different scientific roles; they should not be collapsed into a single undifferentiated list.

**Design lessons:** Represent data splits and evaluation roles as explicit columns. Let row height grow for provenance instead of shrinking citations into illegibility.

**Cautions:** Color of a citation link has no evaluation meaning.

#### Table 3 — Safety trade-off between accepted and rejected candidates

Anchor: physical PDF page 44; full crop `[106, 70, 506, 264]`; body measurement crop `[164, 129, 448, 263]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/anthropic-aar-table-3.json`

**Measured PDF properties:** NimbusRomNo9L-Regu 8.966 pt (242 selected characters); NimbusRomNo9L-Medi 8.966 pt (73 selected characters); CMR9 8.966 pt (8 selected characters); CMMI9 8.966 pt (2 selected characters). Selected stroke widths: 0.797, 0.498 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** One tier with two-line candidate headers; a headline aggregate appears in parentheses.
- **Row groups:** Ten safety dimensions.
- **Column groups:** A candidate passing every gate and a higher-scoring candidate rejected by an over-refusal gate.
- **Alignment:** Left dimensions; right-aligned percentage values.
- **Precision:** One-decimal percentages; two-decimal headline aggregate.
- **Missingness:** None.
- **Emphasis:** Bold column labels; individual values are not winner-highlighted.
- **Rules:** Three horizontal rules, no vertical boundaries.
- **Spacing, visual estimate:** A compact matrix leaves the selection criterion in the header rather than a remote footnote.
- **Caption/notes:** Caption above explains headroom closed, coverage-weighted geometric aggregation and rejection status.
- **Comparability:** A larger aggregate score does not make a gated-out candidate an acceptable deployment choice. Per-dimension percentages and the weighted aggregate have different meanings.

**Design lessons:** Expose feasibility/gating status before showing the numeric comparison. Keep aggregate construction next to the headline value.

**Cautions:** Do not automatically bold the rejected candidate merely because it has the larger aggregate.

### Auditing language models for hidden objectives

- ID: `hidden-objectives`; company grouping: Anthropic; year: 2025.
- Source: https://arxiv.org/pdf/2503.10965v2
- Version: v2
- Affiliation evidence: PDF page 1 identifies Anthropic and MATS and explains that authors worked at Anthropic except as noted.
- SHA-256: `6cea87ef4a49ef861ce9c37a3aeef3d82dced5c70028a5b924211bb27773b60a`

#### Table 1 — Audit-team resources, access and outcome comparison

Anchor: physical PDF page 8; full crop `[106, 68, 505, 310]`; body measurement crop `[110, 69, 502, 225]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/hidden-objectives-table-1.json`

**Measured PDF properties:** NimbusRomNo9L-Regu 7.970 pt (284 selected characters); NimbusRomNo9L-Regu 8.130 pt (56 selected characters); NimbusRomNo9L-Regu 7.851 pt (47 selected characters); NimbusRomNo9L-Regu 7.811 pt (11 selected characters). Selected stroke widths: 0.545, 0.873 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** One tier; long total-effort header wraps.
- **Row groups:** Four teams; resource affordances appear as multi-line lists.
- **Column groups:** Access conditions, solution path, serial elapsed time and total researcher-hours.
- **Alignment:** Left-aligned prose; small numeric columns use simple aligned positions.
- **Precision:** Mixed integer and one-decimal hours; plus signs indicate lower bounds.
- **Missingness:** Failed search is shown as an explicit outcome; ongoing effort uses lower-bound notation.
- **Emphasis:** Check and cross symbols encode allowed resources or failure; they are not colored.
- **Rules:** Top/bottom rules and separators between teams; no vertical grid.
- **Spacing, visual estimate:** Variable-height rows preserve access-condition lists and a sentence-length outcome.
- **Caption/notes:** Caption below defines time measures; an immediate asterisk footnote clarifies effective access for one team.
- **Comparability:** Teams had different affordances; elapsed time and total labor are different units. A failed result after a time budget is censored, not a completed time-to-discovery.

**Design lessons:** Keep experimental affordances and result status in the same table. Support explicit lower-bound and failure notation.

**Cautions:** Do not rank elapsed time against researcher-hours or replace failed discovery with zero.

#### Table 2 — Qualitative examples paired with ranked interpretability measurements

Anchor: physical PDF page 50; full crop `[106, 126, 506, 659]`; body measurement crop `[107, 127, 505, 574]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/hidden-objectives-table-2.json`

**Measured PDF properties:** NimbusRomNo9L-Regu 7.970 pt (681 selected characters); NimbusRomNo9L-Medi 7.970 pt (204 selected characters); NimbusRomNo9L-Regu 7.811 pt (25 selected characters); NimbusRomNo9L-Regu 7.866 pt (22 selected characters). Selected stroke widths: 0.398, 0.545, 0.873 pt. Vector fill colors: none. Text colors: #000000, #0000FF, #FF0000.

- **Headers:** Two header tiers: three rank families with paired settings.
- **Row groups:** Six prompt/response examples with explicit train/test labels.
- **Column groups:** Wide sample and bias columns; narrow rank blocks.
- **Alignment:** Long examples align left/top; integers and dash symbols occupy compact rank columns.
- **Precision:** Integer ranks.
- **Missingness:** A dash means no relevant feature ranked in the top 100; it is a censored rank, not unmeasured data.
- **Emphasis:** Blue marks specific tokens and training labels; red marks test labels; bold identifies a targeted span. Color carries several declared roles.
- **Rules:** Horizontal row separators and vertical boundaries between semantic column groups.
- **Spacing, visual estimate:** Tall rows let prose examples coexist with narrow numeric columns; density makes footnote definitions critical.
- **Caption/notes:** Caption below defines the ranking procedures, colored text, bold text and dash semantics.
- **Comparability:** Rank columns use distinct identification procedures. A dash is not comparable as zero or a missing-value average exclusion without a censoring policy.

**Design lessons:** Let missing-value codes represent typed statuses such as censored rank. Keep prose context when measurements depend on particular sample spans.

**Cautions:** Do not infer one global color meaning; do not treat rank outside top 100 as rank 101 unless explicitly defined.

### Reasoning Models Don't Always Say What They Think

- ID: `reasoning-faithfulness`; company grouping: Anthropic; year: 2025.
- Source: https://arxiv.org/pdf/2505.05410v1
- Version: v1
- Affiliation evidence: PDF page 1 identifies the Alignment Science Team at Anthropic.
- SHA-256: `546afa672e0c50d50b7c86b7dbacb6f51d200be74f33577012d98cb18eee7600`

#### Table 1 — Hint taxonomy with examples

Anchor: physical PDF page 5; full crop `[106, 70, 506, 423]`; body measurement crop `[112, 71, 497, 386]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/reasoning-faithfulness-table-1.json`

**Measured PDF properties:** NimbusRomNo9L-Regu 9.146 pt (388 selected characters); NimbusRomNo9L-Regu 8.966 pt (325 selected characters); NimbusRomNo9L-Regu 8.787 pt (205 selected characters); NimbusRomNo9L-Regu 8.975 pt (42 selected characters). Selected stroke widths: 0.398, 0.299, 0.797, 0.498 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** One tier across category, hint type, description and example.
- **Row groups:** Neutral and misaligned categories span multiple hint rows.
- **Column groups:** Wide example column plus shorter taxonomy and description columns.
- **Alignment:** Left/top-aligned text; category cells span rows; some tight prose is visibly justified.
- **Precision:** Not numeric.
- **Missingness:** No missing cells.
- **Emphasis:** Bold header; examples include symbol and code-like text but no performance emphasis.
- **Rules:** Vertical dividers between columns; partial horizontal lines within categories and stronger full-width category separation.
- **Spacing, visual estimate:** Variable row heights; long embedded examples wrap across multiple lines.
- **Caption/notes:** Caption below summarizes category counts and roles.
- **Comparability:** This defines experimental conditions rather than estimates; category count is not sample count.

**Design lessons:** Use rowspans and partial rules for a genuine hierarchy. Keep example prose in a wider column than its category label.

**Cautions:** Avoid replicating cramped justification or deep wrapping when a wider/landscape alternative is available.

### SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents

- ID: `shade-arena`; company grouping: Anthropic; year: 2025.
- Source: https://arxiv.org/pdf/2506.15740v2
- Version: v2
- Affiliation evidence: PDF page 1 explicitly affiliates two coauthors with Anthropic; other coauthors have independent, Scale AI, Redwood Research, Reduct Video or Constellation affiliations. Company grouping is inclusive, not exclusive.
- SHA-256: `f9c1656907b7387faad5099d405d048a0346071bea8dbffc0b68962a278330f4`

#### Table 2 — Sampling inventory

Anchor: physical PDF page 24; full crop `[192, 77, 419, 295]`; body measurement crop `[208, 99, 404, 293]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/shade-arena-table-2.json`

**Measured PDF properties:** NimbusRomNo9L-Regu 9.963 pt (259 selected characters); NimbusRomNo9L-Medi 9.963 pt (20 selected characters). Selected stroke widths: 0.398, 0.797, 0.498 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** One tier; the sample-count header wraps over three lines.
- **Row groups:** Thirteen model-version rows.
- **Column groups:** Model identifier and samples per transcript type per task.
- **Alignment:** Model strings left aligned; integer sample counts centered.
- **Precision:** Integer counts.
- **Missingness:** None.
- **Emphasis:** Bold header only; no ranking.
- **Rules:** Horizontal rule at every row, a header separator and a double-looking bottom boundary; no vertical lines.
- **Spacing, visual estimate:** A tall header buys a narrow table while retaining exact versioned model IDs.
- **Caption/notes:** Caption above states the sampling unit; surrounding methodology discusses averaging over tasks.
- **Comparability:** Sample counts vary across models and are counts per sampling unit, not total benchmark size.

**Design lessons:** Record the denominator unit explicitly in the caption. Preserve full model versions in a sampling inventory.

**Cautions:** Do not assume identical measurement precision when sampling counts differ.

### System Card: Claude Sonnet 5

- ID: `sonnet5-system`; company grouping: Anthropic; year: 2026.
- Source: https://www-cdn.anthropic.com/283ef97c476cf442c91d9a37d5b214242a55bb92/Claude%20Sonnet%205%20System%20Card.pdf
- Version: Official CDN PDF; cover dated 2026-06-30; retrieved 2026-10-21
- Affiliation evidence: PDF cover identifies anthropic.com; downloaded from the official Anthropic CDN.
- SHA-256: `33573adb9f1871b903f79b77d7755a44cc20bb913ef48ac9000ddb090e41f7ed`

#### Table 4.1.1.A — Safety comparison across deployment conditions

Anchor: physical PDF page 37; full crop `[70, 70, 542, 378]`; body measurement crop `[71, 71, 541, 299]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/sonnet5-system-table-4.1.1.a.json`

**Measured PDF properties:** Lora-Bold 10.995 pt (261 selected characters); Lora-Regular 10.995 pt (154 selected characters). Selected stroke widths: 0.750 pt. Vector fill colors: #141413, #DEDCD1, #F3F3F3, #FFFFFF. Text colors: #FAF9F5, #FFFFFF, #000000.

- **Headers:** One logical tier with tall multi-line headers.
- **Row groups:** Six model rows.
- **Column groups:** Two deployment conditions: API without system prompt and the product setting.
- **Alignment:** All cells left aligned, including uncertainty composites.
- **Precision:** Two-decimal percentages and two-decimal parenthesized plus/minus margins.
- **Missingness:** N/A reflects unavailable product deployment for some models; two such cells are lightly shaded.
- **Emphasis:** White bold header on near-black fill; tinted bold model stub; best per column bold and second-best underlined, declared in caption.
- **Rules:** Full rectangular grid with outer box.
- **Spacing, visual estimate:** Generous padding and variable-height model rows support a report reading size rather than a compact conference matrix.
- **Caption/notes:** Caption below explains direction, rank emphasis, languages, unavailable deployments and evaluation updates.
- **Comparability:** Rank within each deployment column. Different system-prompt conditions are not interchangeable; earlier system-card values may use different evaluation revisions.

**Design lessons:** Provide a report-table variant with stronger boundaries when long headers and uncertainty dominate. Keep deployment conditions and missingness reasons visible.

**Cautions:** A ranked mean is not a significance claim; the table margin type must be carried from methodology, not guessed from the ± sign.

#### Table 4.1.2.A — Over-refusal comparison with opposite metric direction

Anchor: physical PDF page 38; full crop `[70, 70, 542, 362]`; body measurement crop `[71, 71, 541, 283]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/sonnet5-system-table-4.1.2.a.json`

**Measured PDF properties:** Lora-Bold 10.995 pt (254 selected characters); Lora-Regular 10.995 pt (129 selected characters). Selected stroke widths: 0.750 pt. Vector fill colors: #141413, #DEDCD1, #FFFFFF. Text colors: #FAF9F5, #FFFFFF, #000000.

- **Headers:** One tier with wrapped deployment-condition headers.
- **Row groups:** Six model rows; same order as the preceding safety table.
- **Column groups:** Two deployment conditions reused from the preceding table.
- **Alignment:** Left-aligned labels and numeric composites.
- **Precision:** Two-decimal percentages with parenthesized margins.
- **Missingness:** N/A for unavailable product deployment.
- **Emphasis:** Full report styling repeats; bold marks the lowest over-refusal rate, including tied lowest values; underline marks the next distinct rate.
- **Rules:** Full grid and outer border.
- **Spacing, visual estimate:** Consistent row/padding language supports reading as a pair with Table 4.1.1.A.
- **Caption/notes:** Caption below explicitly reverses the desirable direction and reiterates evaluation-update caveats.
- **Comparability:** Lower is desirable here while higher was desirable for harmless-response rate. The table pair should never share an untyped default ranking direction.

**Design lessons:** Make metric direction part of each result column, even in adjacent tables. Resolve ties before assigning second-best formatting.

**Cautions:** Do not carry a higher-is-better rule from the previous table.

### Phi-4-reasoning-vision-15B Technical Report

- ID: `phi-vision`; company grouping: Microsoft Research; year: 2026.
- Source: https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/Phi-4-reasoning-vision-15B-Tech-Report.pdf
- Version: Official PDF; cover dated 2026-03-04; retrieved 2026-10-21
- Affiliation evidence: PDF page 1 identifies Microsoft Research.
- SHA-256: `eb2b08149058f4e73c25bb5e0e1ae5fc033e6ee1fde3576dd88100f184f590dc`

#### Table 2 — Training-stage configuration

Anchor: physical PDF page 5; full crop `[69, 67, 543, 155]`; body measurement crop `[120, 90, 491, 154]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/phi-vision-table-2.json`

**Measured PDF properties:** URWPalladioL-Roma 8.966 pt (129 selected characters); URWPalladioL-Bold 8.966 pt (28 selected characters); MSAM10 9.343 pt (7 selected characters). Selected stroke widths: 0.797, 0.498 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** One tier for stage, trainable modules and data description.
- **Row groups:** Three ordered training stages.
- **Column groups:** Three module-status columns between stage name and data.
- **Alignment:** Left stage/data text; centered status glyphs.
- **Precision:** Categorical status, no numerical results.
- **Missingness:** Cross means frozen, not absent or failed.
- **Emphasis:** Bold header only; check/cross symbols are black and explained in caption.
- **Rules:** Three horizontal rules, no vertical grid.
- **Spacing, visual estimate:** Compact single-line stage rows keep the progression easy to scan.
- **Caption/notes:** Caption above provides the symbol legend.
- **Comparability:** The statuses describe training configuration; they cannot be read as pass/fail results.

**Design lessons:** Use explicit symbol legends for configuration matrices. Preserve the ordered training-stage sequence.

**Cautions:** The same cross glyph can mean frozen, unsupported or failure elsewhere; require a local legend.

#### Table 6 — Wide benchmark matrix with model configurations

Anchor: physical PDF page 14; full crop `[69, 69, 543, 260]`; body measurement crop `[70, 90, 542, 258]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/phi-vision-table-6.json`

**Measured PDF properties:** URWPalladioL-Roma 8.440 pt (380 selected characters); URWPalladioL-Bold 8.440 pt (205 selected characters); URWPalladioL-Roma 6.564 pt (25 selected characters). Selected stroke widths: 0.750, 0.469 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** One logical tier, with model names and reasoning settings wrapped over several lines.
- **Row groups:** Ten benchmarks.
- **Column groups:** Model columns include forced-thinking and token-budget variants.
- **Alignment:** Left benchmark labels; centered numerical results.
- **Precision:** Mostly one-decimal scores, with some integer-looking entries retained.
- **Missingness:** None in selected table.
- **Emphasis:** Bold header labels, regular numeric values; no winner encoding.
- **Rules:** Three horizontal rules, no vertical grid.
- **Spacing, visual estimate:** The header is much taller than body rows; compact model-name wrapping preserves width at the cost of reading effort.
- **Caption/notes:** Short caption above; immediately following prose explains evaluation settings and intended comparison purpose.
- **Comparability:** Reasoning and output budgets differ in the headers. Compare under declared settings; the report explicitly contextualizes fairness and avoids a blanket leaderboard interpretation.

**Design lessons:** Keep materially different budgets in model headers or a configuration field. Allow structural emphasis without ranking emphasis.

**Cautions:** Do not conceal budget differences under shortened model labels; do not invent trailing decimals that the data do not supply.

### SkillOpt: Executive Strategy for Self-Evolving Agent Skills

- ID: `skillopt`; company grouping: Microsoft Research; year: 2026.
- Source: https://arxiv.org/pdf/2605.23904v2
- Version: v2
- Affiliation evidence: PDF page 1 identifies Microsoft alongside Shanghai Jiao Tong, Tongji and Fudan universities; collaborative paper.
- SHA-256: `87f7f0f323b1671e9202b3ebb1596e909e507c71ecd1b360b0075a5ee1727fe3`

#### Table 1 — Dense benchmark matrix with nested blocks and change annotations

Anchor: physical PDF page 7; full crop `[66, 60, 532, 796]`; body measurement crop `[67, 61, 530, 714]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/skillopt-table-1.json`

**Measured PDF properties:** LMRoman8-Regular 7.970 pt (1658 selected characters); LMRoman6-Regular 5.978 pt (1253 selected characters); LMRomanDemi10-Regular 7.970 pt (398 selected characters); LMMathSymbols6-Regular 5.978 pt (45 selected characters). Selected stroke widths: 0.398, 0.327, 0.545, 0.873 pt. Vector fill colors: #EBEBFF, #EDEDED. Text colors: #000000, #0E8A4A, #B91C1C.

- **Headers:** One leaf header tier for benchmark columns; model and harness form nested row groups.
- **Row groups:** Harness bands span the table; model blocks repeat skill-source rows; focal-method rows are tinted.
- **Column groups:** Six benchmark columns follow model and skill-source fields.
- **Alignment:** Left model/method labels; compact numerical entries combine a primary score with a small signed change annotation.
- **Precision:** Main scores one decimal; signed changes one decimal.
- **Missingness:** Dash for benchmark/harness combinations omitted because the task requires an unavailable persistent environment.
- **Emphasis:** Bold means best within the model/harness block and benchmark; underline means second-best. Blue tint identifies focal-method rows. Green/red small changes encode signed change from the matched no-skill baseline.
- **Rules:** Main top/bottom rules, harness separators, light model-block boundaries and underline strokes; no numeric-cell vertical grid.
- **Spacing, visual estimate:** Extremely dense full-page matrix: body near 8 pt, change annotations near 6 pt in the PDF.
- **Caption/notes:** Caption below defines percentage scale, ranking scope, row tint, signed changes and omitted environments.
- **Comparability:** Baseline for each delta is the same model in the same harness. Neither deltas nor best marks should cross block boundaries.

**Design lessons:** Treat score and signed delta as distinct fields, never as mean and uncertainty. Make nested comparison scope machine-readable before automatic best/second-best emphasis.

**Cautions:** Do not copy the tiny annotation scale as a default; red/green sign encoding needs textual +/− redundancy.

#### Table 2 — Hyperparameter small-multiple tables

Anchor: physical PDF page 8; full crop `[66, 61, 531, 246]`; body measurement crop `[70, 62, 524, 188]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/skillopt-table-2.json`

**Measured PDF properties:** LMRomanDemi10-Regular 7.117 pt (392 selected characters); LMRoman8-Regular 7.117 pt (369 selected characters). Selected stroke widths: 0.780, 0.487 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** Six labeled panels arranged in a two-by-three grid; each repeats setting and three benchmark columns.
- **Row groups:** Each panel varies a different scalar or schedule; settings are ordered locally.
- **Column groups:** The same three outcomes repeat across panels.
- **Alignment:** Left setting labels; aligned compact numerical columns.
- **Precision:** One decimal.
- **Missingness:** No missing values in selected panels.
- **Emphasis:** Bold selectively marks high values in each panel/benchmark; panel labels and headers are bold.
- **Rules:** Each panel independently uses top/header/bottom rules; open white gutters separate panels.
- **Spacing, visual estimate:** Very compact panels with approximately 7.12 pt PDF text; consistent widths and baselines support side-by-side reading.
- **Caption/notes:** One caption below explains held-constant defaults and special split/sample meanings.
- **Comparability:** Panels vary different factors. The training-data panel also changes subset size and selection protocol as described; cross-panel apparent optima are not a factorial interaction analysis.

**Design lessons:** Use aligned mini-tables for several short, repeated sweeps. State what stays fixed and name exceptions.

**Cautions:** Do not interpret independent one-factor sweeps as jointly optimized settings.

#### Table 3 — Component ablation with baseline rows

Anchor: physical PDF page 8; full crop `[67, 255, 531, 421]`; body measurement crop `[84, 256, 511, 365]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/skillopt-table-3.json`

**Measured PDF properties:** LMRoman8-Regular 8.998 pt (243 selected characters); LMRomanDemi10-Regular 8.998 pt (84 selected characters). Selected stroke widths: 0.986, 0.369, 0.615 pt. Vector fill colors: #EBEBFF. Text colors: #000000.

- **Headers:** One tier: component, setting and three outcomes.
- **Row groups:** Three component blocks, each repeating a highlighted default row.
- **Column groups:** Three benchmark score columns.
- **Alignment:** Left component/setting labels; centered numerical values.
- **Precision:** One decimal.
- **Missingness:** None.
- **Emphasis:** Light-blue tint marks defaults; bold means best within each component block and benchmark. Those are separate semantics.
- **Rules:** Top/header/bottom rules and partial/light component separators; no vertical grid.
- **Spacing, visual estimate:** Repeated component labels are omitted within groups; concise rows maintain legibility.
- **Caption/notes:** Caption below defines default configuration, ranking scope and a special matching rule for a rejected-buffer ablation.
- **Comparability:** Compare settings within one component block; defaults repeat and are not independent replicate measurements.

**Design lessons:** Keep baseline shading independent of best-value emphasis. Represent ablation grouping explicitly, including repeated reference rows.

**Cautions:** Do not average repeated defaults or imply all ablations vary only one thing when matching exceptions are stated.

#### Table 6 — Optimization cost and artifact-size inventory

Anchor: physical PDF page 14; full crop `[66, 212, 531, 356]`; body measurement crop `[132, 213, 464, 301]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/skillopt-table-6.json`

**Measured PDF properties:** LMRoman9-Regular 8.966 pt (157 selected characters); LMRomanDemi10-Regular 8.966 pt (54 selected characters). Selected stroke widths: 0.873, 0.545 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** One tier with abbreviated units in column headers.
- **Row groups:** Six benchmark rows.
- **Column groups:** Initial/final artifact size, accepted edit count, training tokens and cost per gain point.
- **Alignment:** Left benchmark names; centered numbers with grouped thousands where relevant.
- **Precision:** Integers for lengths/edits; one-decimal millions for token quantities.
- **Missingness:** None.
- **Emphasis:** Bold header only; no minima highlight.
- **Rules:** Three horizontal rules, no vertical grid.
- **Spacing, visual estimate:** Compact six-column table; caption expands economical header abbreviations.
- **Caption/notes:** Caption below defines accepted edits and token cost per absolute test-point gain.
- **Comparability:** The cost-per-point column is a token ratio, not dollars. Different tasks and gains mean smallest raw token count is not automatically the most effective run.

**Design lessons:** Put units and denominator definitions next to cost fields. Separate effort, output size and normalized efficiency.

**Cautions:** Never relabel token cost as monetary cost or omit the gain denominator.

### Agent Lightning: Train ANY AI Agents with Reinforcement Learning

- ID: `agent-lightning`; company grouping: Microsoft Research; year: 2025.
- Source: https://arxiv.org/pdf/2508.03680v1
- Version: v1
- Affiliation evidence: PDF page 1 identifies Microsoft Research.
- SHA-256: `e223648a09b021785a46f60dd5ce13301622eca930ff91a5b45e971b53422561`

#### Table 1 — Task and experimental-configuration overview

Anchor: physical PDF page 11; full crop `[124, 580, 471, 682]`; body measurement crop `[125, 602, 470, 681]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/agent-lightning-table-1.json`

**Measured PDF properties:** URWPalladioL-Roma 9.963 pt (148 selected characters); URWPalladioL-Bold 9.963 pt (33 selected characters). Selected stroke widths: 0.797, 0.498 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** One tier: three task columns across a left attribute stub.
- **Row groups:** Framework, dataset, tool, agent count and fine-tuned-agent count form attribute rows.
- **Column groups:** Three task settings.
- **Alignment:** Attribute labels left aligned; task values centered.
- **Precision:** Integer counts; other cells categorical.
- **Missingness:** None.
- **Emphasis:** Bold column headers only.
- **Rules:** Three horizontal rules, no vertical grid.
- **Spacing, visual estimate:** Compact and narrow enough for a single-column reading context.
- **Caption/notes:** Caption above identifies the experimental setup.
- **Comparability:** Task columns use different datasets, tools and frameworks. The table describes conditions, not comparable success rates.

**Design lessons:** Transpose a setup comparison so shared attributes become rows. Keep numeric counts visually consistent without ranking them.

**Cautions:** Agent count is a configuration variable, not a result to optimize automatically.

### Fara-7B: An Efficient Agentic Model for Computer Use

- ID: `fara`; company grouping: Microsoft Research; year: 2025.
- Source: https://arxiv.org/pdf/2511.19663v1
- Version: v1
- Affiliation evidence: Microsoft Research official publication page identifies Microsoft as publisher (MSR-TR-2025-54); PDF page 1 links official microsoft repositories and model assets.
- SHA-256: `06a6b28b6fb088e7c65bf2fc4094078c13b97a8cef17f2ad9ed404caf6aff586`

#### Table 4 — Cumulative pipeline ablation

Anchor: physical PDF page 9; full crop `[69, 71, 543, 239]`; body measurement crop `[167, 72, 445, 189]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/fara-table-4.json`

**Measured PDF properties:** URWPalladioL-Roma 8.966 pt (159 selected characters); URWPalladioL-Bold 8.966 pt (52 selected characters). Selected stroke widths: 0.498, 0.797 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** One tier, with the modification header on two lines.
- **Row groups:** Ordered baseline followed by indented plus-prefixed additions.
- **Column groups:** Modification, model used by the web component and success rate.
- **Alignment:** Left modification labels with indentation; centered component/model and percentage.
- **Precision:** Integer percentages.
- **Missingness:** None.
- **Emphasis:** Bold headers; no bolded final value or color.
- **Rules:** Header and bottom rules; no top enclosing rule and no vertical grid.
- **Spacing, visual estimate:** Short single-line rows give the accumulation sequence more weight than numeric precision.
- **Caption/notes:** Caption below explicitly calls the ablation cumulative and describes the starting pipeline.
- **Comparability:** Rows accumulate changes, including model changes. Adjacent differences are conditional on prior additions and are not independent component effects.

**Design lessons:** Provide a dedicated cumulative-ablation recipe with visible ordering. Record changed model/configuration columns alongside the added component.

**Cautions:** Do not describe these rows as a one-factor ablation or sum their deltas as independent causal effects.

#### Table 9 — Agent benchmark comparison with model-type blocks

Anchor: physical PDF page 16; full crop `[69, 68, 544, 213]`; body measurement crop `[80, 70, 533, 180]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/fara-table-9.json`

**Measured PDF properties:** URWPalladioL-Roma 8.966 pt (240 selected characters); URWPalladioL-Bold 8.966 pt (29 selected characters); URWPalladioL-Ital 8.966 pt (26 selected characters); URWPalladioL-Bold 8.787 pt (22 selected characters). Selected stroke widths: 0.996, 0.398 pt. Vector fill colors: #F2F2F2. Text colors: #000000.

- **Headers:** One tier for model, parameter count and four benchmark results.
- **Row groups:** Two labeled model-type blocks; the first is lightly shaded.
- **Column groups:** Parameter count is separated conceptually from benchmark scores.
- **Alignment:** Left model names; centered parameters and numeric results.
- **Precision:** One-decimal success rates; model sizes use B suffix.
- **Missingness:** N/A denotes unavailable parameter counts for proprietary models.
- **Emphasis:** Italic model-type labels and gray block shading; no numeric best marks.
- **Rules:** Header rule and a divider between model types; no full outer box or body grid.
- **Spacing, visual estimate:** Compact rows; section labels occupy their own centered line.
- **Caption/notes:** Caption below identifies success-rate metrics and the two agent families; following methods explain live-site controls.
- **Comparability:** Benchmark columns are different task distributions, and model types differ in interface. The nearby methodology describes repeated live-site runs, retries and budgets.

**Design lessons:** Use blocks to make model/interface families explicit. Distinguish unavailable metadata from missing benchmark scores.

**Cautions:** Do not average four benchmark columns without a declared weighting or hide different agent interfaces.

#### Table 10 — Cost-accuracy-effort comparison

Anchor: physical PDF page 17; full crop `[69, 70, 543, 238]`; body measurement crop `[72, 72, 540, 198]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/fara-table-10.json`

**Measured PDF properties:** URWPalladioL-Roma 8.966 pt (343 selected characters); URWPalladioL-Bold 8.966 pt (72 selected characters); CMSY10 9.343 pt (26 selected characters); URWPalladioL-Ital 8.966 pt (26 selected characters). Selected stroke widths: 0.996, 0.398 pt. Vector fill colors: #F2F2F2. Text colors: #000000.

- **Headers:** One tier with wrapped units and arrows in each quantitative header.
- **Row groups:** Same two agent-family blocks as the benchmark table.
- **Column groups:** Cost, accuracy, action count, input tokens and output tokens.
- **Alignment:** Left model names; centered estimates, including plus/minus composites.
- **Precision:** Three-decimal currency cost; one-decimal accuracy/actions; tokens abbreviated in thousands with varying displayed precision.
- **Missingness:** None in this selected table.
- **Emphasis:** Gray shading identifies one agent family; italic block labels. No automatic winner bolding.
- **Rules:** Header rule and family divider, with open edges and no numeric-cell grid.
- **Spacing, visual estimate:** Wrapped headers carry units/direction without forcing wide columns.
- **Caption/notes:** Caption below identifies per-task quantities; accompanying prose describes cost assumptions and token counting.
- **Comparability:** Cost and action/token counts are lower-is-better; accuracy higher-is-better. Efficiency depends on price assumptions, task distribution and full token accounting.

**Design lessons:** Give every efficiency column its own direction and unit. Keep accuracy beside resource consumption so trade-offs remain visible.

**Cautions:** Do not infer the uncertainty type from ± alone; pricing-based efficiency is a dated scenario, not a timeless property.

### Magma: A Foundation Model for Multimodal AI Agents

- ID: `magma`; company grouping: Microsoft Research; year: 2025.
- Source: https://arxiv.org/pdf/2502.13130v1
- Version: v1
- Affiliation evidence: PDF page 1 identifies Microsoft Research alongside collaborating universities.
- SHA-256: `df8e92d42a6b14f4298711d300fb23547bb95a2a1c9a81d6b3287ce96103b994`

#### Table 2 — Cross-domain capability matrix

Anchor: physical PDF page 9; full crop `[57, 69, 555, 257]`; body measurement crop `[59, 70, 554, 208]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/magma-table-2.json`

**Measured PDF properties:** NimbusRomNo9L-Regu 6.988 pt (593 selected characters); NimbusRomNo9L-Medi 6.988 pt (123 selected characters); NimbusMonL-Regu 6.988 pt (5 selected characters); NimbusRomNo9L-ReguItal 6.988 pt (4 selected characters). Selected stroke widths: 0.279, 0.349, 0.559 pt. Vector fill colors: none. Text colors: #000000, #367DBD.

- **Headers:** Two tiers: three capability families span individual task columns.
- **Row groups:** Models are separated into several capability-family blocks; focal model appears at the bottom.
- **Column groups:** Understanding, interface interaction and robotic manipulation form explicit column groups.
- **Alignment:** Left model labels; compact centered results and metadata.
- **Precision:** Mostly one decimal; some cells contain slash-separated paired submetrics.
- **Missingness:** n/a means unavailable; dash means unsupported, explicitly distinguished in the caption.
- **Emphasis:** Selected best-looking numbers bold and some underlined; the caption does not provide a complete ranking legend, so the intended underline rule is not assumed.
- **Rules:** Horizontal group separators and sparse vertical structure around the model/size stub; no full numeric-cell grid.
- **Spacing, visual estimate:** Very dense full-width table, approximately 6.99 pt body text; abbreviated task names require caption decoding.
- **Caption/notes:** Caption below expands task abbreviations, states zero-shot evaluation scope and defines both missingness codes.
- **Comparability:** Different domains and paired submetrics do not share a single scale. Unsupported capability and unavailable results are different evidence states.

**Design lessons:** Use column spanners for genuinely different capability domains. Preserve typed missingness and composite metric schemas.

**Cautions:** Do not merge dash and n/a or infer an undocumented best/runner-up rule.

#### Table 7 — Compact multimodal ablation and baseline comparison

Anchor: physical PDF page 11; full crop `[315, 69, 555, 177]`; body measurement crop `[317, 70, 554, 129]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/magma-table-7.json`

**Measured PDF properties:** NimbusRomNo9L-Regu 5.847 pt (257 selected characters); NimbusRomNo9L-Medi 5.847 pt (30 selected characters); NimbusMonL-Regu 5.847 pt (20 selected characters); NimbusRomNo9L-Regu 4.093 pt (6 selected characters). Selected stroke widths: 0.234, 0.292 pt. Vector fill colors: none. Text colors: #000000, #367DBD.

- **Headers:** One tier with seven benchmark columns.
- **Row groups:** Two external baselines followed by four focal-model training variants.
- **Column groups:** Benchmarks include different score scales.
- **Alignment:** Left model names; compact centered values.
- **Precision:** One decimal across displayed score columns, despite differing ranges.
- **Missingness:** None.
- **Emphasis:** Bold marks selected column-leading values; one ablation variant uses a small superscript marker. No tint.
- **Rules:** Header/section rules and a vertical divider after the stub; no outer box.
- **Spacing, visual estimate:** Body measures approximately 5.85 pt with approximately 4.09 pt superscript text; readable in enlarged crop but crowded at native paper size.
- **Caption/notes:** Caption below explains the variant comparison at a high level.
- **Comparability:** Compare within benchmark columns; a benchmark with a thousand-scale score cannot be averaged with percentage-like scores without a defined transformation.

**Design lessons:** Separate external baselines from controlled training variants. Inspect native-size legibility, not only an enlarged crop.

**Cautions:** Do not copy this very small typography as a default for a new table.

### Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Language Models via Mixture-of-LoRAs

- ID: `phi-mini`; company grouping: Microsoft Research; year: 2025.
- Source: https://arxiv.org/pdf/2503.01743v1
- Version: v1
- Affiliation evidence: PDF page 1 lists Microsoft as the institutional author.
- SHA-256: `e13bf559aee1a1e1295c068b2c99d3cb71e82a65a76bf988ce77755806a86c81`

#### Table 3 — Speech benchmark matrix with mixed metric directions

Anchor: physical PDF page 12; full crop `[58, 58, 554, 282]`; body measurement crop `[72, 128, 538, 280]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/phi-mini-table-3.json`

**Measured PDF properties:** CMR6 5.978 pt (602 selected characters); CMBX6 5.978 pt (58 selected characters); NimbusMonL-Regu 5.978 pt (16 selected characters); MnSymbol6 5.978 pt (7 selected characters). Selected stroke widths: 0.545, 0.873 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** Two conceptual tiers: model identities with size labels, plus task/metric/dataset row structure.
- **Row groups:** Task groups carry their metric and direction; one group includes a decoding-mode row.
- **Column groups:** Six model columns, with some focal-model cells showing two decoding settings.
- **Alignment:** Left task/metric descriptors; centered dataset names and numeric scores.
- **Precision:** Two decimals; paired values preserve a fixed stated ordering.
- **Missingness:** N/A means the model lacks the capability, stated in caption.
- **Emphasis:** Bold selected leading scores; arrows show metric direction separately.
- **Rules:** Top/bottom rules, header separator and task-group rules; no vertical grid.
- **Spacing, visual estimate:** Very dense, approximately 5.98 pt table text, with expanded multi-line caption above.
- **Caption/notes:** Caption defines decoding exceptions, judge/aggregation details and the unavailable-capability code.
- **Comparability:** Metrics include error rate, translation quality, accuracy and judged scores on different ranges. One model has both zero-shot and CoT values where others show zero-shot only.

**Design lessons:** Represent each metric direction and scale explicitly. Treat paired results and decoding modes as structured fields.

**Cautions:** Do not compare the better of two decoding modes against a single-mode baseline without disclosure; avoid shrinking to the source font size.

#### Table 7 — Dense language benchmark matrix

Anchor: physical PDF page 18; full crop `[58, 137, 554, 623]`; body measurement crop `[59, 138, 554, 578]`.
Crop: （research image omitted; regenerate from the recorded PDF page and crop）
Measurement record: `measurements/openai-anthropic-microsoft/phi-mini-table-7.json`

**Measured PDF properties:** CMR10 6.678 pt (993 selected characters); CMR6 3.659 pt (388 selected characters); CMR12 7.319 pt (156 selected characters); CMBX10 6.678 pt (47 selected characters). Selected stroke widths: 0.244 pt. Vector fill colors: none. Text colors: #000000.

- **Headers:** Two conceptual tiers: model names and sizes; benchmark labels include smaller protocol notes.
- **Row groups:** Benchmark families separated by horizontal rules; a final aggregate row.
- **Column groups:** Ten model columns.
- **Alignment:** Centered benchmark labels and numbers; single-decimal numeric columns are visually regular.
- **Precision:** One decimal for scores and aggregate.
- **Missingness:** No missing cells in selected matrix.
- **Emphasis:** The entire aggregate row is bold; individual best cells are not systematically emphasized.
- **Rules:** Thin horizontal rules at family boundaries and a double vertical boundary after the benchmark stub.
- **Spacing, visual estimate:** Primary numeric text measures approximately 6.68 pt; protocol notes around 3.66 pt and some symbols near 3.05 pt.
- **Caption/notes:** Caption below names compared model families; benchmark-specific protocols sit in tiny labels.
- **Comparability:** Shot counts, prompting and benchmark families differ by row. The reported aggregate is source-defined; it is not a generic license to average any benchmark collection.

**Design lessons:** Treat aggregate-row emphasis as a separate semantic choice from best-value highlighting. Move tiny protocol notes to a readable note block or split the matrix when redesigning.

**Cautions:** Do not copy near-3-point notes; do not invent an unweighted aggregate for new data.

## Measurement limits and implementation implications

Font names are extracted from the source PDF; they are not a recommendation to bundle a proprietary font. Microtypographic expansion can yield slightly different nominal sizes for otherwise similar text. Vector width counts include underlines when present; they do not by themselves classify which stroke is a top rule, separator, or emphasis line. Display crops include the explanatory caption, while quantitative style measurements are restricted to table-body regions.

A reusable generator should require structured fields for metric, unit, direction, precision, uncertainty kind, comparison group, missingness status, aggregate definition, ranking scope and ties. It should expose independent presentation roles for structural headers, focal methods, defaults, best/second-best values and positive/negative deltas. A visual verification pass should inspect final-width/native-size readability and ensure no clipped text, malformed spans, ambiguous abbreviations or inconsistent cell alignments.

The measured sizes range from readable report text near 11 pt down to highly compressed matrix notes near 3 pt. This range is evidence of trade-offs in published artifacts, not a recommended target range. Choosing a new table size must be governed by the destination manuscript, page width and legibility, with content reduction or restructuring before aggressive shrinking.
