#!/usr/bin/env python3
"""
Renders the Quarto book and prepends a JPG cover page to produce a merged PDF.
Requires: pypdf, reportlab, Pillow  (pip install -r requirements.txt)

Usage:
  python compile.py [--cover-jpg PATH] [--source-pdf PATH] [--output-pdf PATH]
"""

import argparse
import io
import subprocess
import sys
from pathlib import Path

DEFAULT_COVER_JPG  = Path("assets/frontpage.jpg")
DEFAULT_SOURCE_PDF = Path("_book/Introducción-al-desarrollo-web-frontend.pdf")
DEFAULT_OUTPUT_PDF = Path("web1-frontend-book.pdf")

# A4 dimensions in points (1 pt = 1/72 inch)
A4_W, A4_H = 595.28, 841.89


def jpg_to_a4_pdf(jpg_path: Path) -> bytes:
    """Return a single-page A4 PDF (in memory) with the JPG filling the page."""
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfgen import canvas
    from PIL import Image

    # Open image to get its natural orientation
    with Image.open(jpg_path) as img:
        img_w, img_h = img.size

    # Scale image to cover A4 (crop overflow), preserving aspect ratio
    scale = max(A4_W / img_w, A4_H / img_h)
    draw_w = img_w * scale
    draw_h = img_h * scale
    x_offset = (A4_W - draw_w) / 2
    y_offset = (A4_H - draw_h) / 2

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(A4_W, A4_H))
    c.drawImage(ImageReader(str(jpg_path)), x_offset, y_offset, width=draw_w, height=draw_h)
    c.showPage()
    c.save()
    return buf.getvalue()


def main():
    parser = argparse.ArgumentParser(description="Render Quarto book and prepend a JPG cover page.")
    parser.add_argument("--cover-jpg",  type=Path, default=DEFAULT_COVER_JPG,  metavar="PATH", help=f"Cover image (default: {DEFAULT_COVER_JPG})")
    parser.add_argument("--source-pdf", type=Path, default=DEFAULT_SOURCE_PDF, metavar="PATH", help=f"Rendered book PDF (default: {DEFAULT_SOURCE_PDF})")
    parser.add_argument("--output-pdf", type=Path, default=DEFAULT_OUTPUT_PDF, metavar="PATH", help=f"Output PDF path (default: {DEFAULT_OUTPUT_PDF})")
    args = parser.parse_args()

    cover_jpg  = args.cover_jpg
    source_pdf = args.source_pdf
    output_pdf = args.output_pdf

    print("Running quarto render...")
    result = subprocess.run(["quarto", "render"], check=False)
    if result.returncode != 0:
        print("quarto render failed.", file=sys.stderr)
        sys.exit(result.returncode)

    for path in (source_pdf, cover_jpg):
        if not path.exists():
            print(f"File not found: {path}", file=sys.stderr)
            sys.exit(1)

    try:
        from pypdf import PdfWriter, PdfReader
    except ImportError:
        print("pypdf is not installed. Run: pip install -r requirements.txt", file=sys.stderr)
        sys.exit(1)

    cover_pdf_bytes = jpg_to_a4_pdf(cover_jpg)

    writer = PdfWriter()

    # Cover page first
    cover_reader = PdfReader(io.BytesIO(cover_pdf_bytes))
    for page in cover_reader.pages:
        writer.add_page(page)

    # Then the rendered book
    book_reader = PdfReader(str(source_pdf))
    for page in book_reader.pages:
        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"Saved: {output_pdf}")


if __name__ == "__main__":
    main()
