# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-01-25

### Added

- `-n`/`--max-results` flag to control number of results for free-text searches (1-100, default: 1)
- Graceful handling of individual DOI failures within free-text searches
- Warning messages for failed DOIs include a URL to try manually

### Removed

- `-v`/`--verbose` flag (not useful in practice)

### Changed

- `search_crossref()` now returns a list of DOIs instead of a single DOI

## [0.1.0] - 2025-01-24

### Added

- Initial release
- DOI resolution via doi.org
- Free-text search via Crossref API
- BibTeX formatting
- File input (`--file`) and output (`--output`, `--append`)
- Configurable email for API requests (`--config-email`)
