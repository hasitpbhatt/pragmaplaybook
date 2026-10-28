# pragmaplaybook

**Succinct, powerful, drop-in.** A collection of agent skills and playbooks for interviews, PR reviews, and learning — load any skill into your AI agent and it enforces the same discipline a senior engineer would.

## What's inside

```
skills/         → Agent-loadable SKILL.md files (drop this repo into your agent)
playbooks/      → Human-readable cheat sheets
references/     → Shared checklists skills pull into context
```

## Quick start

```bash
# OpenCode / Claude Code / Cursor / any agent that supports the Agent Skills standard
npx skills add <your-github>/pragmaplaybook
```

Or just point your agent at a single skill:

```
Load skills/pr-review/SKILL.md before reviewing this PR.
```

## Skills

| Skill | Use when |
|---|---|
| `pr-review` | Before merging any change — enforces accuracy → scalability → security → style |
| `system-design` | Technical interview — 6-step framework + trade-off matrix |
| `coding-interview` | DSA + behavioral interview coach (STAR, complexity, honesty gates) |
| `learning` | Turn notes into durable knowledge (spaced repetition, Feynman) |

## Philosophy

- **One idea per file.** No fluff.
- **Process, not prose.** Every skill is a workflow with steps, gates, and exit criteria.
- **Anti-rationalization.** Each skill lists the excuses agents use to skip steps, with rebuttals.
- **Verification is non-negotiable.** "Seems right" is never sufficient.

## License

MIT
