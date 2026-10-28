---
name: pr-review
description: Reviews a PR across accuracy, scalability, security, performance, and style. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use when asked to review a diff or PR, even when pasted inline.
---

# PR Review

## Overview
Reviews any change across five axes in priority order: **Correctness → Scalability → Security → Performance → Style**. Approval standard: approve when it *definitely improves* overall code health, even if not perfect.

**Core principle:** find bugs that could cause incidents, not generate 30 suggestions about code style. Every finding must be actionable with a file:line reference and evidence.

## When to Use
- Before merging any PR or change
- After completing a feature
- When another agent produced code you must evaluate
- After a bug fix (review fix + regression test)

## Process

### Step 1: Understand intent (before reading code)
- What is this change trying to do?
- What spec/task does it implement? (locate the original spec/issue)
- What behavior changes?

### Step 2: Two-dimensional review (run in parallel)
Review along two independent dimensions simultaneously:

**Dimension A — Repo standards adherence**
- Does it follow existing patterns, conventions, lint rules?
- Does it match the codebase's established architecture?

**Dimension B — Spec alignment**
- Does it implement what the spec/issue actually asked for?
- Are all acceptance criteria met?
- Any scope creep or missing requirements?

### Step 3: Review tests first
- Do tests exist? Do they test *behavior*, not implementation?
- Are edge cases covered (null, empty, boundary)?
- Would tests catch a regression if code changed?

### Step 4: Five-axis review (in order)
1. **Correctness** — matches spec? edge cases handled? error paths handled? no off-by-one/race/state bugs?
2. **Scalability** — N+1 queries? unbounded loops/fetches? pagination on lists? sync where async needed? O(n²) where O(n)?
3. **Security** — input validated/sanitized? secrets out of code/logs? auth checks? parameterized queries? XSS encoding? untrusted external data validated at boundary?
4. **Performance** — unnecessary re-renders? large objects in hot paths? missing indexes?
5. **Style** — names clear? straightforward control flow? no dead code? no clever tricks?

### Step 5: Production backend domain checks (when applicable)
For large production backends, also verify:
- **Concurrency** — race conditions, shared mutable state, lock ordering
- **Idempotency** — safe retries, duplicate request handling
- **Retry semantics** — exponential backoff, jitter, max attempts, poison messages
- **Distributed failures** — partial failures, network partitions, timeout handling, circuit breakers
- **Backward compatibility** — API contracts, schema migrations, deprecation paths
- **DB consistency** — transaction boundaries, isolation levels, deadlock risk
- **Observability** — logging, metrics, tracing for new code paths
- **Operational readiness** — feature flags, rollback plan, runbook updates

### Step 6: Categorize findings (evidence-backed only)
Label every comment by severity. Every finding MUST include file:line reference + evidence (code snippet or test result).

| Prefix | Meaning | Author action |
|---|---|---|
| (none) | Required | Must address |
| `Critical:` | Blocks merge | Security vuln, data loss, broken fn |
| `Nit:` | Minor optional | Author may ignore |
| `Optional:` / `Consider:` | Suggestion | Worth considering |
| `FYI` | Informational only | No action |

**Do NOT report:** stylistic preferences, formatting nits without a lint rule, "I would have done X" opinions. If it can't cause an incident or violate a stated standard, skip it.

Lead with what matters: correctness + security first, then structural, then nits. Don't bury real issues under cosmetic nits.

### Step 7: Verify verification
- Tests pass? Build succeeds? Manual verification? Screenshots for UI? Before/after?

## Review Discipline (from Google + Alibaba + industry)

- **Technical facts and data overrule opinions and personal preferences.** Design aspects are rarely pure style — weigh them on underlying principles.
- **Review every line.** Don't scan and assume. If you're not qualified for complex issues (security, concurrency, i18n), ensure a qualified reviewer is on the PR.
- **Author prepares first:** self-review diff, tests pass, clear context (what/why/what to focus on). Reduces wasted cycles.
- **Automated checks before humans:** lint, format, tests, static analysis run first. Humans focus on logic/design/risk.
- **Risk-based scope:** low-risk changes move fast; auth/API/data/AI-generated changes get deeper review.
- **High-level design before line-by-line:** if the design is flawed, discuss early — don't waste effort on line nits.
- **Security examined explicitly:** data flow, access enforcement, abuse assumptions.
- **Tests + docs in same PR as code changes.**
- **One approval standard:** approve once it definitely improves overall code health, even if imperfect. Don't block for "not how I'd write it."
- **Resolve conflicts fast:** direct discussion over extended comment threads. Don't let PRs sit.
- **Defer to author on ties:** if multiple approaches are equally valid (data or solid principles), accept author's preference.
- **Encouragement matters:** acknowledge good practices, not just mistakes.
- ~100 lines changed → good
- ~300 → acceptable if single logical change
- ~1000 → too large, split it
- Watch file size too: ~1000 lines in a single file is a smell

## Red Flags
- PR merged with no review
- Review only checks tests pass
- "LGTM" with no evidence of actual review
- Security-sensitive changes without security review
- Large PRs "too big to review" (split them)
- No regression test with bug fix
- Comments without severity labels or file:line refs
- Accepting "I'll fix it later" (it never happens)
- Findings without evidence (opinions, not bugs)
- Reporting 30+ style suggestions instead of real bugs

## Rationalizations

| Excuse | Reality |
|---|---|
| "It works, good enough" | Unreadable/insecure code creates compounding debt |
| "I wrote it, it's correct" | Authors are blind to their own assumptions |
| "We'll clean it up later" | Later never comes. Cleanup before merge. |
| "AI-generated code is probably fine" | AI code needs *more* scrutiny — confident but wrong |
| "Tests pass, so it's good" | Tests don't catch arch/security/readability issues |
| "It's only a version bump" | A bump is a behavior change you didn't write |
| "Style matters too" | Style doesn't cause incidents. Bugs do. |

## Verification
- [ ] All Critical issues resolved
- [ ] All Required (no-prefix) changes resolved or explicitly deferred with justification
- [ ] Tests pass, build succeeds
- [ ] Verification story documented
- [ ] Every finding has file:line + evidence
- [ ] Verdict given: **Approve** or **Request changes**
