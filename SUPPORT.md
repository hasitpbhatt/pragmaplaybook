# Support

## Getting Help

| Channel | Best For |
|---------|----------|
| [GitHub Discussions](https://github.com/hasitpbhatt/pragmaplaybook/discussions) | Questions, ideas, showing off what you built |
| [GitHub Issues](https://github.com/hasitpbhatt/pragmaplaybook/issues) | Bug reports, skill requests, documentation fixes |
| Email: hasit.p.bhatt@gmail.com | Security concerns (see [SECURITY.md](SECURITY.md)) |

## Before You Ask

1. Check existing issues/discussions.
2. Read the skill — each `SKILL.md` is self-contained.
3. Try the one-liner: `Load skills/<name>/SKILL.md, then <your task>`.

## Common Questions

### "How do I use a skill?"

Any agent: `Load skills/pr-review/SKILL.md before reviewing this PR.`

OpenCode: also works via `opencode.json` `skills` array or `@skill-name` mention.

GitHub Copilot CLI: install the plugin:
```bash
copilot plugin marketplace add hasitpbhatt/pragmaplaybook
copilot plugin install pragmaplaybook-skills@pragmaplaybook
```

### "Can I modify a skill?"

Yes. Copy `skills/<name>/SKILL.md` to your project and edit.

### "A skill gave bad advice"

Open an issue with which skill, what you asked, what it said, what you expected.

### "I want a new skill"

Open a discussion or issue.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
