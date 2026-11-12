# cs-paper-table

An agent skill for designing, repairing and typesetting tables for computer-science research papers: benchmark and leaderboard tables, ablations, efficiency comparisons, dataset registers and capability matrices. It turns a typed JSON spec into editable LaTeX, a vector PDF, a PNG preview, semantic HTML and CSV, and it is built from a close study of how tables are typeset in leading AI research papers.

![Harness² Table 1, redesigned with this skill](gallery/redesign/harness2_t1.png)

<sub>Harness² Table 1, rebuilt with this skill from the values in the paper. See the [comparison with the original](#redesigning-real-tables).</sub>

## What is inside

| Part | Purpose |
| --- | --- |
| [`SKILL.md`](skills/cs-paper-table/SKILL.md) | The workflow: table contract → structure → design at final size → editable output → verification |
| [`table-craft.md`](skills/cs-paper-table/references/table-craft.md) | How it should look: an 18-paper visual study, 27 rules with LaTeX hints, the renderer's defaults and a redesign protocol |
| [`render_table.py`](skills/cs-paper-table/scripts/render_table.py) | Typed spec → LaTeX / PDF / PNG / HTML / CSV, with scoped bold and underline, decimal alignment, ± or (SD), ✓/✗, direction-aware delta rows, heat-map shading on a declared scale, count/share cells, spanning cells, `a·10ⁿ`, thousands separators and automated export checks |
| [`scientific-contract.md`](skills/cs-paper-table/references/scientific-contract.md), [`spec-schema.md`](skills/cs-paper-table/references/spec-schema.md) | What a table may claim: comparison scopes, uncertainty types, typed missing values, provenance |
| `references/evidence*`, `*.csv` | A 54-paper / 95-table evidence corpus with measured fonts, rules and colours |

## Gallery

### Redesigning real tables

Every value, row and column comes from the paper; only the typesetting changes.

#### The Transformer, Table 2 ([arXiv:1706.03762](https://arxiv.org/abs/1706.03762))

| Original (Vaswani et al., 2017) | Redesigned with this skill |
| --- | --- |
| <img src="gallery/redesign/original/transformer_t2_original.png" width="420"> | <img src="gallery/redesign/transformer_t2.png" width="420"> |

- Rows are grouped and labelled (single models, ensembles, this paper) instead of separated by unlabelled rules.
- Empty cells become "–" with a legend; the metric direction (BLEU ↑, cost ↓) is in the header.
- Bold is the best BLEU and underline the second best in each column, stated in the notes; the original bolded 41.29 and 41.8 in the same column.
- The paper's own models are shaded; the shared cost estimate spans both language pairs.

[PDF](gallery/redesign/transformer_t2.pdf) · [spec](skills/cs-paper-table/assets/specs/redesigns/transformer_t2.json)

#### Harness², Table 1 ([arXiv:2610.14224](https://arxiv.org/abs/2610.14224))

| Original (Harness² paper) | Redesigned with this skill |
| --- | --- |
| <img src="gallery/redesign/original/harness2_t1_original.png" width="420"> | <img src="gallery/redesign/harness2_t1.png" width="420"> |

- The rotated monospace model labels become banner rows naming the model and the initial harness.
- Score ↑ and #Steps ↓ carry their direction, so bold works for both.
- The "+ Recursion" changes are coloured by improvement after each column's direction: a step reduction (−2.0) is green, a step increase (+1.3) red.
- SDs stay as small grey (SD); the caption shrinks to two sentences and the definitions move to the notes.

[PDF](gallery/redesign/harness2_t1.pdf) · [spec](skills/cs-paper-table/assets/specs/redesigns/harness2_t1.json)

#### ReHarness, Table 1 ([arXiv:2610.12668](https://arxiv.org/abs/2610.12668))

| Original (ReHarness paper) | Redesigned with this skill |
| --- | --- |
| <img src="gallery/redesign/original/reharness_t1_original.png" width="420"> | <img src="gallery/redesign/reharness_t1.png" width="420"> |

Underline for second best, the method row shaded and set apart, and a derived "Δ vs. best baseline" row (green ahead, grey tied, red behind) so the margin is read, not computed; the doubled midrule and vertical rules are gone. [PDF](gallery/redesign/reharness_t1.pdf) · [spec](skills/cs-paper-table/assets/specs/redesigns/reharness_t1.json)

#### PaperBanana, Table 2 ([arXiv:2601.23265](https://arxiv.org/abs/2601.23265))

| Original (PaperBanana paper) | Redesigned with this skill |
| --- | --- |
| <img src="gallery/redesign/original/paperbanana_t2_original.png" width="420"> | <img src="gallery/redesign/paperbanana_t2.png" width="420"> |

Coloured ✓/✗ with a legend that defines the random retriever, an "Agents" spanner instead of vertical rules, bold and underline per column with the Aesthetic tie stated, and a "Δ Overall vs. ①" column coloured by improvement. [PDF](gallery/redesign/paperbanana_t2.pdf) · [spec](skills/cs-paper-table/assets/specs/redesigns/paperbanana_t2.json)

#### ARE-bench, Table 6 ([arXiv:2611.14364](https://arxiv.org/abs/2611.14364))

| Original (ARE-bench paper) | Redesigned with this skill |
| --- | --- |
| <img src="gallery/redesign/original/arebench_t6_original.png" width="420"> | <img src="gallery/redesign/arebench_t6.png" width="420"> |

The heat map stays, now linear on a shared 0–100% scale named in the notes (the original is quadratic); bold marks the best mean per column, which the original leaves to the shades; SDs are set small; "ISR (%) ↑" becomes one spanner; the shares are recomputed from the counts; the four-line caption becomes two sentences plus notes. [PDF](gallery/redesign/arebench_t6.pdf) · [spec](skills/cs-paper-table/assets/specs/redesigns/arebench_t6.json)

### Five more examples

Synthetic data; each table is designed from the skill's rules for its own reading task.

**Benchmark.** Two budgets as banner groups, the proposed method shaded and last in each, and under it a "Δ vs. Verifier" row: the margin over the strongest baseline, green for higher success and for lower cost alike. Directions sit in the spanners, n under each suite. [PDF](gallery/after/benchmark.pdf) · [spec](skills/cs-paper-table/assets/specs/benchmark.json)

<img src="gallery/after/benchmark.png" width="640">

**Ablation.** The full system first as the shaded reference, removals ordered by their effect, and a change column beside each metric: the paired success difference with its 95% CI, and the latency difference, both coloured by improvement. The component with no detectable effect on success but 177 ms of latency is visible at once. [PDF](gallery/after/ablation.pdf) · [spec](skills/cs-paper-table/assets/specs/ablation.json)

<img src="gallery/after/ablation.png" width="640">

**Dataset register.** The unit sits right after the counts it qualifies, text is ragged right with no rules between records, and a genuine 0 stays distinct from NA and NR. [PDF](gallery/after/registry.pdf) · [spec](skills/cs-paper-table/assets/specs/registry.json)

<img src="gallery/after/registry.png" width="640">

**Efficiency** and **single-column results**, both at 88 mm. Left: metrics as rows with a unit-and-direction column, grey bands for the three test conditions, bold within the matched 16k columns only, OOM as an outcome. Right: ties share the bold, the external reference sits below its own rule with a † instead of a ranking. [PDF](gallery/after/efficiency.pdf) · [spec](skills/cs-paper-table/assets/specs/efficiency.json) · [PDF](gallery/after/budget_comparison.pdf) · [spec](skills/cs-paper-table/assets/specs/budget_comparison.json)

<img src="gallery/after/efficiency.png" width="315"> <img src="gallery/after/budget_comparison.png" width="315">

### Capability matrix

<img src="gallery/after/capability.png" width="620">

Grey category bands instead of rules, hairlines only between column groups, coloured ✓/✗ with the glyph shape still distinct, `1.0×` relative cost, and `*` / `†` cell marks defined once in the notes, following the PlugMem and StudentSim tables (synthetic data). [PDF](gallery/after/capability.pdf) · [spec](skills/cs-paper-table/assets/specs/capability.json)

## What the study found

The skill's [table-craft.md](skills/cs-paper-table/references/table-craft.md) records the typeset tables of DeepSeek-V3, Qwen2.5, Llama 3, LLaMA, Gemini 1.5, GPT-4, Phi-4, Nemotron-4 340B, DINOv2, Hunyuan-Large, Kimi k1.5/K2 and the Transformer, with fonts, rules and colours measured from the PDFs. The short version:

- **Restraint is the style.** 8 of 13 papers use no colour in result tables; text is black; booktabs rules with no vertical lines.
- **Hierarchy comes from type, not lines**: bold names with a small second line for n, unit or shots; spanners with trimmed `\cmidrule`s; centred banners for row groups.
- **One emphasis, defined**: bold = best within a stated scope, ties all bold; underline only with a legend.
- **Secondary numbers recede**: ± and SDs smaller and muted; deltas small and muted green/red (`#408C40` / `#8C4040`, DINOv2).
- **Short captions**: a bold title and one or two sentences.
- **Notes that earn their place**: each note changes how a cell is read; tools, mark placement, procedure from the methods and disclaimers stay out, and the renderer rejects them.
- **Failures to avoid**: `\resizebox` down to 6.9 pt, rotated headers, link-blue emphasis, per-row hairlines, mixed "46%"/"46.2".

## Installation

```bash
# 1. Skills CLI (Claude Code, Codex and other agents)
npx skills@latest add zichuanxu/cs-paper-table-skill

# 2. Claude Code plugin
claude plugin marketplace add zichuanxu/cs-paper-table-skill
claude plugin install cs-paper-table@cs-paper-table-skill

# 3. Codex plugin
codex plugin marketplace add zichuanxu/cs-paper-table-skill
codex plugin add cs-paper-table@cs-paper-table-skill
```

Or copy `skills/cs-paper-table` into `~/.claude/skills/`. The renderer needs Python ≥ 3.10 with `pymupdf` (and `numpy` for the example builder) and a TeX distribution with `pdflatex`, `newtx`, `booktabs`, `dcolumn`, `pifont` and `xcolor`.

## Usage

Ask your agent in plain language, for example "Make the main results table from results.csv for a two-column paper", "Redesign Table 3 of this paper" or "Turn this ablation into a table with SDs and deltas".

To render the examples yourself:

```bash
cd skills/cs-paper-table/scripts
python render_table.py ../assets/specs/redesigns/harness2_t1.json --out /tmp/h2
python build_examples.py --out /tmp/examples --render
```

Each table comes out as `.tex`, `_body.tex` (drop into your `table` float), `_caption.tex`, PDF, PNG (216 dpi, 96 dpi and greyscale), HTML, CSV, the typed spec, an emphasis audit and automated checks.

## License

[MIT](LICENSE), except the original table crops in `gallery/redesign/original/`: the Transformer table is reproduced under Google's permission to reproduce tables and figures of *Attention Is All You Need* for scholarly works with attribution (Vaswani et al., NeurIPS 2017); the Harness² and PaperBanana tables are © their authors under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); the ReHarness and ARE-bench tables are © their authors, reproduced for commentary and comparison and removed on request. The redesigns are independent demonstrations, not affiliated with those papers' authors.
