"""LLM grader — usage: python grader/grade.py <path>

Examples:
  python grader/grade.py leetcode/0001-two-sum
  python grader/grade.py system-design/url-shortener
  python grader/grade.py ml-fundamentals/cards/001-attention.yaml
"""
import os
import pathlib
import re
import sys

import openai

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


def _required_output_instructions(track: str) -> str:
    if track != "leetcode":
        return ""
    return """## Required Output Format
Your response must be valid markdown and start exactly like this:

## Grading Report
Grade: X/10
Take-home: <one sentence with the main lesson>

Then continue with the rubric breakdown, total score /25, improvement suggestions, and the optimal solution if the submitted one is suboptimal.

Rules:
- `Grade:` must be a single overall score from 1 to 10.
- `Take-home:` must be a single concise sentence.
- Do not omit either line.
"""


def _review_has_required_summary(review: str, track: str) -> bool:
    if track != "leetcode":
        return True
    return bool(
        re.search(r"(?im)^Grade:\s*\d{1,2}/10\s*$", review)
        and re.search(r"(?im)^Take-home:\s*.+$", review)
    )


def _build_prompt(track: str, rubric: str, content: str) -> str:
    output_requirements = _required_output_instructions(track)
    return f"""You are a senior ML interviewer at a top-tier tech company (Google/Meta/Anthropic level).

## Rubric
{rubric}

{output_requirements}
## Submission
{content}

Grade this submission strictly according to the rubric. Be honest and constructive.
"""


def grade(target: str):
    path = ROOT / target
    if not path.exists():
        print(f"Path not found: {path}")
        sys.exit(1)

    track = _detect_track(path)
    rubric = (RUBRICS / f"{track}.md").read_text()
    content = _collect_content(path)
    prompt = _build_prompt(track, rubric, content)

    openai.api_key = os.environ["OPENAI_API_KEY"]
    messages = [{"role": "user", "content": prompt}]

    for _ in range(3):
        resp = openai.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.2,
        )
        review = resp.choices[0].message.content.strip()
        if _review_has_required_summary(review, track):
            break
        messages.extend(
            [
                {"role": "assistant", "content": review},
                {
                    "role": "user",
                    "content": (
                        "You omitted the required `Grade: X/10` and/or `Take-home:` "
                        "summary lines. Rewrite the full review and include both lines "
                        "at the top exactly as requested."
                    ),
                },
            ]
        )
    else:
        raise RuntimeError(
            "The LLM response did not include the required summary lines after 3 attempts."
        )

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
