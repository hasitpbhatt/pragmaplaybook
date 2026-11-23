---
name: tdd
description: "Test-driven development: build features and fix bugs one vertical slice at a time with a red-green loop."
---

# TDD

Build in vertical slices: one failing test, then just enough code to pass, repeat. Tests verify behavior through public interfaces, not internals, so they survive refactors.

## Overview

Build in vertical slices: one failing test, then just enough code to pass, repeat. Tests verify behavior through public interfaces, not internals, so they survive refactors. Consult every section before and during the loop, not after.

## When to Use

When building features or fixing bugs test-first, or when the user mentions "red-green-refactor" or integration tests.

## Process

### What a good test is

Tests verify behavior through public interfaces, not implementation details. Code can change entirely; tests shouldn't. A good test reads like a specification: "user can checkout with valid cart" tells you exactly what capability exists, and it survives refactors because it doesn't care about internal structure.

### Seams: where tests go

A **seam** is the public boundary you test at — the interface where you observe behavior without reaching inside. Tests live at seams, never against internals.

**Test only at pre-agreed seams.** Before writing any test, write down the seams under test and confirm them with the user. Ask: "What's the public interface, and which seams should we test?" Give each proposed seam a one-line note on what it catches and what it misses. Don't test internals.

### Anti-patterns

- **Implementation-coupled**: mocks internal collaborators, tests private methods, verifies through a side channel. Breaks when you refactor though behavior hasn't changed.
- **Tautological**: the assertion recomputes the expected value like the code does. Expected values must come from an independent source of truth (known-good literal, worked example, spec).
- **Horizontal slicing**: writing all tests first, then all code. Tests verify imagined behavior and go insensitive. Interleave test + code instead.

### Loop rules

- Red before green: write the failing test first, then minimal code to pass. No speculative features.
- One slice at a time: one seam, one test, one minimal implementation.
- Refactoring is not part of the loop — it belongs to review.

## Rationalizations

| Excuse | Reality |
|---|---|
| Implementation-coupled tests | These break on refactor with no behavior change |
| Tautological assertions | These pass by construction and can never disagree with the code |
| Horizontal slicing | These verify imagined behavior and go insensitive to real changes |

## Red Flags

- Implementation-coupled tests (mock internals, test private methods)
- Tautological assertions (recomputes expected value like the code does)
- Horizontal slicing (all tests first, then all code)

## Verification

- [ ] Every test fails before the fix and passes after
- [ ] Tests target public interfaces, not internals
- [ ] Tests and code interleaved (no horizontal slicing)