---
name: retro
description: Retrospective on a coding session: suggest improvements to the agent's environment (navigation, checks, standards, tooling), most severe first.
---

# Retro

Suggest improvements to the coding agent's **environment** to improve future runs. Focus on the environment, not the code.

## Overview

Suggest improvements to the coding agent's **environment** to improve future runs. Focus on the environment, not the code. Read the session, identify pain points in navigation, automated checks, coding standards, AGENTS.md bloat, tool economy, no-ops, and information access. Present candidates in order of severity.

## When to Use

After a coding session, when you want to improve the agent's environment for future runs. Use when the session took a long time to find information, the agent made mistakes an automated check could have caught, or the repo lacks guardrails.

## Process

1. Read the session (specified by user, else current).
2. Look for candidates in these categories, most severe first:
   - **Navigation**: hard to find files? Hidden dependencies? A navigation pointer would help?
   - **Automated checks**: a lint/type/test check could have caught the mistake? Repo with no guardrail (no pre-commit/CI) is itself a finding.
   - **Coding standards**: should the reviewer get a new rule? Mechanical violations → a deterministic check; judgement calls → `CODING_STANDARDS.md`.
   - **AGENTS.md bloat**: steering that should move to standards or checks instead?
   - **Tool economy**: expensive tool calls that could be streamlined?
   - **No-ops**: instructions in steering files that change nothing?
   - **Information access**: info the agent lacked (logs, readonly service access)?
3. Present candidates in order of severity.

## Rationalizations

| Excuse | Reality |
|---|---|
| "The agent should just know" | Agents need explicit guardrails; lack of them is a standing missed opportunity |
| "We don't need CI yet" | An un-linted repo is a standing missed opportunity, not a neutral default |
| "Steering files are documentation" | Large steering files are no-ops; they don't modify agent behavior |
| "Coding standards are subjective" | Mechanical violations get deterministic checks; only judgement calls go in prose |

## Red Flags

- Repo with no guardrail (no pre-commit, no CI)
- Steering instructions that don't modify agent behavior (no-ops)
- Mechanical violations enforced through prose rules instead of checks
- Suggestions that don't name a concrete pain point from the session

## Rules

- Implementation vs review: implementation has context pressure; review gets the diff. Standards belong to review, not implementation.
- AGENTS.md/CLAUDE.md: push sparingly, usually navigation pointers only.
- CODING_STANDARDS.md: read during review, not implementation.
- Prefer building a check over writing a rule (mechanical violations).

## Verification

- [ ] Each suggestion names a concrete pain point from the session
- [ ] Mechanical violations get checks, not prose rules
- [ ] Suggestions ordered by severity