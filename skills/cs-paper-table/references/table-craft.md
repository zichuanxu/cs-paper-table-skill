# Table craft: what makes a top-lab table look finished

Read this before styling a table. [design-guide.md](design-guide.md) and the evidence atlas cover the
scientific side (scopes, uncertainty, missingness); this file covers the look, and the renderer's
defaults implement it.

## 1. Study (2026-10)

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

Two further studies (2026-10):

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

## 2. Rules (each implemented by the renderer unless noted)

1. **Restraint first.** Black text, booktabs rules, no vertical lines, no per-row hairlines. Colour,
   tints and underlines are opt-in and each needs a stated meaning. (8/13 papers use no colour.)
2. **Rules scale with the type**: `\heavyrulewidth=.08em`, `\lightrulewidth=.05em`, `\cmidrulewidth=.03em`.
3. **Spanners** get `\cmidrule(lr)` so adjacent groups visibly separate. (Phi-4, K2, DINOv2)
4. **Two-line headers**: bold name, then a smaller muted line for n, unit, shots or direction
   (`Math / n=250`, `Latency / ms ↓`). Direction arrows live in the header, not the caption.
5. **Row groups** are centred italic banners after a `\midrule` (Qwen, DINOv2), with short labels
   ("32k-token budget", not "B. 32k-token ceiling · same checkpoint…"). An empty label gives a rule only,
   e.g. to set a spec block (params, architecture) above the results (DeepSeek, Hunyuan).
6. **Bold = best** within a declared scope; ties all bold. A second level (underline = second best, or
   best open model) only when the notes say so. Never bold specs or parameter counts.
7. **Numbers**: one precision per column (or the source's reported precision for transcriptions),
   true minus, thousands separators for counts (`120,000`), `a·10^n` for FLOPs, centred when widths
   are equal and decimal-aligned otherwise. The decimal point takes the bold/underline of its digits.
8. **Uncertainty is secondary text**: `83.5 ±0.6` or `76.5 (1.3)` with the SD smaller and muted (Llama 3, Harness²).
9. **Deltas** are signed and coloured by improvement *after* the metric's direction
   (green `#408C40` better, red `#8C4040` worse, grey for zero), so a `−2.0` in a "#Steps ↓" column is green.
   The sign keeps the meaning in greyscale. (DINOv2)
10. **"Ours"** is marked by position (last block) and, optionally, a pale tint (`#EEF3FA` row, or a column
    band as in Llama 3). Never saturated; never a tint on every good cell.
11. **Status marks**: ✓ / ✗ (✗ muted) instead of Yes/No; the legend is added automatically.
12. **Missing** values are typed; when only one kind occurs, show "–" and define it once.
13. **Caption**: "**Table N. Title.** one or two sentences" stating the comparison. Definitions, emphasis
    legend and data status go to the notes under the table, in a smaller, dark-grey size. Keep the notes
    to two or three lines; six-line notes read as documentation, not a paper.
14. **Type**: 0.85–0.9 of body (8.5–9 pt for a 10 pt paper), secondary text ≥ 7.2 pt, raised marks
    (², †) ≥ 6 pt; never `\resizebox` below ~0.9×. Recompose instead (split, transpose, shorten headers).
15. **Natural width** by default: columns stay close so groups read as groups; stretch to the full
    width (`style.fill`) only when the table is nearly full width anyway.
16. **Categories as bands** when a table has 3+ row blocks of different kinds (`style.group_style: "band"`):
    the band separates blocks, so no rule is needed. Add hairlines between column groups only when groups
    mix kinds of quantities (`style.group_rules`), never between every column. (PlugMem)
17. **Marks travel with the cell**: `{"value": …, "mark": "*"}` plus a root `marks` map; the legend is added
    to the notes. Use them for "reported by the original authors", subset runs, or anomalies. (PlugMem, Phi-4, Kimi K2)
18. **Coloured status only in matrices** (`status_colors`): green ✓ / red ✗ / amber partial, glyph shape still
    differing so greyscale and colour-blind readers lose nothing; set `status_legend` to the table's words
    ("supported / not supported"). (PlugMem)
19. **Units on values when they are ratios** (`suffix: "×"`): `1.0×`, `3.2×`. Put n in the row label rather
    than in a new column, and define a baseline that changes per row in that row's label. (StudentSim)
20. **Show the margin, not just the winner**: a derived "Δ vs. best baseline" delta row, or a change column
    (`column.delta: "max"`) such as "Δ Overall vs. ①", coloured by improvement. Say in the notes and the
    provenance that it is derived. (ReHarness, PaperBanana redesigns)
21. **Row IDs the text can cite**: circled digits ① … ⑩ in a narrow first column.
22. **Never** rotate column headers, put citations or descriptions in data cells, use link blue for
    emphasis, or mix "46%" with "46.2". (Llama 3, Gemini 1.5, GPT-4)
23. **Shade for the pattern, bold for the winner** (`column.heat`): in a matrix of one kind of quantity
    (models × stages, score dimensions, a confusion matrix) fill each cell from white to one hue over a
    *declared* domain shared by every column of that quantity, so columns compare with each other and not only
    within themselves. A second hue (orange) only for a different kind of quantity. Numbers stay printed in
    black, bold still marks the best, total and marginal rows stay unshaded (`row.heat: false`), and the notes
    name the scale (`heat_meaning`). Not for leaderboards with mixed units or for a single column. (ARE-bench)
24. **Header band with shaded bodies** (`style.header_fill`): a pale tint behind the column names keeps header
    and data apart once the cells carry fills. Leave headers unfilled otherwise. (ARE-bench)
25. **Count / denominator (share)** (`kind: "fraction"`): `65/76 (85.5%)`, the share computed from the counts so
    the two cannot drift apart. A denominator common to a column goes in its header ("Successful, 20/20").
26. **One row order for the whole paper**: sort the models once by the headline metric and keep that order in
    every later table, so a model sits in the same row and departures from the headline ranking show as breaks
    in the shading. A total follows a light rule (`rule_before`); when it is not the column sum, the caption
    says what it counts ("the total counts their union"). (Not enforced by the renderer.)
27. **Text tables**: ragged-right wrapped columns, records separated by space and not by rules, a short ID per
    record (O1 … O20) that the prose and other tables cite ("failing O4"), literal identifiers in monospace. In
    a multi-page taxonomy, merge the parent cells, zebra the leaf rows (`#F7F7F7`) and repeat the header with
    "Continued on next page" (manuscript-native `longtable`, see [latex-recipes.md](latex-recipes.md)).

## 3. Defaults the renderer now uses

| Setting | Value | Why |
|---|---|---|
| Preview font | Times (`newtxtext`, `newtxmath`); `style.font: "lmodern"` available | most CS venues; the fragment inherits the manuscript font |
| Header weight | bold name, muted smaller second line (`style.header_weight`) | DeepSeek, Qwen, Kimi, Phi-4 |
| Rules | booktabs em-based, black | all 13 |
| Row groups | centred italic banner after `\midrule` (`style.group_style: "label"` for left labels) | Qwen, DINOv2 |
| Focus tint | `#EEF3FA` (`style.focus_fill`), row or column (`column.focus`) | Llama 3, Harness² |
| Deltas | `#408C40` / `#8C4040`, direction-aware | DINOv2 |
| Muted text | `#6B7280`; notes `#374151` | secondary information recedes |
| Heat shading | off; white → `#5B8CA5` (blue) or `#CA9657` (orange), linear on the declared domain | ARE-bench; black text keeps > 5:1 on the darkest shade |
| Header band | off; `#F0F4F7` behind the column names (`style.header_fill`) | ARE-bench |
| Width | natural, centred (`style.fill: true` to stretch) | close columns group better |
| PNG preview | 216 dpi, plus 96 dpi and greyscale | review at size and without colour |

## 4. Redesign protocol (beat the original)

1. Transcribe every cell from the PDF text layer and check against the rendered page; keep the source's
   precision (`precision: "reported"`) and record the page in `provenance`.
2. List what the original makes hard: unlabeled groups, missing direction, empty cells, rotated or
   monospace labels, emphasis without a legend, deltas that do not say whether they are good.
3. Rebuild with the renderer; change only presentation. Keep every value, row, column and emphasis meaning
   unless the original's emphasis was inconsistent, in which case state the new rule in the notes.
4. Compare side by side at the same width; the redesign must be easier for the five-second question
   ("which is best, by how much, under what conditions?") and no less faithful.

Worked examples: `assets/specs/redesigns/transformer_t2.json` (Vaswani et al. 2017, Table 2),
`assets/specs/redesigns/harness2_t1.json` (Harness², Table 1, CC BY 4.0) and
`assets/specs/redesigns/arebench_t6.json` (ARE-bench, Table 6: the heat map kept, on a linear shared scale,
with bold best, small SDs and a three-line note in place of a four-line caption).
