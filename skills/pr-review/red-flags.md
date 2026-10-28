# PR Review Red Flags

Auto-fail patterns — if you see any, block merge:

- PR merged without any review
- Review that only checks if tests pass
- "LGTM" without evidence of actual review
- Security-sensitive changes without security-focused review
- Large PRs "too big to review properly" (split them)
- No regression tests with bug fix PRs
- Review comments without severity labels
- Accepting "I'll fix it later" (it never happens)
- A refactor that relocates complexity instead of reducing it
- A change that grows an already-large file instead of decomposing it
- New conditionals scattered into unrelated code paths (missing abstraction)
- A bespoke helper duplicating an existing canonical one
- A bulk "bump dependencies" PR with no changelog review
- A lockfile change that's hand-edited or unreviewed
- Feature logic leaking into a shared module
- Silent fallbacks hiding an unclear invariant
