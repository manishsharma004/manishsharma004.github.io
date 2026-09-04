#!/usr/bin/env bash
# Generate resume/manish-sharma-resume.pdf from resume/index.html.
# Output: A4 portrait — 10mm top/right margins, flush left and bottom for sidebar.
# Requires wkhtmltopdf: https://wkhtmltopdf.org/
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HTML="$ROOT/resume/index.html"
OUT="$ROOT/resume/manish-sharma-resume.pdf"

WKHTMLTOPDF="${WKHTMLTOPDF:-wkhtmltopdf}"
if ! command -v "$WKHTMLTOPDF" >/dev/null 2>&1; then
    echo "wkhtmltopdf not found. Install it or set WKHTMLTOPDF to the binary path." >&2
    exit 1
fi

"$WKHTMLTOPDF" \
    --quiet \
    --enable-local-file-access \
    --print-media-type \
    --background \
    --disable-smart-shrinking \
    --page-size A4 \
    --orientation Portrait \
    --dpi 96 \
    --margin-top 10mm \
    --margin-bottom 0 \
    --margin-left 0 \
    --margin-right 10mm \
    "$HTML" \
    "$OUT"

# Verify A4 dimensions (595 × 842 pt ±1)
python3 - "$OUT" <<'PY'
import subprocess, re, sys
info = subprocess.check_output(["pdfinfo", sys.argv[1]], text=True)
m = re.search(r"Page size:\s+([\d.]+) x ([\d.]+) pts", info)
pages = re.search(r"Pages:\s+(\d+)", info)
if not m:
    sys.exit(0)
w, h = float(m.group(1)), float(m.group(2))
if not (594 <= w <= 596 and 841 <= h <= 843):
    print(f"Warning: expected A4 (595×842 pt), got {w}×{h} pt", file=sys.stderr)
    sys.exit(1)
print(f"Verified A4: {w:.0f}×{h:.0f} pt, {pages.group(1)} page(s)")
PY

echo "Wrote $OUT ($(wc -c < "$OUT") bytes)"
