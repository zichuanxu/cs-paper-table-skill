#!/usr/bin/env python3
"""Smallest checks that fail when the renderer's typographic guarantees break. Run: python test_render.py"""
import json
from pathlib import Path

from render_table import header_tex, make_html, make_latex, numeric_tex
from table_core import emphasis, validate

SPECS = Path(__file__).resolve().parents[1] / "assets" / "specs"


def test_bold_number_bolds_point_and_sign():
    # \mathbf would leave ".", "," and the minus at regular weight
    cell = numeric_tex("−1,480.5", bold=True)
    assert "mathbf" not in cell and cell.count(r"\boldmath") == 3  # left half, right half, the point


def test_header_names_share_a_baseline():
    assert header_tex("Method", True, depth=2).count(r"\\") == header_tex(["Math", "n=250"], True, depth=2).count(r"\\") == 1


def test_every_bundled_spec_builds_source():
    for path in sorted(SPECS.rglob("*.json")):
        spec = validate(json.loads(path.read_text()))
        second = set()
        marked, _ = emphasis(spec, second)
        _, fragment, _ = make_latex(spec, marked, second)
        assert r"\providecolor{TableMuted}" in fragment and r"\frenchspacing" in fragment, path.name
        assert make_html(spec, marked, second).count("<u>") == len(second), path.name


if __name__ == "__main__":
    for name, check in list(globals().items()):
        if name.startswith("test_"):
            check()
            print("ok", name)
