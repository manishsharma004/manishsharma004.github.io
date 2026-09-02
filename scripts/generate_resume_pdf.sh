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
    --page-size A4 \
    --margin-top 14mm \
    --margin-bottom 14mm \
    --margin-left 16mm \
    --margin-right 16mm \
    "$HTML" \
    "$OUT"

echo "Wrote $OUT ($(wc -c < "$OUT") bytes)"
