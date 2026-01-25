#!/usr/bin/env bash
set -euo pipefail

# Clean previous builds
rm -rf dist/ build/ src/*.egg-info

# Build
uv build

# Upload to PyPI
uv publish
