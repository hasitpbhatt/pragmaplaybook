# Security Checklist

- [ ] No secrets in code, logs, or version control
- [ ] Input validated and sanitized at boundaries
- [ ] Auth/authz checked where needed
- [ ] SQL queries parameterized (no string concat)
- [ ] Outputs encoded (XSS prevention)
- [ ] Dependencies from trusted sources, no known vulns
- [ ] External data (APIs, logs, user content, config) treated as untrusted
- [ ] External data flows validated at system boundaries before use
