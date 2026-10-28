# Seed case 3 — behavioral regression: error semantics changed, caller not updated.

def parse_date(s):
    """BEFORE this PR: returned None on unparseable input.
    THIS PR: raises ValueError instead — the None fallback was removed."""
    ...

def validate_form(raw):                 # existing caller, NOT updated in this PR
    when = parse_date(raw.get("when"))
    if when is None:                    # still expects the removed None sentinel
        return "invalid date"           # now unreachable on bad input
    return book(when)                   # ValueError escapes to the HTTP layer


# EXPECTED
# - Required: regression — validate_form() branches on the removed None sentinel.
#   Trigger: malformed `when` input. Expected: user-facing "invalid date".
#   Actual: unhandled exception surfaces as a 500.
# - Missing: caller migration and a regression test for the original failure mode.
# - Verdict: Request changes.
