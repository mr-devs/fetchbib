# Packaging & Infrastructure

## Directory Structure

```text
fetchbib/
├── src/
│   └── fetchbib/
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py       # Config file read/write (~/.config/fetchbib/config.json)
│       ├── formatter.py
│       └── resolver.py
├── tests/
│   ├── test_formatter.py
│   ├── test_resolver.py
│   ├── test_cli.py
│   └── test_integration.py
├── specs/
│   ├── README.md
│   ├── formatter.md
│   ├── resolver.md
│   ├── cli.md
│   ├── integration.md
│   └── packaging.md
├── pyproject.toml
├── publish.sh
└── README.md
```

## `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=68.0", "setuptools-scm"]
build-backend = "setuptools.build_meta"

[project]
name = "fetchbib"
version = "0.1.0"
description = "Resolve DOIs and search queries into formatted BibTeX entries."
requires-python = ">=3.9"
dependencies = ["requests"]

[project.scripts]
fbib = "fetchbib.cli:main"

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
markers = ["integration: tests that hit live APIs (deselect with '-m not integration')"]
addopts = "-m 'not integration'"
```

Key points:
- `[tool.setuptools.packages.find] where = ["src"]` tells setuptools to find packages under the `src/` directory.
- The `integration` pytest marker is registered so `pytest` won't emit warnings, and `addopts` excludes integration tests from the default run.

## Deployment Script (`publish.sh`)

```bash
#!/usr/bin/env bash
set -euo pipefail

# Clean previous builds
rm -rf dist/ build/ src/*.egg-info

# Install/upgrade build tools
python3 -m pip install --upgrade build twine

# Build
python3 -m build

# Upload (use --repository testpypi for dry runs)
if [[ "${1:-}" == "--test" ]]; then
    python3 -m twine upload --repository testpypi dist/*
else
    python3 -m twine upload dist/*
fi
```

- `set -euo pipefail` ensures the script stops on any error.
- Old `dist/` and `build/` artifacts are cleaned before building.
- Pass `--test` to upload to TestPyPI instead of production PyPI.
