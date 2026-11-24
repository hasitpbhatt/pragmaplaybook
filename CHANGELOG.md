# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `VERSION` and `CHANGELOG.md`, so the released version is discoverable from the repo root
- `run_tests.py` checks that each calibration case is parseable and states its criteria, exiting non-zero otherwise

### Changed
- README's What's-inside block now lists `CHANGELOG.md` and `VERSION`

### Fixed
- Trailing whitespace in `run_tests.py` that broke `git diff --check`
- Stray tool-output text at the end of `tests/pr-review.md`
- Stale commit reference in `TEST_RESULTS.md`

### Notes
- The six pr-review calibration cases were executed against a reviewer with the skill loaded and all six passed; `TEST_RESULTS.md` records the results.

## [1.0.0] - TBD

### Added
- First versioned release of the skill collection

### Notes
- No automated CI; validation is manual (YAML frontmatter, six sections in order, line count <= 200)
- Calibration tests in tests/pr-review.md were executed against a skill-loaded reviewer: 6/6 pass (see TEST_RESULTS.md)
- Version tagging policy: tags will follow semver; breaking changes to skill interfaces (heading names, frontmatter fields) will bump major