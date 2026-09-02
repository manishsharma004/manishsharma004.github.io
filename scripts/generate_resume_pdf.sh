#!/usr/bin/env bash
# Generate resume/manish-sharma-resume.pdf from resume/index.html.
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
    --margin-top 8mm \
    --margin-bottom 8mm \
    --margin-left 8mm \
    --margin-right 8mm \
    "$HTML" \
    "$OUT"

echo "Wrote $OUT ($(wc -c < "$OUT") bytes)"
