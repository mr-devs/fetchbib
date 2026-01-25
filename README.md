# fetchbib

A command-line tool to resolve DOIs and free-text search queries into formatted BibTeX entries.
Powered by [doi.org](https://www.doi.org/) and the [Crossref API](https://api.crossref.org/).

## Installation

### `pip`

```bash
pip install fetchbib
```

### `uv`

```bash
uv tool install fetchbib
```

Requires Python 3.9+.

## Quick start

Fetch BibTeX by DOI (bare or full URL):

```bash
fbib 10.1073/pnas.2322823121
fbib https://doi.org/10.1073/pnas.2322823121
```

```bibtex
@article{DeVerna_2024,
  author = {DeVerna, Matthew R. and Yan, Harry Yaojun and Yang, Kai-Cheng and Menczer, Filippo},
  DOI = {10.1073/pnas.2322823121},
  ISSN = {1091-6490},
  journal = {Proceedings of the National Academy of Sciences},
  month = dec,
  number = {50},
  publisher = {Proceedings of the National Academy of Sciences},
  title = {Fact-checking information from large language models can decrease headline discernment},
  url = {http://dx.doi.org/10.1073/pnas.2322823121},
  volume = {121},
  year = {2024}
}
```

Search by free text:

```bash
fbib "DeVerna Fact-checking information from large language models"
```

## Usage

```
fbib [-h] [-f FILE] [-o OUTPUT] [-a] [-v] [--config-email EMAIL]
     [inputs ...]
```

### Flexible input

`fbib` accepts DOIs in any format — bare, full URL, or free-text search queries — and you can mix them freely.
Inputs are comma-separated, so all of the following work:

```bash
# Multiple positional arguments
fbib 10.1609/icwsm.v5i1.14126 10.1093/jcmc/zmz022

# Comma-separated string
fbib "10.1609/icwsm.v5i1.14126, 10.1093/jcmc/zmz022"

# Full DOI URLs
fbib "https://doi.org/10.1609/icwsm.v5i1.14126, https://doi.org/10.1093/jcmc/zmz022"

# Mix DOIs, URLs, and search queries
fbib 10.1609/icwsm.v5i1.14126 "DeVerna Fact-checking information from large language models"
```

From a file (`--file`), each line is treated the same way — one entry per line, or comma-separated on a single line:

```bash
fbib --file dois.txt
```

Duplicate inputs are automatically removed.

### Write to a file

Overwrite (default):

```bash
fbib --output refs.bib 10.1609/icwsm.v5i1.14126
```

Append to an existing `.bib` file:

```bash
fbib --append --output refs.bib 10.1093/jcmc/zmz022
```

### Verbose mode

See which DOI was matched when searching by free text:

```bash
fbib -v "DeVerna Fact-checking information from large language models"
# stderr: Searching for: "DeVerna Fact-checking information from large language models" -> DOI: 10.1073/pnas.2322823121
```

### Configure email (optional)

Crossref gives better rate limits to requests that include a contact email. Set yours once and it will be used for all future requests:

```bash
fbib --config-email you@example.com
```

The email is stored in `~/.config/fetchbib/config.json`. If not set, a default placeholder is used.

## Development

Clone the repo and sync dependencies with [uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/mr-devs/fetchbib.git
cd fetchbib
uv tool install -e . # OR pip install -e .
```

> The `-e` flag (`uv tool install -e .`), it performs an editable installation.
> This means any changes you make to the local source code are immediately reflected when you run the command, without needing to reinstall.

Run unit tests:

```bash
uv run pytest
```

Run integration tests (hits live APIs):

```bash
uv run pytest -m integration
```
