## Description

Brief summary of changes. Link related issue if applicable.

## Type of Change

- [ ] New skill (`skills/<name>/SKILL.md`)
- [ ] Skill enhancement (edit existing `SKILL.md`)
- [ ] Framework change (`AGENTS.md`, `README.md`, tooling)
- [ ] Documentation only
- [ ] Test case addition (`tests/`)

## Checklist

### For New/Modified Skills

- [ ] Frontmatter has `name` and `description`
- [ ] All six sections present in order: Overview, When to Use, Process, Rationalizations, Red Flags, Verification
- [ ] Line count under ~200 (or split into multiple skills)
- [ ] "When to Use" lists actionable trigger phrases
- [ ] "Verification" is a runnable checklist (not prose)
- [ ] No executable code, secrets, or network calls in the skill

### For All Changes

- [ ] `AGENTS.md` updated with routing line (if new skill or trigger changed)
- [ ] `README.md` skill table updated (if new skill)
- [ ] Calibration tests added/updated in `tests/` (if applicable)
- [ ] `python run_tests.py` passes
- [ ] `CHANGELOG.md` updated (Keep a Changelog format)

## Testing

Describe how you validated.

## Additional Notes

Anything else reviewers should know?
