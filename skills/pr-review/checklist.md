# PR Review Checklist (condensed)

## Context
- [ ] I understand what this change does and why

## Correctness
- [ ] Matches spec/task requirements
- [ ] Edge cases handled (null, empty, boundary)
- [ ] Error paths handled, not just happy path
- [ ] Tests cover the change adequately

## Scalability
- [ ] No N+1 query patterns
- [ ] No unbounded loops/unconstrained fetches
- [ ] Pagination on list endpoints
- [ ] No sync ops that should be async

## Security
- [ ] No secrets in code/logs
- [ ] Input validated at boundaries
- [ ] No injection (SQL/XSS/command)
- [ ] Auth checks in place
- [ ] External data treated as untrusted

## Performance
- [ ] No unnecessary re-renders
- [ ] No large objects in hot paths
- [ ] No missing indexes

## Style
- [ ] Names clear and consistent
- [ ] Logic straightforward, no clever tricks
- [ ] No dead code
- [ ] File stays within healthy size

## Verification
- [ ] Tests pass / Build succeeds / Manual verification done

## Verdict
- [ ] **Approve** — Ready to merge
- [ ] **Request changes** — Issues must be addressed
