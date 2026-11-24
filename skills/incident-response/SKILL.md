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
- If a mitigation makes things worse, stop and revert. Do not stack fixes on a broken mitigation.
- Safety- or data-loss incidents: pause and get sign-off before rollback; a bad rollback can compound the loss.

### Step 3: Communicate (ongoing)
- Status update every 15 min to stakeholders (impact + ETA + next step).
- Say "we don't know yet" rather than guessing.

### Step 4: Investigate (after mitigation)
- Reproduce in staging if possible; never experiment on prod without a plan.
- Narrow by: deploy diff, config change, dependency, traffic spike, data anomaly.
- Check: logs, metrics, traces, recent changes, dashboards.
- Diagnosis loop (when reproducible): signal that goes red on the bug → minimise the repro → hypothesise → instrument to confirm → fix. If you cannot reproduce, narrow by evidence instead: diff good vs. bad time windows, compare configs, review deploy history.
- Never change prod to "see what happens."

### Step 5: Resolve & verify
- Confirm recovery via metrics, not just "feels better."
- Watch for 30 min post-recovery for recurrence.

### Step 6: Postmortem (within 5 business days)
- Blameless: focus on systems, not people.
- Timeline, root cause, contributing factors, action items with owners + dates.
- Action items must be tracked issues, not promises.
- Regression tests and config hardening go here, not in the live incident loop.

## Rationalizations

| Excuse | Reality |
|---|---|
| "I'll just fix it live" | Untracked changes create new incidents. |
| "Rollback is too slow" | Debugging live is slower and riskier. |
| "Postmortem is bureaucracy" | Untracked fixes recur. |
| "We know who caused it" | Systems fail; people don't. |
| "We don't have time for a timeline" | Un-timestamped timelines block recurrence analysis and turn into blame guessing. |
| "Just restart/retry it" | Restart masks the cause and throws away the failing state and evidence. |

## Red Flags

- Debugging before mitigating
- Untracked prod changes
- "It's probably fine" without metrics
- Postmortem with no action items
- Blaming a person instead of a system
- Skipping the timeline

## Verification
- [ ] Service restored; metrics confirm recovery
- [ ] Mitigation controls (rate limit, flag, failover) removed or reviewed after recovery
- [ ] Timeline documented with timestamps
- [ ] Root cause identified (or explicitly unknown with follow-up)
- [ ] Postmortem filed with tracked action items
- [ ] No untracked prod changes made during the incident
- [ ] Monitoring/alerts improved to catch recurrence earlier