# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.6.1] - 2026-03-15

### Changed

- Updated CLI help text example for `--search` to use a more realistic query

## [0.6.0] - 2026-01-30

### Fixed

- arXiv DOIs from search results now correctly route to arxiv.org (previously failed with HTML response)
- Commas in search queries are now preserved (e.g., "Smith, John 2024" no longer splits into two queries)
- DOI and DOI URL forms are now deduplicated (e.g., `10.1234/x` and `https://doi.org/10.1234/x`)
- arXiv DOIs with different casing are now deduplicated (e.g., `arXiv` vs `arxiv`)
- Invalid BibTeX responses (e.g., HTML from Zenodo) now show a warning instead of crashing
- Exit code is now 1 when all search results fail to resolve

### Changed

- Internal refactoring: introduced `BibTeXEntry` dataclass for cleaner BibTeX manipulation
- Internal refactoring: consolidated resolution logic into `resolve_to_bibtex()` function

## [0.5.0] - 2026-01-29

### Changed

- Switched from Crossref to OpenAlex API for free-text search
- Replaced `--config-email` with `--config-api-key` for OpenAlex API key
- API key warning now shows only once per session (instead of on every search)
- Improved error message when results exist but none have DOIs

### Added

- Support for `OPENALEX_API_KEY` environment variable (takes precedence over config file)

## [0.4.0] - 2026-01-25

### Added

- `--config-exclude-issn` flag to toggle exclusion of ISSN from BibTeX entries
- `--config-exclude-doi` flag to toggle exclusion of DOI from BibTeX entries (already included in URL)

## [0.3.0] - 2025-01-25

### Added

- arXiv DOI support: DOIs starting with `10.48550/arXiv.*` are now routed to arxiv.org's BibTeX endpoint
- `--config-protect-titles` flag to toggle double-bracing of titles (preserves capitalization in BibTeX)
- Confirmation messages when changing config settings

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
