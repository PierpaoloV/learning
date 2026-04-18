"""LLM grader — usage: python grader/grade.py <path>

Examples:
  python grader/grade.py leetcode/0001-two-sum
  python grader/grade.py system-design/url-shortener
  python grader/grade.py ml-fundamentals/cards/001-attention.yaml
"""
import sys, os, pathlib, openai

ROOT = pathlib.Path(__file__).parent.parent
RUBRICS = pathlib.Path(__file__).parent / "rubrics"


def _detect_track(path: pathlib.Path) -> str:
    parts = path.parts
    if "leetcode" in parts:
        return "leetcode"
    if "system-design" in parts:
        return "system-design"
    if "ml-fundamentals" in parts:
        return "ml-fundamentals"
    raise ValueError(f"Cannot detect track from path: {path}")


def _collect_content(path: pathlib.Path) -> str:
    if path.is_file():
        return path.read_text()
    parts = []
    for f in sorted(path.rglob("*")):
        if f.is_file() and f.suffix in {".py", ".md", ".yaml", ".txt"}:
            parts.append(f"### {f.relative_to(ROOT)}\n{f.read_text()}")
    return "\n\n".join(parts)


def grade(target: str):
    path = ROOT / target
    if not path.exists():
        print(f"Path not found: {path}")
        sys.exit(1)

    track = _detect_track(path)
    rubric = (RUBRICS / f"{track}.md").read_text()
    content = _collect_content(path)

    prompt = f"""You are a senior ML interviewer at a top-tier tech company (Google/Meta/Anthropic level).

## Rubric
{rubric}

## Submission
{content}

Grade this submission strictly according to the rubric. Be honest and constructive.
"""

    openai.api_key = os.environ["OPENAI_API_KEY"]
    resp = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    review = resp.choices[0].message.content.strip()

    # Save review
    if path.is_dir():
        out = path / "review.md"
    else:
        out = path.parent / f"review-{path.stem}.md"
    out.write_text(review)
    print(review)
    print(f"\n→ Saved to {out.relative_to(ROOT)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    grade(sys.argv[1])
