#!/usr/bin/env bash
set -euo pipefail

# Clean previous builds
rm -rf dist/ build/ src/*.egg-info

# Build
uv build

# Upload (use --publish-url for TestPyPI dry runs)
if [[ "${1:-}" == "--test" ]]; then
    uv publish --publish-url https://test.pypi.org/legacy/
else
    uv publish
fi
