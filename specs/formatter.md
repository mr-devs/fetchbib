# Phase 1: Formatter (`formatter.py`)

The raw BibTeX returned by servers is often a single, long line. The formatter must produce clean, readable output.

## Requirements

1. The entry header (e.g., `@article{key,`) stays on the first line.
2. Each field appears on its own line with 2-space indentation.
3. The closing brace `}` is on its own line with no indentation.
4. Fields are alphabetized (except the entry header line).
5. Trailing commas after the last field are removed.

**Parsing constraint:** Fields must be split by detecting top-level commas — commas that are *not* nested inside `{}`. A naive split on `,` will break author names like `{Last, First and Last2, First2}`.

## Test Cases (`test_formatter.py`)

### Test 1 — Single-line BibTeX is formatted correctly

Input:
```
@article{Eysenbach2011,doi={10.2196/jmir.1933},title={Can Tweets Predict Citations?},author={Eysenbach, Gunther},year={2011},journal={JMIR}}
```

Expected output:
```
@article{Eysenbach2011,
  author = {Eysenbach, Gunther},
  doi = {10.2196/jmir.1933},
  journal = {JMIR},
  title = {Can Tweets Predict Citations?},
  year = {2011}
}
```

Fields are alphabetized, 2-space indented, and the closing brace is on its own line.

### Test 2 — Already-formatted BibTeX is unchanged

Passing already-clean BibTeX through the formatter should return identical output (idempotency).

### Test 3 — Author names with commas are preserved

Input containing `author={Last, First and Last2, First2}` must not be split across lines at the internal commas.

### Test 4 — Trailing comma is removed

Input where the last field before `}` has a trailing comma should have that comma stripped.

### Test 5 — Nested braces in field values are preserved

Input containing `title={A {GPU}-Accelerated Approach}` must not break on the inner braces.
