# pragmaplaybook

**Succinct, powerful, drop-in.** A collection of agent skills and playbooks for interviews, PR reviews, learning, incident response, and running a solo company — load any skill into your AI agent and it enforces the same discipline a senior engineer would.

## What's inside

```
skills/         → Agent-loadable SKILL.md files (drop this repo into your agent)
AGENTS.md       → Router that tells an agent which skill to load, and when
```

That's it. Every skill is a single `SKILL.md` with YAML frontmatter (`name`, `description`), so any host implementing the Agent Skills standard picks them up with no adapter.

## Quick start

Install the whole collection (Claude Code, Cursor, OpenCode, Copilot CLI, …):

```bash
npx skills add hasitpbhatt/pragmaplaybook
```

Or load one skill on demand — this fallback works in any agent, including ones with no install command:

```
Load skills/pr-review/SKILL.md before reviewing this PR.
```

Or let the agent self-select: drop `AGENTS.md` in your repo root and it routes each situation to the right skill.

To pin a version, install a tag (`npx skills add hasitpbhatt/pragmaplaybook@v1.0.0`) or copy the files you want into your own repo.

## Skills

All skills live under `skills/<name>/SKILL.md`.

| Skill | Use when |
|---|---|
| `pr-review` | Before merging any change — enforces accuracy → scalability → security → style |
| `system-design` | Technical interview — 6-step framework + trade-off matrix |
| `coding-interview` | DSA + behavioral interview coach (STAR, complexity, honesty gates) |
| `learning` | Turn notes into durable knowledge (spaced repetition, Feynman) |
| `incident-response` | Production incidents, on-call, postmortem |
| `wayfinder` | Plan huge, multi-session work as a map of decision tickets |
| `tdd` | Red-green-refactor TDD with vertical slices |
| `debug` | Disciplined debug loop (feedback → hypothesise → fix) |
| `grill` | Relentless interview to stress-test a plan or idea |
| `retro` | Post-session improvements to the agent's environment |

## Using these in your own repo

1. Install, or copy `skills/` and `AGENTS.md` in.
2. Keep `AGENTS.md` — it's the routing table. Without it the agent won't know the skills exist.
3. Skills are read-only guidance: nothing here executes code, and no skill requires network access.

## Philosophy

- **One idea per file.** No fluff.
- **Process, not prose.** Every skill is a workflow with steps, gates, and exit criteria.
- **Anti-rationalization.** Each skill lists the excuses agents use to skip steps, with rebuttals.
- **Verification is non-negotiable.** "Seems right" is never sufficient.

## Contributing

Every skill must include Overview, When to Use, Process, Rationalizations, Red Flags, and Verification. If a `SKILL.md` exceeds ~200 lines, split it. Prefer deletion over addition: a skill that removes complexity beats one that adds it. No skill merges without a Verification section.

## Third-party skills

`skills-lock.json` and any skill it references are local install state, not part of this repo. They're gitignored so consumers don't inherit unrelated skills. Third-party skills keep their own licenses — this repo's MIT covers only the skills listed above.

## License

MIT
