---
name: debug
description: Disciplined debugging for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow.
---

# Debug

A discipline for hard bugs. Skip phases only when explicitly justified.

## Overview

This skill provides a structured loop for diagnosing and fixing bugs and performance regressions. It starts with building a red-capable feedback loop, then moves through reproduction, hypothesising, instrumentation, fixing, and cleanup. Skip phases only when explicitly justified.

## When to Use

When the user says "diagnose" or "debug this", or reports something broken/throwing/failing/slow. Use for hard bugs and performance regressions where a tight feedback loop is needed.

## Process

### Phase 1: Build a feedback loop (the skill)

Everything else is mechanical. If you have a tight pass/fail signal that goes red on *this* bug, you will find the cause. Spend disproportionate effort here. Refuse to give up.

Ways to build one, in order: failing test at the seam; curl/HTTP script; CLI invocation with a fixture; headless browser script; replay a captured trace; throwaway harness; property/fuzz loop; bisection harness; differential loop; human-in-the-loop script (last resort).

Tighten it: faster, sharper signal, more deterministic. For flaky bugs, raise the repro rate until debuggable.

**If you cannot build a loop, stop and say so.** List what you tried; ask for env access, a redacted artifact, or permission to instrument prod. Do not hypothesise without a loop.

Done when one command is red-capable, deterministic, fast, and agent-runnable.

### Phase 2: Reproduce + minimise

Run the loop; confirm it matches the user's symptom, not a nearby failure. Then shrink the repro to the smallest scenario that still goes red — cut inputs, callers, config one at a time. Every remaining element must be load-bearing.

### Phase 3: Hypothesise

Generate 3–5 ranked, falsifiable hypotheses before testing any. Format: "If X is the cause, then changing Y makes the bug disappear / changing Z makes it worse." Show the list to the user before testing.

### Phase 4: Instrument

Each probe maps to a specific prediction. Change one variable at a time. Prefer a debugger over logs; tag every debug log with a unique prefix (e.g. `[DEBUG-a4f2]`) for easy cleanup. For perf regressions: measure first, bisect, fix second.

### Phase 5: Fix and regression test

Write the regression test before the fix, but only if a correct seam exists (one exercising the real bug pattern at the call site). If no correct seam exists, that's the finding — flag the architecture. Then: turn repro into a failing test, watch it fail, apply fix, watch it pass, re-run Phase 1 loop on the un-minimised scenario.

### Phase 6: Cleanup

- Original repro no longer reproduces
- Regression test passes (or absence of seam documented)
- All debug instrumentation removed
- Throwaway prototypes deleted
- Correct hypothesis stated in commit/PR message

## Rationalizations

| Excuse | Reality |
|---|---|
| Hypothesising before a red-capable loop exists | No loop = guessing, not debugging |
| Single hypothesis instead of 3–5 | Anchoring on one idea blocks other lines of inquiry |
| Untagged debug logs left behind | Makes cleanup hard; future debuggers can't grep efficiently |
| Fix without regression test where a seam exists | Gives false confidence; bug can recur |

## Red flags

- Hypothesising before a red-capable loop exists
- Single hypothesis instead of 3–5
- Untagged debug logs left behind
- Fix without regression test where a seam exists

## Verification

- [ ] Original repro no longer reproduces
- [ ] Regression test passes (or absence of seam documented)
- [ ] All debug instrumentation removed
- [ ] Throwaway prototypes deleted
- [ ] Correct hypothesis stated in commit/PR message