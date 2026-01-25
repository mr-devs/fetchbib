# Phase 4: Integration Tests (`test_integration.py`)

These tests hit live APIs and are **not run by default**. Run them with:

```
pytest -m integration
```

All integration tests should be decorated with `@pytest.mark.integration`.

The `integration` marker is registered and excluded from the default test run in `pyproject.toml` — see [packaging.md](packaging.md).

## Test Cases

### Test 1 — DOI resolution end-to-end

Resolve `10.2196/jmir.1933`. Verify the output contains `Eysenbach` and `2011`.

### Test 2 — Free-text search end-to-end

Search `"Eysenbach JMIR 2011"`. Verify the output contains `Eysenbach`.

### Test 3 — File input end-to-end

Write a temp file with `10.2196/jmir.1933` and run through the CLI. Verify BibTeX output.
