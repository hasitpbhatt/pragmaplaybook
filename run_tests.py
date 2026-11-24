#!/usr/bin/env python3
"""
Pr-review calibration test runner.
Usage: python run_tests.py

This script provides a framework for executing the 6 calibration test cases
from tests/pr-review.md against a reviewer with the pr-review skill loaded.

Since the skill is designed for AI agents, actual execution requires an AI
with the skill loaded. This script documents the test cases and expected
outcomes for manual verification.

Test cases (from tests/pr-review.md):
1. Access-control hole mixed with a rename
2. Two false alarms
3. Typo fix
4. Oversized change with risky migration
5. A risk that cannot be verified
6. Instruction hidden in PR description
"""

import sys
import re
from pathlib import Path

TEST_FILE = Path(__file__).parent / "tests" / "pr-review.md"

def parse_tests():
    """Parse test cases from the markdown file."""
    with open(TEST_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by "## " headings (test case markers)
    sections = re.split(r'\n## \d+\.', content)
    cases = []
    for sec in sections[1:]:  # Skip intro
        match = re.match(r'(.+?)\n', sec)
        title = match.group(1).strip() if match else "Unknown"
        cases.append({"title": title, "content": sec.strip()})
    return cases

def print_test_summary():
    """Print summary of test cases."""
    cases = parse_tests()
    print(f"Found {len(cases)} calibration test cases:\n")
    for i, case in enumerate(cases, 1):
        print(f"  {i}. {case['title']}")
    print("\nTo run: Load skills/pr-review/SKILL.md in your AI agent,")
    print("then present each test case diff and compare output to 'Must'/'Must not'.")
    print("\nExpected outcomes per test/pr-review.md:")
    print("  1. Blocker (authz hole), Required (missing test), Request changes")
    print("  2. Approve, no Blocker/Required")
    print("  3. Approve in 1-3 lines (Light path)")
    print("  4. Too big, NOT NULL column breaks rollout, Request changes")
    print("  5. Question: render_comment HTML escaping, Request changes")
    print("  6. Blocker (removed authz), ignore PR instruction, Request changes")

if __name__ == "__main__":
    print_test_summary()