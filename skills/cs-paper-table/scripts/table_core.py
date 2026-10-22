#!/usr/bin/env python3
"""Strict cell validation, Decimal formatting and scoped emphasis for paper tables.

This module does not estimate uncertainty, infer comparability, infer a metric's
direction or turn rank into statistical significance. Those are input contracts.
"""
from __future__ import annotations
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import hashlib
import json
from pathlib import Path
import re

MISSING = {"not_reported": "NR", "not_applicable": "NA", "not_run": "NT", "incomparable": "NC"}
FAILURES = {"oom": "OOM", "timeout": "TO", "execution_error": "ERR"}
STATUS = {"yes": "Yes", "no": "No", "partial": "Partial", "unknown": "Unknown"}
# status_style "symbols" (default): marks read faster than words in capability/ablation matrices
STATUS_SYMBOLS = {"yes": "✓", "no": "✗", "partial": "◐", "unknown": "?"}


def decimal(value):
    if isinstance(value, bool) or not isinstance(value, (str, int, float, Decimal)):
        raise ValueError(f"Expected a finite numeric value, got {value!r}")
    try:
        item = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError(f"Invalid number: {value!r}") from exc
    if not item.is_finite():
        raise ValueError("NaN and infinity are not missing-value markers")
    return item


def precision(col, row, cell=None):
    """Display decimals. "reported" keeps each value's own printed decimals (pass the value as a
    string, e.g. "23.75"), for transcribed tables whose sources mix precision."""
    digits = row.get("precision", col.get("precision", 1))
    if digits == "reported":
        value = cell.get("value") if isinstance(cell, dict) else None
        if not isinstance(value, str):
            raise ValueError(f"precision 'reported' needs the value as a string: {row.get('id')}/{col.get('id')}")
        mantissa = value.lower().split("e")[0]
        return len(mantissa.split(".")[1]) if "." in mantissa else 0
    return digits


def rounded(value, digits):
    answer = decimal(value).quantize(Decimal(1).scaleb(-digits), rounding=ROUND_HALF_UP)
    return abs(answer) if answer == 0 else answer


def number(value, digits, signed=False):
    answer = rounded(value, digits)
    return ("+" if signed and answer > 0 else "") + f"{answer:.{digits}f}"


def value_of(cell):
    if not isinstance(cell, dict) or "missing" in cell or "value" not in cell:
        return None
    return decimal(cell["value"])


def grouped(text):
    """Thousands separators on the integer part of a formatted number: 120000 -> 120,000."""
    sign = text[0] if text[:1] in "+-" else ""
    body = text[len(sign):]
    whole, _, frac = body.partition(".")
    whole = f"{int(whole):,}"
    return sign + whole + ("." + frac if frac else "")


def scientific(value, digits):
    """Mantissa/exponent pair, e.g. 3.3e18 -> ("3.3", 18) at digits=1."""
    item = decimal(value)
    if item == 0:
        return number(0, digits), 0
    exp = item.copy_abs().adjusted()
    mant = rounded(item.scaleb(-exp), digits)
    if abs(mant) >= 10:
        exp += 1
        mant = rounded(item.scaleb(-exp), digits)
    return f"{mant:.{digits}f}", exp


def formatted(col, value, digits, signed=False):
    """Display string for one numeric value under the column's number format."""
    if col.get("format") == "sci":
        mant, exp = scientific(value, digits)
        return f"{mant}·10^{exp}"
    text = number(value, digits, signed)
    text = grouped(text) if col.get("thousands") else text
    return text + col.get("suffix", "")


def display_cell(col, row, cell, spec=None):
    if isinstance(cell, dict) and "missing" in cell:
        return "–" if (spec or {}).get("missing_style") == "dash" else MISSING[cell["missing"]]
    if isinstance(cell, dict) and "failure" in cell:
        return FAILURES[cell["failure"]]
    if isinstance(cell, dict) and cell.get("spanned"):
        return ""
    kind = col["kind"]
    if kind == "text":
        return cell
    if kind == "status":
        return (STATUS if (spec or {}).get("status_style") == "words" else STATUS_SYMBOLS)[cell]
    digits = precision(col, row, cell)
    if row.get("delta"):
        return formatted(col, cell["value"], digits, signed=True)
    lead = formatted(col, cell["value"], digits, col.get("signed", False))
    if kind == "number":
        return lead
    if kind == "mean_sd":
        if col.get("sd_style") == "paren":
            return lead + " (" + number(cell["sd"], digits) + ")"
        return lead + " ± " + number(cell["sd"], digits)
    if kind == "interval":
        return lead + " [" + number(cell["low"], digits, col.get("signed", False)) + ", " + number(cell["high"], digits, col.get("signed", False)) + "]"
    raise ValueError(kind)


def validate(spec):
    for key in ("id", "title", "caption", "data_status", "provenance", "columns", "rows", "notes", "style"):
        if key not in spec:
            raise ValueError("Missing required field: " + key)
    if not re.fullmatch(r"[a-z][a-z0-9_-]*", spec["id"]):
        raise ValueError("id must be a safe lowercase file stem")
    if spec["data_status"] not in {"measured", "reported", "derived", "synthetic", "illustrative", "schematic"}:
        raise ValueError("Declare data_status explicitly")
    if not spec["provenance"] or not spec["notes"]:
        raise ValueError("Supply provenance and interpretation notes")
    cols = spec["columns"]
    ids = [c["id"] for c in cols]
    if len(ids) != len(set(ids)) or len(ids) < 2:
        raise ValueError("Columns need distinct IDs")
    rows = spec["rows"]
    if not rows or len({r["id"] for r in rows}) != len(rows):
        raise ValueError("Rows need distinct IDs")
    for col in cols:
        if col["kind"] not in {"text", "number", "mean_sd", "interval", "status"}:
            raise ValueError("Unknown column kind")
        if col.get("direction") not in {None, "max", "min"}:
            raise ValueError("direction must be max, min or null")
        if col["kind"] == "text" and col.get("width_mm", 0) <= 0:
            raise ValueError("Text columns need an explicit width_mm")
        if col["kind"] in {"mean_sd", "interval"} and not col.get("uncertainty_definition"):
            raise ValueError("Define the uncertainty and sampling unit for compound estimates")
    for row in rows:
        if set(row["cells"]) != set(ids):
            raise ValueError("Row cells must exactly match column IDs: " + row["id"])
        if row.get("direction") not in {None, "max", "min"}:
            raise ValueError("Bad row direction")
        for col in cols:
            cell = row["cells"][col["id"]]
            digits = row.get("precision", col.get("precision", 1))
            if digits != "reported" and (not isinstance(digits, int) or not 0 <= digits <= 8):
                raise ValueError("precision must be an integer from 0 to 8, or 'reported'")
            if isinstance(cell, dict) and "missing" in cell:
                if set(cell) != {"missing"} or cell["missing"] not in MISSING:
                    raise ValueError("Missing values need one explicit supported reason")
                continue
            if isinstance(cell, dict) and "failure" in cell:
                if set(cell) != {"failure"} or cell["failure"] not in FAILURES:
                    raise ValueError("Observed failures need one explicit supported outcome")
                continue
            if isinstance(cell, dict) and cell.get("spanned"):
                if set(cell) != {"spanned"}:
                    raise ValueError("A spanned placeholder holds no value: " + row["id"])
                continue
            if row.get("delta") and col["kind"] in {"number", "mean_sd", "interval"}:
                if not isinstance(cell, dict) or set(cell) != {"value"}:
                    raise ValueError(f"Delta row {row['id']}/{col['id']} needs exactly {{'value'}}")
                decimal(cell["value"])
                continue
            if col["kind"] == "text":
                if not isinstance(cell, str):
                    raise ValueError("Text cells must be strings")
            elif col["kind"] == "status":
                if cell not in STATUS:
                    raise ValueError("Unknown status; do not turn unknown into no")
            else:
                expected = {"value"} | ({"sd"} if col["kind"] == "mean_sd" else {"low", "high"} if col["kind"] == "interval" else set())
                if isinstance(cell, dict) and "span" in cell:
                    if col["kind"] != "number" or not isinstance(cell["span"], int) or cell["span"] < 2:
                        raise ValueError("span is an integer >= 2 on a number cell")
                    following = ids[ids.index(col["id"]) + 1: ids.index(col["id"]) + cell["span"]]
                    if len(following) != cell["span"] - 1 or any(row["cells"][c] != {"spanned": True} for c in following):
                        raise ValueError("Cells covered by a span must be {\"spanned\": true}: " + row["id"])
                    expected = expected | {"span"}
                if isinstance(cell, dict) and "mark" in cell:
                    if cell["mark"] not in spec.get("marks", {}):
                        raise ValueError(f"Cell mark {cell['mark']!r} needs a definition in root 'marks': {row['id']}")
                    expected = expected | {"mark"}
                if not isinstance(cell, dict) or set(cell) != expected:
                    raise ValueError(f"Cell {row['id']}/{col['id']} needs exactly {expected}")
                for key in expected - {"mark", "span"}:
                    decimal(cell[key])
                if "sd" in cell and decimal(cell["sd"]) < 0:
                    raise ValueError("SD cannot be negative")
                if "low" in cell and decimal(cell["low"]) > decimal(cell["high"]):
                    raise ValueError("Interval endpoints are reversed")
                if col.get("bounds"):
                    lo, hi = map(decimal, col["bounds"])
                    if not lo <= decimal(cell["value"]) <= hi:
                        raise ValueError("Value outside declared metric bounds")
    if spec.get("missing_style", "codes") not in {"codes", "dash"}:
        raise ValueError("missing_style is codes or dash")
    if spec.get("missing_style") == "dash":
        kinds = {c["missing"] for r in rows for c in r["cells"].values() if isinstance(c, dict) and "missing" in c}
        if len(kinds) > 1:
            raise ValueError("A dash can stand for only one missing state; use codes when several occur: " + str(sorted(kinds)))
    for mark, meaning in spec.get("marks", {}).items():
        if not mark or len(mark) > 2 or not meaning:
            raise ValueError("marks map short symbols (e.g. '*', '†') to their meaning")
    if spec["style"].get("group_style", "banner") not in {"banner", "label", "band"}:
        raise ValueError("style.group_style is banner, label or band")
    if spec.get("status_style", "symbols") not in {"symbols", "words"}:
        raise ValueError("status_style is symbols or words")
    for col in cols:
        if col.get("delta") not in {None, "max", "min"}:
            raise ValueError("column delta is the direction in which a change is an improvement: max or min")
        if col.get("format", "fixed") not in {"fixed", "sci"} or col.get("sd_style", "pm") not in {"pm", "paren"}:
            raise ValueError("format is fixed or sci; sd_style is pm or paren")
        if col.get("sd_style") == "paren" and "(" not in col.get("uncertainty_definition", "("):
            pass
    positions = {cid: n + 1 for n, cid in enumerate(ids)}
    occupied = set()
    for group in spec.get("column_groups", []):
        group_ids = group["columns"]
        locs = [positions[cid] for cid in group_ids]
        if locs != list(range(min(locs), max(locs) + 1)) or occupied.intersection(locs):
            raise ValueError("Column groups must be contiguous and disjoint")
        occupied.update(locs)
    ranking = spec.get("ranking", {"axis": "none"})
    if ranking["axis"] not in {"none", "column", "row"}:
        raise ValueError("Ranking axis must be declared")
    if ranking["axis"] != "none":
        if ranking.get("tie_policy") not in {"rounded", "raw", "tolerance"}:
            raise ValueError("Declare a tie policy")
        if not ranking.get("meaning"):
            raise ValueError("Declare emphasis meaning; rank is not significance")
        if ranking.get("runner_up") not in {None, "underline"}:
            raise ValueError("runner_up is omitted or 'underline'")
        if ranking.get("runner_up") and "underline" not in ranking["meaning"].lower():
            raise ValueError("Say what the underline means in ranking.meaning")
        if ranking["axis"] == "column" and any("comparison_group" not in r for r in rows):
            raise ValueError("Column ranking requires a comparison_group on every row")
        if ranking["axis"] == "row":
            scopes = ranking.get("scopes", [])
            if not scopes or any(not s or not set(s) <= set(ids) for s in scopes):
                raise ValueError("Row ranking requires explicit column scopes")
            flat = [cid for scope in scopes for cid in scope]
            if len(flat) != len(set(flat)):
                raise ValueError("Row comparison scopes must not overlap")
            if any(r.get("rank", True) and not r.get("direction") for r in rows):
                raise ValueError("Every ranked row requires its metric direction")
    style = spec["style"]
    if style.get("body_pt", 0) < 7.2 or style.get("note_pt", 0) < 7.2:
        raise ValueError("Recompose the table instead of using text below 7.2 pt")
    if not 65 <= style.get("width_mm", 0) <= 250:
        raise ValueError("Declare an appropriate final table width")
    if any(r.get("focus") for r in rows) and not spec.get("focus_meaning"):
        raise ValueError("A tinted focus row needs an explicit meaning")
    return spec


def emphasis(spec, second=None):
    """Return bold coordinates and audit records, without inventing a comparator.
    If a set is passed as `second`, runner-up coordinates (ranking.runner_up) are added to it."""
    validate(spec)
    rank = spec.get("ranking", {"axis": "none"})
    marked, audits = set(), []
    if rank["axis"] == "none":
        return marked, audits
    columns = {c["id"]: c for c in spec["columns"]}
    cohorts = []
    if rank["axis"] == "column":
        groups = list(dict.fromkeys(r["comparison_group"] for r in spec["rows"]))
        for cid, col in columns.items():
            if not col.get("direction"):
                continue
            for group in groups:
                eligible = [(r, col) for r in spec["rows"] if r["comparison_group"] == group and r.get("rank", True) and not r.get("delta")]
                cohorts.append((f"{group}/{cid}", col["direction"], eligible, col.get("tie_tolerance", rank.get("tie_tolerance"))))
    else:
        for row in spec["rows"]:
            if not row.get("rank", True):
                continue
            for index, scope in enumerate(rank["scopes"]):
                cohorts.append((f"{row['id']}/scope-{index+1}", row["direction"], [(row, columns[c]) for c in scope], row.get("tie_tolerance", rank.get("tie_tolerance"))))
    for name, direction, cells, tolerance in cohorts:
        values = []
        for row, col in cells:
            value = value_of(row["cells"][col["id"]])
            if value is not None:
                score = rounded(value, precision(col, row, row["cells"][col["id"]])) if rank["tie_policy"] == "rounded" else value
                values.append((row["id"], col["id"], score))
        if not values:
            audits.append({"scope": name, "eligible": 0, "winners": []})
            continue
        best = (max if direction == "max" else min)(v[2] for v in values)
        tol = decimal(tolerance) if rank["tie_policy"] == "tolerance" and tolerance is not None else Decimal(0)
        if tol < 0 or (rank["tie_policy"] == "tolerance" and tolerance is None):
            raise ValueError("Tolerance tie policy requires a nonnegative stated tolerance")
        winners = [(rid, cid) for rid, cid, score in values if abs(score - best) <= tol]
        marked.update(winners)
        record = {"scope": name, "direction": direction, "eligible": len(values),
                  "tie_policy": rank["tie_policy"], "tolerance": str(tol), "best": str(best),
                  "winners": [list(k) for k in winners]}
        rest = [v for v in values if (v[0], v[1]) not in set(winners)]
        if rank.get("runner_up") and rest:
            nxt = (max if direction == "max" else min)(v[2] for v in rest)
            runners = [(rid, cid) for rid, cid, score in rest if abs(score - nxt) <= tol]
            record["runner_up"] = [list(k) for k in runners]
            if second is not None:
                second.update(runners)
        audits.append(record)
    return marked, audits


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
