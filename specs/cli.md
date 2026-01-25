# Phase 3: CLI (`cli.py`)

## Interface

```
fbib [input1] [input2] ...
fbib "doi1, doi2"
fbib --file list.txt
fbib --output refs.bib [inputs...]
fbib --append --output refs.bib [inputs...]
fbib -v [inputs...]
fbib --config-email user@example.com
```

## Argument Parsing

- `inputs` — Zero or more positional arguments. Each may be a DOI or search query.
- `--file` / `-f` — Path to a text file with one input per line. Blank lines are skipped.
- `--output` / `-o` — Path to an output file. Results are written to this file instead of stdout. **Overwrites** by default.
- `--append` / `-a` — Used with `--output`. Appends results to the file instead of overwriting. Ignored if `--output` is not provided.
- `--verbose` / `-v` — When a search query is used, print `Searching for: "{query}" -> DOI: {doi}` to stderr before printing the BibTeX.
- `--config-email` — Set the email used in the User-Agent header for Crossref API requests. The value is persisted to `~/.config/fetchbib/config.json`. When this flag is provided, the email is saved and the program exits (no resolution is performed). See [resolver.md](resolver.md) for how the email is consumed.

## Input Processing

1. Collect inputs from positional args, splitting any comma-separated values.
2. If `--file` is provided, read additional inputs from the file (one per line, stripping whitespace, skipping blank lines).
3. Deduplicate inputs (preserve first-occurrence order).
4. For each unique input, resolve and format the BibTeX. Print each entry separated by a blank line.

## Error Handling

- If `--file` points to a nonexistent file, print an error message to stderr and exit with code 1.
- If resolution fails for a given input, print the error to stderr, skip that input, and continue processing the rest. Exit with code 1 if any input failed.
- If no inputs are provided (no positional args and no `--file`), print a usage hint to stderr and exit with code 1.

`ResolverError` is defined in `resolver.py` — see [resolver.md](resolver.md).

## Test Cases (`test_cli.py`)

All tests mock `resolver.resolve` to avoid network calls.

### Test 1 — Single positional DOI

Run with a single DOI argument. Verify `resolve` is called once and formatted output is printed to stdout.

### Test 2 — Multiple positional arguments

Run with two arguments. Verify `resolve` is called twice and both entries appear in stdout separated by a blank line.

### Test 3 — Comma-separated string is split

Run with `"10.2196/jmir.1933, 10.1000/xyz123"`. Verify `resolve` is called twice with each DOI (stripped of whitespace).

### Test 4 — File input reads lines

Create a temporary file with two DOIs (one per line) and a blank line. Run with `--file`. Verify `resolve` is called twice (blank line skipped).

### Test 5 — Nonexistent file exits with code 1

Run with `--file nonexistent.txt`. Verify exit code is 1 and stderr contains an error message.

### Test 6 — Duplicate inputs are deduplicated

Run with the same DOI passed twice. Verify `resolve` is called only once.

### Test 7 — Verbose mode prints search info to stderr

Mock `resolver.search_crossref` and `resolver.resolve_doi` separately. Run with a non-DOI query and `-v`. Verify stderr contains the search-to-DOI mapping.

### Test 8 — Output flag writes to file (overwrite by default)

Run with `--output tmp.bib`. Verify the file is created with the formatted BibTeX and nothing is printed to stdout. Run again with different input — verify the file contains only the new output (overwritten, not appended).

### Test 8b — Append flag appends to file

Create a file with existing content. Run with `--output tmp.bib --append`. Verify the existing content is preserved and the new BibTeX is appended after it.

### Test 9 — Resolution error for one input does not stop others

Mock `resolve` to raise `ResolverError` for the first input and return BibTeX for the second. Verify the second entry still appears in stdout, the error is printed to stderr, and exit code is 1.

### Test 10 — No inputs prints usage hint and exits 1

Run with no arguments and no `--file`. Verify exit code is 1 and stderr contains a usage message.

### Test 11 — Config-email saves email and exits

Run with `--config-email user@example.com`. Verify the config file is written to the expected path and the program exits with code 0 without performing any resolution.

### Test 12 — Config-email is read by resolver

Set a config file with a custom email. Run a resolution. Verify the User-Agent header uses the custom email instead of the default.
