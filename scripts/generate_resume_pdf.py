#!/usr/bin/env python3
"""Generate a minimal resume PDF without external dependencies."""

import zlib
from pathlib import Path


def escape_pdf_text(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def build_pdf(lines: list[str]) -> bytes:
    y_start = 780
    line_height = 14
    stream_parts = ["BT", "/F1 11 Tf", f"50 {y_start} Td"]
    for i, line in enumerate(lines):
        if i > 0:
            stream_parts.append(f"0 -{line_height} Td")
        stream_parts.append(f"({escape_pdf_text(line)}) Tj")
    stream_parts.append("ET")
    stream = "\n".join(stream_parts).encode("latin-1", errors="replace")
    compressed = zlib.compress(stream)

    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
        b"/Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>",
        b"<< /Length %d /Filter /FlateDecode >>\nstream\n" % len(compressed) + compressed + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]

    pdf = b"%PDF-1.4\n"
    offsets = [0]
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(pdf))
        pdf += f"{i} 0 obj\n".encode() + obj + b"\nendobj\n"

    xref_pos = len(pdf)
    pdf += f"xref\n0 {len(objects) + 1}\n".encode()
    pdf += b"0000000000 65535 f \n"
    for off in offsets[1:]:
        pdf += f"{off:010d} 00000 n \n".encode()
    pdf += (
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
        f"startxref\n{xref_pos}\n%%EOF\n"
    ).encode()
    return pdf


LINES = [
    "Manish Sharma",
    "Senior Software Engineer · Bengaluru, India",
    "github.com/manishsharma004",
    "",
    "SUMMARY",
    "11+ years building customer-focused products across frontend, backend,",
    "and distributed systems. Experience with RAG, GPT, and STT pipelines.",
    "B.Tech CSE, IIT (ISM) Dhanbad.",
    "",
    "EXPERIENCE",
    "Sequoia (Murren Consulting) — Senior Frontend Engineer (Jul 2024–Present)",
    "SpotLYT (AIBAE Tech.) — Senior Software Engineer (Aug 2023–Present)",
    "Embibe — Senior Software Engineer (Aug 2020–Aug 2023)",
    "AutoGrid India — Senior Software Engineer (Dec 2018–Apr 2020)",
    "Charcoaleats — Senior Software Consultant (Jun 2018–Dec 2018)",
    "Sokrati Technologies — Software Design Engineer (Jun 2015–Jun 2018)",
    "",
    "CORE SKILLS",
    "Java · Python · React · React Native · Spring Boot · FastAPI · Next.js",
    "PostgreSQL · MongoDB · Kafka · Kubernetes · RAG · OpenAI GPT · STT",
]

if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "resume" / "manish-sharma-resume.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(build_pdf(LINES))
    print(f"Wrote {out}")
