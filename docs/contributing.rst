Contributing
============

Contributions are welcome. This page explains how the project is structured, what is and is not
safe to change, and how to get a working development environment.

The generated HL7 models
------------------------

.. warning::

   **Never edit anything inside** ``hl7types/hl7/``. Every file in that directory tree,
   messages, segments, groups, datatypes, and their ``__init__`` modules,  is generated
   automatically from the HL7 XML specification by
   `hl7-parser <https://github.com/KeironO/hl7-parser>`_. Any manual change will be silently
   overwritten the next time the generator runs.

If you find an inaccuracy in a generated model,  a wrong field type, a missing component, an
incorrect cardinality, the fix belongs in `hl7-parser
<https://github.com/KeironO/hl7-parser>`_, not here. Once the generator is corrected and a new
generation pass is run, the fix propagates to all versions and all affected types automagically.

Everything outside ``hl7types/hl7/`` is hand-written and is fair game for contributions. Go mad!

Setting up a development environment
--------------------------------------

The project uses `uv <https://docs.astral.sh/uv/>`_ for dependency management.

.. code-block:: bash

   git clone https://github.com/KeironO/hl7types.git
   cd hl7types
   uv sync --group dev --group docs
   uv run pre-commit install

Running the tests
-----------------

.. code-block:: bash

   uv run pytest

Code style
----------

The project uses `ruff <https://docs.astral.sh/ruff/>`_ for linting and formatting. Pre-commit
runs both automatically on every commit. To run them manually:

.. code-block:: bash

   uv run ruff check --fix
   uv run ruff format

Type checking is enforced with `pyright <https://github.com/microsoft/pyright>`_:

.. code-block:: bash

   uv run pyright

Pre-commit hooks run ruff, pyright, and the full test suite on every commit. A commit that fails
any of these will be rejected locally before it reaches CI.

Commit messages and the changelog
----------------------------------

The :doc:`changelog` is generated automatically from git history using
`git-cliff <https://git-cliff.org/>`_. Each release tag triggers a regeneration, so your commit
messages are what end up in the changelog — write them accordingly.

Prefix commits with one of:

- ``feat:`` — new feature or user-visible behaviour change
- ``fix:`` / ``bug:`` — bug fix
- ``refactor:`` — internal restructuring, no behaviour change
- ``docs:`` — documentation only
- ``test:`` — tests only
- ``chore:`` — maintenance (deps, CI, tooling)

The subject line (first line) is all that appears in the changelog, so make it a clear,
present-tense sentence. Example::

   feat: add truncation character support for HL7 v2.7+ MSH.2

To preview what the next changelog entry will look like before releasing:

.. code-block:: bash

   uv run git-cliff --unreleased

Building the documentation
---------------------------

.. code-block:: bash

   uv run sphinx-build docs docs/_build/html

The built documentation will be available at ``docs/_build/html/index.html``.

The HL7 reference pages (everything under the HL7 Reference section) are generated at build time
by a custom Sphinx extension at ``docs/_ext/hl7_autodoc.py``. Rather than using Sphinx's standard
autodoc, which would need to import every one of the 10,000 or so generated classes,
``hl7_autodoc`` parses the source files directly with Python's ``ast`` module. It walks
``hl7types/hl7/`` at the start of each build, extracts class names, field aliases, types,
``max_length`` constraints, and docstrings without executing any code, and writes one RST page per
version per category (messages, segments, groups, datatypes) into ``docs/hl7/``.

Those generated RST files are never committed to the repository. They are always produced fresh
during the build. If you modify ``hl7_autodoc.py``, the changes take effect on the next
``sphinx-build`` run. If you regenerate the HL7 models via ``hl7-parser``, the reference pages
update automatically on the next build with no further action required. I will fix this, eventually.
