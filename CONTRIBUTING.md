# Contributing

Thanks for considering a contribution. This repo is a collection of agent skills (Markdown only).

## Before you start

1. Read AGENTS.md and README.md.
2. Search existing issues/discussions to avoid duplicates.
3. For substantial changes, open a discussion or issue first.

## Skill standards (required)

Every skill must include these six sections, in order: Overview, When to Use, Process, Rationalizations, Red Flags, Verification. Plus YAML frontmatter with name and description.

- Keep SKILL.md under ~200 lines.
- "When to Use" must list actionable trigger phrases.
- "Verification" must be a runnable checklist.
- No executable code, secrets, or network calls.
- Keep descriptions tool-agnostic.

## How to contribute

1. Fork and create a branch.
2. Make changes.
3. Run: python3 run_tests.py
4. Update CHANGELOG.md and README.md skill table if applicable.
5. Open a pull request using the provided template.

## Code of conduct

By participating, you agree to abide by the Code of Conduct (CODE_OF_CONDUCT.md).

## Questions

See SUPPORT.md.
