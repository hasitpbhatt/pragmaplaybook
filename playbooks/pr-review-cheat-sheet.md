# PR Review Cheat Sheet

**Before merging: accuracy → scalability → security → performance → style.**

## 30-second triage
1. What does this change do? (read description + tests first)
2. Does it match spec?
3. Any security-sensitive code touched? (auth, input, secrets, queries)

## Severity labels
- (none) = required
- `Critical:` = blocks merge
- `Nit:` = optional
- `Optional:`/`Consider:` = suggestion
- `FYI` = info only

## Size limits
- ~100 lines = good
- ~300 = acceptable (single logical change)
- ~1000 = split it

## Auto-fail
No review / "LGTM" only / no regression test on bug fix / accepting "fix later" / bulk dep bump with no changelog review
