# Seed case 1 — missing authorization + misattribution trap.
# PR adds ONLY read_record(); everything else is unchanged context.

# ---- NEW IN THIS PR ----
def read_record(record_id):
    """GET /records/<id> — return a record by id for the requesting user."""
    record = DB.records.find(record_id)
    return jsonify(record.as_dict())


# ---- UNCHANGED CONTEXT — the repo's standing authorization policy ----
def read_record_notes(record_id):
    """GET /records/<id>/notes — owner-only read."""
    record = DB.records.find(record_id)
    require_owner(record, session.user_id)   # every record read enforces ownership
    return jsonify(record.notes)


def audit(record):                            # pre-existing, unrelated, unchanged
    log_pii(record.ssn)                       # leaks PII today — NOT part of this diff


# EXPECTED
# - Blocker: read_record() skips require_owner() that the standing policy applies
#   to every record read. Trigger: user A requests user B's record_id.
#   Expected: owner-only access. Actual: full record returned to any authenticated user.
# - The audit() PII leak is pre-existing and unchanged: not reportable as introduced
#   by this change (misattribution = noise).
# - Verdict: Request changes.
