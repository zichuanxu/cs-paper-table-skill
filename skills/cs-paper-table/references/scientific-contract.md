# Scientific contract for table data and emphasis

Apply this contract before formatting numbers or computing bold cells.
The renderer can validate declared fields; it cannot establish that an experiment was controlled, a reported value is correct, or a comparison is fair.
Keep the input schema as the syntax authority; this reference defines the scientific decisions behind that syntax.

## Contents

- [Provenance and quantity definitions](#provenance-and-quantity-definitions)
- [Comparison scope and eligibility](#comparison-scope-and-eligibility)
- [Missing values, failures, and capability states](#missing-values-failures-and-capability-states)
- [Uncertainty is not decoration](#uncertainty-is-not-decoration)
- [Deltas, ratios, and aggregates](#deltas-ratios-and-aggregates)
- [Independent and cumulative ablations](#independent-and-cumulative-ablations)
- [Emphasis contract](#emphasis-contract)
- [Source counterexamples](#source-counterexamples)
- [Scientific acceptance checks](#scientific-acceptance-checks)

## Provenance and quantity definitions

For each input, preserve its origin: measured by the user, reported by a cited source, derived by a stated calculation, or explicitly synthetic/illustrative/schematic.
Never relabel a synthetic demonstration as a measured result, or infer an unreported score from a chart's appearance.
Keep immutable dataset/model versions, source-table anchors, raw files, and calculation code where available.
For an unversioned report URL, record the report date, retrieval date, and file hash if available.
If a source transcription is uncertain, resolve it against the original or mark the uncertainty in provenance; do not silently choose the plausible digit.
Preserve source errors as documented source observations when reproducing a table; resolve or explicitly qualify them before making a new analytical claim.

For each numeric quantity, record:

| Required decision | Examples of an adequate declaration |
|---|---|
| Entity and unit | Per request; per evaluation item; percentage of tasks; seconds; decimal GB |
| Metric definition | Exact-match success; macro F1; edit distance; measured peak allocation |
| Direction | Higher/lower preferred, or no performance preference; do not guess from the name |
| Scale and bounds | Fraction in `[0,1]` versus percentage in `[0,100]`; whether a metric is unbounded |
| Evaluation population | Benchmark version, split, subset, language, task family, evaluation date |
| Estimator/aggregation | Mean across seeds; pooled success rate; median per-run P95; macro task average |
| Precision | Displayed decimals or justified significant figures for this quantity |
| Measurement setup | Model revision, prompting, decoding, context, budget, tool availability; hardware for timing |

Counts of observations remain integers; a mean of counts may legitimately have decimals.
Keep inequality bounds, censoring, and “at least” qualifiers attached to the value.
An exact number and a lower bound must not enter an ordinary numeric ranking as if they were identical evidence.
If the supported schema cannot preserve a bound, use an explicit unranked textual representation or implement and validate an appropriate typed extension.

## Comparison scope and eligibility

Define a comparison key before setting a winner rule.
Include all conditions material to the intended claim, rather than only the visible dataset name.

| Dimension | Keep together or explicitly separate |
|---|---|
| Benchmark | Dataset revision, split, subset, language, task filtering, leakage/exposure status |
| Evaluation | Harness/judge revision, shots, prompt, scoring, stopping rule, tool permissions |
| Compute/budget | Context, output and total-token ceilings, branches, retries, verifier calls, pass@k |
| Model/recipe | Checkpoint, quantization, fine-tuning, adapters, retrieval corpus |
| Serving | Device/count, precision, batch/concurrency, input/output lengths, software/backend, warmup |
| Evidence origin | Rerun under the shared setup versus external reported result, analytical estimate, or proxy |

A display block may contain explanatory references that are ineligible for ranking.
Conversely, two visual blocks may use the same protocol but remain separate for a legitimate scientific question.
Do not equate `display_group` with `comparison_group`.
For metrics on rows, declare the eligible model-column scope separately for each relevant panel.
For methods on rows, declare the comparison group and eligible rows for each ranked metric.
If eligibility differs by individual cell, encode that difference explicitly; do not exclude or include a whole method by convenience.
If the renderer cannot express the required cell-specific policy, split the result into compatible panels or add audited support before computing emphasis.
State why external, human, oracle, fine-tuned, larger-budget, or contaminated references are included and whether they are eligible.
Do not silently let the best of several decoding settings compete against one fixed-setting baseline.

**Observed precedent:** [Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models](https://arxiv.org/pdf/2504.03624v4), v4, Table 5, physical p. 13, explicitly excludes italic external results from its highest-accuracy bolding.
A larger italic value can therefore coexist with a smaller bold value without a rendering mistake.
This is a source-specific eligibility rule, not a general instruction to exclude all external results.

## Missing values, failures, and capability states

Store the reason, not just a dash. A display symbol is only a serialization of that reason.

| State | Bundled display | Meaning and treatment |
|---|---|---|
| `not_reported` | NR | Source does not supply a result; do not impute zero or infer failure |
| `not_applicable` | NA | Quantity has no defined application under the stated setup |
| `not_run` | NT | An otherwise meaningful evaluation was not executed |
| `incomparable` | NC | Excluded from this comparison for a documented reason |
| `oom` | OOM | Observed memory-capacity failure under the specific setup |
| `timeout` | TO | Observed failure to finish within a stated time limit |
| `execution_error` | ERR | Observed execution failure; record the relevant failure class in notes |
| Numeric zero | `0` or declared precision | An actual measured/reported zero, not any of the states above |

Exclude nonnumeric statuses from arithmetic and ordinary score ranking, while retaining them as evidence.
Do not hide OOM by dropping the row: feasibility is often the result that matters.
Do not replace OOM with infinity unless the analysis defines and justifies that transformation separately.
For a timed-out run, retain the limit and any censoring information; “not completed” does not mean the true runtime equals the limit.
Do not use NaN or infinity as an undocumented missing-value code.
When a source uses one dash for several reasons, separate known reasons and preserve “source unspecified” in provenance rather than inventing a cause.

Capability states are a different type: **Yes**, **No**, **Partial**, and **Unknown** describe support, not experimental scores.
Define Partial in terms of modes, languages, inputs, or constraints.
Use No only for a known lack of the stated capability; use Unknown when the evidence is insufficient.
Do not claim that a support checkmark proves quality, speed, coverage balance, or validation on every supported case.

**Observed precedent:** [HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/pdf/2604.14268v1), v1, Table 14, p. 37, reports OOM alongside memory/time under named GPU and precision settings.
[WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting](https://arxiv.org/pdf/2510.10726v1), v1, Table 3, p. 7, omits a baseline's ScanNet results because ScanNet was used in training; that exclusion is not evidence of low performance.

## Uncertainty is not decoration

Require an explicit definition before rendering `±`, brackets, parentheses, or error superscripts.
State the sampling unit, number of independent units, estimator, and uncertainty method.

| Quantity | What it describes | Required annotation |
|---|---|---|
| SD | Dispersion across the stated observations or replicates | Which observations, sample/population convention, and number of units |
| SE | Uncertainty of an estimator due to sampling | Estimator and method; independent or dependence-aware sampling unit |
| Confidence interval | Interval produced by a procedure with a stated confidence level | Level, method, estimand, sampling/resampling unit, and relevant assumptions |
| Quantile, e.g. P95 | A point in the distribution of observed latency or another quantity | Which distribution, workload, time window, and aggregation order |
| Delta | Difference from an identified reference | Reference, sign convention, and absolute versus relative unit |
| Range/min–max | Extent of observed values | Unit of observation and sample coverage; do not call it a CI |

For an ordinary independent sample mean, the familiar SE estimate is `s / sqrt(n)`; dependence, weights, and hierarchical designs require the appropriate estimator.
A confidence interval for a mean is not a dispersion interval for individual observations.
Do not describe a frequentist 95% CI as a 95% probability that this realized interval contains a fixed parameter.
These distinctions follow the [NIST/SEMATECH e-Handbook, “Confidence Limits for the Mean,” §1.3.5.2](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm).

Do not infer SD from a source's bare `±`; retain “source does not define ±” until resolved.
Do not place SE in a field whose type is SD, or label a percentile interval as a standard deviation.
Use a supported uncertainty type, or extend validation and all output serializers together.
Do not manufacture uncertainty from the number of decimals, number of seeds mentioned elsewhere, or a parenthetical delta.
Match the estimate and displayed uncertainty to a sensible common decimal place; preserve unrounded data separately.
For asymmetric intervals, render both endpoints or separate lower/upper deviations; do not force symmetry.
Do not require every valid interval procedure to contain the displayed point estimate; do require ordered endpoints and a correctly stated procedure.

### Paired effects and repeated runs

Preserve matched seed, task, participant, or run IDs when a paired design is claimed.
Calculate each matched difference before estimating the mean effect or resampling pairs.
Do not independently shuffle the two arms and then claim a paired interval.
Record bootstrap replicate count, random seed, percentile/BCa or other interval method, and the resampled unit when a bootstrap is used.
Distinguish uncertainty across training seeds from uncertainty across evaluation tasks or participants.
An interval over eight seed blocks on a fixed test set does not automatically account for resampling that test set.
Report missing pairs and the handling rule; keep sample-size changes visible.
Do not infer statistical significance from bold rank, non-overlap of arbitrary displayed error bars, or a smaller SD.

## Deltas, ratios, and aggregates

Define a signed absolute delta as `new - reference` and attach the reference ID to the calculation.
For percentage-valued rates, this subtraction is in **percentage points (pp)**.
For example, 74% to 77% is `+3 pp`; the relative increase is `100 × (77 - 74) / 74`, about `+4.1%`.
Define the denominator before showing a relative percentage, speedup, cost reduction, or efficiency ratio.
Do not compute a relative change against zero; preserve an explicit undefined/not-applicable state.
For a lower-is-better metric, a negative raw delta is an improvement. Color follows the declared meaning, not the sign alone.
If using an improvement-oriented delta instead, name the transformation explicitly and retain the original quantity.
Recompute deltas and ratios from raw inputs, then round once for display.
Do not subtract rounded table cells and present the result as a more precise derived measurement.

For averages and totals, declare:

- Whether the aggregation is macro, micro, weighted, median, or another stated function.
- The denominator, weights, and rule for missing/unavailable tasks.
- Whether aggregation happens across tasks, seeds, examples, runs, or nested levels, and in what order.
- Whether the aggregate uses the same items and weights for every method.
- Whether a total counts unique entities, manifest memberships, or repeated observations.

Do not average percentages, Elo, error distances, and latency into an unnamed overall score.
Do not sum documents, problems, trajectories, and episodes into an unlabeled dataset size.
Do not call `mean(P95 per run)` the pooled P95; write the actual computation.
Keep analytical FLOPs estimates distinct from measured runtime and keep proxy outcomes distinct from ground-truth quality.
For currency-based efficiency, preserve the price date, pricing scenario, token accounting, and task distribution.

## Independent and cumulative ablations

Declare the intervention structure in the table title or caption, not only in surrounding prose.

| Design | Row interpretation | Valid contrast | Avoid claiming |
|---|---|---|---|
| Independent removal | Each row removes a component from the same full reference | Each intervention versus that shared full reference | That row order is a sequential build-up |
| Independent addition | Each row adds a component to the same base | Each addition versus the same base | That combined effects equal the sum of separate effects |
| Cumulative sequence | Each row starts from the preceding accumulated state | Adjacent changes, conditional on all prior changes | An isolated causal contribution of each component |
| Joint intervention | Multiple components change together | The named joint configuration versus its reference | Separate individual contributions without extra comparisons |
| Factorial study | A specified combination of factors is crossed | The defined main/interaction contrasts | Causal isolation when budget or data changes with the factors |

Keep all other material conditions visible: parameter count, training data, training duration, evaluation budget, model revision, and optimization settings.
If an “ablation” also changes the backbone or compute, state the combined intervention.
A repeated default row is a reference reused for comparison, not a new independent replicate.
Do not pool separate shorter-run experiments because their metric labels happen to match.

**Observed contrast:** [Fara-7B: An Efficient Agentic Model for Computer Use](https://arxiv.org/pdf/2511.19663v1), v1, Table 4, p. 9, explicitly presents a cumulative pipeline sequence.
[Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](https://arxiv.org/pdf/2601.16163v1), v1, Table 4, p. 20, presents two separate interventions whose caption defines what remains trained.
Use these different structures to motivate different row labels, not one generic “w/o” template.

## Emphasis contract

Declare all of these before generating bold, underline, or color:

1. **Purpose:** highest value, lowest value, chosen reference, default configuration, main metric, or another explicit role.
2. **Axis and scope:** across rows within a cohort, across eligible columns within one metric row, or no ranking.
3. **Eligibility:** all included rows/cells and all excluded references, with reasons.
4. **Direction:** maximum/minimum for each ranked quantity; “best” requires a defensible preference.
5. **Tie rule:** raw equality, equality after displayed rounding, or a stated tolerance in metric units.
6. **Meaning:** rank/selection only, or an independently justified statistical annotation.

Mark all ties covered by the declared rule.
For rounded ties, calculate from the same rounding rule used for display; preserve all unrounded inputs.
For raw ties, explain why equal-looking displayed values can have different marks, or show enough precision to make the distinction readable.
For a tolerance rule, state the tolerance and compare each candidate to the extremum; do not create a transitive chain of near-equalities.
Do not interpret a numeric tie as evidence of statistical equivalence.
If every eligible value ties, all share the rank; do not choose a favorite method.
If only one eligible numeric value remains, prefer no competitive claim and explain the reduced evidence.
Keep a selected/default/reference fill independent of numeric winner emphasis.
Do not hard-code underline as runner-up or gray text as weak performance.
Do not call an emphasized maximum “best” when the maximum is deliberately the least safe or highest-error condition.

## Source counterexamples

These are **observed source semantics**, not recommended universal styling rules.

| Source, inspected version, and physical anchor | Consequence for a new table |
|---|---|
| [Reasoning Models Struggle to Control their Chains of Thought](https://arxiv.org/pdf/2603.05706v1), v1, Table 2, p. 29 | Caption bolds the row-wise highest controllability, including a tie, while lower controllability is safer. Emphasis objective and preferred direction are separate. |
| [SAM 3: Segment Anything with Concepts](https://arxiv.org/pdf/2511.16719v1), v1, Table 8, p. 10 | Underline marks main metrics; gray text indicates training conditions. Neither can be decoded as a generic rank. |
| [SAM 3: Segment Anything with Concepts](https://arxiv.org/pdf/2511.16719v1), v1, Table 9, p. 10 | Caption explicitly rules out comparison across its independent ablation panels. |
| [Gemma 3 Technical Report](https://arxiv.org/pdf/2503.19786v1), v1, Table 8, p. 8 | Blue parenthetical quantities are gains, not uncertainty. |
| [Efficient Universal Perception Encoder](https://arxiv.org/pdf/2603.22387v2), v2, Table 1, p. 7 | Parentheses are gaps to domain experts; `no txt`/`no cls` name unsupported outputs. |
| [DeepSeek-OCR 2: Visual Causal Flow](https://arxiv.org/pdf/2601.20552v1), v1, Tables 1 and 4, pp. 9, 11 | Table 1 has an apparent reading-order direction conflict; Table 4 labels rate subtraction with a percent sign. Verify direction and use explicit pp/relative-% semantics in a new design. |
| [Qwen3-ASR Technical Report](https://arxiv.org/pdf/2601.21337v1), v1, Table 2, p. 5 | P95 latency is a workload quantile. Backend, concurrency, and audio duration qualify comparisons. |
| [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/pdf/2605.23904v2), v2, Table 3, p. 8 | Default tint and within-component best-value bolding coexist; repeated defaults are not replicates. |

## Scientific acceptance checks

Verify the declared quantity, unit, direction, scope, eligibility, and provenance against each header and note.
Recalculate derived totals, deltas, and aggregates from the unrounded source data.
Check all ties, excluded references, missing reasons, and observed failures against the emphasis audit.
Confirm that every uncertainty symbol has a named meaning and the correct sampling unit.
Confirm that interval endpoints, signs, percent/pp units, and displayed precision survive every output format.
Check that the ablation caption matches the actual intervention graph and shared reference.
Preserve raw data and a formatting specification alongside the presentation CSV; a flattened display CSV alone loses scientific context.
Do not assert a result is publication-ready while an unresolved direction, provenance, or comparability contradiction remains.
Fix the scientific contract before polishing its visual encoding.
