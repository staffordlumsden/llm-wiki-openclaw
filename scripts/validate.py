#!/usr/bin/env python3
"""Structural/policy validation for the llm-wiki OpenClaw skill package."""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []

required = [
    "SKILL.md",
    "profiles/wiki-query/SKILL.md",
    "references/openclaw-runtime.md",
    "references/hub-resolution.md",
    "references/wiki-structure.md",
    "references/query.md",
    "references/ingestion.md",
    "references/compilation.md",
    "references/research.md",
    "references/audit-lint.md",
    "references/inventory-datasets.md",
    "references/sessions-feedback.md",
    "references/collections.md",
    "references/archive.md",
    "references/librarian.md",
    "references/projects-outputs.md",
    "references/lessons.md",
    "README.md", "NOTICE.md", "LICENSE"
]
for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

def frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return {}, text
    try:
        head, body = text[4:].split("\n---\n", 1)
    except ValueError:
        errors.append(f"{path.relative_to(ROOT)}: unterminated YAML frontmatter")
        return {}, text
    data = {}
    for line in head.splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if ':' not in line:
            errors.append(f"{path.relative_to(ROOT)}: unsupported frontmatter line {line!r}")
            continue
        k,v = line.split(':',1)
        data[k.strip()] = v.strip()
    return data, body

main_meta, main_body = frontmatter(ROOT / "SKILL.md")
query_meta, query_body = frontmatter(ROOT / "profiles/wiki-query/SKILL.md")

if main_meta.get("name") != "llm-wiki":
    errors.append("main skill name must be llm-wiki")
if query_meta.get("name") != "wiki-query":
    errors.append("query skill name must be wiki-query")
if query_meta.get("disable-model-invocation", "").lower() != "true":
    errors.append("wiki-query must be explicit-only (disable-model-invocation: true)")

for term in ["Never edit", "Do not invoke `exec`", "read-only"]:
    if term.lower() not in query_body.lower():
        errors.append(f"wiki-query missing policy guard: {term}")

# Verify local reference targets used by main skill.
for target in re.findall(r'`(references/[A-Za-z0-9_.\-/]+\.md)`', main_body):
    if not (ROOT / target).exists():
        errors.append(f"SKILL.md links missing reference: {target}")

# A child-research contract is deliberate: workers must not mutate wiki state.
if "sole writer" not in main_body.lower() and "single writer" not in main_body.lower():
    errors.append("main skill lacks single-writer research contract")
if "sessions_spawn" not in main_body or "sessions_yield" not in main_body:
    errors.append("main skill lacks OpenClaw sub-agent mapping")
for workflow in ["collect", "archive", "librarian", "project", "output", "assess", "lessons"]:
    if workflow not in main_body.lower():
        errors.append(f"main skill router missing workflow: {workflow}")

# Flag dangerous accidental examples in query-only profile.
for bad in ["rm -rf", "curl | sh", "chmod 777", "sudo "]:
    if bad in query_body:
        errors.append(f"query profile contains risky pattern: {bad}")

# Basic line hygiene.
for path in ROOT.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    if "\r\n" in text:
        warnings.append(f"{path.relative_to(ROOT)} uses CRLF")
    if len(max(text.splitlines() or [''], key=len)) > 500:
        warnings.append(f"{path.relative_to(ROOT)} has a line longer than 500 chars")

if errors:
    print("FAIL")
    for e in errors: print(" -", e)
    if warnings:
        print("WARNINGS")
        for w in warnings: print(" -", w)
    sys.exit(1)

print(f"PASS: {len(required)} required files present; skill frontmatter and policy guards validated.")
if warnings:
    print("WARNINGS")
    for w in warnings: print(" -", w)
