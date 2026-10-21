# Typed table specification

## Contents

1. Root fields and files
2. Columns, cells and rows
3. Ranking and comparison scopes
4. Style and output behavior
5. Supported boundaries and examples

## 1. Root fields and files

Use UTF-8 JSON. Read the runnable examples in `assets/specs/` and their constructed raw inputs in `assets/data/`. The renderer validates semantic cell types before writing sources. It does not validate the scientific truth of metadata or calculate a metric from a prose description.

| Field | Meaning |
|---|---|
| `id` | Safe output stem: lowercase letter, followed by lowercase letters, digits, `_` or `-` |
| `number` | Optional display table number; default 1 |
| `title`, `caption` | Plain text; the renderer escapes LaTeX and HTML syntax |
| `data_status` | One of `measured`, `reported`, `derived`, `synthetic`, `illustrative`, `schematic` |
| `provenance` | Nonempty object with original source, versions, raw-input locations and calculation details as applicable |
| `columns`, `rows` | Ordered declarations; IDs must be unique within each collection |
| `column_groups` | Optional disjoint, contiguous column ID spans and plain-text labels |
| `row_group_labels` | Optional mapping from display-group IDs to descriptive labels |
| `ranking` | Explicit policy; omit or use `axis: none` for no numerical winner marks |
| `focus_meaning` | Required whenever a row has `focus: true` |
| `notes` | Nonempty list of interpretation notes; preserve source/protocol/uncertainty qualifications |
| `style` | Final width, fonts and spacing; details below |

Use separate fields or a raw-input file for immutable evaluation IDs, experiment IDs, denominators, eligible sets, aggregation weights and environment versions. Arbitrary provenance fields are retained; the renderer cannot prove their completeness.

The generated `_spec.json` preserves full typed inputs; the display `.csv` preserves formatted cell strings and row IDs. **Do not recalculate results from the display CSV**: it has already rounded values and merged uncertainty into strings. Preserve raw inputs alongside both.

## 2. Columns, cells and rows

Every column has `id`, `label` and `kind`. Set `label` to a string or a list of lines. Set `precision` for numeric display (0–8; default 1), optional `direction` to `max` or `min`, and optional `bounds` to a two-element numeric interval. A row's `precision` overrides the column setting when metrics are rows with different units.

| `kind` | Cell payload | Additional requirements |
|---|---|---|
| `text` | Plain string | Set `width_mm`; explicit newlines become wrapped lines |
| `number` | `{"value": 73.25}` | Finite number or decimal string; no boolean, NaN or infinity |
| `mean_sd` | `{"value": 73.25, "sd": 0.43}` | Nonnegative SD; column must have `uncertainty_definition` |
| `interval` | `{"value": -2.31, "low": -3.02, "high": -1.60}` | Ordered endpoints; column must have `uncertainty_definition` |
| `status` | `"yes"`, `"no"`, `"partial"`, `"unknown"` | Printed as ✓ ✗ ◐ ? with an automatic legend (root `status_style: "words"` for words); unknown is not no |

Number formatting options on a column: `thousands: true` (120,000), `format: "sci"` (`3.3·10^18`, mantissa at `precision` decimals), `precision: "reported"` (keep each value's own decimals; give values as strings such as `"23.75"`), `sd_style: "paren"` (`76.5 (1.3)` with a small muted SD instead of `±`), `focus: true` (pale column band; needs `focus_meaning`). Text columns accept `align: "l" | "c" | "r"`.

A number cell may span later columns: `{"value": "3.3e18", "span": 2}` followed by `{"spanned": true}` in each covered column (one value shared by two settings).

Use `signed: true` on a numeric column for explicit positive signs. Values are rounded with decimal ROUND_HALF_UP at the last display step; negative zero becomes zero. Calculations and ranking policies should be chosen upstream with knowledge of the data. This renderer's decimal tie convention may differ from a source's scientific or binary rounding convention; record any intentional difference.

`mean_sd` means SD only. Never put SE, a CI radius, a quantile or an unexplained `±` value into `sd`. Use an `interval` for defined interval endpoints. Its `uncertainty_definition` must explain the estimand, interval level, method, repetition count and sampling unit. A CI need not contain the point estimate, so the validator checks endpoint order without imposing that restriction. `bounds` constrains the central value, not endpoints of an unbounded statistical approximation.

Any cell can instead contain exactly one typed special state:

| Payload | Printed marker | Interpretation |
|---|---|---|
| `{"missing": "not_reported"}` | NR | Source did not supply the value |
| `{"missing": "not_applicable"}` | NA | Metric or cell does not apply |
| `{"missing": "not_run"}` | NT | Experiment was not executed |
| `{"missing": "incomparable"}` | NC | No valid comparison under this protocol |
| `{"failure": "oom"}` | OOM | Out-of-memory outcome |
| `{"failure": "timeout"}` | TO | Timeout outcome |
| `{"failure": "execution_error"}` | ERR | Execution failure |

Keep the original marker's meaning in notes when normalizing it. Unsupported modality, censored rank outside top-k, intentionally excluded contaminated benchmark, and permission-blocked evaluation can require **new domain-specific states**; do not silently map all of these to NA. Extend the schema and its legend or produce manuscript-native LaTeX for such cases. Failure is a measured or constructed outcome with its own status, not a successful run with a score of zero.

Each row has a unique `id` and a `cells` object whose keys exactly match the column IDs. Additional controls:

- `display_group`: select a visually labeled block. Keep each block contiguous.
- `comparison_group`: required on every row for column ranking, even excluded context rows. It is a scientific comparison key, not inferred from visual proximity.
- `rank: false`: exclude an entire row from ranking. For row-oriented ranking, it disables ranking for that metric row.
- `direction`: required per ranked row in row-oriented mode.
- `focus: true`: apply the pale role fill; requires root `focus_meaning`.
- `space_before: true`: insert additional vertical space at a real semantic boundary.
- `precision`: override display precision for the whole row, useful for mixed metric units.
- `tie_tolerance`: optional row-specific tolerance for row-oriented ranking.
- `delta: true`: a change row (e.g. "+ Recursion"). Numeric cells hold only `{"value": …}`, print signed, are coloured green/red by improvement after the column's direction (grey for zero), and are never ranked.
- `rule_before: true`: a light full-width rule before the row inside a group.

Root `missing_style: "dash"` prints typed missing values as "–" with one legend entry; it is refused when more than one missing kind occurs. An empty `row_group_labels` entry draws the group rule without a label (e.g. a spec block above the results).

## 3. Ranking and comparison scopes

Use **no ranking** for descriptive tables or where the comparison conditions are unresolved:

```json
{"ranking": {"axis": "none"}}
```

For models in rows and metrics in columns, provide a `direction` only for columns that should be ranked. Every row must name its `comparison_group`:

```json
{
  "ranking": {
    "axis": "column",
    "tie_policy": "rounded",
    "meaning": "Bold marks the best displayed value within each budget block; display ties are all marked. Rank is not significance."
  }
}
```

For metrics in rows and configurations in columns, provide explicit disjoint scopes of eligible column IDs; declare a metric direction for each ranked row:

```json
{
  "ranking": {
    "axis": "row",
    "scopes": [["dense16k", "sparse16k", "hybrid16k"]],
    "tie_policy": "rounded",
    "meaning": "Bold marks the best 16k value according to each row's direction. The extra-context column is excluded."
  }
}
```

Supported ties:

- `rounded`: compare values at their declared display precision. All identical displayed optima are bold. Use consistent precision within a comparison scope.
- `raw`: rank unrounded values. Explain why identical displayed numbers can have different emphasis, or add justified precision so the distinction is intelligible.
- `tolerance`: mark values within the stated nonnegative absolute `tie_tolerance` of the optimum. Units are the metric's own units. Supply a global tolerance or column/row override. Do not call a numerical tolerance statistical equivalence.

The renderer skips missing and failed cells. It does **not** automatically exclude externally reported results, alternate harnesses, larger models, changed budgets or unsupported configurations; encode eligibility in groups, row exclusions or scopes. A scope containing one eligible cell can still be marked; assess whether that would misleadingly suggest a meaningful competitive win.

No statistical significance is inferred. `"runner_up": "underline"` underlines the second-best value in each scope; because papers use underlining for several incompatible purposes, the ranking `meaning` must say what the underline means (the validator checks that it mentions it). Cell-specific eligibility and overlapping comparison scopes need custom code or separate panels. Inspect `_emphasis.json`: it records the scope, direction, eligible count, tie policy, best value and marked coordinates.

## 4. Style and output behavior

Recommended starting settings for the included full-width specimens:

```json
{
  "style": {
    "width_mm": 180,
    "body_pt": 8.5,
    "note_pt": 7.6,
    "caption_pt": 9.0,
    "tabcolsep_pt": 5.0,
    "arraystretch": 1.18
  }
}
```

Visual options (defaults follow [table-craft.md](table-craft.md)): `font` (`"times"` | `"lmodern"`), `header_weight` (`"bold"` | `"regular"`), `group_style` (`"banner"` centred italic | `"label"` left italic), `fill` (stretch to the full width; default natural width, centred), `focus_fill` (hex, default `EEF3FA`), `tint_delta_rows` (default false).

These are original design defaults, not measured company mandates. Width is constrained to 65–250 mm; select the real manuscript's width. Set `leading_pt` if needed; default is 1.25 times body size. Body and note size must be at least 7.2 TeX pt. TeX pt and PDF points differ slightly (72.27 versus 72 per inch), so automated PDF checking includes a small conversion allowance.

The renderer uses black rules, muted text `#6B7280`, note text `#374151`, focus fill `#EEF3FA` and delta colours `#408C40` / `#8C4040`; all are defined in the standalone preamble and must be supplied when integrating a body fragment. Rule widths are booktabs' em-based `.08em / .05em / .03em`, so they scale with the type. The body fragment sets these inside a group. To change colors or line conventions, edit those source definitions deliberately and repeat review.

Numeric columns use `dcolumn` math-mode decimal alignment. The renderer reserves a spare fractional slot as **spacing**, not as invented extra precision, to accommodate bold digits. Compound estimates are centered as intact expressions; they are not a full multi-part uncertainty alignment engine. For more elaborate alignment, use `siunitx` or explicit estimate/uncertainty subcolumns and verify the installed package version.

The renderer measures the natural table width, refuses an oversized table, and centres it at natural width (or expands cell padding with `style.fill`). It does not apply geometric scaling. Long unbroken text, overly wide group headers, or an excessive number of columns can still require deliberate recomposition. Use `--source-only` only to export uncompiled editable material, not to bypass a failed production gate. Source-only output refuses a directory containing that table's earlier compiled files, before changing sources; choose a fresh directory so stale PDFs cannot be mistaken for the new input. Provenance lists only files emitted by the current mode.

Outputs include full LaTeX, body/caption fragments, vector PDF, 216 dpi PNG, 96 dpi review PNG, grayscale PNG, semantic HTML, display CSV, typed spec, emphasis audit, automated PDF checks and provenance hashes. The standard PDF is not claimed to be tagged or PDF/UA compliant.

## 5. Supported boundaries and examples

| Spec | What it demonstrates | Raw input |
|---|---|---|
| `benchmark.json` | Multilevel headers; two budget scopes; macro from unrounded rates; cost/quality directions | Constructed successes and task denominators |
| `ablation.json` | Component matrix; sample SD; paired seed bootstrap; independent versus joint removals | Eight synthetic seed blocks and paired differences |
| `efficiency.json` | Metric rows; mixed directions and precision; excluded context column; OOM | Constructed point estimates and failure states |
| `registry.json` | Wrapped prose; aligned counts; units; genuine zero versus NA/NR; no invalid grand total | Synthetic split manifest |

All four are original synthetic examples, not numerical reproductions of a source paper. Rebuild with `scripts/build_examples.py --out /absolute/workdir/examples --render`; preserve `specs/` and `data/` together. The builder uses NumPy's seeded generator for the paired bootstrap and saves full seed-level values, making the uncertainty calculation inspectable.

Use manuscript-native production for: Chinese or other unsupported Unicode in the `pdflatex` preview, longtable across pages, arbitrary nested headers, condition-specific ranking within individual cells, more sophisticated status ontologies, rotated stubs, formal significance tests, or custom caption packages. Carry forward the same scientific and visual review rules.
