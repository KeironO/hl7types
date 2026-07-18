# Contributing

Contributions are welcome. This page explains how the project is structured, what is and is not
safe to change, and how to get a working development environment.

## The generated HL7 models

> **Warning:** Never edit anything inside `hl7types/hl7/`. Every file in that directory tree,
> messages, segments, groups, datatypes, and their `__init__` modules, is generated automatically
> from the HL7 XML specification by [hl7-parser](https://github.com/KeironO/hl7-parser). Any manual
> change will be silently overwritten the next time the generator runs.

If you find an inaccuracy in a generated model, a wrong field type, a missing component, an
incorrect cardinality, the fix belongs in [hl7-parser](https://github.com/KeironO/hl7-parser), not
here. Once the generator is corrected and a new generation pass is run, the fix propagates to all
versions and all affected types automatically.

Everything outside `hl7types/hl7/` is hand-written and is fair game for contributions. Go mad!

## Setting up a development environment

The project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
git clone https://github.com/KeironO/hl7types.git
cd hl7types
uv sync --group dev --group docs
uv run pre-commit install
```

## Dependencies

This section describes how `hl7types` selects, obtains, and tracks its dependencies.

### Selection

Runtime dependencies are kept to a minimum and are chosen for a specific purpose:

- **[Pydantic](https://docs.pydantic.dev/)** — provides the model base classes and validation used by every generated HL7 type.
- **[defusedxml](https://github.com/tiran/defusedxml)** — provides safer XML parsing and mitigates XXE / entity expansion attacks.
- **[typing_extensions](https://github.com/python/typing_extensions)** — supplies back-ports of newer typing constructs for supported Python versions.

Development and documentation dependencies (linters, type checkers, test runners, Sphinx, etc.) are declared separately and are not installed by end users.

### Obtaining

Dependencies are obtained from the Python Package Index (PyPI) using [uv](https://docs.astral.sh/uv/):

```bash
uv sync --group dev --group docs
```

For release builds, the CI pipeline uses the same tooling (`uv sync` and `uv build`) so the published artifacts are produced from the resolved dependency set.

### Tracking

- Direct runtime and development dependencies are declared in `[project.dependencies]` and `[dependency-groups]` in `pyproject.toml`.
- Exact, reproducible versions for the full transitive dependency graph are recorded in `uv.lock`, which is committed to version control.
- [Dependabot](https://github.com/KeironO/hl7types/blob/main/.github/dependabot.yml) monitors the dependency manifests and opens pull requests when updated versions are available.
- Pull requests that change dependencies trigger the full test, lint, and type-check suite before they can be merged.

## Running the tests

```bash
uv run pytest
```

## Code style

The project uses [ruff](https://docs.astral.sh/ruff/) for linting and formatting. Pre-commit runs
both automatically on every commit. To run them manually:

```bash
uv run ruff check --fix
uv run ruff format
```

Type checking is enforced with [pyright](https://github.com/microsoft/pyright):

```bash
uv run pyright
```

Pre-commit hooks run ruff, pyright, and the full test suite on every commit, and a `commit-msg`
hook enforces the commit message format described below. A commit that fails any of these will be
rejected locally before it reaches CI.

## Commit messages and the changelog

The [changelog](changelog.md) is generated from git history using
[git-cliff](https://git-cliff.org/). Because `main` is protected, the `Update changelog` GitHub
Actions workflow opens a pull request with the generated `CHANGELOG.md` instead of pushing directly
to `main`.

Prefix commits with one of:

- `feat:` new feature or user-visible behaviour change
- `fix:` / `bug:` bug fix
- `refactor:` internal restructuring, no behaviour change
- `docs:` documentation only
- `test:` tests only
- `chore:` maintenance (deps, CI, tooling)

The subject line (first line) is all that appears in the changelog, so make it a clear,
present-tense sentence. Example:

```
feat: add truncation character support for HL7 v2.7+ MSH.2
```

To preview what the next changelog entry will look like before releasing:

```bash
uv run git-cliff --unreleased
```

## Release process

1. Bump the version in `pyproject.toml`.
2. Commit the bump: `chore: bump version to X.Y.Z`
3. Create the release tag: `git tag X.Y.Z`
4. Push the tag: `git push origin X.Y.Z`

GitHub Actions then runs automatically:

- `publish.yml` — runs the test suite, builds the package, and publishes to PyPI.
- `changelog.yml` — generates a fresh `CHANGELOG.md` via git-cliff and opens a pull request against
  `main`.

Review the changelog pull request, then merge it through the normal branch protection checks.
There is no need to trigger the workflow manually.

## Building the documentation

```bash
uv run sphinx-build docs docs/_build/html
```

The built documentation will be available at `docs/_build/html/index.html`.

The HL7 reference pages (everything under the HL7 Reference section) are generated at build time by
a custom Sphinx extension at `docs/_ext/hl7_autodoc.py`. Rather than using Sphinx's standard
autodoc, which would need to import every one of the 10,000 or so generated classes, `hl7_autodoc`
parses the source files directly with Python's `ast` module. It walks `hl7types/hl7/` at the start
of each build, extracts class names, field aliases, types, `max_length` constraints, and docstrings
without executing any code, and writes one RST page per version per category (messages, segments,
groups, datatypes) into `docs/hl7/`.

Those generated RST files are never committed to the repository. They are always produced fresh
during the build. If you modify `hl7_autodoc.py`, the changes take effect on the next
`sphinx-build` run. If you regenerate the HL7 models via `hl7-parser`, the reference pages update
automatically on the next build with no further action required.
