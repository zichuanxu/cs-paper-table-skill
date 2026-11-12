# Craft study: what the inspected papers do

Evidence behind [table-craft.md](table-craft.md). Read it when a rule needs its source, a measured value, or a
counter-example; the rules themselves are in table-craft.md. Every table here was rendered from the typeset PDF
and looked at (not read from arXiv HTML, which re-renders tables); sizes, rule widths and colours were measured
with PyMuPDF. Award status was taken from venue or institutional announcements and is marked where it rests on a
single source. These are examples of design decisions, not a ranking of papers.

| Study | Papers | Tables | Scope |
|---|---:|---:|---|
| 1. AI-lab reports (2026-10) | 13 | about 39 | DeepSeek, Qwen, Meta, Google, OpenAI, Microsoft, NVIDIA, Tencent, Moonshot |
| 2. Single papers (2026-10 to 2026-11) | 5 | about 30 | PlugMem, StudentSim, PaperBanana, ReHarness, ARE-bench |
| 3. ML award papers (2026-11) | 9 | 39 | NeurIPS 2025, ICLR 2026, ICML 2026 |
| 4. Vision and NLP award papers (2026-11) | 9 | 40 | CVPR 2026, ICCV 2025, ACL 2026, EMNLP 2025 |
| 5. Systems, security, data and HCI award papers (2026-11) | 14 | 45 | OSDI, SOSP, NSDI, USENIX Security, S&P, CCS, VLDB, SIGMOD, PLDI, CHI |

The separate 54-paper / 95-table measurement corpus is described in [evidence-atlas.md](evidence-atlas.md).

## 1. AI-lab reports

Typeset PDF pages of 13 papers were rendered and inspected (not arXiv HTML, which re-renders tables),
about 39 tables in total, with fonts, rule widths and colours measured with PyMuPDF.

| Paper (lab) | What it does well | What to avoid |
|---|---|---|
| Attention Is All You Need (Google), T2–T3 | booktabs hierarchy (0.8 / 0.4 / 0.3 pt); `a·10^n` costs; bold best only | T3: vertical rules, hairlines between groups, many empty cells |
| LLaMA (Meta), T3–T10 | plain header, model **size column** next to the name, family as `\multirow`, captions "**Title.** one sentence" | — |
| Llama 3 (Meta), T2, T17–19 | pale **column band** for the new models (`#C6E7FF`), smaller ± for CIs, best within a size class | rotated model names |
| Phi-4 (Microsoft), T1, T3 | two-line header (bold name / light size), `\cmidrule(lr)` spanners with gaps, airy 1.4× rows | hyphen used as minus in delta table |
| Nemotron-4 340B (NVIDIA), T3–T6 | bold/underline legend stated in caption | T5 shrunk to 6.9 pt with `\resizebox`; hairline under every row |
| GPT-4 report (OpenAI), T1–T2 | small second line for shots/source under the benchmark | vertical rule after labels, centred labels, "85.6" next to "85.5%", 7-line caption |
| DINOv2 (Meta), T1, T4, T8–T10 | centred sub-banners for row groups, ✓/✗, **muted delta colours** `#408C40` / `#8C4040` set small | 14-column table running past the margin |
| DeepSeek-V3, T3–T9 | spec block (architecture, active/total params) above its own rule; group labels; ties bold; "within 0.3 = same level" | vertical rules close to text |
| Qwen2.5, T2–T7 | calm: bold best only, centred italic group rows boxed by rules | cramped group rows; hyphen for missing |
| Hunyuan-Large (Tencent), T3–T4 | minimal, consistent | bold applied to parameter counts |
| Kimi k1.5 / K2 (Moonshot), T2–T4 | spanners "Open source / Proprietary" with gaps; legend in caption; `*` = from report | k1.5 mixes "94" and "94.0" |
| Gemini 1.5 (Google), T1, T11, T18 | metric direction `WER (↓)` in its own column; win-rate summary | best in link blue `#0000FF`, which merges with citations |

Cross-paper facts: table type is 0.82–0.9 of body size; rows are 1.0–1.4× the type size; heavy:light
rule ≈ 1.6:1 (booktabs' em-based defaults); 8 of 13 use no colour at all in result tables; text is
pure black; missing values are "–" or "—", never blank.

## 2. Single papers


- **PlugMem** (arXiv 2603.03296, UIUC / Tsinghua / Microsoft Research). Grey full-width category bands
  (`#EBEBEB`, centred labels "Vanilla baseline / Task-agnostic / Task-specific / Ours") instead of rules;
  a cooler near-white tint for the "ours" row (`#F2F5FA`) with the name in small caps; thin vertical
  hairlines **only between column groups** (meta | results | cost); a feature matrix with coloured ✓/✗
  (teal / red, amber ✗ for partial) that reads like a heat map; `*` = from the original paper and `†` =
  subset evaluation as cell marks defined in the caption; scientific notation for ratios spanning orders of
  magnitude; the full model first in ablations with "No X" rows below. Weak: no deltas or intervals; tables
  shrunk to ~7 pt; `52.6/58.4` pairs with only one half bolded.
- **StudentSim** (arXiv 2609.01591, Microsoft Research / UIUC). Strict booktabs (0.8 / 0.5 / 0.3 pt, no
  fills); n inside the row label ("Chess (30 players)"); a metric-definition column carrying the arrow
  ("top-1 accuracy (↑)"); ours as the last column, the only bold; a small `±0.0003` after bold values;
  a signed "ΔR vs. ρ = 0" column with the default row tagged "(default)"; relative cost as `1.0×`,
  `≈ 2.0×`; ranges in a cell ("59 (21–99)"); "N/A" for structurally impossible cells. Weak: no second-best
  mark, no intervals in main tables, a "naive baseline" that changes meaning per row.
- **PaperBanana** (arXiv 2601.23265). A shaded own-method row with indented "w/ …" sub-rows; a module matrix
  with ✓ / - / ○; circled row IDs (① … ⑥) that the text cites; the default ablation row in bold; iteration
  counts as cell values ("3 iters"). Weak: per-cell shading seams, a broken vertical rule, no deltas.
- **ReHarness** (arXiv 2610.12668). Benchmark × backbone spanners over 10 numeric columns; a doubled midrule;
  "Average / Δ per revision" column pairs with ↑/↓ in the group header; the setting encoded as τ symbols in
  the leading columns. Weak: bold is the only emphasis, the method row looks like a baseline, and the margin
  over the strongest baseline is left to mental subtraction.
- **ARE-bench** (arXiv 2611.14364, Shanghai AI Laboratory / Fudan and others; 18 tables, studied 2026-11). Cell
  shading as a heat map in seven results tables: one blue (white → `#5B8CA5`) on a scale shared by every column
  of the table, so "CSR is high for everyone, ISR is not" reads before any digit; orange kept for a different
  quantity (share of failures, gap between models); the marginal totals of a confusion matrix in neutral grey;
  each such caption ends by naming the scale. A pale header band (`#F0F4F7`) with regular-weight names; the same
  model order (by overall ISR) in every table; `65/76 (85.5%)` cells and "20/20" in a column header; a Total row
  whose caption says it is a union, not a sum; text tables with record IDs (O1 … O20) cited from other tables,
  monospace identifiers, and a six-page taxonomy with merged parent cells and zebra leaf rows. Weak: no best
  mark anywhere, so a column's winner is read off shades; ± SD at full size; a quadratic colour scale that
  flattens the low range; Table 1 at 6.4 pt with red ✓ beside black ✗ and link-blue citations in every row;
  four- to seven-line captions carrying the definitions; `4,096–49152`.

## 3. ML award papers (NeurIPS 2025, ICLR 2026, ICML 2026)

| Paper (venue, award; arXiv) | What it does well | What to avoid |
|---|---|---|
| Gated Attention for LLMs (NeurIPS 2025 best paper; 2505.06708), T1, T4, T5 (T2 measured only) | rows numbered (1)…(15) and cited from the prose; centred group banners that carry the group's constant ("Baseline uses q=32, k=4"); one vertical hairline between configuration and result columns; 7.8 pt on 10 pt | perplexity beside accuracies with no direction; bold never defined; `82.90(-6.0)` with a hyphen and mixed precision; 64–77-word captions |
| LLMs Get Lost in Multi-Turn Conversation (ICLR 2026 outstanding; 2505.06120), T1–T3, T6, T7 | raw scores printed, each cell **shaded by its drop from the unshaded reference block** (white → `#E58484`); the caption carries a swatch of the tint and states the sort order; red kept for degradation, blue for level; an Average row after a hairline; small tables wrapped beside their paragraph | 6.7–7.4 pt; no best mark; icons as column headers; row-normalised shading in T6–T7 that is not declared |
| The Flexibility Trap (ICML 2026 outstanding; 2601.15165), T1, T2, T4–T6 | a table of quoted results (mixed settings) paired with a table reproduced under one protocol (`*` = reproduced); †/‡ caveats as footnotes under the table; ours last after a midrule, bold name; caption titles that state the finding; 9.1 pt on 11 pt | a 121-word caption; 27 of 96 cells "-"; link-blue citations in every label |
| Does RL Really Incentivize Reasoning Capacity… (NeurIPS 2025 runner-up; 2504.13837), T1–T4 | a 2×2 outcome table with ✓/✗ columns; appendix tables that give the numbers behind a named figure | vertical rules between every group; "%" in every cell; zebra on a fully centred setup table |
| Motion Attribution for Video Generation (ICML 2026 honourable mention; 2601.08828), T1, T2, T6 | main table at body size (10.2 pt); ours tinted `#E7F5EE`; "ours w/o X" grouped with ours by space; caption says once "all values in %, higher is better" | ties bolded in one row and not in another; a boxed grid with justified narrow columns |
| MedAgentGym (ICLR 2026 oral; 2506.04405), T1–T4, T9 | subtotal rows tinted lighter than the grand total, both bold; bold scope stated ("best at each scale"); a training ladder by indentation (+SFT → +GRPO) with a Δ-vs-base column | 5.9 pt; saturated ✓ `#009B55` / ✗ `#FF0000`; arrows that are not metric direction; `50768.08`; "3K" beside "9,318" |
| Agent Data Protocol (ICLR 2026 oral; 2510.24702), T1, T3, T4, T6 | matched blocks per benchmark under a grey italic band, a baseline row then ours with the gain inline, `20.2% (+19.8%)`; the caption states which rows are quoted | ours in `#FFD9D9`, which reads as a warning, and on every row of T6; "1046.1K" |
| The Obfuscation Atlas (ICML 2026 honourable mention; 2602.15515), T1, T2, T5, T6, T16, T17 | 9 pt on 10 pt, no fills; `10 (100%)` cells; an N (runs) column where n varies by row; the default row tagged "(default)"; captions end with the finding | `90.0% ± 9.5%` at full size with % twice; the model name repeated on every row |
| Artificial Hivemind (NeurIPS 2025 best paper, datasets and benchmarks; 2510.22954), T2, T12, T19 | the reference value in the spanner ("LM perplexities (full = .361)"); a taxonomy with merged parents and partial rules | a "#" column that holds a percentage; hand hyphenation; 6–7 pt |

Counts (n = 9): direction arrows in headers 0, direction in the caption 2, otherwise unstated; bold meaning stated in
1 of the 7 papers that bold a best value; underline for second best 0; no fills in results tables 5; at least one
vertical rule 7, in 6 of them between setting and result columns; main-results type median 7.8 pt (0.78 of body),
a table at or below 7.0 pt in 5; captions median 29 words (range 8–121), above the table in 8; uncertainty shown 1;
signed deltas 4; small tables wrapped beside text 5; "%" repeated in cells 4; hyphen for missing 4. Sizes of
5.9–7.1 pt are read as `\resizebox` from their non-standard values, not from source.

## 4. Vision and NLP award papers (CVPR 2026, ICCV 2025, ACL 2026, EMNLP 2025)

| Paper (venue, award; arXiv) | What it does well | What to avoid |
|---|---|---|
| D4RT (CVPR 2026 best paper; 2512.08924), T1–T9 | best and second as **one hue in two strengths** (`#CDE3FF`, `#F3F9FF`); ours last under its own hairline with a bold name; the condition (w/ GT intrinsics) as a leading ✗/✓ block label; an ablation with the full model in absolute values and each "w/o X" row as **signed deltas** | the fills are never defined; neighbouring tables scaled to 6.2–8.5 pt with rules thinned to 0.21 pt; hyphen as minus |
| TRELLIS.2 (CVPR 2026 best student paper; 2512.14692), T1–T3, T6, T7 | one fixed 7.0 pt for every table; rules 0.8 / 0.5 / 0.3 pt; two small tables side by side under a full-width one; a small inline secondary quantity, `2.0K (131K)` | per-column red → yellow → green heat on every cell plus bold plus underline, unexplained; `1182.` beside `0.3132`; `503387`; "%" in header and cells |
| SAM 3D (CVPR 2026 honourable mention; 2511.16624), T1–T4 | citations in the caption, cells clean; cumulative "+ stage" rows; †‡§ defined in the caption | four decimals everywhere; one table at 6.2 pt beside one at 10 pt |
| ChordEdit (CVPR 2026 best student paper, honourable mention; 2602.19083), T1–T3 | the only paper to define rank colours, with swatches in the caption; "Naive \| Ours" paired under each metric spanner | three hues (yellow best, orange second, blue third) where the second outshouts the first; red/green marks plus vertical rules at 6.7 pt |
| RayZer (ICCV 2025 honourable mention, single source; 2505.00702), T1, T3, T4, T6, T7 | group banners that carry the comparability caveat ("Oracle methods (assume inputs are posed…)"); ablation rows (0)–(4) cited from the caption; bold = "beats the oracle", stated | 5.2–5.7 pt; five saturated fills, undefined; captions up to 103 words |
| BrickGPT (ICCV 2025 Marr Prize; 2505.05469), T1 | one table at body size and natural width; "N/A" for impossible cells | bold and underline undefined; a 94-word caption |
| LingGym (EMNLP 2025 outstanding; 2511.00343), T1–T4 | 9 pt strict booktabs; family → size two-level header; thousands separators and a Total row | bold per row, unstated; eight pastel bands that repeat the Family column |
| The Imperfective Paradox in LLMs (ACL 2026 best paper, single source; 2601.09373), T1–T4, T7 | a bold block label spanning its rows, the same model order in all four blocks; example tables that italicise the contrastive span | one pink heat on ↑ and ↓ columns alike, no legend; pure `#00FF00` ✓ |
| HalluCitation Matters (ACL 2026 outstanding, single source; 2601.18724), T1, T4–T6 | 9 pt with up to ten numeric columns in a 77 mm column through tight padding; bold and underline mark threshold crossings, both defined | two percentages stacked as 6 pt super- and subscripts; a 127-word caption |

Counts (n = 9): type median 7.0 pt (0.70 of body) in the six vision papers and 9.0 pt (0.82) in the three NLP papers;
a main-text table below 7 pt in 5; fills somewhere in 7, colour fills in results tables in 5; rank fills in 3 (all
vision); emphasis legend fully stated in 2, absent in 6; arrows in headers 6; grey text for non-comparable rows 0;
a dedicated tint for the own method 0; signed deltas 1; ± in results tables 0; vertical rules 4 (all vision);
captions median about 30 words (range 8–127), above the table in 3; a single column carries a label plus at most
6–7 numeric columns at 7–9 pt in all 9.

## 5. Systems, security, data and HCI award papers

| Paper (venue, award) | What it does well | What to avoid |
|---|---|---|
| My ZIP isn't your ZIP (USENIX Security 2025 distinguished), T1–T4 | ●/○ matrix with its legend on a line between caption and table; an index table (# 1–50) that feeds a 50 × 50 pairwise matrix headed by those numbers | a hairline under every row; link-blue names; "-" in three meanings |
| Telegram propaganda (USENIX Security 2025 distinguished), T1, T3, T4 | two emphases with separate, stated meanings (bold = best per row, red = the detector's five worst topics); a worked reading example in the caption; the human baseline as first row | "2.3M" beside "1.25M"; "%" in every cell |
| NDD (NSDI 2025 outstanding), T1–T6, T8 | failed and censored runs as values: "TO" (defined as > 24 h), "> 180" GB; the unit in the spanner | double vertical rules; `1354365`; the own column bold wholesale; pure green/red LoC diffs |
| Basilisk (OSDI 2025 best paper), T1 | mirrored blocks (the same seven sub-columns under each system); a pale `#FFE9E8` fill on the **baseline's** cells where it loses; direction stated once ("a lower number is better for every column") | an eight-line caption defining every column |
| Follow My Flow (IEEE S&P 2025 distinguished), T2–T6 | booktabs 0.8 / 0.5 / 0.3 pt, 8 pt on 10 pt; "[RQ3]" opening each caption; Sub-total and Total rows; exploit strings in monospace | the own row bold wholesale; "97.30%" beside "92.3%"; ± at full size |
| SLAP (IEEE S&P 2025 distinguished), T1, T2 | units in the cells because they differ by row ("9,140 b/s", "11.39 ms"); the chance baseline in the caption | red ✗ on zebra |
| CortenMM (SOSP 2025; award unverified), T1–T5 | ①–⑦ row IDs cited from the prose; a ✓/× matrix in which the own system shows an honest ×; a Spec / Proof / Impl lines-of-code table with a Total | 6.2–6.8 pt on a 10 pt body; `4868` |
| SSH client signatures (CCS 2025 distinguished; arXiv 2509.09331), T1–T5 | a share at 9 pt in black over its raw count at 8 pt in grey `#7F807F`, right-aligned, with a Total row and spanners naming source and date; ●/○ with a third glyph for a third state; colour for the security outcome (red = bad key accepted) with a black control row | icon column heads that need a six-line caption |
| AnyBlox (VLDB 2025 best paper), T1, T2 | an ordinal scale in words-as-signs, "+++ / + / +/− / − / −−−" | saturated traffic-light fills (`#2DFF42`, `#FFD600`, `#FF1A24`); hyphenated heads ("Porta-bility") |
| Creative writers' attitudes (CHI 2025 best paper), T1–T4 | a codebook table: bold theme, code, italic quote with the key phrase underlined, participant ID; demographics as an indented hierarchy | overlapping counts that nothing declares |
| Traversing dual realities (CHI 2025 best paper; arXiv 2504.00371), T1 | descriptive statistics only; tests stay in the prose | no dispersion |
| AWDIT (PLDI 2025 distinguished; arXiv 2504.06975), T1 | a question as spanner ("Reported?") that makes ✓/✗ self-explaining; a qualified cell "✓/✗ (only in RC)" | — |
| LpBound (SIGMOD 2025 best paper; arXiv 2502.05912), T1, T2 | `+` / `*` marks on system names for provenance; a "<0.001" floor | a full grid; no best mark |
| "It's trained by non-disabled people" (CHI 2026 honourable mention; arXiv 2511.08917), T2, T4, T7; statistics tables only | regression estimates with star superscripts keyed in the caption, predictors grouped by rules, fit rows after a rule; `718 (98.5%)` cells | — |

Counts (n = 13 award papers): caption above 9, below 4; no vertical rules 8, a full grid in at least one table 3,
a hairline under every row in at least one table 5; table type median 9 pt and **equal to the body size in 7** (all
five acmart sigconf / PVLDB papers); bold best per row or column 1, the own system bold wholesale 2, no bold in
results 10; status-glyph matrices 8 (✓/✗ 6, ●/○ 2); units in the header 3, in cells 3, in the caption only 2;
uncertainty in any table 2; p-values or test statistics in a table 0; numbers ≥ 10,000 without separators 4;
citations in row labels 4.
