# Release Guide

Steps to publish a new version of `fetchbib` to PyPI.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) installed
- PyPI account with API token configured
- All tests passing

## Steps

### 1. Update Version Number

Edit `pyproject.toml` and bump the version following [Semantic Versioning](https://semver.org/):

```toml
[project]
version = "X.Y.Z"
```

- **MAJOR** (X): Breaking changes
- **MINOR** (Y): New features, backward compatible
- **PATCH** (Z): Bug fixes, backward compatible

### 2. Update Changelog

Add a new section to `CHANGELOG.md`:

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added

- New features

### Changed

- Changes to existing features

### Fixed

- Bug fixes

### Removed

- Removed features
```

### 3. Run Tests

```bash
uv run pytest
uv run pytest -m integration
```

### 4. Build and Upload

Use the `publish.sh` script in the repo root:

```bash
./publish.sh
```

This script:

- Cleans previous builds (`dist/`, `build/`, `*.egg-info`)
- Builds source and wheel distributions
- Uploads to PyPI

You'll be prompted for your PyPI API token (or set it as an environment variable `$UV_PUBLISH_TOKEN`).

### 5. Verify the Release

```bash
uv tool install --force fetchbib
uv tool list | grep fetchbib
```

### 6. Tag the Release (Optional)

```bash
git tag -a vX.Y.Z -m "Release vX.Y.Z"
git push origin vX.Y.Z
```

## PyPI API Token Setup

1. Go to https://pypi.org/manage/account/token/
2. Create a token scoped to the `fetchbib` project
3. Configure in `~/.pypirc`:

```ini
[pypi]
username = __token__
password = pypi-YOUR-TOKEN-HERE
```

Or set the environment variable:

```bash
export UV_PUBLISH_TOKEN=pypi-YOUR-TOKEN-HERE
```
