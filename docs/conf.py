import sys
from pathlib import Path

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent / "_ext"))

_pyproject = tomllib.loads((Path(__file__).parent.parent / "pyproject.toml").read_text())

# -- Project information -----------------------------------------------------

project = "hl7types"
copyright = "2025: Keiron O'Shea"
author = "Keiron O'Shea"

release = _pyproject["project"]["version"]
version = ".".join(release.split(".")[:2])

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "myst_parser",
    "hl7_autodoc",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
suppress_warnings = []

viewcode_exclude_modules = [r"hl7types\.hl7\..*"]

language = "en"

# -- Autodoc -----------------------------------------------------------------

autodoc_member_order = "bysource"

# Suppress type annotation noise for the generated HL7 universe.
# Field types are already described in each class docstring.
autodoc_typehints = "none"
autodoc_preserve_defaults = False

# Separate __init__ signature from class description; for Pydantic models the
# constructor signature is a giant generated blob that adds no value.
autodoc_class_signature = "separated"

# Defaults that keep generated pages light: only declared members, no Pydantic
# inherited machinery, no private/special attributes.
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": False,
    "inherited-members": False,
    "special-members": False,
    "private-members": False,
}

# autosummary: do not re-generate .rst stubs on every build.
autosummary_generate = False
autosummary_imported_members = False

# -- Napoleon ----------------------------------------------------------------

napoleon_google_docstring = False
napoleon_numpy_docstring = True

# -- HTML output -------------------------------------------------------------

html_theme = "furo"
html_static_path = []

# -- Hooks -------------------------------------------------------------------

# Names and prefixes that belong to Pydantic's internal machinery and add
# nothing useful to the generated HL7 model docs.
_PYDANTIC_SKIP_PREFIXES = ("model_", "__pydantic_")
_PYDANTIC_SKIP_NAMES = {
    "model_config",
    "model_fields",
    "model_computed_fields",
    "__class_vars__",
    "__private_attributes__",
    "__signature__",
}
# Public HL7Model methods that *should* appear in the docs.
_KEEP_NAMES = {"model_validate_er7", "model_dump_er7"}


def _skip_pydantic_member(app, what, name, obj, skip, options):
    if name in _KEEP_NAMES:
        return False
    if any(name.startswith(p) for p in _PYDANTIC_SKIP_PREFIXES):
        return True
    if name in _PYDANTIC_SKIP_NAMES:
        return True
    return skip


def _suppress_generated_signature(app, what, name, obj, options, signature, return_annotation):
    module = getattr(obj, "__module__", "") or ""
    if module.startswith("hl7types.hl7."):
        return "", None
    return signature, return_annotation


def setup(app):
    app.connect("autodoc-skip-member", _skip_pydantic_member)
    app.connect("autodoc-process-signature", _suppress_generated_signature)
