#!/usr/bin/env python3
"""Generate a standards-compliant resume PDF without external dependencies."""

from __future__ import annotations

import re
from pathlib import Path

# ASCII replacements for PDF WinAnsi safety
_ASCII = str.maketrans({
    "\u2014": "-",  # em dash
    "\u2013": "-",  # en dash
    "\u00b7": " - ",  # middle dot
    "\u2022": "-",  # bullet
})


def to_ascii(text: str) -> str:
    text = text.translate(_ASCII)
    return text.encode("ascii", errors="replace").decode("ascii")


def escape_pdf_text(text: str) -> str:
    return (
        to_ascii(text)
        .replace("\\", "\\\\")
        .replace("(", "\\(")
        .replace(")", "\\)")
    )


def build_content_stream(lines: list[str]) -> bytes:
    leading = 15
    y_start = 750
    parts = [
        "BT",
        "/F1 11 Tf",
        f"{leading} TL",
        f"50 {y_start} Td",
    ]
    for i, line in enumerate(lines):
        if i > 0:
            parts.append("T*")
        parts.append(f"({escape_pdf_text(line)}) Tj")
    parts.append("ET")
    return "\n".join(parts).encode("ascii")


def build_pdf(lines: list[str]) -> bytes:
    stream = build_content_stream(lines)
    stream_obj = (
        f"<< /Length {len(stream)} >>\nstream\n".encode("ascii")
        + stream
        + b"\nendstream"
    )

    objects: list[bytes] = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        (
            b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            b"/Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>"
        ),
        stream_obj,
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>",
    ]

    header = b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
    body = bytearray()
    offsets = [0]

    for i, obj in enumerate(objects, start=1):
        offsets.append(len(header) + len(body))
        body.extend(f"{i} 0 obj\n".encode("ascii"))
        body.extend(obj)
        body.extend(b"\nendobj\n")

    xref_start = len(header) + len(body)
    xref = bytearray()
    xref.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    xref.extend(b"0000000000 65535 f \n")
    for off in offsets[1:]:
        xref.extend(f"{off:010d} 00000 n \n".encode("ascii"))

    trailer = (
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
        f"startxref\n{xref_start}\n%%EOF\n"
    ).encode("ascii")

    return header + body + xref + trailer


LINES = [
    "Manish Sharma",
    "Senior Software Engineer - Bengaluru, India",
    "github.com/manishsharma004",
    "",
    "SUMMARY",
    "11+ years building customer-focused products across frontend, backend,",
    "and distributed systems. Experience with RAG, GPT, and STT pipelines.",
    "B.Tech CSE, IIT (ISM) Dhanbad.",
    "",
    "EXPERIENCE",
    "Sequoia (Murren Consulting) - Senior Frontend Engineer (Jul 2024-Present)",
    "SpotLYT (AIBAE Tech.) - Senior Software Engineer (Aug 2023-Present)",
    "Embibe - Senior Software Engineer (Aug 2020-Aug 2023)",
    "AutoGrid India - Senior Software Engineer (Dec 2018-Apr 2020)",
    "Charcoaleats - Senior Software Consultant (Jun 2018-Dec 2018)",
    "Sokrati Technologies - Software Design Engineer (Jun 2015-Jun 2018)",
    "",
    "CORE SKILLS",
    "Java, Python, React, React Native, Spring Boot, FastAPI, Next.js",
    "PostgreSQL, MongoDB, Kafka, Kubernetes, RAG, OpenAI GPT, STT",
]

if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "resume" / "manish-sharma-resume.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(build_pdf(LINES))
    print(f"Wrote {out} ({out.stat().st_size} bytes)")
