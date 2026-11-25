# Support

## Getting Help

| Channel | Best For |
|---------|----------|
| [GitHub Discussions](https://github.com/hasitpbhatt/pragmaplaybook/discussions) | Questions, ideas, showing off what you built |
| [GitHub Issues](https://github.com/hasitpbhatt/pragmaplaybook/issues) | Bug reports, skill requests, documentation fixes |
| Email: hasit.p.bhatt@gmail.com | Security concerns (see [SECURITY.md](SECURITY.md)) |

## Before You Ask

1. **Check existing issues/discussions** — your question may be answered
2. **Read the skill** — each `SKILL.md` is self-contained; the answer is often in the "When to Use" or "Process" sections
3. **Try the one-liner** — most skills work with just: `Load skills/<name>/SKILL.md, then <your task>`

## Common Questions

### "How do I use a skill?"

**Any agent** (Claude Code, Cursor, Copilot, OpenCode, Continue, etc.):
```
Load skills/pr-review/SKILL.md before reviewing this PR.
```

**OpenCode**: Also works via `opencode.json` `skills` array or `@skill-name` mention.

**GitHub Copilot CLI**: Install the plugin:
```bash
copilot plugin marketplace add hasitpbhatt/pragmaplaybook
copilot plugin install pragmaplaybook-skills@pragmaplaybook
```

### "Can I modify a skill?"

Yes! Copy `skills/<name>/SKILL.md` to your project and edit. Skills are meant to be adapted. The originals stay here as references.

### "A skill gave bad advice"

Open an issue with:
- Which skill
- What you asked
- What it said
- What you expected

Include the skill's "Verification" checklist results if you ran them.

### "I want a new skill"

Open a discussion or issue. We'll help you design it to fit the project's standards (six sections, ~200 lines, verification checklist).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add skills, fix bugs, or improve docs.