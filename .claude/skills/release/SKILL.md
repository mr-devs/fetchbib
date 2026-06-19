---
name: release
description: Use when the user wants to release, publish, or ship a new version of fetchbib to PyPI, cut a release, or bump the package version.
disable-model-invocation: true
argument-hint: [major|minor|patch|X.Y.Z]
allowed-tools: Read Edit Grep Bash(uv run pytest*) Bash(uv build*) Bash(uv tool*) Bash(git status*) Bash(git diff*) Bash(git log*) Bash(git tag*) Bash(git add*) Bash(git commit*) Bash(cat*) Bash(grep*) Bash(rm -rf dist*)
---

# Release fetchbib to PyPI

Publish a new version of `fetchbib` to PyPI. This skill is the canonical release
process for the project. It is manual-only because it has irreversible,
outward-facing effects (a PyPI upload cannot be undone or reused, and a published
version number can never be republished).

`$ARGUMENTS` is the requested version: a bump type (`major`, `minor`, `patch`)
or an explicit `X.Y.Z`. If empty, infer the bump from the changes and confirm
with the user before proceeding.

## Instructions

### 1. Pre-flight checks (abort on any failure)

- **Clean tree**: run `git status --short`. If there are uncommitted changes,
  stop and report them — the release must be cut from a clean state.
- **On main**: confirm the current branch is `main` (`git rev-parse --abbrev-ref HEAD`).
  If not, ask the user whether to continue.
- **Tests green**: run both `uv run pytest` and `uv run pytest -m integration`.
  The integration tests hit live APIs and are deselected by default, so they
  must be run explicitly here. If anything fails, stop and report.

### 2. Determine the new version

- Read the current `version` from `pyproject.toml`.
- Resolve the target version from `$ARGUMENTS` (SemVer — MAJOR=breaking,
  MINOR=new feature/back-compat, PATCH=bug fix/back-compat):
  - `major` / `minor` / `patch` → bump the corresponding component.
  - An explicit `X.Y.Z` → use it verbatim (sanity-check it is greater than current).
  - Empty → review `git log <last-tag>..HEAD` to recommend a bump, then confirm.
- Verify the chosen version is not already a git tag (`git tag | grep "vX.Y.Z"`).

### 3. Update version and changelog

- Edit `pyproject.toml`: set `version = "X.Y.Z"`.
- Draft the `CHANGELOG.md` entry from the commits since the last tag
  (`git log <last-tag>..HEAD --oneline`). Add a new section at the top of the
  changelog list, following the existing Keep a Changelog format and today's date:

  ```markdown
  ## [X.Y.Z] - YYYY-MM-DD

  ### Added
  - ...

  ### Changed
  - ...

  ### Fixed
  - ...
  ```

  Only include subsections that have entries. Show the drafted entry to the user
  and let them edit before committing.

### 4. Commit the release prep

- Commit `pyproject.toml` and `CHANGELOG.md` together:
  `Release vX.Y.Z` (keep the message free of any AI-assistance mention, per the
  repo's git workflow). Do not push yet.

### 5. Build and publish (CONFIRMATION GATE)

This step is irreversible. **Stop and get explicit user confirmation** before
running it — show the version, the changelog entry, and the test results, then
ask the user to approve the upload.

After approval, run the bundled script from the repo root:
`./.claude/skills/release/publish.sh` (cleans `dist/`/`build/`/`*.egg-info`, runs
`uv build`, then `uv publish`). Run it from the repo root so the build operates on
the project's files. If you cannot run an interactive prompt, tell the user to run
it themselves via `! ./.claude/skills/release/publish.sh`.

If publishing fails on authentication, the PyPI token needs to be available —
tell the user to set `UV_PUBLISH_TOKEN=pypi-...` in the environment (or configure
`~/.pypirc`).

### 6. Verify the release

- `uv tool install --force fetchbib`
- `uv tool list | grep fetchbib` and confirm the new version is installed.
- Restore the local editable install so development reflects local changes again:
  `uv tool install -e .`

### 7. Tag and push

- `git tag -a vX.Y.Z -m "Release vX.Y.Z"`
- Confirm with the user, then push the branch and the tag:
  `git push && git push origin vX.Y.Z`.

## Notes

- There is currently no CI/CD; every step runs locally. If the user wants to
  automate this, suggest a release-on-tag GitHub Action using PyPI Trusted
  Publishing.
- Never skip the confirmation gate in step 5 or push (steps 4, 7) without the
  user's go-ahead.
