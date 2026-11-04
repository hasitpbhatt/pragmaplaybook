---
name: incident-response
description: Triage and resolve production incidents. Use during on-call, when an alert fires, when a service degrades, or when writing a postmortem. Use for debugging production issues and blameless root-cause analysis.
---

# Incident Response

## Overview
Incidents are won or lost in the first 10 minutes. **Mitigate first, investigate second.** The goal is restoring service, not finding the perfect root cause live. Root cause comes in the postmortem.

## When to Use
- An alert fires or a user reports degradation
- A deploy caused unexpected behavior
- Writing a postmortem / RCA
- Any on-call shift

## Process

### Step 1: Triage (2 min)
- What's broken? Who's affected? Since when?
- Severity: is revenue/data/safety at risk? Page if yes.
- Assign incident commander; open a channel; start a timeline.

### Step 2: Mitigate (5 min)
- Prefer rollback / feature flag off / traffic shift over debugging.
- If unknown cause, reduce blast radius: rate limit, shed load, failover.
- Never make untracked changes in prod; log every action with timestamp.

### Step 3: Communicate (ongoing)
- Status update every 15 min to stakeholders (impact + ETA + next step).
- Say "we don't know yet" rather than guessing.

### Step 4: Investigate (after mitigation)
- Reproduce in staging if possible; never experiment on prod without a plan.
- Narrow by: deploy diff, config change, dependency, traffic spike, data anomaly.
- Check: logs, metrics, traces, recent changes, dashboards.

### Step 5: Resolve & verify
- Confirm recovery via metrics, not just "feels better."
- Watch for 30 min post-recovery for recurrence.

### Step 6: Postmortem (within 5 business days)
- Blameless: focus on systems, not people.
- Timeline, root cause, contributing factors, action items with owners + dates.
- Action items must be tracked issues, not promises.

## Red Flags
- Debugging before mitigating
- Untracked prod changes
- "It's probably fine" without metrics
- Postmortem with no action items
- Blaming a person instead of a system
- Skipping the timeline

## Rationalizations

| Excuse | Reality |
|---|---|
| "I'll just fix it live" | Untracked changes create new incidents. |
| "Rollback is too slow" | Debugging live is slower and riskier. |
| "Postmortem is bureaucracy" | Untracked fixes recur. |
| "We know who caused it" | Systems fail; people don't. |

## Verification
- [ ] Service restored; metrics confirm recovery
- [ ] Timeline documented with timestamps
- [ ] Root cause identified (or explicitly unknown with follow-up)
- [ ] Postmortem filed with tracked action items
- [ ] Monitoring/alerts improved to catch recurrence earlier