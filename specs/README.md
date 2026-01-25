# fetchbib — Development Specs

`fetchbib` is a CLI-based bibliography management tool that resolves DOIs or free-text search queries into pretty-printed BibTeX entries.

**Core Command:** `fbib`

## Development Order (Test-Driven)

Follow this order strictly. For each phase: **write the tests first**, verify they fail, then implement until they pass.

| Phase | Spec File | Source File | Why This Order |
|-------|-----------|-------------|----------------|
| 1 | [formatter.md](formatter.md) | `formatter.py` | Pure string manipulation, no dependencies |
| 2 | [resolver.md](resolver.md) | `resolver.py` | Depends on `requests`; all unit tests use mocked HTTP |
| 3 | [cli.md](cli.md) | `cli.py` | Depends on formatter and resolver; tests mock the resolver |
| 4 | [integration.md](integration.md) | `test_integration.py` | Live API tests, opt-in only |

Infrastructure and build configuration are in [packaging.md](packaging.md).

## Spec File Conventions

- Each module spec contains **requirements** followed by **test cases**.
- Test cases describe inputs, expected outputs, and the behavior to assert.
- Cross-module references (e.g., `ResolverError` in the CLI spec) point back to the defining spec rather than duplicating the definition.
