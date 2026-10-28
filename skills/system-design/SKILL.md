---
name: system-design
description: Guides technical system design interviews. Use when preparing for or conducting a system design interview. Use when asked to design a system at scale. Use when evaluating architecture trade-offs.
---

# System Design

## Overview
A 6-step framework for any system design interview. Each step has a time budget; skip none. The goal isn't a perfect design — it's demonstrating structured thinking and trade-off awareness.

## When to Use
- Technical interview (system design round)
- Architecture review for a real system
- When asked "design X at scale"

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

## Verification
- [ ] Requirements clarified (functional + non-functional + out-of-scope)
- [ ] Scale estimated with numbers
- [ ] Data model defined with consistency choices
- [ ] Components drawn with responsibilities
- [ ] Bottlenecks identified with mitigations
- [ ] Trade-offs stated explicitly with justification
- [ ] Can answer "what breaks first at 10x load?"
