---
name: coding-interview
description: DSA + behavioral interview coach. Use when preparing for coding/behavioral interview rounds. Covers 6-step DSA process (clarify → brute force → optimize → code → test → discuss), complexity cheat sheet, and STAR method with honesty gates.
---

# Coding Interview

## Overview
A 6-step DSA process for coding interviews plus behavioral STAR framework. Each step has a time budget; skip none. The goal is demonstrating structured problem-solving, not just getting the right answer.

## When to Use
- Coding interview (DSA round)
- Behavioral interview prep
- Any interview where you write code and discuss trade-offs

## Process

### DSA Process (6 steps, ~33 min)

1. **Clarify** (2 min) — restate; ask edge cases, constraints, input size; confirm output format.
2. **Brute force** (3 min) — state naive solution; don't code yet.
3. **Optimize** (5 min) — find bottleneck; apply pattern (two pointers, sliding window, hash map, binary search, DP); state new complexity.
4. **Code** (15 min) — clean, readable, meaningful names, explicit edge cases.
5. **Test** (5 min) — walk example; test empty/single/dups/negatives; trace complexity.
6. **Discuss** (3 min) — trade-offs; what with more time?; "what if 10x larger?"

### Complexity cheat sheet
| Pattern | Time | Space |
|---|---|---|
| Hash map | O(1) | O(n) |
| Binary search | O(log n) | O(1) |
| Two pointers | O(n) | O(1) |
| Sliding window | O(n) | O(k) |
| BFS/DFS | O(V+E) | O(V) |
| DP 2D | O(n²) | O(n²) or O(n) |
| Heap | O(n log k) | O(k) |

### Behavioral (STAR)
1. Pick a real situation with a measurable outcome.
2. **S**ituation (2 sentences), **T**ask (your responsibility), **A**ction (what YOU did, "I"), **R**esult (quantified + learned).
3. Honesty gates: don't claim team wins; admit failures; "I don't know" beats confident wrong.

## Rationalizations

| Excuse | Reality |
|---|---|
| "I'll just start coding" | Clarifying first prevents solving the wrong problem |
| "Brute force is a waste of time" | It shows you understand the problem before optimizing |
| "Edge cases don't matter" | They're the difference between pass and fail |
| "Team wins are my wins" | Interviewers want YOUR impact; claim "I", not "we" |

## Red Flags

- Jumping to code without clarifying; silent coding; skipping edge-case tests
- Claiming team outcomes; optimizing prematurely

## Verification
- [ ] Problem restated; constraints and edge cases confirmed
- [ ] Brute force stated before optimizing
- [ ] Complexity stated before coding
- [ ] Code is clean with meaningful names and explicit edge cases
- [ ] Tested with examples + edge cases (empty, single, dups, negatives)
- [ ] STAR answers use "I" with quantified results
- [ ] Honesty gates applied: no team wins claimed, failures admitted