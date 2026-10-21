#!/usr/bin/env python3
"""Build four reproducible, explicitly synthetic table specimens and raw inputs.

Every numeric result is constructed for demonstration, not a reported result
about a named real model. Requires numpy only for the paired bootstrap example.
Use --render to compile each spec through render_table.py.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import subprocess
import sys
import numpy as np
from table_core import write_json


def val(x):
    return {"value": float(x) if isinstance(x, np.floating) else x}


def base(stem, title, caption, number):
    return {"id": stem, "number": number, "title": title, "caption": caption,
            "data_status": "synthetic", "provenance": {"origin": "Original constructed demonstration data; no real system results", "generator": "scripts/build_examples.py"},
            "style": {"width_mm": 180, "body_pt": 8.5, "note_pt": 7.6, "caption_pt": 9.0, "tabcolsep_pt": 5.0, "arraystretch": 1.18},
            "columns": [], "rows": [], "notes": [], "ranking": {"axis": "none"}}


def benchmark():
    spec = base("benchmark", "Quality and cost under matched inference budgets",
                "Success rate on four task suites and inference cost, compared within each token budget.", 1)
    tasks = [("math", "Math", 250), ("code", "Code", 200), ("docs", "Docs", 150), ("tools", "Tools", 100)]
    spec["columns"] = [{"id": "method", "label": "Method", "kind": "text", "width_mm": 30}]
    for key, label, size in tasks:
        spec["columns"].append({"id": key, "label": [label, "n=" + str(size)], "kind": "number", "precision": 1, "direction": "max", "bounds": [0, 100]})
    spec["columns"] += [{"id": "macro", "label": ["Avg.", "macro"], "kind": "number", "precision": 1, "direction": "max", "bounds": [0, 100]},
                        {"id": "tokens", "label": ["Tokens", "mean ↓"], "kind": "number", "precision": 0, "direction": "min", "thousands": True},
                        {"id": "latency", "label": ["Latency", "ms ↓"], "kind": "number", "precision": 0, "direction": "min", "thousands": True}]
    spec["column_groups"] = [{"label": "Task success (%) ↑", "columns": [t[0] for t in tasks] + ["macro"]},
                             {"label": "Inference cost", "columns": ["tokens", "latency"]}]
    records = [
        ("16k", "Direct", [164, 123, 110, 54], 4800, 410.3),
        ("16k", "Chain of thought", [180, 136, 116, 61], 6200, 520.8),
        ("16k", "Search", [197, 148, 123, 65], 10150, 811.2),
        ("16k", "Verifier", [195, 151, 125, 64], 11280, 952.6),
        ("16k", "Adaptive routing", [201, 155, 128, 69], 9800, 754.4),
        ("32k", "Chain of thought", [184, 141, 121, 64], 9700, 742.5),
        ("32k", "Search", [207, 155, 131, 71], 17200, 1236.4),
        ("32k", "Verifier", [208, 158, 133, 72], 18400, 1402.7),
        ("32k", "Adaptive routing", [212, 163, 135, 76], 15100, 1128.3)]
    raw = []
    for i, (budget, label, counts, tokens, latency) in enumerate(records):
        scores = [100*c/t[2] for c, t in zip(counts, tasks)]
        cells = {"method": label, **{t[0]: val(s) for t, s in zip(tasks, scores)}, "macro": val(sum(scores)/4), "tokens": val(tokens), "latency": val(latency)}
        spec["rows"].append({"id": "r" + str(i), "display_group": budget, "comparison_group": budget, "focus": label == "Adaptive routing", "cells": cells})
        raw.append({"budget": budget, "method": label, "successes": dict(zip([t[0] for t in tasks], counts)), "denominators": dict((t[0], t[2]) for t in tasks), "mean_tokens": tokens, "latency_ms": latency})
    spec["row_group_labels"] = {"16k": "16k-token budget", "32k": "32k-token budget"}
    spec["ranking"] = {"axis": "column", "tie_policy": "rounded", "runner_up": "underline", "meaning": "Bold: best and underline: second best within each budget (ties at the shown precision share the mark; not a significance test)."}
    spec["focus_meaning"] = "Shaded: the proposed method."
    spec["notes"] = ["Rate = successes / n; Avg. = unweighted mean of the four unrounded rates. Budgets cap all branches and verification calls."]
    return spec, raw


def ablation():
    spec = base("ablation", "Controlled ablations with paired uncertainty",
                "Removing components from the full system; each row is paired with the full system on the same eight seeds.", 2)
    spec["style"].update({"body_pt": 8.3, "tabcolsep_pt": 2.3})
    spec["columns"] = [{"id": "method", "label": "Configuration", "kind": "text", "width_mm": 34}]
    spec["columns"] += [{"id": x, "label": label, "kind": "status"} for x, label in [("retrieve", "Retrieve"), ("verify", "Verify"), ("route", "Route"), ("cache", "Cache")]]
    spec["columns"] += [{"id": "score", "label": ["Success (%)", "mean ± SD"], "kind": "mean_sd", "precision": 1, "uncertainty_definition": "Sample standard deviation across 8 independent synthetic training-seed blocks; ddof=1, not a confidence interval", "bounds": [0, 100]},
                        {"id": "delta", "label": ["Δ vs. full (pp)", "[95% CI]"], "kind": "interval", "precision": 1, "signed": True, "uncertainty_definition": "Paired seed bootstrap of the mean difference from full; 20,000 resamples, 8 paired seed blocks, percentile 2.5/97.5, generator seed 120"},
                        {"id": "latency", "label": ["Latency", "ms"], "kind": "number", "precision": 0}]
    spec["column_groups"] = [{"label": "Components", "columns": ["retrieve", "verify", "route", "cache"]}, {"label": "Paired evaluation", "columns": ["score", "delta"]}]
    ref = np.array([82.6, 83.8, 83.0, 84.2, 84.5, 83.3, 83.6, 83.0])
    conditions = [
        ("full", "Full system", [1,1,1,1], np.zeros(8), 512, "single"),
        ("no_retrieve", "Remove retrieval", [0,1,1,1], np.array([-7.9,-8.4,-8.1,-8.9,-7.7,-8.4,-8.6,-8.2]), 418, "single"),
        ("no_verify", "Remove verifier", [1,0,1,1], np.array([-4.4,-4.9,-4.5,-4.7,-5.2,-4.8,-4.4,-4.7]), 435, "single"),
        ("no_route", "Remove routing", [1,1,0,1], np.array([-3.0,-3.4,-2.8,-3.5,-3.1,-2.7,-3.4,-3.0]), 566, "single"),
        ("no_cache", "Remove cache", [1,1,1,0], np.array([.1,-.2,.2,.1,-.1,.2,-.1,.0]), 689, "single"),
        ("no_rv", "Remove retrieval + verifier", [0,0,1,1], np.array([-11.6,-12.3,-12.0,-12.7,-11.9,-12.2,-12.5,-12.1]), 341, "joint"),
        ("no_rc", "Remove routing + cache", [1,1,0,0], np.array([-3.1,-3.5,-2.9,-3.4,-3.2,-2.8,-3.5,-3.0]), 748, "joint")]
    rng = np.random.default_rng(120)
    index = rng.integers(0, len(ref), size=(20000, len(ref)))
    raw = {"seed_ids": list(range(8)), "bootstrap_seed": 120, "bootstrap_replicates": 20000, "rows": []}
    for key, label, flags, delta, latency, group in conditions:
        scores = ref + delta
        low, high = np.quantile(delta[index].mean(axis=1), [.025, .975])
        cells = {"method": label, **dict(zip(["retrieve","verify","route","cache"],["yes" if f else "no" for f in flags])),
                 "score": {"value": float(scores.mean()), "sd": float(scores.std(ddof=1))},
                 "delta": {"missing": "not_applicable"} if key == "full" else {"value": float(delta.mean()), "low": float(low), "high": float(high)}, "latency": val(latency)}
        spec["rows"].append({"id": key, "display_group": group, "focus": key == "full", "cells": cells})
        raw["rows"].append({"id": key, "seed_success_percent": scores.tolist(), "paired_delta_pp": delta.tolist(), "illustrative_latency_ms": latency})
    spec["row_group_labels"] = {"single": "Remove one component", "joint": "Remove two components"}
    spec["focus_meaning"] = "Shaded: the reference for Δ."
    spec["notes"] = ["SD over 8 seeds; CI is a paired percentile bootstrap over seeds (20,000 resamples), so it excludes item-sampling uncertainty. pp = percentage points. Joint removals do not isolate single-component effects."]
    return spec, raw


def efficiency():
    spec = base("efficiency", "Quality, serving cost and capacity constraints",
                "Quality and serving cost of three attention variants at 16k context; the 32k column is for reference and is not ranked.", 3)
    spec["columns"] = [{"id": "metric", "label": "Metric", "kind": "text", "width_mm": 50}]
    spec["columns"] += [{"id": x, "label": label, "kind": "number", "precision": 1} for x, label in [("dense", ["Dense", "16k"]), ("sparse", ["Sparse", "16k"]), ("hybrid", ["Hybrid", "16k"]), ("extended", ["Hybrid", "32k"])]]
    spec["column_groups"] = [{"label": "Matched 16k context", "columns": ["dense", "sparse", "hybrid"]}, {"label": "Reference", "columns": ["extended"]}]
    entries = [
        ("accuracy", "Task success (%) ↑", "max", [74.2,74.3,76.6,78.0], "quality", 1),
        ("calibration", "Calibration error (pp) ↓", "min", [4.8,4.2,3.5,3.2], "quality", 1),
        ("latency", "P95 request latency (ms) ↓", "min", [184.2,157.9,149.8,230.3], "serve", 1),
        ("throughput", "Throughput (requests/s) ↑", "max", [30.4,34.7,36.2,23.5], "serve", 1),
        ("memory", "Peak device memory (GB) ↓", "min", [36.4,30.1,28.5,44.8], "serve", 1),
        ("energy", "Energy per request (J) ↓", "min", [9.8,8.2,7.6,12.4], "serve", 1),
        ("stress_latency", "P95 request latency (ms) ↓", "min", [None,392,351,None], "stress", 0),
        ("stress_throughput", "Throughput (requests/s) ↑", "max", [None,61.3,66.9,None], "stress", 1)]
    raw = []
    for key, label, direction, values, group, digits in entries:
        spec["rows"].append({"id": key, "display_group": group, "direction": direction, "precision": digits,
                             "cells": {"metric": label, **{c["id"]: {"failure": "oom"} if v is None else val(v) for c, v in zip(spec["columns"][1:], values)}}})
        raw.append({"metric": key, "values": values, "direction": direction, "block": group})
    spec["row_group_labels"] = {"quality": "Quality (1,000 requests)", "serve": "Serving (batch 4)", "stress": "Capacity stress (batch 32)"}
    spec["ranking"] = {"axis": "row", "scopes": [["dense", "sparse", "hybrid"]], "tie_policy": "rounded", "meaning": "Bold: best 16k value in each row, following its arrow."}
    spec["notes"] = ["One 80 GB GPU, BF16 weights, 256 output tokens per request. P95 is a within-run latency quantile, not an interval."]
    return spec, raw


def registry():
    spec = base("registry", "Dataset and evaluation split register",
                "Collections and split sizes. Counts are in each collection's own unit, so no total is given.", 4)
    spec["style"].update({"body_pt": 8.4, "arraystretch": 1.22})
    spec["columns"] = [{"id": "collection", "label": "Collection", "kind": "text", "width_mm": 28},
                        {"id": "unit", "label": "Unit", "kind": "text", "width_mm": 17},
                        {"id": "train", "label": "Train", "kind": "number", "precision": 0, "thousands": True},
                        {"id": "dev", "label": "Dev", "kind": "number", "precision": 0, "thousands": True},
                        {"id": "test", "label": "Test", "kind": "number", "precision": 0, "thousands": True},
                        {"id": "coverage", "label": "Coverage", "kind": "text", "width_mm": 22},
                        {"id": "separation", "label": "Separation rule", "kind": "text", "width_mm": 39}]
    spec["column_groups"] = [{"label": "Split size", "columns": ["train", "dev", "test"]}]
    entries = [
        ("proofs", "Mathematical proofs", "problem", 120000,2000,3000, "English", "Hold out entire problem families", "training"),
        ("patches", "Repository patches", "task", 8200,600,900, "Python / C++", "Disjoint repositories; freeze revision", "training"),
        ("tools", "Tool trajectories", "trajectory", 45000,1500,2500, "6 languages", "Hold out goal templates and tool schemas", "training"),
        ("docs", "Long-document QA", "question", 18000,800,1200, "2 domains", "Split by source document before sampling", "training"),
        ("manuals", "Technical manuals", "document", 125000,0,5000, "12 domains", "Zero dev entries are intentional", "training"),
        ("holdout", "Sealed code tasks", "problem", {"missing":"not_applicable"},{"missing":"not_reported"},750, "Python", "Evaluation only; dev count unspecified", "evaluation"),
        ("actions", "Interactive tasks", "episode", {"missing":"not_applicable"},100,400, "Browser / CLI", "Freeze environment and initial state", "evaluation")]
    raw = []
    for key, label, unit, train, dev, test, coverage, separation, group in entries:
        cells = {"collection": label, "unit": unit, "train": val(train) if not isinstance(train, dict) else train, "dev": val(dev) if not isinstance(dev, dict) else dev, "test": val(test) if not isinstance(test, dict) else test, "coverage": coverage, "separation": separation}
        spec["rows"].append({"id": key, "display_group": group, "cells": cells})
        raw.append({"id": key, **cells})
    spec["row_group_labels"] = {"training": "Training and held-out", "evaluation": "Evaluation only"}
    spec["notes"] = ["Counts are manifest entries. 0 is an intentionally empty split, distinct from NA and NR."]
    return spec, raw


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", required=True, type=Path)
    p.add_argument("--render", action="store_true")
    args = p.parse_args()
    out = args.out.expanduser().resolve()
    root = Path(__file__).resolve().parents[1]
    if out == root or root in out.parents:
        p.error("Write examples outside the installed skill")
    (out / "specs").mkdir(parents=True, exist_ok=True)
    (out / "data").mkdir(exist_ok=True)
    for build in [benchmark, ablation, efficiency, registry]:
        spec, raw = build()
        spec["provenance"]["raw_data"] = "../data/" + spec["id"] + "_raw.json"
        spec_path = out / "specs" / (spec["id"] + ".json")
        write_json(spec_path, spec)
        write_json(out / "data" / (spec["id"] + "_raw.json"), {"data_status": "synthetic", "data": raw})
        if args.render:
            subprocess.run([sys.executable, str(root / "scripts/render_table.py"), str(spec_path), "--out", str(out / spec["id"])], check=True)
    print(json.dumps({"output": str(out), "examples": 4, "data_status": "synthetic"}))


if __name__ == "__main__":
    main()
