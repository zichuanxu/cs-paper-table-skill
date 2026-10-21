> Portable evidence notes. Source PDFs and images are not bundled. Measurement paths below are relative to this directory; consult [measurement-method.md](measurement-method.md) for scope and reproduction.

# Table design study: Google/DeepMind, Meta and NVIDIA

**Verified scope:** 18 distinct reports, 30 visually inspected table anchors. Six reports and ten tables per company grouping. Ten reports were first published in 2025 and eight in 2026. The revised 2026 version of the agent-scaling report remains a 2025 first-publication item.

All selected reports already appear in the restored figure corpus, but the tables were independently rendered and opened for this study. The sample does **not** constitute table inspection of all 120 earlier figure-study papers. Primary arXiv pages were opened to verify titles and versions; affiliation evidence comes from the PDFs. Company groupings are organizational coverage labels, not evidence of a shared house style.

## Evidence and measurement method

The complete audit is in `findings.json`. Each table has an exact PDF version, 1-based page, top-left-origin crop rectangle in PDF points, a 216 dpi PNG, font-resource and visible-text measurements, colors/opacity, structural line measurements, observations, lessons and cautions. Every counted anchor was visually opened as a page render; selected tiny/complex tables were additionally opened as enlarged crops. PDF text extraction located captions and measured objects, but did not substitute for visual review.

Font programs and point sizes refer to the selected source placement. The main table area is measured separately from the caption. Font-resource lists are page-level, while visible table font summaries are region-specific. Structural horizontal rules are extracted from line segments at least 15 points long, so numerical underlines are excluded from that summary; all raw paths remain in the measurement JSON. Row-baseline summaries are heuristic output-layout measurements, not recovered LaTeX row padding. The packed PerceptionLM catalog is deliberately excluded from a single row-spacing summary.

**Evidence classes:** measured PDF properties; visually observed layout/semantics; and recommended reusable design decisions are kept separate. No source table artwork is intended for inclusion in the new skill.

## Cross-source findings

### 1. Table semantics must precede visual formatting

The same visible token means different things across sources. Parentheses indicate SD in Harness² Table 1, gaps to the strongest expert in EUPE Table 1, and performance gains in Gemma 3 Table 8 or Cosmos-Reason1 Table 7. Underline denotes a runner-up within a size block in Cosmos 3 Table 10, but a designated main metric in SAM 3 Table 8. Gray can be a row-tracking fill, a human-reference fill, a capability separator, an uncertainty text color, or a training-exposure warning. The reusable schema should encode these meanings before styling cells.

### 2. Ranking requires an explicit comparison scope and eligibility mask

Cosmos 3 Table 10 ranks within separate model-size blocks. SAM 3 Table 9 contains independent panels that its caption explicitly says are not directly comparable. Nemotron-H Table 5 excludes italicized externally reported values from winner bolding. Miras Table 2 uses class-specific highlighted winners and changes the rule in its largest-scale block. A correct renderer therefore needs a scope key, a direction, a tie policy and eligible cells. It should not implement unconditional row-max bolding or underline=second as a universal rule.

### 3. Hierarchy is usually structural, with restrained color assigned a specific job

Family spanners, partial header rules, section labels, indentation and group whitespace recur across the sample. Several tables have no score color or winner bolding at all: Gemma 4 Table 5, Gemma 3 Table 6, Fast BLT Table 1 and Nemotron 3 Super Table 5 remain intelligible through structure. Color is effective when it has a narrow role, such as a focal row/column, aggregate columns, modality group or signed change. Do not infer that every pale green NVIDIA-related column or every blue Google-related annotation is a corporate design rule.

### 4. Scientific comparability lives in headers, stubs and notes

Model scale, training budget, tool/harness configuration, context length, token budget, precision, hardware, image resolution, provenance and data exposure repeatedly appear next to results. These are not optional caption garnish. EUPE Table 11 makes device and resolution explicit; Cosmos 3 Table 8 specifies per-GPU throughput and total GPU counts; DINOv3 Table 3 fixes token budget and metric definitions; Nemotron-H Table 5 distinguishes a same-data control from external reports. Captions and cells should preserve this experimental contract.

### 5. Ablation structure has several distinct meanings

Harness² Table 3 removes one component at a time. Nemotron Diffusion Table 1 progressively adds techniques, while its numeric cells remain absolute scores. Perception Encoder Table 2 uses component checks and a source-data qualification; SAM 3 Table 9 places independent experiments in parallel panels. The data model should declare `independent_removal`, `cumulative_addition`, `factor_matrix` or `independent_panels`, and rendering should preserve that dependency structure. A plus-prefixed label is not automatically a delta-valued row.

### 6. Numeric formatting should follow metric meaning

The sample often uses one decimal for benchmark scores, two for language-model benchmarks, three for depth errors or statistical coefficients, and integer counts for datasets. These are observations, not universal precision rules. A practical generator should define precision per metric, explicitly represent unavailable/inapplicable values, keep units in headers, preserve signed deltas and define SD/SE/CI separately. Numeric centering in a source PDF does not prove use of decimal-column machinery; a new implementation can prefer decimal alignment where mixed digit counts make scanning harder.

### 7. Density is a tradeoff to evaluate, not a quality signal to copy

Observed primary text ranges from 4.483 pt in the PerceptionLM catalog to 10.909 pt in Gemma 4 tables. Perception Encoder uses 5.978 pt values in dense tables; Cosmos Policy Table 1 uses 5.383 pt in a paired layout. Those examples offer useful hierarchy patterns but also show why a new table may need splitting, landscape placement, a dedicated page or an appendix. Nemotron 3 Super Table 5 demonstrates a tall full-page alternative that retains 9.963 pt body text. No minimum font size or universal line weight is inferred from the sample.

### 8. “No vertical rules” is a useful default, not a discovered absolute

Most sampled tables use horizontal group rules without a grid. Miras Table 2, Cosmos 3 Table 10, Cosmos Policy Tables 1/4, Cosmos-Reason1 Table 4 and Nemotron 3 Super Table 5 use selected vertical separators. Their useful role is to distinguish semantic regions, not surround every cell. A default sparse-rule recipe can permit a justified divider while still avoiding a heavy spreadsheet grid.

## Measured source-placement overview

All sizes below are nominal PDF text sizes. The listed font is the region’s dominant visible text font by extracted character count, which can be a header font in a two-row table. Use the detailed table notes to interpret the role.

| Report | Table / PDF page | Dominant font program | Size (pt) | Structural horizontal-rule widths (pt) |
|---|---|---|---:|---|
| gemma4 | Table 3 / 3 | XCharter-Roman | 10.909 | 0.542, 0.868 |
| gemma4 | Table 5 / 5 | XCharter-Roman | 10.909 | 0.325, 0.542, 0.868 |
| harness2 | Table 1 / 8 | XCharter-Roman | 8.611 | 0.281, 0.468, 0.750 |
| harness2 | Table 3 / 10 | XCharter-Roman | 9.963 | 0.542, 0.868 |
| gemini25 | Table 3 / 13 | XCharter-Roman | 8.505 | 0.253, 0.423, 0.677 |
| gemma3 | Table 6 / 6 | XCharter-Roman | 8.966 | 0.325, 0.542, 0.868 |
| gemma3 | Table 8 / 8 | XCharter-Roman | 10.909 | 0.542, 0.868 |
| miras | Table 2 / 17 | LinLibertineT | 9.043 | 0.452, 0.723 |
| agent-scaling | Table 1 / 9 | XCharter-Roman | 9.845 | 0.489, 0.783 |
| agent-scaling | Table 4 / 20 | XCharter-Roman | 9.602 | 0.522, 0.837 |
| eupe | Table 1 / 7 | SFRM0900 | 7.324 | 0.244, 0.407, 0.651 |
| eupe | Table 11 / 14 | SFRM1000 | 9.963 | 0.299, 0.498, 0.797 |
| fast-blt | Table 1 / 14 | SFRM1000 | 9.963 | 0.498, 0.797 |
| dinov3 | Table 3 / 19 | LMRoman9-Regular | 8.966 | 0.299, 0.498, 0.797 |
| perception-encoder | Table 2 / 6 | NimbusRomNo9L-Regu | 5.978 | 0.398, 0.498 |
| perception-encoder | Table 5 / 9 | NimbusRomNo9L-Regu | 5.978 | 0.398, 0.498 |
| perception-lm | Table 9 / 14 | NimbusRomNo9L-Regu | 4.483 | 0.224, 0.359 |
| sam3 | Table 1 / 8 | SFRM0700 | 6.974 | 0.299, 0.498 |
| sam3 | Table 8 / 10 | SFRM0700 | 6.974 | 0.299, 0.339 |
| sam3 | Table 9 / 10 | SFRM0700 | 6.974 | 0.498 |
| cosmos3 | Table 8 / 46 | XCharter-Bold | 9.259 | 0.463, 0.741 |
| cosmos3 | Table 10 / 51 | XCharter-Roman | 7.551 | 0.453, 0.755, 1.208 |
| cosmos-policy | Table 1 / 8 | NimbusRomNo9L-Regu | 5.383 | 0.269, 0.431 |
| cosmos-policy | Table 4 / 20 | NimbusRomNo9L-Regu | 8.261 | 0.413, 0.661 |
| nemotron3-super | Table 5 / 31 | LMRoman10-Regular | 9.963 | 0.542, 0.868 |
| nemotron-diffusion | Table 1 / 4 | LMRoman10-Regular | 7.819 | 0.391, 0.626 |
| nemotron-diffusion | Table 5 / 11 | LMRoman10-Regular | 7.463 | 0.373, 0.597 |
| cosmos-reason1 | Table 4 / 9 | XCharter-Roman | 6.660 | 0.370, 0.592 |
| cosmos-reason1 | Table 7 / 18 | XCharter-Roman | 8.966 | 0.498, 0.797 |
| nvidia-nemotron-h | Table 5 / 13 | LMRoman8-Regular | 7.970 | 0.542, 0.868 |

All sampled text and fill/stroke colors reported here have nominal opacity 1.0. Exact color values are measured, but no universal palette is recommended. For example, Harness² uses pale blue `#E4EEFC`, Miras uses pale yellow `#FDF5E0` and blue `#E6F3FC`, PerceptionLM modality ribbons use `#C0DFDB`, `#D9CAEF` and `#E5E6E5`, Cosmos 3 focal columns use `#E8F4E0`, and Cosmos Policy uses `#FFF9AE`. The measured files retain the role, opacity and object bounds for each color.

## Per-report and per-table audit

### Gemma 4 Technical Report

**Source:** [v2; revised 2026-07-24](https://arxiv.org/pdf/2607.02770v2). First publication: 2026. Coverage grouping: Google / DeepMind.

**Affiliation evidence:** Page 1: Gemma Team, Google DeepMind; Google DeepMind copyright.

#### Table 3 — PDF page 3

**Role:** Compact memory / deployment profile.

**Location:** crop `[60, 427, 293, 590]` pt; table-only bounds `[63, 430, 290, 527]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/gemma4-t3.json`.

**Measured:** XCharter-Roman 10.909 pt (87 characters); XCharter-Bold 10.909 pt (20 characters); XCharterMathMI 10.036 pt (6 characters); txsys 7.970 pt (5 characters). Structural horizontal-rule widths: 0.542, 0.868 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** One model stub plus bf16, Quantized, and KV Cache columns. Model names are bold; no multilevel header.

**Numbers and alignment (visual):** Values appear centered by column. Mostly one decimal; quantized entries include two decimals, and the MoE row uses slash-separated compound values. KV entries carry an explicit plus sign. Superscripts attach quantization qualifications.

**Uncertainty and missingness:** No dispersion or interval. The dagger and double dagger describe quantization methods; the asterisk on one model is a separate marker, not an uncertainty symbol.

**Emphasis semantics:** Model names are bold for scanning; numerical values have no winner ranking, no fill and no color.

**Rules and spacing (visual):** Three horizontal rules (top, header separator, bottom); no vertical lines. Caption wraps below the narrow table.

**Caption and comparability:** The caption states text-only weights and added int8 KV cache at 32k context and decodes two quantization markers. It prints the memory unit as “Gb”, so a reusable design should spell out an unambiguous byte/bit convention.

**Recommended lessons:**

- A small deployment table can remain unshaded; put precision, context length and cache convention beside the measurements.
- Treat compound memory entries as structured values with a defined denominator or component meaning.

**Cautions:**

- Do not interpret a plus sign as an improvement; here it marks additional cache memory.
- Do not copy the ambiguous Gb notation or an unexplained slash/asterisk into a new table.

#### Table 5 — PDF page 5

**Role:** Broad model capability benchmark matrix.

**Location:** crop `[60, 82, 535, 461]` pt; table-only bounds `[99, 84, 496, 424]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/gemma4-t5.json`.

**Measured:** XCharter-Roman 10.909 pt (578 characters); XCharter-Roman 5.978 pt (43 characters). Structural horizontal-rule widths: 0.325, 0.542, 0.868 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Two family spanners, Gemma 4 over five sizes and Gemma 3 over one comparator. Short partial rules sit under each family. Capability clusters are separated by horizontal rules without an extra category column.

**Numbers and alignment (visual):** Centered numeric columns; most scores use one decimal. Codeforces uses integers and an Elo annotation, while benchmark qualifiers are small text in the left stub. Several dash cells indicate unavailable entries.

**Uncertainty and missingness:** No uncertainty is displayed. Dashes are not zero. Tiny header text marks the Gemma 3 comparator as non-thinking.

**Emphasis semantics:** No numerical best/second-best formatting; the table relies on placement and grouping rather than pervasive bold.

**Rules and spacing (visual):** Stronger outer rules, lighter internal group rules and shorter family rules. The table uses a single wide panel.

**Caption and comparability:** Caption says models use thinking mode unless stated otherwise. The explicit non-thinking comparator qualification affects interpretation. Different benchmark units live on different rows.

**Recommended lessons:**

- Define evaluation mode at column level when it differs by model.
- Let family grouping and restrained rules carry the comparison when rank emphasis is unnecessary.

**Cautions:**

- The rows mix percentages, task-specific scores and Elo; do not aggregate them without a justified transform.
- The small non-thinking qualifier must remain legible after final placement.

### Harness²: Recursive Agent Harnessing for an Open World

**Source:** [v1; submitted 2026-10-09](https://arxiv.org/pdf/2610.14224v1). First publication: 2026. Coverage grouping: Google / DeepMind.

**Affiliation evidence:** Page 1: Northwestern University and Google Cloud AI Research; first-author internship at Google Cloud AI Research stated.

#### Table 1 — PDF page 8

**Role:** Main benchmark with performance, efficiency, uncertainty and recursive changes.

**Location:** crop `[60, 84, 535, 497]` pt; table-only bounds `[61, 147, 535, 495]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/harness2-t1.json`.

**Measured:** XCharter-Roman 8.611 pt (880 characters); XCharter-Roman 6.889 pt (800 characters); XCharter-Bold 8.611 pt (196 characters); LMMonoLt10-Bold 7.578 pt (19 characters). Structural horizontal-rule widths: 0.281, 0.468, 0.750 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Two-level columns pair Score and #Steps under Code, Web, Office and Avg. Vertically written model-family labels span separate blocks. Each harness block repeats baselines, the method and a + Recursion delta row.

**Numbers and alignment (visual):** One decimal for primary values and signed deltas. SDs appear as smaller gray parenthetical values; score and SD remain visually adjacent. Fixed precision makes the main values easy to scan.

**Uncertainty and missingness:** Caption explicitly defines SD over runs and Avg as a macro-average of three domains. Delta rows contain signed changes without a parenthetical SD.

**Emphasis semantics:** Caption defines bold as the best result before recursion, so the delta row is outside that ranking scope. Pale blue fills mark + Recursion rows; a related blue strip carries the model label. Gray text de-emphasizes SDs.

**Rules and spacing (visual):** Partial rules organize metric spanners; dashed separators mark the method boundary; solid rules divide experimental blocks. No full vertical grid.

**Caption and comparability:** Caption defines k=1 for the method, k=5 for recursion, the averaging unit and the dagger for offline optimization on separate tasks. It acts as a compact experiment contract.

**Recommended lessons:**

- Store the rank scope separately from the display row group, especially when absolute scores and deltas coexist.
- Separate primary estimate from uncertainty typographically without making uncertainty unreadable.
- Repeat the control/harness block when the same method has a different operating baseline.

**Cautions:**

- Parentheses mean SD here, unlike EUPE gap annotations.
- A delta row cannot be directly ranked against absolute values above it.
- The smaller 6.889 pt SD text is an observed source choice, not a minimum-size recommendation.

#### Table 3 — PDF page 10

**Role:** One-component-removal ablation.

**Location:** crop `[324, 429, 535, 544]` pt; table-only bounds `[325, 468, 534, 543]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/harness2-t3.json`.

**Measured:** XCharter-Roman 9.963 pt (82 characters); XCharter-Bold 9.963 pt (15 characters); XCharter-Roman 7.273 pt (1 characters). Structural horizontal-rule widths: 0.542, 0.868 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** A baseline row is followed by indented w/o library, w/o scoping and w/o composition rows; two benchmark columns.

**Numbers and alignment (visual):** One decimal throughout; values are centered in compact columns.

**Uncertainty and missingness:** No interval or SD in this ablation, even though the main results table reports SD.

**Emphasis semantics:** Pale blue marks the full method; its two scores are bold. The indented removals have no fill.

**Rules and spacing (visual):** Top/header/bottom rules only; indentation expresses the ablation relationship.

**Caption and comparability:** The short caption names both benchmarks. The neighboring prose supplies the fixed model, harness and k=1 setup; the isolated table does not repeat all of that context.

**Recommended lessons:**

- A removal ablation should make the full configuration visually unmistakable and indent each single change.
- Carry fixed experimental settings into the caption or notes when exporting the table alone.

**Cautions:**

- Do not assume a row sequence is cumulative removal; the prose describes separate removals.
- Do not silently transfer uncertainty from the main-results table to the ablation.

### Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities

**Source:** [v6; revised 2025-12-19](https://arxiv.org/pdf/2507.06261v6). First publication: 2025. Coverage grouping: Google / DeepMind.

**Affiliation evidence:** Page 1: Gemini Team, Google; Google correspondence address and copyright.

#### Table 3 — PDF page 13

**Role:** Capability benchmark across six model variants.

**Location:** crop `[60, 182, 535, 667]` pt; table-only bounds `[61, 185, 535, 617]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/gemini25-t3.json`.

**Measured:** XCharter-Roman 8.505 pt (751 characters); XCharter-Bold 8.505 pt (203 characters); XCharter-Italic 7.767 pt (48 characters); XCharter-Roman 8.335 pt (13 characters). Structural horizontal-rule widths: 0.253, 0.423, 0.677 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** A multirow Capability stub groups benchmarks. A secondary, unlabeled qualifier area holds single/multiple attempts, context lengths and tool conditions. Model headers wrap to two lines.

**Numbers and alignment (visual):** Centered values usually carry one decimal and a percent sign. ZeroBench includes two-decimal values; qualifiers are italic and smaller. Long names wrap in the benchmark stub.

**Uncertainty and missingness:** No intervals are shown. A dash replaces a missing score and a dagger qualifies selected entries.

**Emphasis semantics:** Bold identifies selected row-leading scores; no row/column tint. The 1M MRC-v2 result emphasizes the Flash score rather than always emphasizing the newest/largest model column.

**Rules and spacing (visual):** Horizontal rules divide capability and benchmark subgroups. No vertical lines; merged category labels use whitespace.

**Caption and comparability:** The caption points to other tables for audio/video and to an appendix for benchmark variants and evaluation details. Attempt count and context length are scientifically material row qualifiers.

**Recommended lessons:**

- Use a separate condition subcolumn when the same benchmark has multiple evaluation protocols.
- Make emphasis data-driven rather than automatically bolding the focal model column.

**Cautions:**

- The caption is not a complete evaluation protocol; preserve the appendix reference.
- Mixed decimal counts should be intentional; do not infer measurement precision solely from the number of printed digits.

### Gemma 3 Technical Report

**Source:** [v1; submitted 2025-03-25](https://arxiv.org/pdf/2503.19786v1). First publication: 2025. Coverage grouping: Google / DeepMind.

**Affiliation evidence:** Page 1: Gemma Team, Google DeepMind; Google DeepMind copyright.

#### Table 6 — PDF page 6

**Role:** Model-family comparison on zero-shot capabilities.

**Location:** crop `[60, 82, 535, 304]` pt; table-only bounds `[78, 83, 519, 268]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/gemma3-t6.json`.

**Measured:** XCharter-Roman 8.966 pt (585 characters). Structural horizontal-rule widths: 0.325, 0.542, 0.868 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Four family spanners with short rules sit over eleven model columns. Benchmarks are grouped by light horizontal separators; the left stub stays unrotated.

**Numbers and alignment (visual):** One-decimal centered scores with aligned short numeric strings. Dashes occupy unavailable visual-model entries.

**Uncertainty and missingness:** No uncertainty. A dash communicates missing/not-applicable performance rather than zero.

**Emphasis semantics:** No result bolding and no colored backgrounds. Group headers and rules carry the hierarchy.

**Rules and spacing (visual):** Outer rules are stronger than subgroup and family rules. The full-width table accommodates many columns while retaining ordinary horizontal labels.

**Caption and comparability:** Caption establishes instruction-tuned models and zero-shot comparisons across abilities.

**Recommended lessons:**

- A grouped table can communicate family/size structure without additional color.
- Preserve an explicit nonvalue token when only some models support a benchmark.

**Cautions:**

- A model family spanner is not itself evidence that training data, inference budget or modality support are controlled.

#### Table 8 — PDF page 8

**Role:** Paired intervention comparison at two model scales.

**Location:** crop `[304, 134, 535, 327]` pt; table-only bounds `[312, 136, 526, 252]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/gemma3-t8.json`.

**Measured:** XCharter-Roman 10.909 pt (88 characters); XCharter-Roman 8.966 pt (38 characters); XCharterMathRM 10.036 pt (2 characters). Structural horizontal-rule widths: 0.542, 0.868 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Two three-row blocks: original, with Pan & Scan, and delta; columns are DocVQA, InfoVQA and TextVQA.

**Numbers and alignment (visual):** Primary results use one decimal; blue parenthetical deltas include an explicit plus sign. Delta labels use the mathematical symbol.

**Uncertainty and missingness:** Parentheses encode gain, not SD. No uncertainty is reported.

**Emphasis semantics:** Blue is confined to positive delta annotations; the main scores remain black. No best-value bolding or row shading.

**Rules and spacing (visual):** One rule separates the two model scales; no vertical grid. Delta text is smaller than primary values.

**Caption and comparability:** Caption states four-shot evaluation on the validation set and says this is a pretrained checkpoint intervention.

**Recommended lessons:**

- Put paired absolute scores and signed deltas in separate rows with explicit treatment and control labels.
- Assign a semantic role to annotation color rather than using color as generic decoration.

**Cautions:**

- Do not confuse the parenthetical gain with dispersion.
- A plus sign and blue color indicate change here, not statistical significance.

### It's All Connected: A Journey Through Test-Time Memorization, Attentional Bias, Retention, and Online Optimization

**Source:** [v1; submitted 2025-04-17](https://arxiv.org/pdf/2504.13173v1). First publication: 2025. Coverage grouping: Google / DeepMind.

**Affiliation evidence:** Page 1: all four named authors marked Google Research, with google.com correspondence.

#### Table 2 — PDF page 17

**Role:** Scale-controlled language-model and commonsense benchmark.

**Location:** crop `[70, 69, 563, 606]` pt; table-only bounds `[96, 124, 537, 604]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/miras-t2.json`.

**Measured:** LinLibertineT 9.043 pt (2124 characters); LinLibertineTB 9.043 pt (52 characters); txsys 9.043 pt (10 characters); txsys 6.601 pt (4 characters). Structural horizontal-rule widths: 0.452, 0.723 pt. Extracted vertical divider segments: 72. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Three full-width bands state parameter and token budgets. Rows further distinguish baseline, proposed simple and hybrid variants. Headers include dataset abbreviations, metric names and up/down arrows.

**Numbers and alignment (visual):** Two decimals throughout the numeric body. The first two perplexity columns are separated from accuracy columns. Values appear centered by column.

**Uncertainty and missingness:** No SD or confidence intervals; asterisks identify hybrid models rather than significance.

**Emphasis semantics:** Pale yellow and pale blue cells mark best results in different model classes; the caption explains the classes and changes the comparison rule in the largest-scale block. Bold is used in headers, not as the primary winner channel.

**Rules and spacing (visual):** Horizontal rules separate budget and method blocks; a small number of vertical separators divide the model stub and metric families. A doubled header boundary is present; this is not a universal no-vertical-line example.

**Caption and comparability:** Caption explicitly declares both highlight classes and the largest-scale exception, preventing an otherwise ambiguous two-color ranking.

**Recommended lessons:**

- Treat each budget/class block as a distinct comparison scope.
- Use metric direction in the header whenever higher/lower-is-better differs across columns.

**Cautions:**

- Copying its colors without copying the scope legend would change the meaning.
- The largest-scale highlight rule differs from the earlier blocks.
- Color-only winner marking should gain a redundant cue when producing an accessible or grayscale-ready table.

### Towards a Science of Scaling Agent Systems

**Source:** [v3; revised 2026-04-08; first submitted 2025-12-09](https://arxiv.org/pdf/2512.08296v3). First publication: 2025. Coverage grouping: Google / DeepMind.

**Affiliation evidence:** Page 1: author affiliations include Google Research, Google DeepMind and MIT.

#### Table 1 — PDF page 9

**Role:** Benchmark coverage and evaluation-design catalog.

**Location:** crop `[60, 93, 535, 209]` pt; table-only bounds `[61, 108, 535, 208]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/agent-scaling-t1.json`.

**Measured:** XCharter-Roman 9.845 pt (388 characters); XCharter-Bold 9.845 pt (29 characters). Structural horizontal-rule widths: 0.489, 0.783 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Three left-aligned text columns: benchmark, task and evaluation design. Benchmark labels retain years.

**Numbers and alignment (visual):** This is categorical information, not a score table. Column widths favor complete phrases and short lines.

**Uncertainty and missingness:** No uncertainty or missing numerical values.

**Emphasis semantics:** Alternating light-gray rows guide tracking across descriptive columns; bold is restricted to column headers.

**Rules and spacing (visual):** Only top/header/bottom rules. Shading replaces repeated horizontal row rules.

**Caption and comparability:** The caption states the six-benchmark scope; the table pairs each task with what is actually evaluated.

**Recommended lessons:**

- Use a text-first coverage table when the purpose is to explain what evidence exists.
- Alternating fills can support row tracking without implying rank.

**Cautions:**

- Do not import a numerical leaderboard’s winner semantics into a categorical catalog.

#### Table 4 — PDF page 20

**Role:** Statistical coefficient and uncertainty table.

**Location:** crop `[60, 83, 535, 480]` pt; table-only bounds `[64, 176, 534, 478]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/agent-scaling-t4.json`.

**Measured:** XCharter-Roman 9.602 pt (1031 characters); txsys 9.602 pt (59 characters); XCharter-Italic 9.602 pt (52 characters); XCharterMathMI 8.834 pt (35 characters). Structural horizontal-rule widths: 0.522, 0.837 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Five columns: predictor, coefficient, 95% CI, p and interpretation. Italic in-body section labels split main effects, coordination structure and critical interactions.

**Numbers and alignment (visual):** Coefficients and interval endpoints use three decimals; p uses three decimals or a threshold such as <0.001. Signs and bracketed intervals remain explicit. Mathematical predictor notation is separated from plain-language interpretation.

**Uncertainty and missingness:** 95% confidence intervals and p-values are named in the header; a dagger marks nonsignificant terms by the stated p>0.05 convention.

**Emphasis semantics:** No winner highlighting or significance color. Header weight and italic section labels provide hierarchy.

**Rules and spacing (visual):** Three interior horizontal separators and stronger outer rules; no vertical grid. The interpretation column prevents symbolic coefficients from standing alone.

**Caption and comparability:** Caption includes N, model fit, cross-validation, centering and the dagger rule. It explains contextual model choices that affect coefficient interpretation.

**Recommended lessons:**

- Statistical tables need named uncertainty and interpretable effect labels rather than best-score emphasis.
- Keep CI type, p-value convention, sample count and transformations adjacent to the table.

**Cautions:**

- A small p-value does not make a larger coefficient a universal winner.
- The printed negative zero-like coefficient is a rounding artifact to handle explicitly in a new formatter, not a claim of exact zero.

### Efficient Universal Perception Encoder

**Source:** [v2; revised 2026-03-31](https://arxiv.org/pdf/2603.22387v2). First publication: 2026. Coverage grouping: Meta / FAIR.

**Affiliation evidence:** Page 1: Meta Reality Labs and FAIR at Meta.

#### Table 1 — PDF page 7

**Role:** Multi-domain encoder benchmark with comparison-to-expert gaps.

**Location:** crop `[69, 61, 545, 279]` pt; table-only bounds `[74, 116, 540, 277]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/eupe-t1.json`.

**Measured:** SFRM0900 7.324 pt (533 characters); OptimisticDisp-Bd 6.445 pt (131 characters); SFTI0900 7.324 pt (33 characters); CMSY9 7.324 pt (1 characters). Structural horizontal-rule widths: 0.244, 0.407, 0.651 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Six top-level task categories span eleven benchmark columns. Rotated benchmark labels preserve horizontal room. Domain Experts and Agglomerative Methods are italic row-group labels.

**Numbers and alignment (visual):** Scores use metric-appropriate precision: many one-decimal values, three-decimal depth error, and larger-scale MME values. Parenthetical shortfalls appear beside selected EUPE scores; numeric cells are visually centered.

**Uncertainty and missingness:** Caption explicitly says parentheses are gaps to the best domain expert. no txt and no cls distinguish unsupported feature outputs from absent results; there is no uncertainty interval.

**Emphasis semantics:** Gray fills identify the proposed row. Bold identifies best results across the stated comparison. Blue author-year citations are link typography, not score semantics.

**Rules and spacing (visual):** Partial rules define column groups; short full-width rules define method groups. No vertical grid.

**Caption and comparability:** Caption defines no txt/no cls, parentheses and the asterisk describing a discrepancy from encoder-only evaluation without an adapter head.

**Recommended lessons:**

- Use distinct tokens for absent capability, absent measurement and a valid zero.
- A compact parenthetical annotation must have a declared statistical or comparative meaning.

**Cautions:**

- Do not parse the parentheses as SD.
- Rotated labels and 7.324 pt values are source density choices; widen/split a new table before shrinking to that scale.

#### Table 11 — PDF page 14

**Role:** Hardware-aware model cost profile.

**Location:** crop `[69, 227, 545, 435]` pt; table-only bounds `[122, 271, 487, 433]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/eupe-t11.json`.

**Measured:** SFRM1000 9.963 pt (231 characters); OptimisticDisp-Bd 8.767 pt (47 characters); CMSY7 6.974 pt (2 characters). Structural horizontal-rule widths: 0.299, 0.498, 0.797 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Model and #Params columns precede two grouped sections: inference GFLOPs and latency (ms), each split by resolution 256 and 512. A row rule separates ConvNeXt and ViT families.

**Numbers and alignment (visual):** Parameter counts include an M suffix; GFLOPs are integral; latency uses one decimal. Numeric columns appear centered.

**Uncertainty and missingness:** No dispersion; an asterisk flags models outside the released EUPE family rather than a statistical property.

**Emphasis semantics:** Bold headers only. Neither lower cost nor the proposed model is automatically highlighted.

**Rules and spacing (visual):** Outer/header/group rules, with partial underlines under cost spanners. No fills or vertical lines.

**Caption and comparability:** Caption states image size, device (iPhone 15 Pro CPU), metrics and the reason starred models are included.

**Recommended lessons:**

- Make hardware, resolution, units and inference regime part of an efficiency table’s specification.
- Display different physical quantities at different appropriate precisions.

**Cautions:**

- Do not treat the FLOPs or latency columns as hardware-independent throughput.
- The table gives inference latency; it is not a training-cost comparison.

### Fast Byte Latent Transformer

**Source:** [v1; arXiv submission 2026-05-08; PDF interior date 2026-05-11](https://arxiv.org/pdf/2605.08044v1). First publication: 2026. Coverage grouping: Meta / FAIR.

**Affiliation evidence:** Page 1: FAIR at Meta, Stanford University and University of Washington.

#### Table 1 — PDF page 14

**Role:** Small quality comparison across decoding/training variants.

**Location:** crop `[69, 61, 545, 192]` pt; table-only bounds `[150, 105, 459, 191]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/fast-blt-t1.json`.

**Measured:** SFRM1000 9.963 pt (100 characters); OptimisticDisp-Bd 8.767 pt (80 characters). Structural horizontal-rule widths: 0.498, 0.797 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Five benchmark rows and four model columns; all model headers carry the shared 3B scale and explicit block-size variant.

**Numbers and alignment (visual):** Two decimals in all score cells. A broad model-header width allows clear labels without rotation.

**Uncertainty and missingness:** No uncertainty and no missing cells in this anchor.

**Emphasis semantics:** Bold sans-serif row labels and headers contrast with serif score text. Numerical winners are not bolded; no fill or color.

**Rules and spacing (visual):** Three horizontal rules and generous surrounding whitespace. The table is narrower than the text area.

**Caption and comparability:** Caption frames an accuracy/speed tradeoff, but the table itself contains quality only; speed evidence appears elsewhere in the paper.

**Recommended lessons:**

- A small table should remain compact and readable rather than stretching to fill the page.
- Typography can separate labels from values without color or cell borders.

**Cautions:**

- Do not claim a quantified speed/quality tradeoff from this anchor alone; add the matching efficiency data or a precise cross-reference.

### DINOv3

**Source:** [v1; submitted 2025-08-13](https://arxiv.org/pdf/2508.10104v1). First publication: 2025. Coverage grouping: Meta / FAIR.

**Affiliation evidence:** Page 1: Meta AI Research; additional WRI and Inria author markers.

#### Table 3 — PDF page 19

**Role:** Frozen-backbone dense prediction comparison.

**Location:** crop `[70, 77, 542, 324]` pt; table-only bounds `[132, 146, 480, 323]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/dinov3-t3.json`.

**Measured:** LMRoman9-Regular 8.966 pt (300 characters); LMRoman8-Italic 7.970 pt (72 characters); LMRoman9-Bold 8.966 pt (22 characters); LMMathSymbols9-Regular 8.966 pt (2 characters). Structural horizontal-rule widths: 0.299, 0.498, 0.797 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Segmentation and Depth spanners cover three and two datasets. Model and ViT columns separate method identity from architecture. Italic full-width labels define three supervision families.

**Numbers and alignment (visual):** Segmentation scores use one decimal; depth errors use three. Depth columns carry downward arrows. Values have consistent alignment and precision within each metric.

**Uncertainty and missingness:** No uncertainty or missing entries in this table.

**Emphasis semantics:** The DINOv3 scores are bold; baseline family labels are italic. There is no shading, and model labels are not excessively emphasized.

**Rules and spacing (visual):** Outer rules, family separators and two partial spanner rules; no vertical grid.

**Caption and comparability:** Caption defines mIoU versus RMSE, frozen backbones and the resolution adaptation to a constant token budget.

**Recommended lessons:**

- Separate model capacity from model identity in its own stub column.
- Use precision and direction per metric, with the evaluation normalization stated in the caption.

**Cautions:**

- A one-decimal accuracy and three-decimal RMSE are different units; do not format or average them identically.

### Perception Encoder: The best visual embeddings are not at the output of the network

**Source:** [v1; submitted 2025-04-17](https://arxiv.org/pdf/2504.13181v1). First publication: 2025. Coverage grouping: Meta / FAIR.

**Affiliation evidence:** Page 1: Meta FAIR, UT Austin, MBZUAI, Fudan University and Meta Reality Labs; internship roles marked.

#### Table 2 — PDF page 6

**Role:** Component-selection ablation for a video data engine.

**Location:** crop `[281, 148, 545, 329]` pt; table-only bounds `[282, 149, 540, 237]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/perception-encoder-t2.json`.

**Measured:** NimbusRomNo9L-Regu 5.978 pt (329 characters); NimbusRomNo9L-ReguItal 4.981 pt (44 characters); NimbusRomNo9L-Regu 4.981 pt (39 characters); NimbusRomNo9L-ReguItal 5.978 pt (28 characters). Structural horizontal-rule widths: 0.398, 0.498 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Four rotated component columns use checks/blank cells, followed by grouped image and video zero-shot metrics. Each family begins with a shaded average column.

**Numbers and alignment (visual):** Primary scores use one decimal. Metrics have rotated labels and small dataset-reference subscripts. Numeric values are centered.

**Uncertainty and missingness:** No uncertainty; the asterisk on a video-caption check means captions produced without the indicated human-refined training data. Blank feature cells function as off states in this design, not absent scores.

**Emphasis semantics:** Teal/blue tinted headers distinguish image/video families. Average columns have gray fills. No result-wide best-value formatting.

**Rules and spacing (visual):** Only top, header and bottom rules. The table is wrapped into a narrow page region, producing 5.978 pt primary text.

**Caption and comparability:** The caption explains the in-development encoder, frame averaging, how captions are generated, and the asterisk; these are important to interpreting the feature matrix.

**Recommended lessons:**

- Separate binary design choices from performance metrics in the schema.
- Give aggregate columns a different structural treatment from individual datasets.

**Cautions:**

- Do not infer that every row is a pure cumulative addition; the asterisk also changes the caption-generation source.
- The narrow-wrap layout is a readability caution, not a font-size target.
- Add an explicit off-state legend when using blank feature cells in a new table.

#### Table 5 — PDF page 9

**Role:** Large image benchmark across model-scale cohorts.

**Location:** crop `[67, 60, 547, 340]` pt; table-only bounds `[67, 61, 547, 280]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/perception-encoder-t5.json`.

**Measured:** NimbusRomNo9L-Regu 5.978 pt (1380 characters); OptimisticDisp-Bd 5.260 pt (297 characters); NimbusRomNo9L-Regu 4.981 pt (132 characters); NimbusRomNo9L-ReguItal 4.981 pt (118 characters). Structural horizontal-rule widths: 0.398, 0.498 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Rotated benchmark headers are grouped as zero-shot classification, fine-grained classification and retrieval. Stub columns include encoder parameters, resolution and training-data scale. Row cohorts are Proprietary, B Scale, L Scale and Unbounded Scale.

**Numbers and alignment (visual):** Most scores have one decimal; metadata uses B/M unit suffixes. Dashes occur for unreported metrics. Average columns are visually prominent and retain numeric alignment.

**Uncertainty and missingness:** No dispersion. Reported/reevaluated settings and source links appear in notes and row labels; dashes are nonvalues.

**Emphasis semantics:** Pale tinted family headers and gray average columns aid navigation. Bold marks selected results within the model cohorts; the scope should be spelled out if reproducing the design.

**Rules and spacing (visual):** Few horizontal rules separate cohorts; no vertical grid. The single full-width matrix uses 5.978 pt primary values and several smaller labels.

**Caption and comparability:** Caption distinguishes proprietary/open encoders and notes reevaluation settings for some baselines, with appendix references.

**Recommended lessons:**

- Record parameters, resolution and data scale beside scores when those variables affect comparability.
- Use a model-cohort identifier as an explicit rank scope in a generator.

**Cautions:**

- Do not assume every bold value is a global maximum across all model sizes.
- The density is high; splitting benchmark families may improve a new table more than rotating more labels.

### PerceptionLM: Open-Access Data and Models for Detailed Visual Understanding

**Source:** [v3; revised 2025-07-23](https://arxiv.org/pdf/2504.13180v3). First publication: 2025. Coverage grouping: Meta / FAIR.

**Affiliation evidence:** Page 1: Meta FAIR, UT Austin, MBZUAI and Meta Reality Labs.

#### Table 9 — PDF page 14

**Role:** Full dataset-mixture inventory.

**Location:** crop `[106, 69, 507, 398]` pt; table-only bounds `[106, 69, 497, 349]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/perception-lm-t9.json`.

**Measured:** NimbusRomNo9L-Regu 4.483 pt (3032 characters); NimbusRomNo9L-Medi 4.483 pt (135 characters). Structural horizontal-rule widths: 0.224, 0.359 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Four independently packed vertical columns of mini-tables repeat Dataset and Size headings. Task groups include image QA/captioning/grounding/synthetic data, video tasks and text QA. Colored side ribbons identify modality; some vertical ribbon labels name source mixtures.

**Numbers and alignment (visual):** Dataset counts are integers, right aligned in the Size column. Bold total rows appear at group ends. No decimal or percentage units; exact counts retain their full digits.

**Uncertainty and missingness:** No uncertainty. The catalog is a declaration of data composition rather than a performance estimate.

**Emphasis semantics:** Teal, purple and gray ribbons distinguish image, video and text-only groups. Bold total rows provide a second hierarchy; gray headings and blue reference links have separate roles.

**Rules and spacing (visual):** Each mini-table has its own horizontal rules and whitespace. The four-column packing permits many datasets but reduces nominal body text to 4.483 pt.

**Caption and comparability:** Caption defines the modality colors and states the data-access/provenance policy. Some subtables continue an image mixture across columns, so reading order matters.

**Recommended lessons:**

- For large catalogs, use repeated mini-table headers, task groups and explicit totals; retain source identifiers.
- Promote the catalog to an appendix/landscape/multipage table when necessary to preserve readable type.

**Cautions:**

- The extremely small source font must not become a recommended default.
- Do not compute a global row-spacing statistic across independent packed columns.
- Keep totals separate from individual data rows and avoid double counting nested or continued mixtures.

### SAM 3: Segment Anything with Concepts

**Source:** [v1; submitted 2025-11-20](https://arxiv.org/pdf/2511.16719v1). First publication: 2025. Coverage grouping: Meta / FAIR.

**Affiliation evidence:** Page 1: Meta Superintelligence Labs; contributor/intern/project-lead markers.

#### Table 1 — PDF page 8

**Role:** Multi-task segmentation/detection benchmark with training-exposure annotations.

**Location:** crop `[69, 61, 547, 234]` pt; table-only bounds `[69, 62, 546, 199]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/sam3-t1.json`.

**Measured:** SFRM0700 6.974 pt (466 characters); OptimisticDisp-Bd 6.137 pt (163 characters); SFRM0700 6.834 pt (36 characters); SFRM0500 4.981 pt (11 characters). Structural horizontal-rule widths: 0.299, 0.498 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Three major families (instance segmentation, box detection and semantic segmentation) each split into datasets and metrics, making a three-level header. Human reference and model rows share the matrix.

**Numbers and alignment (visual):** Most scores use one decimal; a Bio pmF1 metric uses two. Dashes indicate unreported cells. Numeric columns are centered under short metric labels.

**Uncertainty and missingness:** No intervals. Multiple superscripts flag data exposure or the origin of results. Gray text specifically indicates use of the closed-set training data.

**Emphasis semantics:** The human row has a gray background; gray score text means training-set usage. The SAM 3 row uses bold; those two uses of gray must be distinguished.

**Rules and spacing (visual):** Partial rules define nested header spans. Only a few body rules, no vertical grid. The matrix uses compact 6.974 pt primary type.

**Caption and comparability:** Caption decodes APo and several markers, defines gray score text, and points to additional baseline/human details.

**Recommended lessons:**

- Store training exposure and result provenance as explicit cell metadata, independent of rank.
- Separate a reference row’s fill from a score’s text-status encoding.

**Cautions:**

- Gray does not mean a weak baseline or missing value here.
- Do not include differently trained or externally reported results in an undifferentiated ranking without a stated policy.

#### Table 8 — PDF page 10

**Role:** Agent benchmark across two task families with a designated main metric.

**Location:** crop `[69, 61, 547, 204]` pt; table-only bounds `[92, 62, 516, 179]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/sam3-t8.json`.

**Measured:** SFRM0700 6.974 pt (415 characters); OptimisticDisp-Bd 6.137 pt (75 characters); SFRM0500 4.981 pt (1 characters). Structural horizontal-rule widths: 0.299, 0.339 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Model and MLLM stubs precede ReasonSeg and OmniLabel groups. ReasonSeg divides validation/test and test-duration subsets; OmniLabel splits description categories.

**Numbers and alignment (visual):** One decimal for most scores; asterisks attach to reproduced results and dashes mark unavailable entries. The underlined header labels identify main metrics.

**Uncertainty and missingness:** No intervals. Gray text marks fine-tuned ReasonSeg results; asterisk and dagger explain provenance/model differences.

**Emphasis semantics:** Underline means main metric, not second place. Bold emphasizes selected strong results. Gray text carries training-condition meaning.

**Rules and spacing (visual):** Nested short rules and a method-block separator supply structure; no full grid.

**Caption and comparability:** Caption explicitly decodes the underline, gray, asterisk and dagger conventions, including different underlying models for separate benchmarks.

**Recommended lessons:**

- Keep separate metadata for primary metric, best/second rank and training exposure.
- Always attach underline semantics to the caption; do not assume a field-wide convention.

**Cautions:**

- A renderer with a hard-coded underline=runner-up rule would misrepresent this table.
- Metrics across the two families have distinct definitions and settings.

#### Table 9 — PDF page 10

**Role:** Four independent compact ablation panels.

**Location:** crop `[69, 218, 547, 308]` pt; table-only bounds `[69, 220, 548, 289]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/sam3-t9.json`.

**Measured:** SFRM0700 6.974 pt (188 characters); SFRM0900 8.966 pt (57 characters); OptimisticDisp-Bd 6.137 pt (48 characters); SFRM0700 6.953 pt (12 characters). Structural horizontal-rule widths: 0.498 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Panels (a) presence head, (b) hard negatives, (c) training data and (d) AI verifiers each have their own header and compact rows. Binary inclusion columns use checks/crosses; panel labels sit below the tables.

**Numbers and alignment (visual):** One-decimal task scores are mixed with a two-decimal IL_MCC metric and integer negatives-per-image counts. Each panel is aligned locally rather than forced into a shared global grid.

**Uncertainty and missingness:** No uncertainty. Check/cross cells encode component inclusion. A gray Human row acts as a reference in the verifier panel.

**Emphasis semantics:** Bold selects values within each panel; it does not imply comparability across panels. Gray fill marks the human reference only.

**Rules and spacing (visual):** One short header rule per panel; whitespace and panel labels separate the four experiments without boxes.

**Caption and comparability:** Caption explicitly warns that values across the sub-tables are not directly comparable. Nearby prose explains they use different shorter training runs.

**Recommended lessons:**

- Independent experiments need independent rank scopes and clear panel identity.
- Use a component matrix only for on/off factors and keep count-valued factors numeric.

**Cautions:**

- Never recompute winner formatting across panels whose scores are declared incomparable.
- Do not combine these subpanels into one leaderboard merely because they share metric names.

### Cosmos 3: Omnimodal World Models for Physical AI

**Source:** [v4; revised 2026-06-23](https://arxiv.org/pdf/2606.02800v4). First publication: 2026. Coverage grouping: NVIDIA.

**Affiliation evidence:** Page 1: NVIDIA as group author and NVIDIA copyright; contributors in Appendix G.

#### Table 8 — PDF page 46

**Role:** Training-throughput profile for two dense model configurations.

**Location:** crop `[60, 79, 535, 190]` pt; table-only bounds `[85, 141, 507, 188]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/cosmos3-t8.json`.

**Measured:** XCharter-Bold 9.259 pt (85 characters); XCharter-Roman 9.259 pt (44 characters). Structural horizontal-rule widths: 0.463, 0.741 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Model stub followed by iteration seconds, TFLOPS, MFU, iterations/hour, image tokens/hour/GPU and video tokens/hour/GPU. Units are in headers.

**Numbers and alignment (visual):** Precision differs by physical quantity: seconds one decimal, FLOPs and iteration count integers, MFU and token throughput two decimals. Values appear centered.

**Uncertainty and missingness:** No uncertainty or missing cells.

**Emphasis semantics:** Bold headers and model names only; no “winner” formatting and no fill.

**Rules and spacing (visual):** Three horizontal rules, no vertical rules. Two rows keep the large caption-to-data ratio readable.

**Caption and comparability:** Caption states per-GPU accounting, million-token units, GB200 hardware and different total GPU counts for Nano and Super.

**Recommended lessons:**

- Treat denominator, hardware and scale as part of each efficiency measurement.
- Do not conflate total training throughput with normalized per-GPU throughput.

**Cautions:**

- The models use different GPU counts; whole-job speed/cost cannot be inferred from normalized cells alone.

#### Table 10 — PDF page 51

**Role:** Dense benchmark matrix with per-size model comparisons.

**Location:** crop `[60, 79, 535, 764]` pt; table-only bounds `[61, 141, 535, 762]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/cosmos3-t10.json`.

**Measured:** XCharter-Roman 7.551 pt (3458 characters); XCharter-Bold 7.551 pt (757 characters); CMSY5 7.551 pt (1 characters). Structural horizontal-rule widths: 0.453, 0.755, 1.208 pt. Extracted vertical divider segments: 159. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Rotated model names form three size cohorts, each anchored by a Cosmos 3 variant. Benchmark rows are grouped into four domains with rotated domain labels and benchmark counts; average rows terminate each domain.

**Numbers and alignment (visual):** One decimal throughout the score body. Many aligned numeric columns fit on a dedicated full-page table.

**Uncertainty and missingness:** No dispersion. A dagger denotes a closed model; average rows are separate from individual benchmarks.

**Emphasis semantics:** Pale green columns identify the three focal variants, gray fills mark aggregate rows, bold marks best and underline second best within each separated model block. The caption defines that scope.

**Rules and spacing (visual):** Stronger outer rules and double/group boundaries isolate domains. A small number of semantic vertical dividers separate model blocks; short underlines on values are rank markers, not table grid strokes.

**Caption and comparability:** Caption declares benchmark groups, per-row scores, per-block rank scope and the closed-model marker.

**Recommended lessons:**

- Represent model cohort and benchmark domain separately; apply rank operations within a cohort.
- Keep structural highlighting (focal model/aggregate row) independent from statistical or rank formatting.

**Cautions:**

- Do not rank all model sizes globally.
- The font is 7.551 pt and headers rotate; density should be an explicit appendix/full-page decision.
- Stroke histograms contain numerical underlines; use long-rule extraction when inferring table border weights.

### Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning

**Source:** [v1; submitted 2026-01-22](https://arxiv.org/pdf/2601.16163v1). First publication: 2026. Coverage grouping: NVIDIA.

**Affiliation evidence:** Page 1: NVIDIA and Stanford University affiliations; NVIDIA research project URL.

#### Table 1 — PDF page 8

**Role:** Robot success-rate benchmark with replication details.

**Location:** crop `[107, 80, 306, 251]` pt; table-only bounds `[107, 170, 306, 251]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/cosmos-policy-t1.json`.

**Measured:** NimbusRomNo9L-Regu 5.383 pt (430 characters); NimbusRomNo9L-Medi 5.383 pt (21 characters); CMR7 3.768 pt (3 characters); CMMI10 5.383 pt (2 characters). Structural horizontal-rule widths: 0.269, 0.431 pt. Extracted vertical divider segments: 60. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** One method stub and four LIBERO suites plus Average. It sits alongside a separate RoboCasa table on the page.

**Numbers and alignment (visual):** One decimal; each suite header names SR (%). Missing results use dashes. Citation text is green inside method names.

**Uncertainty and missingness:** Caption gives 500 trials per suite and three random seeds, but the score cells do not show SD/CI.

**Emphasis semantics:** Pale yellow marks the proposed row, while bold marks leading cells, including a baseline’s Spatial score. Green text is for citations, not outcome quality.

**Rules and spacing (visual):** Horizontal outer/header rules with thin vertical metric dividers. The paired layout scales primary text to 5.383 pt.

**Caption and comparability:** Caption supplies task-suite composition, trial count and seeds, making aggregation interpretable even though uncertainty is absent.

**Recommended lessons:**

- Keep replication counts and aggregation units with success-rate results.
- Distinguish focal-row fill from per-column best scores.

**Cautions:**

- Averaging over seeds does not imply an interval has been reported.
- The small source type and paired layout are readability cautions.
- Do not label a missing suite result as zero success.

#### Table 4 — PDF page 20

**Role:** Two independent policy ablations on the same robot benchmark.

**Location:** crop `[107, 344, 506, 504]` pt; table-only bounds `[166, 445, 447, 503]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/cosmos-policy-t4.json`.

**Measured:** NimbusRomNo9L-Regu 8.261 pt (174 characters). Structural horizontal-rule widths: 0.413, 0.661 pt. Extracted vertical divider segments: 25. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Full method and two removal rows, evaluated on the four LIBERO suites plus average. Numbered row labels correspond to the two experimental explanations in the caption.

**Numbers and alignment (visual):** One decimal in all percentage values. The same metric headers repeat SR (%) for clarity.

**Uncertainty and missingness:** No dispersion. The two rows are separate interventions, not a cumulative sequence.

**Emphasis semantics:** No best-value bolding, no color and no shading; the comparison rests on row labels and numerical differences.

**Rules and spacing (visual):** Horizontal top/header/bottom rules and thin vertical metric dividers. The ablation is larger and more readable than the paired main-results table.

**Caption and comparability:** An unusually detailed caption defines auxiliary-loss masking versus training from scratch, including what remains trained in the world/value model.

**Recommended lessons:**

- Number ablations when the explanation is too long for the row label.
- Specify what remains fixed when a component is removed.

**Cautions:**

- Do not reduce both removals to a vague “without component” description that loses the actual intervention.

### Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning

**Source:** [v1; submitted 2026-04-14](https://arxiv.org/pdf/2604.12374v1). First publication: 2026. Coverage grouping: NVIDIA.

**Affiliation evidence:** Page 1: NVIDIA as group author and NVIDIA copyright.

#### Table 5 — PDF page 31

**Role:** Large evaluation suite grouped by capability.

**Location:** crop `[60, 112, 535, 730]` pt; table-only bounds `[65, 112, 532, 691]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/nemotron3-super-t5.json`.

**Measured:** LMRoman10-Regular 9.963 pt (894 characters); LMRoman10-Bold 9.963 pt (137 characters); LMMathSymbols10-Regular 9.963 pt (2 characters). Structural horizontal-rule widths: 0.542, 0.868 pt. Extracted vertical divider segments: 33. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Benchmark stub plus three model columns. Light-gray full-width bands mark six capability sections. TauBench V2 has an internal bold label and indented subdomains/average.

**Numbers and alignment (visual):** Most scores use two decimals, but some external entries keep one decimal. Dashes mark unreported comparisons. Numeric cells are visually centered.

**Uncertainty and missingness:** No uncertainty. Tool use, harness and subset conditions are written in the row labels rather than encoded only by markers.

**Emphasis semantics:** Bold group labels and column headers; ordinary numerical cells are not rank-highlighted. Gray fills encode capability sections.

**Rules and spacing (visual):** A single vertical separation after the benchmark stub and horizontal group/outer rules. The full-page format retains 9.963 pt primary text.

**Caption and comparability:** Caption names the comparison models; rows preserve distinctions such as with/without tools and alternative harnesses.

**Recommended lessons:**

- A tall table can preserve readable text better than a wide compressed matrix.
- Show evaluation harness and tool conditions directly when they define separate results.

**Cautions:**

- Do not equate variants of the same benchmark when their tools or harness differ.
- Mixed source precision should be normalized only under a documented formatting policy.

### Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying Autoregressive, Diffusion, and Self-Speculation Decoding

**Source:** [v1; submitted 2026-07-07](https://arxiv.org/pdf/2607.05722v1). First publication: 2026. Coverage grouping: NVIDIA.

**Affiliation evidence:** Page 1: NVIDIA copyright and NVIDIA internship note; additional Georgia Tech, HKU, University of Chicago and MIT affiliations.

#### Table 1 — PDF page 4

**Role:** Cumulative training-technique ablation.

**Location:** crop `[60, 83, 535, 170]` pt; table-only bounds `[64, 100, 534, 169]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/nemotron-diffusion-t1.json`.

**Measured:** LMRoman10-Regular 7.819 pt (261 characters); LMRoman10-Bold 7.819 pt (56 characters). Structural horizontal-rule widths: 0.391, 0.626 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** An initial Block-wise attention row is followed by four + technique rows and six benchmarks plus average. The sequence represents successive additions.

**Numbers and alignment (visual):** Two decimals in all scores; numeric columns are centered, and no compact delta is substituted for the absolute scores.

**Uncertainty and missingness:** No uncertainty or missing cells.

**Emphasis semantics:** Bold headers only, no score ranking, no color. Plus-prefixed labels communicate the trajectory.

**Rules and spacing (visual):** Three horizontal rules; no vertical grid or internal row rules.

**Caption and comparability:** Caption states continuous pretraining on 25B tokens. Neighboring prose explicitly says techniques are progressively added to the same starting model.

**Recommended lessons:**

- Declare cumulative versus independent ablation semantics in data and caption.
- Preserve absolute results through an ablation chain so readers can inspect nonmonotonic changes.

**Cautions:**

- A + row is not a gain-valued row; the numeric cells remain absolute performance.
- Do not compare each row as an independent one-factor intervention.

#### Table 5 — PDF page 11

**Role:** Quality/decoding-efficiency comparison across generation modes.

**Location:** crop `[60, 83, 535, 325]` pt; table-only bounds `[63, 113, 534, 324]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/nemotron-diffusion-t5.json`.

**Measured:** LMRoman10-Regular 7.463 pt (766 characters); LMRoman10-Bold 7.463 pt (136 characters); LMRoman10-Italic 7.463 pt (62 characters). Structural horizontal-rule widths: 0.373, 0.597 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Model spanners sit above a Gen. Mode row. The focal model spans four decoding modes, while SDAR has multiple mode/setting entries. Full-width italic task-group labels organize scientific QA, coding and math; an average block ends with Accuracy and TPF.

**Numbers and alignment (visual):** Two decimals in score and TPF rows. Multiple modes of one model are explicitly separate columns, preventing them from being mistaken for separately trained models.

**Uncertainty and missingness:** No uncertainty. No missing cells in this anchor.

**Emphasis semantics:** Pale green fills identify the focal model’s mode columns. Numerical maxima are not systematically bolded; color groups modes rather than certifying superiority.

**Rules and spacing (visual):** Outer rules and task-block rules; no vertical grid. Header spanners and fill combine to identify the same model across modes.

**Caption and comparability:** Caption identifies benchmark areas; surrounding text defines tokens per forward pass and evaluation choices. TPF is a model-execution measure, not directly wall-clock latency.

**Recommended lessons:**

- A unified model with multiple decoding modes needs explicit mode-level columns.
- Pair quality with a well-defined efficiency metric and preserve its actual physical meaning.

**Cautions:**

- Do not rename TPF as throughput or speedup without a hardware measurement.
- Green denotes the focal model family, not per-cell best performance.

### Cosmos-Reason1: From Physical Common Sense To Embodied Reasoning

**Source:** [v1; submitted 2025-03-18](https://arxiv.org/pdf/2503.15558v1). First publication: 2025. Coverage grouping: NVIDIA.

**Affiliation evidence:** Page 1: NVIDIA as group author and NVIDIA copyright; contributors in Appendix C.

#### Table 4 — PDF page 9

**Role:** Training-data composition by capability and annotation type.

**Location:** crop `[64, 680, 535, 750]` pt; table-only bounds `[64, 705, 535, 749]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/cosmos-reason1-t4.json`.

**Measured:** XCharter-Roman 6.660 pt (248 characters). Structural horizontal-rule widths: 0.370, 0.592 pt. Extracted vertical divider segments: 16. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Two rows (Understanding and Reasoning) across grouped Physical Common Sense, Embodied Reasoning, Intuitive Physics and Total columns. Subheaders name data sources or tasks.

**Numbers and alignment (visual):** Counts use K/M suffixes with varying decimal precision. Values are centered. A small table height accompanies many columns.

**Uncertainty and missingness:** Dashes occur where a capability/annotation combination is not supplied. No statistical uncertainty.

**Emphasis semantics:** No colored fill or bold numeric ranking; hierarchy comes from grouped headers.

**Rules and spacing (visual):** Horizontal outer/header rules and semantic vertical group dividers. Primary text is 6.660 pt.

**Caption and comparability:** Caption states the supervised-fine-tuning role; nearby prose distinguishes understanding annotations from reasoning chains and describes curation.

**Recommended lessons:**

- A coverage table should distinguish what is counted and which combinations exist.
- Keep total counts separate from heterogeneous annotation subtotals.

**Cautions:**

- K/M formatting loses exact counts; use explicit rounding policy when totals need to be auditable.
- A dash should not silently become a numerical zero in aggregation.

#### Table 7 — PDF page 18

**Role:** Post-training effect against both external systems and own backbones.

**Location:** crop `[140, 544, 452, 704]` pt; table-only bounds `[143, 570, 450, 703]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/cosmos-reason1-t7.json`.

**Measured:** XCharter-Roman 8.966 pt (321 characters). Structural horizontal-rule widths: 0.498, 0.797 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Three row blocks: external models, pretrained backbones and post-trained variants. Columns cover Space, Time, Other Physics and Avg.

**Numbers and alignment (visual):** One-decimal scores; green parenthetical gains attach to the last two average entries. Model labels are visually right/center aligned in the stub.

**Uncertainty and missingness:** Parenthetical values are gains relative to own backbones, not uncertainty. The nearby experiment text reports averaging five inferences with different seeds, but no dispersion appears in cells.

**Emphasis semantics:** Only the improvement annotations are green; there is no winner bolding. Horizontal blocks distinguish external comparison from paired control.

**Rules and spacing (visual):** Outer/header/block rules and no vertical grid. The table is centered at a narrower width than the page.

**Caption and comparability:** Caption is short; the neighboring setup specifies temperature, top-p and zero-shot chain-of-thought prompting. Those settings would need to accompany an isolated export.

**Recommended lessons:**

- Pair post-trained variants with their own controls and show their delta in a defined location.
- Keep the delta reference explicit when external comparison models share the same table.

**Cautions:**

- Do not treat the green parenthesis as a confidence interval or significance claim.
- Averages across repeated inferences do not substitute for reported variance.

### Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models

**Source:** [v4; revised 2025-09-05](https://arxiv.org/pdf/2504.03624v4). First publication: 2025. Coverage grouping: NVIDIA.

**Affiliation evidence:** Page 1: NVIDIA as group author and NVIDIA copyright.

#### Table 5 — PDF page 13

**Role:** Controlled hybrid-versus-transformer benchmark plus external references.

**Location:** crop `[60, 83, 535, 415]` pt; table-only bounds `[61, 84, 535, 352]` pt. Crop: （research image omitted; regenerate from the recorded PDF page and crop）. Measurement audit: `measurements/google-meta-nvidia/nvidia-nemotron-h-t5.json`.

**Measured:** LMRoman8-Regular 7.970 pt (515 characters); LMRoman8-Bold 7.970 pt (183 characters); LMRoman8-Italic 7.970 pt (16 characters). Structural horizontal-rule widths: 0.542, 0.868 pt. Extracted vertical divider segments: 0. These are object-segment counts, not the number of semantic table columns.

**Header and grouping:** Four capability blocks in a task stub and five model columns. Each benchmark row includes shot count and decoding/evaluation qualifiers.

**Numbers and alignment (visual):** One decimal across displayed scores. Selected externally reported values are italicized; blank cells occur where no result is supplied.

**Uncertainty and missingness:** No dispersion. Blank external entries are nonvalues. Italics signal a different evidence/provenance status, not emphasis for a runner-up.

**Emphasis semantics:** Caption defines bold as the highest accuracy per row excluding italicized values. A larger italicized external value can coexist with a smaller bold eligible maximum.

**Rules and spacing (visual):** Outer/header/group rules only, no color or vertical grid. Bold category labels separate task families.

**Caption and comparability:** Caption states that the Nemotron-T control uses exactly the same training data and distinguishes the externally sourced Gemma likelihood evaluations from rerun results.

**Recommended lessons:**

- Winner logic needs an eligibility mask, not just max(values).
- Place protocol qualifiers and provenance beside each score or row so ranking does not conceal differences.

**Cautions:**

- Do not bold an excluded italicized value just because it is numerically largest.
- Blank and zero must remain distinct; external reports and reruns are not automatically comparable.

## Reusable recipe implications

A table skill can support seven concrete starting points without claiming one company or one venue style: a sparse numerical comparison, family-grouped benchmark, independent removal ablation, cumulative addition/factor ablation, efficiency profile, dataset/coverage catalog and coefficient/uncertainty table. The common core is semantic data plus metadata, reproducible ranking and formatting, readable final placement, and a caption that declares the comparison. Each recipe should preserve the source-independent principles above while using synthetic fixtures and original renderings.

## Research-only file map

- `findings.json`: complete normalized evidence record.
- `findings.md`: this narrative audit and synthesis.
- `selected-papers.json`: exact prior-corpus selections.
- `anchors-measured.json`: crop-level measurement summary.
- `pdfs/`: 18 primary-source PDFs, research only.
- `pages/`: 29 rendered source pages, research only.
- `crops/`: 30 table regions, research only.
- `measurements/`: detailed PDF-object and layout reports, research only.

The PDFs, page images and crops must not be bundled as skill artwork. Source citations, original observations, measured scalar facts and fresh synthetic examples can be incorporated into the skill.
