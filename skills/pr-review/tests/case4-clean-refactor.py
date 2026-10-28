# Seed case 4 — clean, behavior-preserving refactor. Noise trap: looks reviewable, isn't.

class Checkout:
    def _compute_price(self, price, rule):
        # extracted verbatim from the old apply_rule_discount body (mechanical move)
        ...

    def apply_rule_discount(self, item):
        # behavior preserved: delegates to _compute_price; logic AST-identical
        return self._compute_price(item.price, item.rule)


# tests updated in this same PR (unit + integration renamed accordingly)

# EXPECTED
# - No defect findings. Naming choice is the author's (a tie defers to the author).
# - Zero speculative findings — no invented perf/concurrency/style concerns.
# - Verdict: Approve.
