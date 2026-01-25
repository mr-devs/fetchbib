# Phase 2: Resolver (`resolver.py`)

## Public Interface

- `is_doi(input: str) -> bool` — Returns `True` if the input matches the DOI pattern.
- `resolve_doi(doi: str) -> str` — Fetches BibTeX from `https://doi.org/{doi}` with header `{"Accept": "text/bibliography; style=bibtex"}`. Returns the raw BibTeX string.
- `search_crossref(query: str) -> str` — Queries `https://api.crossref.org/works?query={query}`, extracts the DOI from the first result, and returns it.
- `resolve(input: str) -> str` — Orchestrator: if input is a DOI, calls `resolve_doi`; otherwise calls `search_crossref` then `resolve_doi`.

## DOI Regex

```python
DOI_PATTERN = re.compile(r'^10\.\d{4,9}/[-._;()/:A-Z0-9]+$', re.IGNORECASE)
```

Note the escaped `\.` — the original spec had an unescaped `.` which would match any character.

## User-Agent

All HTTP requests must include the header:

```
User-Agent: fetchbib/1.0 (mailto:<email>)
```

The email is resolved in this order:
1. Custom email from the config file (`~/.config/fetchbib/config.json`), set via `fbib --config-email`.
2. Default: `fetchbib@example.com`.

The resolver exposes a `get_user_agent() -> str` function that reads the config and returns the full User-Agent string. Config file reading is handled by a `config.py` module — see [packaging.md](packaging.md) for the directory structure.

## Error Handling

`ResolverError` is a custom exception defined in this module.

- `resolve_doi`: If the response status is not 200, raise `ResolverError` with the HTTP status code and DOI.
- `search_crossref`: If the response status is not 200, or if `message.items` is empty, raise `ResolverError` with a descriptive message.

## Test Cases (`test_resolver.py`)

All tests use `unittest.mock.patch` to mock `requests.get`.

### Test 1 — `is_doi` recognizes valid DOIs

- `10.2196/jmir.1933` -> `True`
- `10.1000/xyz123` -> `True`
- `not a doi` -> `False`
- `10.12345` (no suffix) -> `False`

### Test 2 — `is_doi` rejects invalid inputs

- Empty string -> `False`
- `http://doi.org/10.2196/jmir.1933` (full URL, not bare DOI) -> `False`

### Test 3 — `resolve_doi` returns BibTeX on success

Mock `requests.get` to return a 200 response with a BibTeX string body. Verify the function returns that string and that the request was made with the correct Accept header and User-Agent.

### Test 4 — `resolve_doi` raises `ResolverError` on HTTP failure

Mock a 404 response. Verify `ResolverError` is raised and the message includes the status code and DOI.

### Test 5 — `search_crossref` extracts DOI from first result

Mock a 200 Crossref JSON response with a `message.items` list. Verify the function returns the DOI from the first item.

### Test 6 — `search_crossref` raises `ResolverError` on empty results

Mock a 200 response where `message.items` is an empty list. Verify `ResolverError` is raised.

### Test 7 — `search_crossref` raises `ResolverError` on HTTP failure

Mock a 503 response. Verify `ResolverError` is raised.

### Test 8 — `resolve` routes DOIs directly

Mock `resolve_doi`. Pass a DOI string. Verify `resolve_doi` is called and `search_crossref` is not.

### Test 9 — `resolve` routes non-DOIs through search

Mock both `search_crossref` and `resolve_doi`. Pass a free-text string. Verify `search_crossref` is called first, then `resolve_doi` with the returned DOI.
