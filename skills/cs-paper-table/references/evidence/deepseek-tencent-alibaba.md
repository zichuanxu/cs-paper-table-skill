> Portable evidence notes. Source PDFs and images are not bundled. Measurement paths below are relative to this directory; consult [measurement-method.md](measurement-method.md) for scope and reproduction.

# Table-design study: DeepSeek, Tencent/Hunyuan, Alibaba/Qwen

## Scope and evidence standard

This study contains **18 distinct reports and 32 visually inspected table anchors**, with six reports per company group. There are 9 first-publication reports from 2025 and 9 from 2026. The count is based on each unique paper once, not on versions, pages, or old figure studies. Seventeen sources come from the recovered `cs-paper-figure` corpus; Hunyuan-A13B adds language-model benchmark and throughput coverage.

Each counted crop was rendered at 216 dpi from the primary PDF and opened for visual reading. Caption extraction alone did not qualify an anchor. Every entry records source URL, inspected version, PDF page, crop rectangle, evidence path, and a separate table-body measurement rectangle. The JSON contains exact fonts, nominal point sizes, RGB/opacity, stroke widths, long-rule objects, and candidate numeric baseline gaps. Coordinates use PDF points from the top-left of the unrotated page.

Measurements are observations, not recommended defaults. A source's six-to-seven-point table body may be a density compromise, not a style to reproduce. Numerical baseline gaps are extraction candidates rather than an automatic row-height model. Underlines are also PDF strokes, and thin filled black rectangles can be rules; neither should be mistaken for background shading. The pale fills in HY-World 2.0 Table 7 are **opaque**, not translucent overlays.

Primary-company indexing records affiliations while preserving academic collaboration in Engram, Native Sparse Attention, and WorldMirror. It makes no claim that all authors belong to one company, that a company's papers share one official house style, or that any design pattern caused conference acceptance. The analysis concerns table construction and scientific interpretation, not the truth of a paper's performance claims.

## Transferable findings

### 1. Emphasis needs an explicit contract

There is no universal meaning for bold and underline. DeepSeek-V4 Table 1 defines highest/second-highest with a stated 0.3 tolerance. Qwen3-VL Table 2 defines best reasoning/best non-reasoning, which are separate ranking pools. Qwen3-VL-Embedding Table 2 bolds the proposed model names without bolding their scores. Qwen3-VL Table 12 emphasizes only the aggregate. A renderer should require `emphasis_role`, `ranking_scope`, `metric_direction`, `tie_policy`, and `display_precision`, and should not infer any of these from glyph appearance.

Rounded ties require deliberate handling: Hunyuan-A13B Table 3 shows two 44.6 values with different ranks. This may reflect unshown precision or an inconsistent tie policy; the visible table does not resolve it. A new table should either rank at displayed precision or explain the hidden-precision policy. Bold is not statistical significance.

### 2. Structure encodes the comparison

Benchmark rows work well with category stubs, explicit metric suffixes, and model-version headers. Wide multimodal tables use column-group rules to distinguish datasets or modes; ablation tables usually place the changed factor in the first column and held-constant controls in the caption. Configuration and coverage tables need different cell types from scores: counts, language sets, check/cross flags, modes, and schedule stages should not be forced into a numeric leaderboard.

The best structural lesson is the preservation of the experimental condition. Engram Table 4 embeds hardware, workload, and length distribution above its throughput values. Qwen3.8-Next Table 8 explicitly distinguishes budget reallocation from extra capacity. WorldMirror Table 5 separates two input conditions. HY-World 2.0 Table 14 keeps GPU count and OOM outcomes next to time and memory.

### 3. Color has a role, not a default aesthetic

Most inspected anchors use black data on white. Source color is often hyperlink provenance. OCR2 uses blue deltas, Engram mutes a secondary larger-budget column in gray, and HY-World 2.0 uses pale row fills to identify a baseline and selected setting. Those are distinct roles, not a generic corporate palette or heatmap. For new tables, reserve one low-saturation role fill for the baseline/selected row only when needed, and duplicate the role in text so grayscale remains meaningful.

Measured exceptional colors include Engram secondary text `#7F807F`, OCR2 delta text `#0000FF`, and HY-World 2.0 role fills `#FFE5E5` / `#E5E5FF`; each is opacity 1.0. Citation colors are separate source-link roles, including `#1976D2`, `#000080`, `#00AEEF`, and `#367DBD` in different reports. These measured values are not an endorsed palette.

### 4. Sparse rules generally serve hierarchy

Most tables use top/header/bottom rules plus rules at meaningful row-group boundaries. Partial horizontal rules are especially useful for grouped headers. A few tables use thin vertical separators only between labels and result fields or between model families. None of the inspected patterns needs a complete spreadsheet-like box grid to remain interpretable. A new design should map every rule to a boundary in the table's meaning.

Measured nominal body sizes span roughly 6.36 to 11.21 pt in this sample; exact per-anchor values follow below. Many dense comparison tables are around nine points, while simple setup and cost tables remain larger. Hairline rules in the most compressed Qwen embedding table are as small as about 0.10 pt in extracted PDF coordinates. This is evidence of aggressive scaling, not a recommended minimum. Prefer shortening headers, moving shared units into headers, splitting panels, or changing page orientation before shrinking text.

### 5. Units, directions, and missing-state semantics must be checked

Precision is metric-specific: one-decimal benchmark scores coexist with three-decimal losses/edit distances, four-decimal similarity/timing values, integers for counts, and explicit unit suffixes. Formatting all columns to a fashionable number of decimals destroys information. Keep greater-than token-budget qualifiers, percentages versus percentage points, and expected versus measured speedups explicit.

A dash has several incompatible source meanings: unsupported, not evaluated, omitted for training overlap, and structural not-applicable. OOM is an observed failure outcome and must remain distinct. In OCR2 Table 1 the reading-order edit header points upward while the improvement delta points downward; this apparent source inconsistency is a useful reminder to validate metric directions rather than copying arrows automatically.

### 6. Uncertainty and deltas are different data

HunyuanVideo 1.5 Table 7 reports plus/minus timing values. Nearby prose only says averages over multiple runs; neither the selected caption nor adjacent method text identifies SD, SE, CI, or n. The new skill must not silently invent these. Conversely, Qwen3.8-Next Table 6 explicitly uses subscripts for paired deltas, and Qwen3-ASR Table 2 reports p95 latency. Neither notation denotes a confidence interval. Require a typed statistical field and a complete legend when uncertainty is present; preserve honest absence when it is not.

## Recommended table families for the new skill

| Family | Useful source anchors | Core design contract |
|---|---|---|
| Main benchmark | DeepSeek-V4 T1; Qwen3-VL T2 | Model versions, metric labels, comparable ranking pools, explicit tie/footnote policy |
| Controlled ablation | Qwen3.8-Next T5/T8; Qwen3-VL T12 | Changed factor, fixed controls, per-task results, declared aggregate |
| Paired intervention | Qwen3.8-Next T6; OCR2 T4 | Baseline relation, typed deltas, no confusion with uncertainty |
| Efficiency/configuration sweep | Engram T4; Qwen3-ASR T2; HY-World2 T14 | Hardware/workload, units, concurrency/resources, tail latency, failure states |
| Dataset or capability coverage | Qwen3-ASR T1; Qwen3-Omni T3; Qwen embedding T2 | Counts and memberships, non-additive overlap, support versus measured quality |
| Training recipe | HunyuanImage3 T1; HunyuanVideo1.5 T2 | Stage ID, phase, input settings, trained modules/tasks, data-volume definition |
| Multi-objective selection | HY-World2 T7; WorldMirror T5 | Selection objective, visible trade-offs, role styling separate from ranking |
| Analytical cost | Native Sparse Attention T4 | Derived/expected label, approximation, units, separation from measured timing |

## Paper and table studies

### DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence

**DeepSeek · first-publication year 2026 · inspected 2606.19348v1**  
Primary PDF: [https://arxiv.org/pdf/2606.19348v1](https://arxiv.org/pdf/2606.19348v1)  
Affiliation evidence: Author organization DeepSeek-AI and research@deepseek.com printed on cover.

#### Table 1 — Benchmark comparison with model-budget metadata

**PDF page 28 · visually inspected.** Crop `[68, 82, 536, 505]` pt; measurement body `[70, 149, 536, 503]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/deepseek-v4-table-1.json`
- **Structure:** Two-line model headers; category stub, benchmark-with-metric stub, shot-count column, then three model columns. A three-row architecture/parameter block precedes four benchmark-domain blocks.
- **Alignment and precision:** Benchmark names are left aligned; model values and shot counts are centered. Benchmark scores use one decimal, while parameter counts retain meaningful B/T units. Metric suffixes are much smaller than the benchmark names.
- **Emphasis and color:** Bold marks the highest row score and underline the second. The caption explicitly treats gaps no larger than 0.3 as the same level. No shaded cells or decorative color.
- **Rules and spacing:** Heavy top/bottom rules, thinner section rules, and one fine vertical divider after shot count. The vertical divider stops at section breaks; no cell-by-cell horizontal grid.
- **Caption and notes:** Caption above; it identifies the shared internal evaluation framework, common settings, and tie rule.
- **Missing values and statistics:** Hyphens in metadata cells; no confidence intervals or repeat counts in the table. The 0.3 tolerance is an emphasis rule, not a statistical significance test.
- **Comparison contract:** Model size, active size, architecture, and shots are exposed before the results, so the table makes unequal resources visible rather than implying equal budgets.
- **Measured PDF properties:** main regular text 8.966 pt; leading font entries: URWPalladioL-Roma 8.966 pt, URWPalladioL-Bold 8.966 pt, URWPalladioL-Roma 5.978 pt. Extracted stroke widths: 0.398, 0.502, 0.542, 0.868 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Put evaluation conditions beside results when they vary by row or model. Compute emphasis from an explicit metric direction and tie policy.
- **Caution:** Do not inherit 0.3 as a universal tie threshold. Do not interpret small bold differences as significant without uncertainty evidence.

#### Table 10 — Compact cost-proxy comparison

**PDF page 55 · visually inspected.** Crop `[69, 391, 527, 483]` pt; measurement body `[111, 431, 486, 482]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/deepseek-v4-table-10.json`
- **Structure:** One header tier and two method rows; three result columns separate tool-call count, input-prefill tokens, and output tokens.
- **Alignment and precision:** Long method names are left aligned; numeric columns are right aligned. Mean calls have one decimal; token quantities are shown as integers.
- **Emphasis and color:** Only the header is bold. No rank emphasis or fill.
- **Rules and spacing:** Three horizontal rules and generous intercolumn space; the table stays narrower than the full text block.
- **Caption and notes:** Caption above labels values as means and says agentic calls are mostly parallel.
- **Missing values and statistics:** An em dash appears for retrieval tool calls without a separate missing-value legend; no dispersion or sample count is attached to means.
- **Comparison contract:** The values are usage proxies. Parallel calls mean tool-call count does not directly imply wall-clock latency, and token counts alone do not specify monetary cost.
- **Measured PDF properties:** main regular text 9.963 pt; leading font entries: URWPalladioL-Roma 9.963 pt, URWPalladioL-Bold 9.963 pt. Extracted stroke widths: 0.542, 0.868 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Use compact tables for a small number of precisely defined resource measures. Keep resource units in column headings.
- **Caution:** Distinguish not-applicable, unmeasured, and zero tool calls. Do not relabel these counts as currency or measured latency.
### DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression

**DeepSeek · first-publication year 2026 · inspected 2609.19969v1**  
Primary PDF: [https://arxiv.org/pdf/2609.19969v1](https://arxiv.org/pdf/2609.19969v1)  
Affiliation evidence: Author organization DeepSeek-AI and research@deepseek.com printed on cover.

#### Table 1 — Benchmark comparison extended to multimodal capability

**PDF page 24 · visually inspected.** Crop `[68, 82, 541, 466]` pt; measurement body `[69, 149, 541, 465]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/deepseek-v41-flash-table-1.json`
- **Structure:** Two-line model headers sit above a metadata block and grouped text, reasoning, code/math, long-context, and multimodal benchmark rows. Activated parameters are a dedicated row.
- **Alignment and precision:** Centered score columns use one decimal; benchmark labels are left aligned with small metric suffixes. The activated-parameter entry preserves a slash-separated prefill/decode budget.
- **Emphasis and color:** Bold highest and underlined second follow the caption's 0.3 tie policy. The multimodal rows with only one reported model are not automatically bolded as wins.
- **Rules and spacing:** Section rules plus a segmented divider before model results. No interior row grid or fill.
- **Caption and notes:** Caption above defines common evaluation settings, emphasis, and tie tolerance.
- **Missing values and statistics:** Dashes occur in predecessors' multimodal cells; no uncertainty is reported.
- **Comparison contract:** The table displays capability coverage as well as accuracy. A missing predecessor capability is a different comparison situation from a measured lower score.
- **Measured PDF properties:** main regular text 8.966 pt; leading font entries: URWPalladioL-Roma 8.966 pt, URWPalladioL-Bold 8.966 pt, URWPalladioL-Roma 5.978 pt. Extracted stroke widths: 0.398, 0.502, 0.542, 0.868 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Expose distinct prefill/decode resource quantities rather than collapsing them to one number. Permit unranked single-observation rows.
- **Caution:** Define whether a dash means unsupported or not evaluated. Do not count unreported cells as losses.

#### Table 3 — Wide frontier benchmark comparison with subset footnotes

**PDF page 33 · visually inspected.** Crop `[68, 166, 527, 475]` pt; measurement body `[70, 221, 527, 474]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/deepseek-v41-flash-table-3.json`
- **Structure:** Seven model columns each retain a reasoning-effort line. Rotated category labels divide reasoning and agentic tasks; benchmark metrics appear in small suffixes.
- **Alignment and precision:** Centered results mix one-decimal percentages, integer ratings, and a parenthetical alternate HLE score. Column headers are closely packed.
- **Emphasis and color:** Bold best and underlined second are defined in the caption; no shaded own-model column. Fine vertical rules isolate the result field and final model.
- **Rules and spacing:** Minimal horizontal rules at major task boundaries; rotated labels save width but impose a reading cost.
- **Caption and notes:** Caption above defines a dagger as the text-only HLE subset. This symbol travels with individual values, including the alternate parenthetical result.
- **Missing values and statistics:** Dashes denote absent reported results; no intervals. Parenthetical HLE values are alternate subsets, not uncertainty.
- **Comparison contract:** Max effort is shown, but this is not proof of equal compute across architectures. Text-only HLE values must remain distinguishable from full-set values.
- **Measured PDF properties:** main regular text 9.113 pt; leading font entries: URWPalladioL-Roma 9.113 pt, URWPalladioL-Bold 9.113 pt, URWPalladioL-Roma 6.075 pt. Extracted stroke widths: 0.404, 0.510, 0.551, 0.882 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Encode evaluation-subset provenance per cell, not just per column. Keep effort labels in the header when they affect comparability.
- **Caution:** Do not rank full-set and subset values as interchangeable. Use rotated group labels only when the resulting layout remains readable at final size.
### Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models

**DeepSeek · first-publication year 2026 · inspected 2601.07372v1**  
Primary PDF: [https://arxiv.org/pdf/2601.07372v1](https://arxiv.org/pdf/2601.07372v1)  
Affiliation evidence: Numbered affiliations explicitly identify Peking University and DeepSeek-AI; this is a collaboration, not solely corporate authorship.

#### Table 1 — Controlled parameter-budget comparison with secondary scaling condition

**PDF page 9 · visually inspected.** Crop `[69, 82, 527, 597]` pt; measurement body `[70, 177, 527, 597]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/engram-table-1.json`
- **Structure:** Category and benchmark stubs plus shots precede four model columns. Five explicit metadata rows disclose total/active parameters, training tokens, experts, and memory size.
- **Alignment and precision:** Left-aligned benchmark names and centered numeric columns; losses use three decimals and benchmark scores one. Small metric suffixes reduce label width.
- **Emphasis and color:** The larger Engram-40B condition is gray text and gray divider strokes, while the controlled comparison is black. The Engram-27B results are bolded. This is de-emphasis of a secondary budget condition, not a heatmap.
- **Rules and spacing:** Heavy outer rules, section dividers, and sparse vertical separators; category labels occupy multirow cells.
- **Caption and notes:** Caption above explains the iso-parameter comparison, equal active parameters and training tokens, and the extra memory in the larger condition.
- **Missing values and statistics:** Hyphens indicate inapplicable memory/expert fields. No intervals or independent-run counts.
- **Comparison contract:** The gray column has a different total-parameter budget. The caption makes that exception explicit; color alone would be inadequate evidence of the comparison group.
- **Measured PDF properties:** main regular text 8.966 pt; leading font entries: URWPalladioL-Roma 8.966 pt, URWPalladioL-Roma 5.978 pt, URWPalladioL-Bold 8.966 pt. Extracted stroke widths: 0.398, 0.542, 0.868 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1), #7F807F (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Show the resource envelope before benchmark results. Visually separate auxiliary scaling conditions while preserving an explicit textual explanation.
- **Caution:** Do not assume gray means worse, missing, or statistically insignificant. Keep comparable ranking groups explicit when total budgets differ.

#### Table 4 — Efficiency table with embedded experimental setup

**PDF page 18 · visually inspected.** Crop `[69, 82, 527, 300]` pt; measurement body `[130, 127, 466, 300]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/engram-table-4.json`
- **Structure:** A full-width Experimental Setup section lists hardware, workload, and sequence-length distribution; a second Throughput Results section contains paired baseline/offload rows for two base-model sizes.
- **Alignment and precision:** Labels are left aligned, setup values and throughput centered. Throughput uses thousands separators and two decimals; the unit is tokens per second in the header.
- **Emphasis and color:** Bold section/header labels and italic setup-field labels establish hierarchy; numerical results have no winner emphasis or fill.
- **Rules and spacing:** Horizontal-only rules separate setup, results header, and paired model groups. The table uses a substantially larger body font than the dense benchmark tables.
- **Caption and notes:** Caption above states the 100B memory layer is entirely offloaded to host memory.
- **Missing values and statistics:** No missing cells or uncertainty. A small throughput difference is presented as a value, without a significance claim encoded by typography.
- **Comparison contract:** The hardware, 512-sequence workload, and Uniform(100,1024) length distribution are attached to the measurement, making the result more independently interpretable.
- **Measured PDF properties:** main regular text 10.909 pt; leading font entries: URWPalladioL-Roma 10.909 pt, URWPalladioL-Bold 10.909 pt, URWPalladioL-Ital 10.909 pt. Extracted stroke widths: 0.542, 0.868 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Use a setup block for efficiency results when several conditions apply to every row. Pair baseline and intervention within each hardware/model condition.
- **Caution:** Report repeats and a defined variability statistic when small timing differences matter. Do not treat parameter count alone as measured runtime cost.
### DeepSeek-OCR 2: Visual Causal Flow

**DeepSeek · first-publication year 2026 · inspected 2601.20552v1**  
Primary PDF: [https://arxiv.org/pdf/2601.20552v1](https://arxiv.org/pdf/2601.20552v1)  
Affiliation evidence: Haoran Wei, Yaofeng Sun, and Yukun Li are followed by DeepSeek-AI on the cover.

#### Table 1 — OCR benchmark with resource and quality metrics plus delta row

**PDF page 9 · visually inspected.** Crop `[69, 80, 527, 505]` pt; measurement body `[70, 146, 527, 503]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/deepseek-ocr2-table-1.json`
- **Structure:** Model rows are divided into pipeline and end-to-end systems. Visual-token budget precedes several quality metrics; the two DeepSeek rows and a delta row form the final block.
- **Alignment and precision:** Names are left aligned; numeric fields centered. Percent-like scores use two decimals, edit distances three, and token limits retain greater-than signs.
- **Emphasis and color:** Blue data text encodes the difference from the preceding DeepSeek version. Citation links use a different blue. Bold is largely structural rather than a global winner ranking; no background fill.
- **Rules and spacing:** Outer and group rules, with narrow vertical separators after model name, token budget, and overall score. No row grid inside comparison groups.
- **Caption and notes:** Caption above defines the visual-token maximum and identifies externally sourced results versus the authors' own evaluations.
- **Missing values and statistics:** Dashes occur for unavailable token counts. The delta row is not an uncertainty interval. No run counts or intervals.
- **Comparison contract:** Comparing resource ceilings requires retaining greater-than qualifiers and the distinction between pipeline and end-to-end methods. An apparent source inconsistency exists: the reading-order edit header points upward while its blue improvement delta points downward.
- **Measured PDF properties:** main regular text 8.966 pt; leading font entries: URWPalladioL-Roma 8.966 pt, URWPalladioL-Bold 8.966 pt, XCharterMathMI 6.049 pt. Extracted stroke widths: 0.398, 0.542, 0.897 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1), #1976D2 (alpha 1), #0000FF (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Give improvements their own explicitly labeled delta row when the baseline relationship is central. Keep source provenance and resource-limit qualifiers.
- **Caution:** Verify metric directions independently instead of copying a source arrow. Separate hyperlink color from data semantics.

#### Table 4 — Production proxy metric with inline change annotations

**PDF page 11 · visually inspected.** Crop `[69, 82, 527, 193]` pt; measurement body `[125, 136, 469, 192]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/deepseek-ocr2-table-4.json`
- **Structure:** Two models share a vertically merged Repeat metric cell; two result columns distinguish user-image logs and pretraining PDFs.
- **Alignment and precision:** Percentages use two decimals. Improvements are appended to the new model values rather than placed in separate columns.
- **Emphasis and color:** Inline blue downward deltas show reduction from the earlier model. The model names and measurements remain black; no rank-based bold or row fill.
- **Rules and spacing:** Heavy outer rules, a header rule, two fine vertical dividers, and a partial horizontal rule that respects the merged metric cell.
- **Caption and notes:** Caption above explains that unavailable production ground truth motivates use of repetition rate as an observable proxy.
- **Missing values and statistics:** No intervals, sample counts, or missing values. The printed delta uses a percent sign even though subtraction of rates represents percentage-point change.
- **Comparison contract:** The table compares a production quality proxy, not a direct ground-truth OCR accuracy measurement.
- **Measured PDF properties:** main regular text 9.963 pt; leading font entries: URWPalladioL-Roma 9.963 pt, txsys 9.963 pt. Extracted stroke widths: 0.325, 0.398, 0.542, 0.868 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1), #0000FF (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Make a proxy outcome explicit in the caption. Use an inline delta only when its baseline is unambiguous.
- **Caution:** Label absolute rate changes as percentage points. Do not reinterpret a reduced repetition rate as a quantified accuracy gain.
### DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

**DeepSeek · first-publication year 2025 · inspected 2501.12948v1**  
Primary PDF: [https://arxiv.org/pdf/2501.12948v1](https://arxiv.org/pdf/2501.12948v1)  
Affiliation evidence: Author organization DeepSeek-AI and research@deepseek.com printed on cover.

#### Table 4 — Mixed-domain benchmark table with model metadata

**PDF page 13 · visually inspected.** Crop `[97, 113, 498, 461]` pt; measurement body `[97, 114, 498, 435]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/deepseek-r1-table-4.json`
- **Structure:** Model/version headers span two lines. Architecture and parameter metadata precede English, code, math, and Chinese row groups; benchmark metric names are retained in the stub.
- **Alignment and precision:** Benchmark labels are left aligned and scores centered. Most results use one decimal, while Codeforces ratings remain integers.
- **Emphasis and color:** Numerically strong cells are bolded throughout multiple model columns; the authors' model is not uniformly bold. No fill or color.
- **Rules and spacing:** Thin vertical separators divide blocks of model columns and stop at horizontal category rules. Top/bottom rules are thicker than internal rules.
- **Caption and notes:** The caption is below and is short; the table itself carries model dates, metric labels, and size information.
- **Missing values and statistics:** Hyphens in unreported metadata and benchmark cells; no uncertainty. The caption does not separately define a tie policy.
- **Comparison contract:** Different metrics and scales coexist by row, so ranking is meaningful within a row only. Model names include evaluation-specific version dates.
- **Measured PDF properties:** main regular text 8.966 pt; leading font entries: URWPalladioL-Roma 8.966 pt, URWPalladioL-Roma 5.978 pt, URWPalladioL-Bold 8.966 pt. Extracted stroke widths: 0.398, 0.542, 0.868 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Preserve metric names and model versions in benchmark tables. Allow baseline models to receive the same winner treatment as the proposed model.
- **Caution:** Do not average heterogeneous row values without a declared normalization and aggregation rule. Add a missing-value and emphasis legend when making a standalone table.
### Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention

**DeepSeek · first-publication year 2025 · inspected 2502.11089v1**  
Primary PDF: [https://arxiv.org/pdf/2502.11089v1](https://arxiv.org/pdf/2502.11089v1)  
Affiliation evidence: Numbered affiliations explicitly identify DeepSeek-AI, Peking University, and University of Washington; primary-company indexing does not erase academic collaborators.

#### Table 4 — Analytical efficiency estimate

**PDF page 14 · visually inspected.** Crop `[69, 83, 527, 213]` pt; measurement body `[151, 86, 442, 161]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/native-sparse-attention-table-4.json`
- **Structure:** Context lengths are the column headers; baseline and sparse memory-access volumes occupy two rows; a separated final row shows expected speedup.
- **Alignment and precision:** Integer access volumes are centered. Speedup uses a multiplication symbol and preserves one decimal only when needed.
- **Emphasis and color:** The derived speedup values are bold. Other values and labels remain regular; no color or shading.
- **Rules and spacing:** Horizontal-only rules and a narrow centered table leave substantial surrounding white space. Larger body text avoids unnecessary full-width expansion.
- **Caption and notes:** Caption below explains the equivalence in tokens and the memory-bound approximation behind expected speedup.
- **Missing values and statistics:** No uncertainty is shown because these are derived access-volume estimates rather than repeated timing measurements.
- **Comparison contract:** The word expected and the stated approximation are essential: the table does not claim these ratios are measured end-to-end wall-clock speedups.
- **Measured PDF properties:** main regular text 11.213 pt; leading font entries: URWPalladioL-Roma 11.213 pt, URWPalladioL-Bold 11.213 pt, txsys 11.213 pt. Extracted stroke widths: 0.557, 0.892 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Use a visually separate derived-results row. Keep theoretical, simulated, and measured quantities explicitly distinguished.
- **Caution:** Do not remove the approximation from the caption. Do not use the table as a measured runtime comparison.
### On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability

**Alibaba / Qwen · first-publication year 2026 · inspected 2608.30320v1**  
Primary PDF: [https://arxiv.org/pdf/2608.30320v1](https://arxiv.org/pdf/2608.30320v1)  
Affiliation evidence: Cover author Qwen Team; official repository explicitly says developed by Qwen Team, Alibaba Group.
Supporting affiliation source: https://github.com/QwenLM/Qwen3.8-Flash-Next

#### Table 5 — Residual-design ablation

**PDF page 11 · visually inspected.** Crop `[69, 68, 527, 182]` pt; measurement body `[70, 111, 525, 180]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/qwen38-next-table-5.json`
- **Structure:** Two logical header tiers group nine benchmarks into Knowledge, STEM, Reasoning, Multilingual, and Code. Loss and Avg. flank the benchmark groups; four residual variants form the body.
- **Alignment and precision:** Variants are left aligned, numeric fields centered. Loss has three decimals; scores and average have two.
- **Emphasis and color:** Bold identifies per-column best results, including a minimum for loss. Winners vary across columns; no color, underline, or shaded proposed row.
- **Rules and spacing:** Three main horizontal rules plus short rules under column groups; no vertical grid. Compact four-row body.
- **Caption and notes:** Caption above fixes model size, 560B training tokens, four branches, and the distinction between static and dynamic variants.
- **Missing values and statistics:** No missing cells, variance, confidence intervals, or repeat counts.
- **Comparison contract:** The table makes the controlled budget explicit and preserves regressions rather than presenting a single aggregate alone.
- **Measured PDF properties:** main regular text 7.483 pt; leading font entries: TeXGyrePagella-Regular 7.483 pt, TeXGyrePagella-Bold 7.483 pt. Extracted stroke widths: 0.250, 0.416, 0.665 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Place controls and the changed factor in the caption for ablations. Use grouped headers to retain task breadth without repeating long labels.
- **Caution:** A best cell is not proof of statistical significance. The measured small type should not become a universal size default.

#### Table 6 — Paired normalization ablation with subscript deltas

**PDF page 12 · visually inspected.** Crop `[303, 272, 529, 414]` pt; measurement body `[325, 336, 505, 414]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/qwen38-next-table-6.json`
- **Structure:** A narrow three-column table compares a residual design, base loss, and loss with GatedNorm. Five designs fit beside prose in the source layout.
- **Alignment and precision:** Losses have three decimals. Signed changes appear as smaller subscripts attached to the new loss value.
- **Emphasis and color:** Only the smallest loss is bolded. Subscripts are deltas from the left column, not confidence intervals or standard errors.
- **Rules and spacing:** Horizontal-only top/header/bottom rules. The narrow layout wraps the caption into several lines while keeping body entries on one line.
- **Caption and notes:** Caption above explicitly defines GN, the layer count, the sublayer parameter S, and the meaning of the subscripts.
- **Missing values and statistics:** An em dash occurs for GR's base-loss entry. No repeated-run uncertainty is reported.
- **Comparison contract:** The paired layout encodes the intervention relation. A design without the left-hand condition should not be assigned a fabricated baseline.
- **Measured PDF properties:** main regular text 8.966 pt; leading font entries: TeXGyrePagella-Regular 8.966 pt, LMRoman7-Regular 6.974 pt, LMRoman9-Regular 8.966 pt. Extracted stroke widths: 0.498, 0.797 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Distinguish paired changes from uncertainty in both schema and caption. Use a narrow table for a small local comparison.
- **Caution:** Do not parse subscript deltas as error bars. Define structural not-applicable cells explicitly.

#### Table 8 — Budget-controlled capacity allocation ablation

**PDF page 15 · visually inspected.** Crop `[69, 267, 527, 375]` pt; measurement body `[73, 310, 522, 374]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/qwen38-next-table-8.json`
- **Structure:** Two header tiers place vocabulary scale and parameter ratio first, followed by loss, perplexity, and grouped domain benchmarks. Four allocation settings are shown.
- **Alignment and precision:** Scale and ratio share a label cell; losses have three decimals, perplexity and downstream scores two. Numeric cells are centered.
- **Emphasis and color:** Bold marks best per metric, with different winners across metrics. No shading or global best-row designation.
- **Rules and spacing:** Minimal horizontal rules and short group rules; the many columns result in a measured body size below seven points.
- **Caption and notes:** Caption above states total model parameters are fixed and MoE experts are reduced to offset memory growth.
- **Missing values and statistics:** No missing entries or uncertainty. Parameter ratios are configuration metadata, not score percentages.
- **Comparison contract:** The controlled total budget is the reason this table supports an allocation comparison. It must not be conflated with the adjacent experiment that adds parameters.
- **Measured PDF properties:** main regular text 6.789 pt; leading font entries: TeXGyrePagella-Regular 6.789 pt, TeXGyrePagella-Bold 6.789 pt, LMMathSymbols10-Regular 6.789 pt. Extracted stroke widths: 0.204, 0.339, 0.543 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Keep fixed-budget and extra-budget experiments as separate tables or explicitly labeled panels. Retain both loss and downstream metrics when they respond differently.
- **Caution:** Do not merge experiments with different resource controls. Prefer splitting panels or abbreviating carefully over copying aggressive downscaling.
### Qwen3-ASR Technical Report

**Alibaba / Qwen · first-publication year 2026 · inspected 2601.21337v1**  
Primary PDF: [https://arxiv.org/pdf/2601.21337v1](https://arxiv.org/pdf/2601.21337v1)  
Affiliation evidence: Cover author Qwen Team and official QwenLM/Qwen3-ASR repository link.
Company mapping: [official Qwen organization](https://github.com/QwenLM).

#### Table 1 — Capability and language-coverage inventory

**PDF page 4 · visually inspected.** Crop `[69, 124, 527, 358]` pt; measurement body `[72, 180, 523, 357]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/qwen3-asr-table-1.json`
- **Structure:** One header tier covers model, languages, dialects, inference mode, maximum length, and audio types. Two ASR model sizes share a row; the aligner has a separate row.
- **Alignment and precision:** Long language and dialect lists wrap inside wide cells; model labels and compact categorical entries are centered vertically. The resulting font is below seven points.
- **Emphasis and color:** Bold model labels and an entirely bold descriptive caption. No rank emphasis or fill.
- **Rules and spacing:** Top/header/model-boundary/bottom horizontal rules; variable-width columns accommodate lists.
- **Caption and notes:** Caption above separates 30 languages from 22 Chinese dialects and defines sequence length and NAR.
- **Missing values and statistics:** A dash is used for dialect coverage of the aligner; the table reports capabilities, so uncertainty is not applicable.
- **Comparison contract:** Support counts and language membership are capability claims, not measured recognition quality or equal training-data coverage.
- **Measured PDF properties:** main regular text 6.750 pt; leading font entries: URWPalladioL-Roma 6.750 pt, URWPalladioL-Bold 6.750 pt. Extracted stroke widths: 0.375, 0.600 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Use list-bearing cells for modest inventories and a separate appendix when they become too dense. Separate language, dialect, mode, and maximum-input-length fields.
- **Caution:** Do not equate support with benchmark performance. Keep not-applicable support fields explicit, and avoid very small text for long lists.

#### Table 2 — Concurrency sweep across inference modes

**PDF page 5 · visually inspected.** Crop `[69, 68, 527, 458]` pt; measurement body `[71, 146, 522, 456]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/qwen3-asr-table-2.json`
- **Structure:** An offline block contains RTF and throughput; an online asynchronous block contains mean TTFT, p95 TTFT, RTF, and throughput. Model blocks share a concurrency column.
- **Alignment and precision:** Numbers are centered with five-decimal RTF, two-decimal throughput, and integer milliseconds. Multirow model labels reduce repetition across long concurrency sweeps.
- **Emphasis and color:** Bold model and header labels only. There is no automatic best-throughput emphasis, consistent with a latency/throughput trade-off.
- **Rules and spacing:** Group rules separate models; short header rules span inference modes; no vertical grid.
- **Caption and notes:** Caption above defines concurrency and p95, distinguishes vLLM from PyTorch, and gives different input-audio durations for ASR and alignment.
- **Missing values and statistics:** Dashes cover unsupported online alignment and unreported high-concurrency online runs. p95 is a latency quantile, not a confidence interval.
- **Comparison contract:** Backend and workload differences constrain cross-model comparisons. The caption's hardware description is generic, so it is not a complete hardware specification.
- **Measured PDF properties:** main regular text 8.462 pt; leading font entries: URWPalladioL-Roma 8.462 pt, URWPalladioL-Bold 8.462 pt. Extracted stroke widths: 0.282, 0.470, 0.752 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Report tail latency beside throughput. Keep workload, backend, and concurrency attached to efficiency results.
- **Caution:** Differentiate unsupported from unmeasured cells. Do not call p95 a confidence interval or infer a specific GPU from a generic compute-resource description.
### Qwen3-TTS Technical Report

**Alibaba / Qwen · first-publication year 2026 · inspected 2601.15621v1**  
Primary PDF: [https://arxiv.org/pdf/2601.15621v1](https://arxiv.org/pdf/2601.15621v1)  
Affiliation evidence: Cover author Qwen Team and official QwenLM/Qwen3-TTS repository link.
Company mapping: [official Qwen organization](https://github.com/QwenLM).

#### Table 2 — Streaming latency decomposition by model and concurrency

**PDF page 5 · visually inspected.** Crop `[69, 592, 527, 772]` pt; measurement body `[70, 612, 525, 772]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/qwen3-tts-table-2.json`
- **Structure:** Four model/tokenizer configurations each have a three-row concurrency sweep. Columns decompose LM first-packet time, tokenizer decode time, total first-packet latency, token-packet time, and real-time factor.
- **Alignment and precision:** Model strings repeat per row; numeric timings include ms in each cell. RTF uses three decimals, concurrency integers.
- **Emphasis and color:** Only header/caption emphasis; data are regular black text. No winner color, bold, or background.
- **Rules and spacing:** Horizontal rules separate each model configuration. Long single-line headers create a tight fit across the page.
- **Caption and notes:** The caption above identifies tokenizer and concurrency comparison; the surrounding efficiency section carries additional measurement context.
- **Missing values and statistics:** No missing values or reported uncertainty in the selected table.
- **Comparison contract:** The decomposition prevents readers from attributing all first-packet latency to the language model. Concurrency changes both latency and throughput-related measures.
- **Measured PDF properties:** main regular text 8.966 pt; leading font entries: URWPalladioL-Roma 8.966 pt, URWPalladioL-Bold 8.966 pt. Extracted stroke widths: 0.498, 0.797 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Expose component and end-to-end timings together. Use consistent configuration blocks for repeated workloads.
- **Caution:** Move repeated units into headers in a new design when width is scarce. Preserve measurement context when extracting the table from surrounding prose.
### Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking

**Alibaba / Qwen · first-publication year 2026 · inspected 2601.04720v1**  
Primary PDF: [https://arxiv.org/pdf/2601.04720v1](https://arxiv.org/pdf/2601.04720v1)  
Affiliation evidence: Author affiliation explicitly printed as Tongyi Lab, Alibaba Group.

#### Table 2 — Multimodal retrieval benchmark with coverage counts

**PDF page 11 · visually inspected.** Crop `[69, 68, 527, 333]` pt; measurement body `[70, 126, 525, 332]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/qwen3-vl-embedding-table-2.json`
- **Structure:** Two tiers group result columns under Image, Video, VisDoc, and All. A dataset-count row precedes open-source, closed-source, and Qwen model blocks; model size is a separate field.
- **Alignment and precision:** Left-aligned model labels and centered results. Mostly one decimal, with some integers shown without a trailing zero; many result columns lead to small type and very thin rules.
- **Emphasis and color:** The authors' model labels are bold, but their numeric results are regular. Bold-italic section titles mark model families; dark-blue reference links are provenance links, not performance encoding.
- **Rules and spacing:** Only horizontal rules, with short group-header rules and extra breaks between size blocks. No fill or per-cell grid.
- **Caption and notes:** Caption above expands abbreviations, identifies model-homepage links, and states an updated out-of-distribution split was re-evaluated except for one model.
- **Missing values and statistics:** Size dashes appear for closed-source systems. No uncertainty. The table distinguishes reported coverage through dataset counts.
- **Comparison contract:** The re-evaluation exception limits direct comparison on OOD. Counts alone do not define how the overall aggregate weights datasets or groups.
- **Measured PDF properties:** main regular text 6.841 pt; leading font entries: URWPalladioL-Roma 6.841 pt, URWPalladioL-Bold 6.841 pt, URWPalladioL-BoldItal 6.841 pt. Extracted stroke widths: 0.099, 0.165, 0.264 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1), #000080 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Show coverage denominators beside aggregate results. Keep emphasis on identity separate from emphasis on numerical ranking.
- **Caution:** Do not infer best scores from bold model names. Carry split-version exceptions and define aggregate weighting.
### Qwen3-Omni Technical Report

**Alibaba / Qwen · first-publication year 2025 · inspected 2509.17765v1**  
Primary PDF: [https://arxiv.org/pdf/2509.17765v1](https://arxiv.org/pdf/2509.17765v1)  
Affiliation evidence: Cover author Qwen Team and official QwenLM/Qwen3-Omni repository link.
Company mapping: [official Qwen organization](https://github.com/QwenLM).

#### Table 3 — Compact modality-specific language support

**PDF page 7 · visually inspected.** Crop `[97, 227, 499, 307]` pt; measurement body `[97, 247, 499, 307]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/qwen3-omni-table-3.json`
- **Structure:** Three columns and three rows distinguish text, speech input, and speech output. Counts are adjacent to language inventories.
- **Alignment and precision:** Counts are centered; the language column lists short codes. Text coverage points to a fuller list elsewhere rather than placing 119 names in one cell.
- **Emphasis and color:** Caption title is bold; the body has no rank or color emphasis.
- **Rules and spacing:** Three horizontal rules; a compact table uses large readable text rather than filling the page with extra columns.
- **Caption and notes:** Caption above identifies the model. A cross-reference in the text row delegates the long list to Qwen3.
- **Missing values and statistics:** No missing values or uncertainty; these are supported-language sets.
- **Comparison contract:** Input and output support are distinct capability sets and are not additive counts of unique languages.
- **Measured PDF properties:** main regular text 9.963 pt; leading font entries: URWPalladioL-Roma 9.963 pt. Extracted stroke widths: 0.498, 0.797 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Use a short inventory plus a precise external or appendix reference for long sets. Separate input and output capability.
- **Caution:** Do not sum overlapping modality-specific language counts. A standalone reproduction needs a resolvable reference to the full list.
### Qwen3-VL Technical Report

**Alibaba / Qwen · first-publication year 2025 · inspected 2511.21631v1**  
Primary PDF: [https://arxiv.org/pdf/2511.21631v1](https://arxiv.org/pdf/2511.21631v1)  
Affiliation evidence: Cover author Qwen Team and official QwenLM/Qwen3-VL repository link.
Company mapping: [official Qwen organization](https://github.com/QwenLM).

#### Table 2 — Full-page multimodal benchmark by reasoning mode

**PDF page 15 · visually inspected.** Crop `[69, 68, 538, 792]` pt; measurement body `[70, 113, 536, 790]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/qwen3-vl-table-2.json`
- **Structure:** Four model-family headers each span two mode columns. Category and benchmark stubs support many domain groups. Header lines retain family, size/version, and reasoning mode.
- **Alignment and precision:** Both labels and scores are largely centered. Metrics require row-specific precision: percentages, integers, and three-decimal edit distances coexist.
- **Emphasis and color:** The caption defines bold as the best reasoning-model score and underline as the best non-reasoning score. Underline does not mean second place. Asterisks indicate reported values and plus signs tool use.
- **Rules and spacing:** Vertical rules separate model families, not the two modes inside each family. Horizontal rules separate domains, allowing a tall full-page table without row-by-row boxes.
- **Caption and notes:** Caption above explains emphasis groups, source provenance, and tool-use markers.
- **Missing values and statistics:** Dashes mark unreported outcomes; no intervals. Some lower-is-better metrics lack explicit row arrows, so a renderer needs independent direction metadata.
- **Comparison contract:** Ranking occurs within reasoning groups. Tool use, external-report sourcing, and model-specific mode names must remain visible for scientific comparability.
- **Measured PDF properties:** main regular text 8.140 pt; leading font entries: URWPalladioL-Roma 8.140 pt, URWPalladioL-Bold 8.140 pt, URWPalladioL-Roma 6.331 pt. Extracted stroke widths: 0.326, 0.398, 0.452, 0.724 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Represent ranking groups explicitly in the table specification. Keep source and tool-use flags as cell-level metadata.
- **Caution:** Never apply a universal best/second-best legend to this pattern. Do not compute row winners before validating direction and comparable group membership.

#### Table 12 — Small controlled component ablation

**PDF page 24 · visually inspected.** Crop `[69, 669, 527, 758]` pt; measurement body `[70, 714, 525, 757]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/qwen3-vl-table-12.json`
- **Structure:** Two method rows compare baseline with DeepStack; an AVG column comes immediately after the method before individual benchmark columns.
- **Alignment and precision:** All reported scores use one decimal. Compact benchmark abbreviations fit a wide single-tier header.
- **Emphasis and color:** Only the improved AVG is bold; individual scores remain regular, including a small regression. No colored row or fill.
- **Rules and spacing:** Top/header/bottom rules only. Two rows keep the comparison visually direct.
- **Caption and notes:** Caption above fixes the internal language-model size, 200B-token pretraining, validation-set evaluation, and absence of post-training.
- **Missing values and statistics:** No missing values, intervals, or repeat counts.
- **Comparison contract:** The local ablation is controlled separately from the report's large-model benchmark comparisons. Retaining each task reveals that aggregate improvement is not universal.
- **Measured PDF properties:** main regular text 8.390 pt; leading font entries: URWPalladioL-Roma 8.390 pt, URWPalladioL-Bold 8.390 pt, URWPalladioL-Ital 6.376 pt. Extracted stroke widths: 0.419, 0.671 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Expose the target aggregate alongside component metrics. Attach model, training budget, and evaluation stage to ablations.
- **Caution:** Define how AVG is calculated. Do not infer every task improved from a bold aggregate.
### HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds

**Tencent · first-publication year 2026 · inspected 2604.14268v1**  
Primary PDF: [https://arxiv.org/pdf/2604.14268v1](https://arxiv.org/pdf/2604.14268v1)  
Affiliation evidence: Cover explicitly identifies Tencent Hunyuan and its official Tencent-Hunyuan repository.

#### Table 1 — Trajectory configuration and capability inventory

**PDF page 8 · visually inspected.** Crop `[105, 301, 507, 393]` pt; measurement body `[130, 337, 483, 392]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/hunyuanworld2-table-1.json`
- **Structure:** Trajectory types are columns; maximum count and two boolean properties are rows; a Total column applies to the count row.
- **Alignment and precision:** Counts, check marks, crosses, and dashes are centered. Longer trajectory headers are kept horizontal.
- **Emphasis and color:** No cell emphasis or color; the caption begins with a bold subject phrase.
- **Rules and spacing:** Top/header/bottom horizontal rules; a small centered table with generous spacing.
- **Caption and notes:** Caption above explains that maxima depend on detected object segments and that aerial trajectories combine two types.
- **Missing values and statistics:** Crosses and dashes both appear, but their meanings are not fully spelled out in a symbol legend. Uncertainty is not applicable to the configuration matrix.
- **Comparison contract:** The numbers are configured maxima, not measured dataset frequencies or guaranteed numbers of generated trajectories.
- **Measured PDF properties:** main regular text 8.966 pt; leading font entries: NimbusRomNo9L-Regu 8.966 pt, CMSY9 8.966 pt, MSAM10 8.966 pt. Extracted stroke widths: 0.498, 0.797 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Separate counts from boolean capability fields. Explain dynamic constraints on configuration values.
- **Caution:** Define cross versus dash explicitly. Do not present maxima as observed counts.

#### Table 7 — Multi-objective ablation with baseline and selected-row shading

**PDF page 27 · visually inspected.** Crop `[105, 581, 507, 723]` pt; measurement body `[107, 640, 506, 721]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/hunyuanworld2-table-7.json`
- **Structure:** Two configuration columns precede grouped Camera Metrics, Visual Quality, and User Study headers. Five candidate configurations share the same columns.
- **Alignment and precision:** Camera/quality metrics use three decimals, user-study results two-decimal percentages. Direction arrows are attached to every metric header.
- **Emphasis and color:** Baseline cells have opaque pale-red fill and final selected cells opaque pale-blue fill. Numeric bold/underlines are also present, but their ranking meaning is not separately defined in this caption.
- **Rules and spacing:** Short group-header rules and sparse horizontal rules. Color spans complete row cells rather than continuous value-dependent heatmap intensities.
- **Caption and notes:** Caption above explicitly defines the red baseline and blue final setting and says model selection prioritizes user study when automatic metrics disagree.
- **Missing values and statistics:** One user-study row has dashes; no uncertainty or participant counts in the table.
- **Comparison contract:** The selected configuration does not dominate every metric. The table preserves that disagreement instead of making selection look like universal numerical superiority.
- **Measured PDF properties:** main regular text 7.970 pt; leading font entries: NimbusRomNo9L-Regu 7.970 pt, NimbusRomNo9L-Medi 7.970 pt, CMSY8 7.970 pt. Extracted stroke widths: 0.299, 0.359, 0.498, 0.797 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). Non-black fills: #FFE5E5 (alpha 1.0), #E5E5FF (alpha 1.0).
- **Transferable recommendation:** Use role-based shading to distinguish baseline and selected configuration. Keep the selection objective explicit in multi-objective experiments.
- **Caution:** Add textual baseline/selected labels so color is not the only role cue. Do not call the pale fills partially transparent: extracted fill opacity is 1.0.

#### Table 14 — Memory/runtime scaling with hardware count and failure outcomes

**PDF page 37 · visually inspected.** Crop `[105, 69, 508, 196]` pt; measurement body `[109, 120, 504, 196]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/hunyuanworld2-table-14.json`
- **Structure:** View-count groups each contain memory and time columns; configuration and GPU count precede them. Rows enumerate precision and parallelism variants.
- **Alignment and precision:** Memory in GB and wall-clock time in seconds use two decimals. OOM is a literal outcome in both cells for failed configurations.
- **Emphasis and color:** Header labels are bold; no best-cell or best-row emphasis. No shaded rows; thin black filled rectangles are rules, not heatmap backgrounds.
- **Rules and spacing:** Short group rules and outer/header boundaries; many columns create a body below seven points.
- **Caption and notes:** Caption above fixes resolution, GPU model, FP32 baseline meaning, and the definition of sequence parallelism.
- **Missing values and statistics:** OOM is a resource failure, not generic missing data. No timing intervals or repeat counts.
- **Comparison contract:** GPU count varies, so the fastest row is not automatically the most resource-efficient. Precision and parallelism settings must remain attached to results.
- **Measured PDF properties:** main regular text 6.447 pt; leading font entries: NimbusRomNo9L-Regu 6.447 pt, NimbusRomNo9L-Medi 6.447 pt, CMSY10 6.447 pt. Extracted stroke widths: 0.193, 0.516 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Reserve explicit outcome tokens for resource failures. Place GPU count, precision, and problem size alongside timing and memory.
- **Caution:** Do not replace OOM with zero or a generic dash. State whether added optimizations are cumulative or independent, and clarify per-GPU versus total memory.
### HunyuanImage 3.0 Technical Report

**Tencent · first-publication year 2025 · inspected 2509.23951v1**  
Primary PDF: [https://arxiv.org/pdf/2509.23951v1](https://arxiv.org/pdf/2509.23951v1)  
Affiliation evidence: Cover author Tencent Hunyuan Foundation Model Team.

#### Table 1 — Training-stage specification

**PDF page 8 · visually inspected.** Crop `[105, 578, 508, 677]` pt; measurement body `[110, 614, 503, 676]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/hunyuanimage-3-table-1.json`
- **Structure:** One header tier lists stage, VAE resolution anchor, ViT resolution anchor, trained component, and task mix. Four Roman-numbered stages form the rows.
- **Alignment and precision:** All cells are centered; task sets and component names remain textual. Pixel units are attached to resolution values.
- **Emphasis and color:** No bold data, rank, fill, or decorative color. All stages receive equal typographic weight.
- **Rules and spacing:** Three horizontal rules and comfortable spacing; no per-row grid.
- **Caption and notes:** Caption above defines resolution anchor as aspect-ratio-preserving resizing and distinguishes progressive VAE anchors from a fixed ViT anchor.
- **Missing values and statistics:** No missing values; uncertainty is not meaningful for this configuration table.
- **Comparison contract:** Training stages are a schedule, not disjoint datasets. Resolution anchors are not necessarily square image dimensions.
- **Measured PDF properties:** main regular text 8.626 pt; leading font entries: NimbusRomNo9L-Regu 8.626 pt. Extracted stroke widths: 0.431, 0.690 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Use a configuration table rather than a timeline when precise settings matter. Keep data-processing semantics with numeric settings.
- **Caution:** Do not total stage quantities as if they were independent dataset counts. Expand task abbreviations when the table must stand alone.
### HunyuanVideo 1.5 Technical Report

**Tencent · first-publication year 2025 · inspected 2511.18870v1**  
Primary PDF: [https://arxiv.org/pdf/2511.18870v1](https://arxiv.org/pdf/2511.18870v1)  
Affiliation evidence: Cover author Tencent Hunyuan Foundation Model Team.

#### Table 2 — Training curriculum and data-volume schedule

**PDF page 7 · visually inspected.** Crop `[105, 76, 507, 242]` pt; measurement body `[120, 113, 493, 241]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/hunyuanvideo-1.5-table-2.json`
- **Structure:** Eight Roman-numbered stages are grouped into image pretraining, video pretraining, and continual-training blocks. Five columns cover index, phase, resolution/frame-rate/duration, volume, and tasks.
- **Alignment and precision:** Cells are centered. Resolution, fps, and duration share one field; volume mixes billion and M notation.
- **Emphasis and color:** No winner emphasis or fill. A thin vertical separator after the stage index distinguishes identifier from settings.
- **Rules and spacing:** Horizontal rules divide meaningful training blocks; no line between every stage.
- **Caption and notes:** Caption above defines volume notation, including slash-separated video/image amounts, although the inspected data cells do not actually use slashes.
- **Missing values and statistics:** No missing cells or uncertainty. The two first headers both say Stage, making index and phase less explicit than they could be.
- **Comparison contract:** Quantities describe training stages; the table alone does not establish whether volumes are unique data items or training exposures.
- **Measured PDF properties:** main regular text 9.963 pt; leading font entries: NimbusRomNo9L-Regu 9.963 pt, CMSY10 9.963 pt. Extracted stroke widths: 0.398, 0.498, 0.797 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Group rows at actual curriculum transitions. Use explicit Stage ID and Phase labels in a new table.
- **Caution:** Do not copy a legend for notation absent from the displayed table. Define volume units and unique samples versus exposures.

#### Table 7 — Runtime comparison with reported plus/minus variation

**PDF page 11 · visually inspected.** Crop `[105, 76, 507, 201]` pt; measurement body `[125, 103, 489, 200]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/hunyuanvideo-1.5-table-7.json`
- **Structure:** Five columns carry task, exact pixel resolution, total frames, sparse-attention flag, and seconds per diffusion step. Rows pair sparse and dense settings where available.
- **Alignment and precision:** Value and plus/minus term both retain four decimals and share a centered cell. Symbols are actual check/cross glyphs.
- **Emphasis and color:** No winner styling; the table presents timing observations without a selected-row color.
- **Rules and spacing:** Outer/header rules and one resolution-group break; no full grid.
- **Caption and notes:** Caption above states engineering acceleration is absent. Nearby text says measurements average multiple runs and use 8 H800 GPUs with context parallelism.
- **Missing values and statistics:** Plus/minus quantities are present, but neither the caption nor the inspected adjacent methods text identifies SD, SE, CI, or the number of runs. They must remain unclassified.
- **Comparison contract:** Hardware and backend context are stated outside the table. The uncertainty notation is visually precise but semantically incomplete for reproduction.
- **Measured PDF properties:** main regular text 9.963 pt; leading font entries: NimbusRomNo9L-Regu 9.963 pt, CMR10 9.963 pt, CMSY10 9.963 pt. Extracted stroke widths: 0.498, 0.797 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Keep value and uncertainty aligned and give them compatible precision. Require uncertainty type and sample count in a new caption or note.
- **Caution:** Do not invent that the plus/minus term is standard deviation. Do not infer significance from non-overlapping unclassified plus/minus terms.

#### Table 8 — Measured end-to-end inference time with accelerated implementation

**PDF page 11 · visually inspected.** Crop `[105, 212, 507, 338]` pt; measurement body `[111, 239, 502, 337]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/hunyuanvideo-1.5-table-8.json`
- **Structure:** Rows pair resolution, frame count, and sparse-attention switch. Total time and average time per step are separate result columns.
- **Alignment and precision:** Configuration values are centered. Total times have two decimals and per-step means four; check/cross symbols encode sparse attention.
- **Emphasis and color:** No bold winners, color, or shaded rows.
- **Rules and spacing:** One row-group break separates 480p from 720p; outer and header rules suffice for the six-row table.
- **Caption and notes:** Caption above fixes 50 diffusion steps and the accelerated condition. The surrounding section specifies 8 H800 GPUs with context parallelism and identifies the engineering optimizations.
- **Missing values and statistics:** No intervals are shown in this table. The Time headers omit an explicit unit even though the discussion provides timing context.
- **Comparison contract:** This table must stay distinct from the adjacent unaccelerated per-step experiment: kernels, compilation, and caching differ.
- **Measured PDF properties:** main regular text 9.980 pt; leading font entries: NimbusRomNo9L-Regu 9.980 pt, CMSY10 9.980 pt, Dingbats 9.980 pt. Extracted stroke widths: 0.499, 0.798 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Keep end-to-end and per-component measurements separate. Report configuration switches as explicit columns.
- **Caution:** Put seconds in both time headers for an extracted standalone table. Do not compare two timing tables after dropping implementation context.
### Hunyuan3D 2.1: From Images to High-Fidelity 3D Assets with Production-Ready PBR Material

**Tencent · first-publication year 2025 · inspected 2506.15442v1**  
Primary PDF: [https://arxiv.org/pdf/2506.15442v1](https://arxiv.org/pdf/2506.15442v1)  
Affiliation evidence: Cover author Tencent Hunyuan and official Tencent-Hunyuan repository.

#### Table 1 — Compact 3D quality benchmark

**PDF page 7 · visually inspected.** Crop `[105, 67, 507, 190]` pt; measurement body `[156, 68, 454, 157]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/hunyuan3d-2.1-table-1.json`
- **Structure:** Model names precede four metric columns, each with an upward arrow. Seven models form an ungrouped comparison.
- **Alignment and precision:** Model labels are left aligned; scores are centered and consistently use four decimals.
- **Emphasis and color:** The proposed model's four numerical values are bold and are the column maxima. Citation links are cyan-blue; there is no background fill.
- **Rules and spacing:** Uniform thin rules at top, header, and bottom; one vertical rule separates identifiers from scores. No row dividers.
- **Caption and notes:** Caption below gives a short comparison description; metric definitions appear in the surrounding evaluation section.
- **Missing values and statistics:** No missing cells or uncertainty. Small score gaps retain four-digit precision rather than being rounded into artificial ties.
- **Comparison contract:** The metrics measure different learned similarity scores; the table alone does not establish matched compute or training data.
- **Measured PDF properties:** main regular text 8.966 pt; leading font entries: NimbusRomNo9L-Regu 8.966 pt, NimbusRomNo9L-Medi 8.966 pt, CMSY9 8.966 pt. Extracted stroke widths: 0.398 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1), #00AEEF (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Preserve meaningful precision when differences are small. Use arrows to make metric direction explicit.
- **Caution:** Do not round all scores to a universal one-decimal style. Keep metric definitions and experimental eligibility available when reproducing the table.
### WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting

**Tencent · first-publication year 2025 · inspected 2510.10726v1**  
Primary PDF: [https://arxiv.org/pdf/2510.10726v1](https://arxiv.org/pdf/2510.10726v1)  
Affiliation evidence: Affiliation 3 is Tencent Hunyuan; affiliations 1 and 2 are Zhejiang University and Chinese University of Hong Kong.

#### Table 3 — Cross-dataset benchmark with explicit training-overlap exclusion

**PDF page 7 · visually inspected.** Crop `[105, 87, 507, 214]` pt; measurement body `[109, 125, 504, 213]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/worldmirror-table-3.json`
- **Structure:** Three dataset groups each contain mean/median angular error and two threshold-accuracy metrics. Methods occupy a wide stub with inline citations.
- **Alignment and precision:** Results use one decimal. Lower-is-better and higher-is-better arrows are explicit; the dense twelve-result-column layout uses small type.
- **Emphasis and color:** Bold and underlined numeric cells visibly distinguish strong results. The proposed method is not treated as best in every column; reference links are blue.
- **Rules and spacing:** Short rules separate header groups, with an extra rule before the proposed method. No row fill; thin black filled objects are line elements.
- **Caption and notes:** Caption above says a baseline's ScanNet results are omitted because that dataset was used for its training.
- **Missing values and statistics:** Dashes in the excluded dataset block have a known eligibility reason, not merely absent reporting. No uncertainty intervals.
- **Comparison contract:** The omission protects out-of-domain comparison. A table schema must preserve the exclusion reason rather than treating the dash as a poor score.
- **Measured PDF properties:** main regular text 6.360 pt; leading font entries: NimbusRomNo9L-Regu 6.360 pt, NimbusRomNo9L-Medi 6.360 pt, CMR10 6.360 pt. Extracted stroke widths: 0.191, 0.254, 0.318, 0.509 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1), #367DBD (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Attach benchmark eligibility and contamination/exposure notes to omitted values. Retain metric direction independently for each column.
- **Caution:** Do not turn excluded cells into zero. Avoid copying very small dense typography when a split layout would improve reading.

#### Table 5 — Input-conditioned representation ablation with parameter cost

**PDF page 9 · visually inspected.** Crop `[105, 87, 507, 190]` pt; measurement body `[127, 113, 484, 190]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/worldmirror-table-5.json`
- **Structure:** Two row sections distinguish image-plus-pose inputs from image-plus-intrinsics. Each compares a dense representation with a single token; columns include extra parameters and multiple task scores.
- **Alignment and precision:** Extra parameters use two decimals and M units; score fields use two decimals. Labels are left aligned and values centered.
- **Emphasis and color:** Bold is structural in headers and input-section labels; individual score cells are not bolded. No shaded proposed row.
- **Rules and spacing:** Horizontal rules bracket the table and separate the two input conditions. No per-cell grid.
- **Caption and notes:** Caption above states two evaluation datasets and a fixed ten-view input setting.
- **Missing values and statistics:** No missing outcomes or reported uncertainty.
- **Comparison contract:** Input conditions differ between sections and must not be flattened into one ranking pool. Parameter count is a model-cost proxy, not a measured timing result.
- **Measured PDF properties:** main regular text 6.705 pt; leading font entries: NimbusRomNo9L-Regu 6.705 pt, NimbusRomNo9L-Medi 6.705 pt, CMSY10 6.705 pt. Extracted stroke widths: 0.536 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Group ablations by the input or task condition that changes comparability. Show cost and quality without implying a single winner when objectives conflict.
- **Caution:** Define the aggregate Avg. calculation. Do not equate fewer parameters with measured lower latency.
### Hunyuan-A13B Technical Report

**Tencent · first-publication year 2025 · inspected 2609.27284v1**  
Primary PDF: [https://arxiv.org/pdf/2609.27284v1](https://arxiv.org/pdf/2609.27284v1)  
Affiliation evidence: Cover author Tencent Hunyuan Team; official repository also names Tencent Hunyuan.
Date note: report cover and official repository date the release to 2025-06-27; the inspected arXiv v1 was submitted 2026-09-23. The year count uses the earlier report date.

#### Table 3 — Domain-grouped reasoning benchmark

**PDF page 9 · visually inspected.** Crop `[69, 68, 528, 319]` pt; measurement body `[117, 68, 479, 287]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/hunyuan-a13b-table-3.json`
- **Structure:** Four model columns follow category and benchmark stubs. Eight category groups make a long comparison scannable; category labels are bold and sometimes wrap.
- **Alignment and precision:** Labels are left aligned and values centered. Precision is inconsistent within some rows: integers appear beside one-decimal scores.
- **Emphasis and color:** Caption defines bold highest and underlined second. One row displays two identical 44.6 scores but assigns different emphasis, leaving rounded-tie treatment ambiguous.
- **Rules and spacing:** Only horizontal category rules, with no vertical grid. The table is narrower than the text block despite a measured body under seven points.
- **Caption and notes:** Caption below identifies slow-thinking evaluation and the emphasis policy; model versions remain in headers.
- **Missing values and statistics:** No missing outcomes or intervals in the selected table. No explicit tie tolerance.
- **Comparison contract:** Models differ in size and mode implementation. The table is a reported benchmark comparison, not a matched-resource ablation.
- **Measured PDF properties:** main regular text 6.864 pt; leading font entries: URWPalladioL-Roma 6.864 pt, URWPalladioL-Bold 6.864 pt, PazoMath-Italic 6.864 pt. Extracted stroke widths: 0.275, 0.392 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Use category stubs and section rules for long benchmark lists. Require a declared rounding and tie policy before styling winners.
- **Caution:** Do not copy differing ranks for equal displayed values without explaining hidden precision. Do not adopt unnecessary downscaling as a design default.

#### Table 7 — Compact throughput configuration table

**PDF page 11 · visually inspected.** Crop `[157, 487, 434, 575]` pt; measurement body `[157, 487, 434, 553]` pt.  
Evidence crop: （research image omitted; regenerate from the recorded PDF page and crop）  
Object report: `measurements/deepseek-tencent-alibaba/hunyuan-a13b-table-7.json`
- **Structure:** Four rows show batch size, input length, output length, and throughput. Repeated input lengths preserve each row as a self-contained configuration.
- **Alignment and precision:** Batch is left aligned; token lengths and throughput are centered. Throughput uses two decimals and tokens/s in the header.
- **Emphasis and color:** Header labels are bold; data have no rank or color emphasis.
- **Rules and spacing:** Top/header/bottom horizontal rules with generous spacing; no grid or background.
- **Caption and notes:** Caption below names the model. Hardware and inference context live in the surrounding efficiency section rather than the caption.
- **Missing values and statistics:** No missing values, repeat counts, or variability estimates.
- **Comparison contract:** Batch and generated length both vary, so throughput differences should not be attributed to batch alone across all rows.
- **Measured PDF properties:** main regular text 8.966 pt; leading font entries: URWPalladioL-Roma 8.966 pt, URWPalladioL-Bold 8.966 pt. Extracted stroke widths: 0.498, 0.797 pt (including rules/underlines, not a recommendation). Text colors: #000000 (alpha 1). No non-black fill objects in the measured table body.
- **Transferable recommendation:** Keep workload dimensions in the table alongside throughput. Use simple typography for a small configuration matrix.
- **Caution:** Attach hardware, precision, runtime, and timing protocol when extracting for standalone use. Do not compare rows as a one-factor sweep when output length changes.

## Audit and limitations

- Every counted anchor has `inspection_status: pdf_visual_inspected`; 32 crop PNGs were opened, not merely generated.
- Paper counts: DeepSeek 6 / 10 anchors; Alibaba/Qwen 6 / 10 anchors; Tencent 6 / 12 anchors. Total: 18 / 32.
- All inspected sources are pinned v1 PDFs. This preserves comparable evidence with the earlier corpus rather than claiming each source is its latest revision.
- The source table artwork is research-only. The intended skill should build new tables from user data and semantic specifications rather than redistribute these crops as templates.
- This is a purposeful sample of table-rich reports, not a statistical survey of company-wide practice or top-venue acceptance.
- No benchmark values were recalculated, independent experiments reproduced, or performance claims validated. Geometry, typography, table semantics, and declared experimental conditions were the research target.
