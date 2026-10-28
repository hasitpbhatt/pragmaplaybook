---
name: coding-interview
description: Coaches coding and behavioral interviews. Use when preparing for or conducting a coding interview. Use when solving DSA problems. Use for behavioral interview prep with STAR method.
---

# Coding Interview

## Overview
Two halves: **DSA** (solve correctly, then optimize) and **Behavioral** (STAR, honesty-first). The bar isn't "got the answer" — it's "showed structured thinking under pressure."

## When to Use
- Preparing for a coding/behavioral interview
- Solving a LeetCode-style problem in an interview setting
- Practicing STAR answers

## Process — DSA

### Step 1: Clarify (2 min)
- Restate problem in your own words
- Ask about edge cases, constraints, input size
- Confirm expected output format

### Step 2: Brute force (3 min)
- State the naive O(n²) or O(n³) solution first
- Don't code yet — just describe

### Step 3: Optimize (5 min)
- Identify the bottleneck (nested loop? repeated work?)
- Apply pattern: two pointers, sliding window, hash map, binary search, DP
- State new complexity before coding

### Step 4: Code (15 min)
- Write clean, readable code
- Name variables meaningfully
- Handle edge cases explicitly

### Step 5: Test (5 min)
- Walk through with example input
- Test edge cases: empty, single, duplicates, negatives
- Trace complexity claim

### Step 6: Discuss (3 min)
- Trade-offs of your approach
- What would you do differently with more time?
- Follow-up: "what if input is 10x larger?"

## Complexity Cheat Sheet

| Pattern | Time | Space |
|---|---|---|
| Hash map lookup | O(1) | O(n) |
| Binary search | O(log n) | O(1) |
| Two pointers | O(n) | O(1) |
| Sliding window | O(n) | O(k) |
| BFS/DFS | O(V+E) | O(V) |
| DP (2D) | O(n²) | O(n²) or O(n) |
| Heap | O(n log k) | O(k) |

## Process — Behavioral (STAR)

### Step 1: Pick the story
- Choose a real situation, not a hypothetical
- It must have a measurable outcome

### Step 2: Structure as STAR
- **S**ituation: context in 2 sentences
- **T**ask: what you were responsible for
- **A**ction: what YOU did (use "I", not "we")
- **R**esult: quantified outcome + what you learned

### Step 3: Honesty gates
- Don't claim team wins as personal
- Admit failures; show what changed after
- "I don't know" beats a confident wrong answer

## Red Flags
- Jumping to code without clarifying
- Silent coding (narrate your thinking)
- Not testing edge cases
- Claiming team outcomes as personal
- "I would have done X" (hypotheticals)
- Optimizing prematurely

## Rationalizations

| Excuse | Reality |
|---|---|
| "I'll figure it out as I code" | Clarify first. Coding is the last step. |
| "The interviewer wants speed" | They want thinking. Narrate. |
| "Edge cases are obvious" | They're the bugs. Test them. |
| "I don't have a good story for that" | Use a failure. Failures are the best stories. |

## Verification
- [ ] Problem restated + edge cases confirmed
- [ ] Brute force stated before optimizing
- [ ] Complexity stated before coding
- [ ] Code tested with examples + edge cases
- [ ] Can explain trade-offs and follow-ups
- [ ] STAR answers use "I" and have quantified results
