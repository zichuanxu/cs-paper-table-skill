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
    spec = base("benchmark", "Task success and inference cost at two token budgets",
                "Adaptive routing is best on every suite within each budget: 2.9 and 2.4 points above Verifier, the strongest baseline, on average, with 13% and 18% fewer tokens.", 1)
    tasks = [("math", "Math", 250), ("code", "Code", 200), ("docs", "Docs", 150), ("tools", "Tools", 100)]
    spec["columns"] = [{"id": "method", "label": "Method", "kind": "text", "width_mm": 30}]
    for key, label, size in tasks:
        spec["columns"].append({"id": key, "label": [label, "n=" + str(size)], "kind": "number", "precision": 1, "direction": "max", "bounds": [0, 100]})
    spec["columns"] += [{"id": "macro", "label": ["Avg.", "macro"], "kind": "number", "precision": 1, "direction": "max", "bounds": [0, 100]},
                        {"id": "tokens", "label": ["Tokens", "mean"], "kind": "number", "precision": 0, "direction": "min", "thousands": True},
                        {"id": "latency", "label": ["Latency", "ms"], "kind": "number", "precision": 0, "direction": "min", "thousands": True}]
    spec["column_groups"] = [{"label": "Task success (%) ↑", "columns": [t[0] for t in tasks] + ["macro"]},
                             {"label": "Cost ↓", "columns": ["tokens", "latency"]}]
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
    raw, numeric, strongest = [], [c["id"] for c in spec["columns"][1:]], {}
    for i, (budget, label, counts, tokens, latency) in enumerate(records):
        scores = [100*c/t[2] for c, t in zip(counts, tasks)]
        cells = {"method": label, **{t[0]: val(s) for t, s in zip(tasks, scores)}, "macro": val(sum(scores)/4), "tokens": val(tokens), "latency": val(latency)}
        spec["rows"].append({"id": "r" + str(i), "display_group": budget, "comparison_group": budget, "focus": label == "Adaptive routing", "cells": cells})
        raw.append({"budget": budget, "method": label, "successes": dict(zip([t[0] for t in tasks], counts)), "denominators": dict((t[0], t[2]) for t in tasks), "mean_tokens": tokens, "latency_ms": latency})
        if label == "Verifier":
            strongest[budget] = cells
        if label == "Adaptive routing":
            # the margin over the strongest baseline (highest Avg. in both budgets), from unrounded values
            spec["rows"].append({"id": "margin_" + budget, "display_group": budget, "comparison_group": budget, "delta": True,
                                 "cells": {"method": "Δ vs. Verifier", **{c: val(cells[c]["value"] - strongest[budget][c]["value"]) for c in numeric}}})
    spec["row_group_labels"] = {"16k": "16k-token budget", "32k": "32k-token budget"}
    spec["ranking"] = {"axis": "column", "tie_policy": "rounded", "meaning": "Bold: best within a budget."}
    spec["focus_meaning"] = "Shaded: proposed method."
    spec["provenance"]["derived"] = "Δ vs. Verifier rows: Adaptive routing minus Verifier in the same budget, computed from unrounded values."
    spec["notes"] = ["Success = successes / n; Avg. is the unweighted mean of the four rates, and orders the baselines. Δ is Adaptive routing minus Verifier, from unrounded values; green marks an improvement."]
    return spec, raw


def ablation():
    spec = base("ablation", "Component ablations",
                "Retrieval contributes most to success; the cache has no detectable effect on success but saves 177 ms.", 2)
    spec["style"].update({"tabcolsep_pt": 4.2})
    parts = [("retrieve", "Retrieve"), ("verify", "Verify"), ("route", "Route"), ("cache", "Cache")]
    spec["columns"] = [{"id": "method", "label": "Configuration", "kind": "text", "width_mm": 34}]
    spec["columns"] += [{"id": x, "label": label, "kind": "status"} for x, label in parts]
    spec["columns"] += [{"id": "score", "label": ["Success", "% ↑, ± SD"], "kind": "mean_sd", "precision": 1, "bounds": [0, 100],
                         "uncertainty_definition": "Sample standard deviation across 8 independent synthetic training-seed blocks; ddof=1, not a confidence interval"},
                        {"id": "delta", "label": ["Δ vs. full", "pp [95% CI]"], "kind": "interval", "precision": 1, "delta": "max",
                         "uncertainty_definition": "Paired seed bootstrap of the mean difference from full; 20,000 resamples, 8 paired seed blocks, percentile 2.5/97.5, generator seed 120"},
                        {"id": "latency", "label": ["Latency", "ms ↓"], "kind": "number", "precision": 0},
                        {"id": "dlat", "label": ["Δ vs. full", "ms"], "kind": "number", "precision": 0, "delta": "min"}]
    spec["column_groups"] = [{"label": "Components", "columns": [x for x, _ in parts]}]
    ref = np.array([82.6, 83.8, 83.0, 84.2, 84.5, 83.3, 83.6, 83.0])
    conditions = [  # the reference first, then removals ordered by their effect on success
        ("full", "Full system", [1,1,1,1], np.zeros(8), 512, "ref"),
        ("no_retrieve", "− Retrieval", [0,1,1,1], np.array([-7.9,-8.4,-8.1,-8.9,-7.7,-8.4,-8.6,-8.2]), 418, "single"),
        ("no_verify", "− Verifier", [1,0,1,1], np.array([-4.4,-4.9,-4.5,-4.7,-5.2,-4.8,-4.4,-4.7]), 435, "single"),
        ("no_route", "− Routing", [1,1,0,1], np.array([-3.0,-3.4,-2.8,-3.5,-3.1,-2.7,-3.4,-3.0]), 566, "single"),
        ("no_cache", "− Cache", [1,1,1,0], np.array([.1,-.2,.2,.1,-.1,.2,-.1,.0]), 689, "single"),
        ("no_rv", "− Retrieval, verifier", [0,0,1,1], np.array([-11.6,-12.3,-12.0,-12.7,-11.9,-12.2,-12.5,-12.1]), 341, "joint"),
        ("no_rc", "− Routing, cache", [1,1,0,0], np.array([-3.1,-3.5,-2.9,-3.4,-3.2,-2.8,-3.5,-3.0]), 748, "joint")]
    rng = np.random.default_rng(120)
    index = rng.integers(0, len(ref), size=(20000, len(ref)))
    raw = {"seed_ids": list(range(8)), "bootstrap_seed": 120, "bootstrap_replicates": 20000, "rows": []}
    for key, label, flags, delta, latency, group in conditions:
        scores = ref + delta
        low, high = np.quantile(delta[index].mean(axis=1), [.025, .975])
        full = key == "full"
        cells = {"method": label, **dict(zip([x for x, _ in parts], ["yes" if f else "no" for f in flags])),
                 "score": {"value": float(scores.mean()), "sd": float(scores.std(ddof=1))},
                 "delta": {"missing": "not_applicable"} if full else {"value": float(delta.mean()), "low": float(low), "high": float(high)},
                 "latency": val(latency), "dlat": {"missing": "not_applicable"} if full else val(latency - conditions[0][4])}
        spec["rows"].append({"id": key, "display_group": group, "focus": full, "cells": cells})
        raw["rows"].append({"id": key, "seed_success_percent": scores.tolist(), "paired_delta_pp": delta.tolist(), "illustrative_latency_ms": latency})
    spec["row_group_labels"] = {"ref": "", "single": "One component removed", "joint": "Two components removed"}
    spec["missing_style"] = "dash"
    spec["status_legend"] = {"yes": "kept", "no": "removed"}
    spec["focus_meaning"] = "Shaded: the full system, the reference for Δ."
    spec["provenance"]["derived"] = "Latency Δ vs. full: each row's latency minus the full system's 512 ms."
    spec["notes"] = ["Success Δ is the paired difference from the full system on the same 8 seeds, with a percentile-bootstrap 95% CI over seeds; ± is the SD across seeds. Δ is green for an improvement, red for a loss, grey for none."]
    return spec, raw


def efficiency():
    spec = base("efficiency", "Quality and serving cost of three attention variants",
                "Hybrid is best on every metric at 16k context; Dense runs out of memory at batch 32.", 3)
    spec["style"].update({"width_mm": 88, "tabcolsep_pt": 3.4, "group_style": "band"})
    spec["columns"] = [{"id": "metric", "label": "Metric", "kind": "text", "width_mm": 25},
                       {"id": "unit", "label": "Unit", "kind": "text", "width_mm": 11}]
    spec["columns"] += [{"id": x, "label": label, "kind": "number", "precision": 1} for x, label in [("dense", "Dense"), ("sparse", "Sparse"), ("hybrid", "Hybrid"), ("extended", "Hybrid")]]
    spec["column_groups"] = [{"label": "16k context", "columns": ["dense", "sparse", "hybrid"]}, {"label": "32k", "columns": ["extended"]}]
    entries = [  # one unit and direction per row, so both sit beside the metric name rather than in a header
        ("accuracy", "Task success", "% ↑", "max", [74.2,74.3,76.6,78.0], "quality", 1),
        ("calibration", "Calibration error", "pp ↓", "min", [4.8,4.2,3.5,3.2], "quality", 1),
        ("latency", "P95 latency", "ms ↓", "min", [184.2,157.9,149.8,230.3], "serve", 1),
        ("throughput", "Throughput", "req/s ↑", "max", [30.4,34.7,36.2,23.5], "serve", 1),
        ("memory", "Peak memory", "GB ↓", "min", [36.4,30.1,28.5,44.8], "serve", 1),
        ("energy", "Energy / request", "J ↓", "min", [9.8,8.2,7.6,12.4], "serve", 1),
        ("stress_latency", "P95 latency", "ms ↓", "min", [None,392,351,None], "stress", 0),
        ("stress_throughput", "Throughput", "req/s ↑", "max", [None,61.3,66.9,None], "stress", 1)]
    raw = []
    for key, label, unit, direction, values, group, digits in entries:
        spec["rows"].append({"id": key, "display_group": group, "direction": direction, "precision": digits,
                             "cells": {"metric": label, "unit": unit, **{c["id"]: {"failure": "oom"} if v is None else val(v) for c, v in zip(spec["columns"][2:], values)}}})
        raw.append({"metric": key, "values": values, "direction": direction, "block": group})
    spec["row_group_labels"] = {"quality": "Quality · 1,000 requests", "serve": "Serving · batch 4", "stress": "Stress · batch 32"}
    spec["ranking"] = {"axis": "row", "scopes": [["dense", "sparse", "hybrid"]], "tie_policy": "rounded", "meaning": "Bold: best of the three 16k variants; the 32k column is context and is not ranked."}
    spec["notes"] = ["One 80 GB GPU, BF16 weights, 256 output tokens per request."]
    return spec, raw


def registry():
    spec = base("registry", "Datasets and evaluation splits",
                "Counts are in each collection's own unit, so no total is given.", 4)
    spec["style"].update({"tabcolsep_pt": 4.2, "arraystretch": 1.25})
    count = lambda cid, label: {"id": cid, "label": label, "kind": "number", "precision": 0, "thousands": True}
    spec["columns"] = [{"id": "collection", "label": "Collection", "kind": "text", "width_mm": 30},
                       {"id": "coverage", "label": "Coverage", "kind": "text", "width_mm": 20},
                       count("train", "Train"), count("dev", "Dev"), count("test", "Test"),
                       {"id": "unit", "label": "Unit", "kind": "text", "width_mm": 16},
                       {"id": "separation", "label": "Separation rule", "kind": "text", "width_mm": 58}]
    # the unit column sits right after the counts it qualifies: "120,000  2,000  3,000  problem"
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
    spec["notes"] = ["Counts are manifest entries; 0 is an intentionally empty split."]
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
