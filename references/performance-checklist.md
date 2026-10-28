# Performance Checklist

## Targets
- Core Web Vitals: LCP < 2.5s, INP < 200ms, CLS < 0.1
- API p99 < 200ms (read), < 500ms (write)

## Check
- [ ] No N+1 query patterns
- [ ] No unbounded loops/unconstrained fetches
- [ ] Pagination on list endpoints
- [ ] No sync ops that should be async
- [ ] No unnecessary re-renders
- [ ] No large objects in hot paths
- [ ] Indexes on filtered/sorted columns
- [ ] Caching where read-heavy
