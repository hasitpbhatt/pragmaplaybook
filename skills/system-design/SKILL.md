---
name: system-design
description: Guides technical system design interviews. Use when preparing for or conducting a system design interview. Use when asked to design a system at scale. Use when evaluating architecture trade-offs.
---

# System Design

## Overview
A 6-step framework for any system design interview. Each step has a time budget; skip none. The goal isn't a perfect design — it's demonstrating structured thinking and trade-off awareness.

## When to Use
- Technical interview (system design or coding round)
- Architecture review for a real system
- When asked "design X at scale"
- Solving a DSA problem in an interview setting
- Behavioral interview prep (STAR method)

## Process

### Step 1: Clarify requirements (5 min)
- Functional: what must the system do? (list 3-5 core features)
- Non-functional: scale, latency, availability, consistency targets
- Out of scope: explicitly state what you're NOT building
- Ask: "Is there a specific part you'd like me to focus on?"

### Step 2: Estimate scale (3 min)
- Users (DAU/MAU), QPS (read/write ratio)
- Storage: objects × size × retention
- Bandwidth: QPS × payload size
- Growth: 10x in 2 years?

### Step 3: Define data model (5 min)
- Core entities + relationships
- Read vs write patterns (which dominates?)
- Consistency requirements per entity (strong vs eventual)
- Storage choice: SQL vs NoSQL vs cache — justify

### Step 4: Design components (10 min)
- API layer (REST/GraphQL/gRPC)
- Service layer (stateless services)
- Data layer (DB, cache, object store)
- Async (queues, workers)
- Draw boxes; label each with responsibility

### Step 5: Identify bottlenecks (5 min)
- Single points of failure
- Hot partitions / hot keys
- Thundering herd, cache stampede
- Network choke points
- Mitigation: sharding, replication, rate limiting, backpressure

### Step 6: Address trade-offs (5 min)
- CAP: consistency vs availability (pick one per subsystem)
- Latency vs throughput
- Cost vs performance
- Complexity vs maintainability
- State explicitly: "I chose X because Y, at the cost of Z."

## Trade-off Matrix (quick reference)

| Decision | Option A | Option B | Pick when |
|---|---|---|---|
| Consistency | Strong (SQL) | Eventual (NoSQL) | Money/identity vs feeds/metrics |
| Scaling | Vertical | Horizontal | <10x load vs >10x load |
| Caching | Write-through | Write-behind | Read-heavy vs write-heavy |
| Sync | Sync call | Async queue | <100ms SLA vs >100ms OK |
| Storage | SQL | NoSQL | Relations/joins vs flat KV |

## Red Flags
- Jumping to components before clarifying requirements
- No scale numbers ("it should scale")
- Ignoring failure modes
- No trade-offs stated ("this is just the best")
- Designing a DB schema for 5 min then skipping bottleneck analysis

## Rationalizations

| Excuse | Reality |
|---|---|
| "Requirements are obvious" | They never are. Clarify first. |
| "Scale doesn't matter for the interview" | Scale drives every decision. Estimate. |
| "I'll mention trade-offs at the end" | Trade-offs ARE the answer. State them inline. |
| "A simple design is too simple" | Simple + correct beats complex + wrong. |

## Coding Interview (DSA + Behavioral)

### DSA Process
1. **Clarify** (2 min) — restate; ask edge cases, constraints, input size; confirm output format.
2. **Brute force** (3 min) — state naive solution; don't code yet.
3. **Optimize** (5 min) — find bottleneck; apply pattern (two pointers, sliding window, hash map, binary search, DP); state new complexity.
4. **Code** (15 min) — clean, readable, meaningful names, explicit edge cases.
5. **Test** (5 min) — walk example; test empty/single/dups/negatives; trace complexity.
6. **Discuss** (3 min) — trade-offs; what with more time?; "what if 10x larger?"

Complexity cheat sheet: hash map O(1)/O(n); binary search O(log n)/O(1); two pointers O(n)/O(1); sliding window O(n)/O(k); BFS/DFS O(V+E)/O(V); DP 2D O(n²)/O(n²) or O(n); heap O(n log k)/O(k).

### Behavioral (STAR)
1. Pick a real situation with a measurable outcome.
2. **S**ituation (2 sentences), **T**ask (your responsibility), **A**ction (what YOU did, "I"), **R**esult (quantified + learned).
3. Honesty gates: don't claim team wins; admit failures; "I don't know" beats confident wrong.

### Red Flags (coding)
- Jumping to code without clarifying; silent coding; skipping edge-case tests; claiming team outcomes; optimizing prematurely.

## Verification
- [ ] Requirements clarified (functional + non-functional + out-of-scope)
- [ ] Scale estimated with numbers
- [ ] Data model defined with consistency choices
- [ ] Components drawn with responsibilities
- [ ] Bottlenecks identified with mitigations
- [ ] Trade-offs stated explicitly with justification
- [ ] Can answer "what breaks first at 10x load?"
- [ ] DSA: problem restated, brute force stated, complexity stated before coding, tested with examples + edge cases
- [ ] STAR answers use "I" with quantified results
