# System Design Cheat Sheet

**6 steps, in order, every time:**

1. **Clarify** — functional + non-functional + out of scope (5 min)
2. **Scale** — DAU, QPS, storage, bandwidth (3 min)
3. **Data model** — entities, read/write ratio, consistency, storage choice (5 min)
4. **Components** — API, services, data, async (10 min)
5. **Bottlenecks** — SPOF, hot keys, thundering herd + mitigations (5 min)
6. **Trade-offs** — "I chose X because Y, at the cost of Z" (5 min)

## Must-answer questions
- What breaks first at 10x load?
- What's the single point of failure?
- How do we recover from a DB outage?

## CAP quick pick
- Money/identity → strong consistency (SQL)
- Feeds/metrics → eventual consistency (NoSQL)
- Don't pick "both" — pick per subsystem
