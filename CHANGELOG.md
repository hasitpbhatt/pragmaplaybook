# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial skill collection: pr-review, system-design, coding-interview, learning, incident-response, debug, tdd, grill, wayfinder, retro
- AGENTS.md router for self-selecting skills
- tests/pr-review.md calibration cases

### Changed
- Standardized YAML frontmatter quoting for skills with colons in descriptions (tdd, retro)
- Canonicalized section order across all skills: Overview, When to Use, Process, Rationalizations, Red Flags, Verification
- Renamed "Red Flags in the Change" heading to "Red Flags" in pr-review skill
- Clarified performance/scalability review bar wording in pr-review
- Folded retro's extra Rules section into Process
- Repaired README structure and claims (installer, versioning, Copilot config)

### Fixed
- Stray pipe corruption in README.md around line 13
- Section ordering in coding-interview, incident-response, learning, system-design

## [1.0.0] - TBD

### Added
- First versioned release of the skill collection

### Notes
- No automated CI; validation is manual (YAML frontmatter, six sections in order, line count <= 200)
- Calibration tests in tests/pr-review.md have not been executed against a skill-loaded reviewer
- Version tagging policy: tags will follow semver; breaking changes to skill interfaces (heading names, frontmatter fields) will bump major