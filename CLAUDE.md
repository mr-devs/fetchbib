# CLAUDE.md

This document describes the coding principles and conventions for the `fetchbib` project.

## Project Overview

`fetchbib` is a CLI tool that resolves DOIs and search queries into formatted BibTeX entries. The main entry point is `fbib`.

## Development Setup

```bash
uv sync        # Install dependencies (prefer uv over pip)
uv run pytest  # Run tests
```

## Package Management

- **Use `uv` over `pip`** for all dependency management and script execution
- Dependencies are defined in `pyproject.toml`

## Testing

This project follows **test-driven development (TDD)**:

1. Write tests first, then implement the feature
2. Run tests frequently during development: `uv run pytest`
3. All new functionality should have corresponding tests

**Test organization:**
- Unit tests mock external dependencies (no network calls)
- Integration tests are marked with `@pytest.mark.integration` and excluded by default
- Run integration tests explicitly: `uv run pytest -m integration`
- Group tests by functionality using test classes (e.g., `TestInputParsing`, `TestErrorHandling`)

## Code Style

### Formatting

- Use **black** for code formatting
- Follow PEP 8 conventions

### Structure & Organization

- **src layout**: Package lives under `src/fetchbib/`
- **Single responsibility**: Each module has a focused purpose
  - `cli.py` - Argument parsing and main entry point
  - `resolver.py` - DOI resolution and Crossref API calls
  - `formatter.py` - BibTeX string formatting
  - `config.py` - User configuration persistence
- **Small, focused functions**: Each function does one thing well

### Type Hints

- Use return type annotations on all functions (e.g., `-> str`, `-> bool`)
- Use parameter type hints (e.g., `value: str`, `verbose: bool`)

### Documentation

- Every module starts with a docstring explaining its purpose
- Public functions have docstrings describing behavior and exceptions
- Use inline comments sparingly, only for non-obvious logic

### Error Handling

- Use custom exception classes for domain-specific errors (e.g., `ResolverError`)
- Validate arguments early with clear error messages
- Handle errors gracefully—one failure shouldn't stop processing of other inputs

### Simplicity

- Minimize dependencies (currently just `requests`)
- Prefer standard library where possible (`argparse`, `json`, `pathlib`)
- Avoid unnecessary abstractions

## CLI Conventions

- **stdout**: Only output results (BibTeX entries)
- **stderr**: All errors, warnings, and verbose/informational messages
- **Exit codes**:
  - `0` - Success
  - `1` - Runtime error (resolution failure, file not found, no inputs)
  - `2` - Argument error (invalid flag combinations, missing required args)

## Git Workflow

- Write clear, descriptive commit messages
- Do not mention Claude or AI assistance in commit messages
