# Table craft: principles, rules and defaults

Read this before styling a table. It distills five visual studies (50 papers, about 190 typeset tables; the
per-paper evidence, measurements and counts are in [craft-study.md](craft-study.md)) into eight principles, the
rules that follow from them, and the renderer settings that implement each rule.
[design-guide.md](design-guide.md) and [scientific-contract.md](scientific-contract.md) cover what a table may
claim; this file covers how it should look.

## 1. Eight principles

A rule in section 2 is an application of one of these. When a table is in a situation no rule covers, decide from
the principle.

1. **One table answers one question.** Name the comparison the reader must make, then make it the shortest path
   for the eye: the compared numbers adjacent, down a column, in an order the caption states. A table that
   answers two questions is two tables (quoted results and reproduced results; settings and outcomes).
2. **The reader never computes.** Print what would otherwise be subtracted, divided or looked up: the direction
   of each metric, the unit, n, the reference, and the margin over the strongest baseline or the full model.
3. **Space and alignment before ink.** Position, whitespace and type weight carry the structure. A rule marks a
   boundary that exists in the data (header, group, total); a fill marks one declared role.
4. **Emphasis is a budget.** One mark per meaning and one meaning per mark, stated where the table is. A fill has
   one job per table. When a quarter of the cells are marked, nothing is. This is the most common defect in the
   studies: bold is defined in 1 of 7 ML award papers that use it, and the legend is complete in 2 of 9 vision
   and NLP papers.
5. **Secondary information recedes but stays readable.** Uncertainty, units, n, counts behind a share and
   citations are smaller or muted; never below the size floor.
6. **Comparability is visible.** What may be compared sits in one block under a banner that names the condition
   or the caveat; what may not is separated, marked or moved to another table. Missing, failed and censored
   results are values with a stated meaning.
7. **Design at the final size, in the venue's template.** One table size for the whole paper, fitted by
   recomposing and never by scaling. Every table under 7 pt in the studies was scaled, and those are the least
   readable.
8. **One paper, one system.** The same row order, precision, marks and hue meanings in every table, so a reader
   learns the conventions once.

## 2. Rules

Renderer fields are in `code`; "manuscript" means the rule needs manuscript-native LaTeX
([latex-recipes.md](latex-recipes.md)). Sources in parentheses are in craft-study.md.

### Structure and order

- **Orientation.** Methods on rows when one metric is scanned across many systems; metrics on rows when each has
  its own unit and direction and few systems are compared (then a unit-and-direction column sits beside the
  metric name, or the unit goes in the cell when it differs by row: "9,140 b/s").
- **Settings before outcomes.** Configuration columns first, results after. One hairline may separate what was
  set from what was measured (`style.group_rules`); it is the one vertical rule the award papers agree on
  (6 of 9 ML papers). No other vertical rules, no hairline under every row, no double rules, no full grid.
- **Row order is stated and kept.** Sort once by the headline metric, say so in the caption, and keep that order
  in every later table. Ours is last in its block; in an ablation the full system is first.
- **Row groups** are centred italic banners after a `\midrule` (`style.group_style: "banner"`), or grey bands
  when a table has three or more blocks of different kinds (`"band"`; the band replaces the rule). The banner
  carries what the block shares: the budget ("32k-token budget"), the constant ("baseline uses q = 32, k = 4") or
  the caveat ("Oracle methods: inputs are posed"). An empty label gives a rule only, e.g. under a spec block.
  In a single column, a block label spanning its rows at the left costs no height (manuscript, `\multirow`).
- **Quoted and reproduced numbers.** Mark quoted cells (`mark: "*"`) or give them their own table: one with the
  numbers as published under their own settings, one re-run under a single protocol. (Flexibility Trap)
- **Two-system comparisons** use mirrored blocks: the same sub-columns, in the same order, under each system.
  (Basilisk)
- **Row IDs the text can cite**: ① … ⑩ or (1) … (15) in a narrow first column; records in text tables get
  short IDs (O1 … O20). An index table can feed a pairwise matrix headed by those IDs.
- **Totals** follow a light rule (`rule_before`) and stay unshaded (`row.heat: false`). When a total is not the
  column sum, the caption says what it counts. Two tiers: subtotal lighter than grand total.

### Headers

- **Two lines**: a bold name, then a smaller muted line for n, unit, shots or a plain-word gloss of a coded
  header ("0–20%" / "earliest"). All names share one baseline. Spanners get `\cmidrule(lr)`.
- **Direction is always stated, once.** Arrows in the header when directions are mixed (`Latency` / `ms ↓`); a
  single sentence ("higher is better in every column") when they are uniform. Use arrows for metric direction
  only. No ML award paper in the study used header arrows and only two stated direction at all; six of nine
  vision and NLP papers used arrows.
- **A reference value can live in the spanner** ("Perplexity (full model = 0.361)") instead of costing a row.
- **Never** rotate headers, use icons as the only header, or hyphenate a header to fit ("Porta-bility"):
  shorten it or add a second line.

### Numbers

- **One precision per column**, chosen by the quantity (or the source's own decimals when transcribing,
  `precision: "reported"`). No "97.30%" beside "92.3%", no four decimals by default.
- **Units once**: in the header or spanner, not "%" in every cell. Ratios keep their sign (`suffix: "×"`).
- **Separators and magnitudes**: `120,000` (`thousands`), `a·10^n` for costs spanning orders of magnitude
  (`format: "sci"`). "3K" beside "9,318" or "1046.1K" is wrong; abbreviate K/M only in descriptive tables, at
  fixed significant digits.
- **True minus**, never a hyphen; decimal alignment when widths differ; a bold number is bold including its
  point, comma and sign.
- **Uncertainty is secondary text**: `83.5 ±0.6` or `76.5 (1.3)` with the spread smaller, and "%" not repeated.
- **Count and share together**: `65/76 (85.5%)` (`kind: "fraction"`), the share computed from the counts. For a
  wide table, the share over its raw count in small grey on a second line (manuscript; SSH client signatures).
- **Missing, failed and censored**: typed codes, or "–" when one kind occurs; OOM / TO as outcomes; a bound as a
  value, `> 180` or `< 0.001` (`bound`), with its threshold in the notes. Never blank, never zero, never a
  hyphen with three meanings.

### Emphasis

- **Bold = best within a declared scope**, ties all bold; underline = second best only with a legend
  (`ranking.runner_up`). Bold may instead mark a stated threshold ("beats the oracle"). Never bold specs,
  parameter counts or a whole row because it is ours.
- **When ours wins every cell, bold says nothing.** Show the margin instead (a Δ row), or shade the baseline's
  cells where it loses. (Basilisk)
- **Rank tints** (`ranking.fill`) suit wide vision-style tables where bold is hard to find among a dozen
  columns: one hue in two strengths, darker for best, with bold kept so the mark survives greyscale. Never
  three hues (the second can outshout the first), and not together with a heat scale or a focus tint.
- **Ours** is marked by position and optionally a pale cool tint (`focus`, `#EEF3FA`), or by a bold name under
  its own hairline. Never pink or red (it reads as a warning), never on every row.
- **Marks travel with the cell**: `*`, `†`, `‡` (`mark`), defined once in the notes; use them for quoted values,
  subset runs and exceptions.

### Change and margins

- **Signed and coloured by improvement** after the metric's direction (green `#408C40`, red `#8C4040`, grey for
  zero), so `−2.0` under "#Steps ↓" is green; the sign carries the meaning in greyscale.
- **The margin over the strongest baseline** as a derived "Δ vs. best baseline" row (`row.delta`), or a change
  column beside the metric (`column.delta`). Say in the notes that it is derived.
- **Ablations as deltas**: the full model in absolute values, then each "w/o X" row as signed changes
  (`row.delta`). (D4RT) For a staged pipeline, indent the stages (+SFT → +GRPO) and add a Δ-vs-base column.

### Colour and fills

- **Restraint is the default**: black text, white ground, booktabs rules. 8 of 13 lab reports and 5 of 9 ML
  award papers use no fills in results tables; 10 of 13 systems papers use no bold either.
- **Heat shading** (`column.heat`) only when the table is a matrix of one kind of quantity and the pattern is
  the point: one hue on a declared domain shared by those columns, numbers still printed, the scale named in
  the notes. Never one scale across columns whose directions differ, never a per-column traffic light.
- **Shade the change, print the value** (`heat.reference`): leave the reference block white and tint every
  other cell by how much worse it is than the same row's reference, so the loss is seen and the raw score is
  still read. (Lost in Conversation)
- **Hue has a meaning that holds across the paper**: red for loss, blue for level, orange for a second kind of
  quantity. Saturated fills (`#FF1A24`, `#2DFF42`, pure `#00FF00` marks) never.
- **Status marks**: ✓ / ✗ with the ✗ muted, or ●/◐/○ in security and systems feature matrices
  (`status_style: "circles"`); the legend uses the table's own words. Colour them only in matrices
  (`status_colors`), desaturated, with shapes that still differ. A third state gets its own glyph.
- **Header band** (`style.header_fill`) only when body cells carry fills.

### Caption and notes

- **Caption**: a bold title and one or two sentences that name the comparison; it may end with the finding and
  its number ("18–300× faster"). Median length in the award papers is about 30 words; the 100-word captions are
  the ones that define every column. Position (above or below) and label style come from the template.
- **Notes** under the table hold definitions, the emphasis legend, the heat scale and data status, in two or
  three lines. Each note must change how a cell is read. A legend for a tint is clearest with a swatch of the
  tint on the word it defines (manuscript, `\colorbox`).
- **Citations**: numeric `[23]` after a method name is normal where the venue uses numbered citations;
  author–year citations go to the caption. Never in data cells, never link-blue on every row.

### Size and fit

- **Follow the template first.** acmart and PVLDB set tables at body size (7 of 13 systems award papers do not
  shrink at all); ML, vision and NLP papers use about 0.8–0.9 of body.
- **One size for every table in the paper**, 8–9 pt where the template allows; body and notes ≥ 7.2 pt, raised
  marks ≥ 6 pt. Never `\resizebox`.
- **Column budget**: a single column (about 83–88 mm) holds a label plus six or seven numeric columns at
  7–9 pt; from about ten columns, span both columns.
- **Natural width**: columns stay close so groups read as groups; stretch (`style.fill`) only when the table is
  nearly full width anyway. A table of five or fewer columns can sit beside its paragraph (`wraptable`), and two
  small tables side by side under a full-width one.
- **When it does not fit**: remove repeated words and units, wrap headers into two lines, split by cohort,
  transpose, span both columns, move detail to the appendix. In that order.

### Text tables and matrices

- Ragged-right wrapped columns, records separated by space, a short ID per record, literal identifiers in
  monospace. In a multi-page taxonomy merge the parent cells, tint alternate leaf rows very lightly and repeat
  the header.
- Codebook tables (HCI): bold theme, code, an italic quote with the key phrase underlined, participant ID. A
  demographic hierarchy says when its counts overlap.
- A question as spanner ("Reported?") makes ✓/✗ self-explaining.

### Community conventions

| Community | Convention to follow | Evidence |
|---|---|---|
| ML (NeurIPS, ICML, ICLR) | caption above; booktabs; 0.8–0.9 of body; bold best | 8 of 9 above |
| Vision (CVPR, ICCV) | two-column template; arrows in headers; numeric citations in labels; rank tints accepted | 6 of 9 arrows |
| NLP (ACL, EMNLP) | about 9 pt in a 77 mm column, fitted by tight column padding | median 9.0 pt in 3 papers |
| Systems and security (USENIX, ACM, IEEE) | table at body size; no bold-best habit; ●/○ matrices; lines-of-code tables with a Total; "TO" and "> x" as values; IEEE "TABLE N" above | 10 of 13 no bold |
| Data management (VLDB, SIGMOD) | body size; ordinal scales in words or signs, not traffic lights | — |
| HCI (CHI) | descriptive statistics in tables, tests in prose; if tabulated, stars keyed in the caption, predictors grouped, fit rows after a rule | 0 of 3 CHI best papers tabulate test statistics |

## 3. What the studies warn against

| Defect | Seen in |
|---|---|
| Emphasis with no legend | 6 of 7 ML papers that bold; 6 of 9 vision and NLP papers |
| Type scaled to 7 pt or less | 5 of 9 ML; 5 of 9 vision and NLP; one systems paper at 6.2 pt beside a 10 pt body |
| Metric direction stated nowhere | 7 of 9 ML papers |
| "%" in every cell; a hyphen for a missing value | 4 of 9 ML papers each |
| Numbers ≥ 10,000 without separators | 4 of 13 systems papers |
| Three-hue or traffic-light fills | ChordEdit, RayZer, TRELLIS.2, AnyBlox |
| The own row or column bold wholesale, or tinted pink | Follow My Flow, NDD, Agent Data Protocol |
| Captions of 90–130 words that define each column | Flexibility Trap, RayZer, BrickGPT, HalluCitation, Basilisk |
| Mixed precision in one column | Gated Attention, Follow My Flow, TRELLIS.2 |

## 4. Renderer defaults

| Setting | Value | Why |
|---|---|---|
| Preview font | Times (`newtxtext`, `newtxmath`); `style.font: "lmodern"` available | the fragment inherits the manuscript font |
| Header | bold name, muted smaller second line, names on one baseline (`style.header_weight`) | principle 3 |
| Rules | booktabs em-based `.08em` / `.05em` / `.03em`, black | measured 0.8 / 0.5 / 0.3 pt at 10 pt in the booktabs papers |
| Row groups | centred italic banner after `\midrule` (`group_style`: `banner`, `label`, `band`) | Qwen, DINOv2, PlugMem |
| Bold numbers | `\boldmath`, so the point, comma, minus and unit are bold too | `\mathbf` leaves them regular |
| Focus tint | `#EEF3FA` row or column | cool and pale; never pink |
| Rank tints | off; `#CDE3FF` best, `#EBF3FF` second (`ranking.fill`) | D4RT: one hue, two strengths; the second is our choice, a step darker than its measured `#F3F9FF`, to survive print |
| Deltas | `#408C40` / `#8C4040`, direction-aware | DINOv2 |
| Muted text | `#6B7280`; notes `#374151` | secondary information recedes |
| Heat shading | off; white → `#5B8CA5` (blue), `#CA9657` (orange) or `#E58484` (red, for a loss), linear on the declared domain | ARE-bench, Lost in Conversation; black text keeps > 5:1 |
| Header band | off; `#F0F4F7` (`style.header_fill`) | ARE-bench |
| Width | natural, centred (`style.fill: true` to stretch); notes as wide as the table | close columns group better |
| Sentence spacing | `\frenchspacing` in caption and notes | no double space after "Avg." or "vs." |
| Colours | defined by the fragment with `\providecolor` | a manuscript overrides by defining the same name |
| PNG preview | 216 dpi, plus 96 dpi and greyscale | review at size and without colour |

## 5. Redesign protocol

1. Transcribe every cell from the PDF text layer and check it against the rendered page; keep the source's
   precision (`precision: "reported"`) and record the page in `provenance`.
2. List what the original makes hard, against the eight principles: the question it answers, what the reader
   must compute, unlabelled groups, missing direction, emphasis without a legend, empty cells, scaled type.
3. Rebuild with the renderer; change only presentation. Keep every value, row, column and emphasis meaning
   unless the original's emphasis was inconsistent, in which case state the new rule in the notes.
4. Compare side by side at the same width. The redesign must be easier for the five-second question and no
   less faithful.

Worked examples in `assets/specs/redesigns/`: `transformer_t2.json`, `harness2_t1.json`, `reharness_t1.json`,
`paperbanana_t2.json` and `arebench_t6.json`.

## 6. Five-second review

Look at the rendered table at its final size and answer, without reading the caption twice:

1. Which comparison is this table for, and are those numbers next to each other?
2. Which is best, by how much, and under what condition? Was any of that computed in your head?
3. Is every mark, tint and symbol defined in the caption or notes, and does each mean one thing?
4. Is the direction of every metric stated?
5. Does anything need a magnifier, and is this the same type size as the paper's other tables?
6. In greyscale, does the reading survive?
7. Is there a cell that is blank, a bare hyphen, or a number whose unit you had to guess?

A "no" is fixed by recomposing the table, not by adding a note.
