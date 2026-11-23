---
name: grill
description: Relentlessly interview the user about a plan, decision, or idea until every branch of the design tree is resolved. Use when stress-testing a plan or design before building.
---

# Grill

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

## Overview

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it. Work in rounds, asking the whole frontier at once, then wait for answers. Do not act until the user confirms shared understanding.

## When to Use

When stress-testing a plan or design before building. Use when you need to surface hidden assumptions, resolve ambiguous decisions, or align with the user before writing code.

## Process

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are settled — questions you can ask now without guessing at answers you haven't heard. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Format a round:

```
❓ **Q1** - **<title>**: <body>

➡️ <recommended answer>

---

❓ **Q2** - **<title>**: <body>

➡️ <recommended answer>
```

Word each question so "yes" accepts your recommended answer.

Each round reshapes the tree: settled decisions push the frontier outward. Recompute and ask the next round. A question depending on an open question in this round belongs to a later round.

Finding **facts** is your job, never the user's — dispatch a sub-agent with fresh context to look up anything in the environment. Don't block on it; only downstream questions wait. The **decisions** are the user's: put each to them and wait.

Done when the frontier is empty: every branch visited, nothing silently assumed. Do not act until the user confirms shared understanding.

## Rationalizations

| Excuse | Reality |
|---|---|
| Acting before shared understanding | Misalignment is the #1 failure mode; act early, build wrong |
| Asking the user for facts you could look up | Wastes their time; you have tools, use them |
| One question at a time | Serial bottleneck; the frontier has multiple independent branches |

## Red Flags

- Acting before shared understanding
- Asking the user for facts you could look up
- One question at a time when the frontier has several

## Verification

- [ ] Shared understanding confirmed with user
- [ ] All decision branches resolved and documented
- [ ] Frontier is empty (no unresolved questions)