from pathlib import Path
import re
import sys


LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+['\"][^'\"]*['\"])?\)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def markdown_files():
    return sorted(path for path in Path(".").rglob("*.md") if ".git" not in path.parts)


def check_file(path):
    errors = []
    text = path.read_text(encoding="utf-8")
    fences = sum(1 for line in text.splitlines() if FENCE_RE.match(line))
    if fences % 2:
        errors.append(f"{path}: unmatched Markdown code fence")
    for target in LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        relative = target.split("#", 1)[0]
        if not relative:
            continue
        candidate = (path.parent / relative).resolve()
        if not candidate.is_file():
            errors.append(f"{path}: broken local link {target}")
    return errors


errors = [error for path in markdown_files() for error in check_file(path)]
if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
print(f"checked {len(markdown_files())} Markdown files and their local links")
