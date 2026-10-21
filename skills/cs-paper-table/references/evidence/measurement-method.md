# Measurement, provenance, and reproduction

This document specifies the measurement methods used by the three source-table studies inspected on **2026-10-21**. Their measured values describe the PDF artifacts at their inspected versions. Visual interpretations are recorded separately, and recommended design choices are not presented as author or company policy.

## Evidence files and their scope

| File | Contents |
|---|---|
| `../source-index.json` | Canonical `papers[]` and `tables[]`; the latter separates `observed`, `measured`, and `recommended` fields. |
| `../paper-corpus.csv` | One row per distinct report; source URL, inspected version, SHA256, affiliation evidence, publication-year basis, and table IDs. |
| `../table-corpus.csv` | One row per independently visually inspected table anchor; page, crop/body bounds, measured font summary, and lessons. |
| Three company-group `.json` files | Full structured study findings with portable paths. Their `observations` are observed, `measurements` are measured, and `lessons`/`cautions` are recommended. |
| Three company-group `.md` files | Full study narrative and per-table learning. Research-only image links have been removed. |
| `measurements/<group>/<anchor>.json` | Distribution copies of structured PDF-object style measurements, with input paths replaced by reproducible provenance. Span style metadata, object bounds, colors, opacity, font names, widths, character counts, and caveats are retained; extracted source text is omitted. |
| `measurements/google-meta-nvidia/*-layout.json` | Thirty supplementary layout measurements for the same thirty table anchors; these are not additional table inspections. |
| `catalog-validation.json` | Counts, deduplication keys, actual-PDF SHA256 verification, and checksums of the source research notes. |

Paths beginning `references/` in the index are relative to the skill root. Measurement paths in a company-group JSON/Markdown file are relative to this `evidence` directory. Source PDFs, crop images, and font binaries are not bundled.

**Distribution policy:** `distribution omits extracted source text; style properties retained`. The packaged measurement JSON omits each span's `text_in_pdf_order` string and any equivalent source-text extraction fields. It retains every numeric style/geometry field and the extraction method. Original analyst observations, design analysis, and research-only evidence remain unchanged. The cleanup counts are recorded in `catalog-validation.json`; source text can be re-extracted from the version- and hash-verified PDF when needed for a new inspection.

## Identity and counting

One paper is one canonical work: an arXiv identifier without its version suffix, or a normalized primary-source URL for an official report. The inspected version and complete PDF SHA256 are retained independently. All 54 actual PDF byte streams were hashed again when the portable catalog was built, and all recorded hashes matched. There are 54 distinct canonical works and 54 distinct PDF hashes.

One counted table is a unique `(canonical_work_id, printed_table_anchor)`. Including its physical PDF page as an additional key still gives 95 unique records. Every counted table has `pdf_visual_inspected` status in its source study. The 95 body/caption measurement records, 30 supplementary layout records, additional crops, and prior figure studies do not increase that count. Hash verification checks file identity; it is not a fresh independent visual review of all tables.

For arXiv, the primary PDF URLs contain an explicit version. Official-report URLs can later serve different bytes: a matching filename or URL is insufficient. Compare the downloaded PDF SHA256 with the catalog before relying on the recorded coordinates. If it differs, retain the new version as a distinct inspection and do not silently apply the old measurements.

The `year` filter uses the first-publication/report year recorded by the source study, not necessarily the inspected revision year. Hunyuan-A13B deliberately has `year: 2025`: its cover is dated 2025-06-27, while the inspected arXiv submission is dated 2026-09-23. Its original `publication_date_note` and [official repository](https://github.com/Tencent-Hunyuan/Hunyuan-A13B) evidence are retained. Company grouping records affiliation evidence and allows collaborations; it does not imply that every author belongs to the named company.

## Coordinates and visual inspection

- Pages are **1-based physical PDF pages**, not printed page numbers or section numbering.
- Coordinates are PDF points: **1 pt = 1/72 inch**. The origin is the **top-left of the unrotated physical page**, x increases rightward, and y downward.
- A rectangle is `[x0, y0, x1, y1]`. The source inspector sets page rotation to zero in memory; it does not rewrite the source PDF.
- `display_crop_bbox_pt` contains the selected table and relevant caption/notes. `table_body_bbox_pt` isolates the intended body. `raw_measurement_bbox_pt` records exactly which rectangle the original object extractor used.
- Source pages/crops were explicitly opened for visual reading. The portable catalog preserves the researchers' inspection status and method, along with direct source URLs and reconstructible crop bounds; it does not bundle the viewed images.

| Source study | Display crop | Raw object-measurement region | Body text measurements |
|---|---|---|---|
| OpenAI / Anthropic / Microsoft | 144 dpi; separate body preview at 180 dpi | Table body | Character centers inside body rectangle |
| Google / DeepMind / Meta / NVIDIA | 216 dpi | Display crop, **including caption** | Separate body-only font/style measurements are retained; page font resources are also retained and must not be confused with table fonts |
| DeepSeek / Tencent / Alibaba | 216 dpi | Table body | Character centers inside body rectangle; separately identified caption-region text lies within display crop and outside body |

These scopes are intentionally preserved. A caption-inclusive vector histogram must not be silently relabeled as body-only. Per-table `measurement_method` and raw `selected_region` fields identify the applicable scope.

## Nominal PDF-object extraction

The original studies used **PyMuPDF 1.26.6** and the same `inspect_pdf_style.py` measurement helper. The skill's `scripts/inspect_table_pdf.py` preserves that extraction logic and exposes a table-oriented command line. The catalog's raw reports record the original extraction schema version and package version.

### Text and fonts

`Page.get_texttrace()` supplies the traces. Membership in the selected region is decided for **each character by the center of its bounding box**, with boundary points included. The selected characters' boxes are then combined to form a reported span box. Partial traces retain `partial_trace_at_crop_boundary`.

Text with nominal rendering mode 0 or 1 and positive opacity is classified `visible`; rendering mode 3 or zero opacity is `invisible`; other modes are `other`. This classification does not solve clipping, later overpainting, optional-content visibility, masks, or blend groups. A visually hidden or duplicated trace is therefore still possible.

Font summaries group by visibility class, font program name, nominal size, and rendering mode. They retain both trace and selected-character counts. A dominant font is the largest contribution by selected-character count; it may be a bold header font in a tiny table and is not automatically a main body font. Superscripts, inline metric labels, captions, and math glyphs can have separate sizes. Page-level font resources list available/referenced programs; only region-selected traces establish that a program was used inside the measured table region.

Nominal point sizes can reflect PDF scaling or microtypographic expansion. Neither font names nor measured sizes establish the original LaTeX package, source font-size command, column specification, or cell padding. The names do not grant permission to redistribute a font. Outlined glyphs and raster lettering cannot be assigned a font merely from this report.

The research extractor obtained trace text in PDF paint order without inferred spaces or reading order. The distribution copy removes those verbatim strings while preserving span coordinates, style properties, character counts, partial-trace flags, and invalid-glyph numeric metadata. The extractor's Unicode caveat describes how a fresh extraction represents invalid scalars as U+FFFD; it does not imply that the packaged spans contain source text. Read the rendered glyph when extraction is ambiguous. Fill-and-stroke text may contribute duplicate counts.

### Vector paths, widths, and colors

`Page.get_drawings(extended=True)` is used when available, with a plain-call fallback. Selected paths have bounds intersecting the crop, expanded by half of the trusted stroke width. This includes zero-height horizontal and zero-width vertical bounds. Paths crossing the region retain full object bounds and are marked accordingly. Clip/group context is retained where available; composite visibility is not reconstructed.

Nonfinite, negative, or larger-than-the-longest-page-dimension raw widths are flagged as untrusted. They do not enter point-width summaries and do not enlarge selection bounds. This is a conservative sanity check, not proof that every PDF transform has been reconciled.

The all-stroke histogram counts **objects**, including value underlines, separators, outlines, and possibly clipped/obscured objects. It is not a histogram of semantic table rules. Thin filled black rectangles can also form rules and must not be mistaken for row shading. Long-rule subsets described below are candidate geometry, not automatic semantic labels.

Colors preserve extracted components and opacity. One-component gray is expanded to three equal components; three-component RGB is quantized to 8-bit hex using rounded, clamped components. Other component counts are retained without an RGB guess. A path count is not occupied color area or visual importance. Transparency, background, blending, and color management can alter final appearance. A pale color with opacity 1.0 is an opaque pale fill, not evidence of a transparent overlay.

### Raster occurrences

`Page.get_image_info()` occurrences whose boxes intersect the selected region are counted with bounds, dimensions, colorspace, and mask metadata. The report counts occurrences rather than distinct image assets and infers neither fonts nor palette from embedded raster content.

## Study-specific layout measurements

### OpenAI / Anthropic / Microsoft

The `fonts`, `vector_colors`, and `stroke_widths_pt` summaries come from the body-only raw report. Their `stroke_widths_pt` include all selected strokes. Descriptions of spacing, numeric alignment, wrapping, and semantic rule hierarchy are visual observations; no exact row-height, `tabcolsep`, or decimal-column implementation is inferred.

### Google / DeepMind / Meta / NVIDIA

The supplemental layout extraction examines actual line segments (`l` drawing items) within the body rectangle, allowing a 1 pt tolerance at its bounds. A horizontal candidate has endpoint y difference below 0.05 pt and length at least 15 pt. A vertical candidate has endpoint x difference below 0.05 pt and length at least 5 pt. The subset retains endpoints, width, dash pattern, and opacity. Short value underlines are often excluded by the horizontal-length condition, but geometry alone does not prove structural role.

Numeric baselines come from horizontal extracted text lines (`abs(direction_y) <= 0.01`) containing single-span strings matching `[+−-]?digits[.digits][%]`. Origins are rounded to 0.1 pt; a baseline is retained only if at least two such spans occur there. Adjacent gaps between 2 and 30 pt contribute to the reported median. Mixed-size annotations and split numeric strings can be missed. This is an output-layout statistic, not an inferred TeX row-padding setting.

`all_vector_stroke_widths_caption_inclusive` and `vector_color_counts_caption_inclusive` retain their caption-inclusive scope. `visible_table_font_summary` uses the separate body rectangle. Text-color counts in these summaries count spans, whereas some other studies count characters; these counts must not be pooled as equivalent quantities.

### DeepSeek / Tencent / Alibaba

Long horizontal candidates are selected from raw vector paths whose bounding-box width exceeds **30% of the body-region width** and whose height is at most **1.5 pt**. The subset can include stroked paths or filled rectangles and retains both fill and stroke metadata.

The reported `main_regular_text_size_pt` is a heuristic: among font-summary entries sorted by character count, it first chooses a font name containing `Roma`, `Regular`, or `Regu` and not containing `Bold` or `Ital`; if none matches it falls back to the dominant entry. It is not a universal text-role classifier.

For candidate numeric baselines, extracted spans must have centers inside the body, a nominal font size within 0.15 pt of that main-size heuristic, and a complete numeric string with optional sign/decimal/percent. Baselines are rounded to 0.01 pt; successive baseline positions within 0.4 pt are collapsed. Adjacent gaps from 5 to 25 pt are reported as a frequency distribution. Unlike the preceding study, this is not a median and does not require two numeric spans per baseline.

`caption_font_summary` selects extracted spans with centers inside the display crop and outside the body. It can therefore include notes or another nearby label included by the crop. The original record's naming is preserved, with this scope qualification.

## Reproduce a specific inspection

1. Use `scripts/search_corpus.py` to select a table. Read its source URL, inspected version, PDF SHA256, physical page, and both crop rectangles.
2. Download the primary PDF into your working directory, verify SHA256, and open the recorded physical page. If the hash differs, investigate the version before using old coordinates.
3. Run the inspector on the appropriate recorded region. For example, Astra Table 1 has body rectangle `[70, 404, 542, 560]` on PDF page 11:

```bash
python scripts/inspect_table_pdf.py source.pdf \
  --page 11 --bbox 70 404 542 560 --out inspection/astra-table-1
```

The command writes `measurement.json` and `crop.png` to the chosen output directory. Inspect the generated image directly before interpreting object summaries. To review the full caption context, run the same command with display crop `[68, 384, 544, 561]` and a separate output directory. Generated artifacts from this new check do not alter the source catalog automatically.

4. Compare raw object properties within the same region and extraction version. Reproduce the study-specific rules above when matching baseline or long-rule statistics. A new inspector run is useful evidence, but byte-for-byte JSON equality is not required across library versions or normalized metadata.
5. Record new measurements under `measured`, visual interpretation under `observed`, and proposed design choices under `recommended`. Do not turn an observed 4–7 pt source table into a prescribed production size, a colored source link into a data encoding, or a bold cell into a significance claim.

The sample is a purposive study of table construction and scientific communication. It does not certify scientific claims, journal/conference rank, acceptance causality, exhaustive corporate practice, or readability for every intended output size.
