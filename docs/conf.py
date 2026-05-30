import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

# -- Project information -----------------------------------------------------

project = "hl7types"
copyright = "2024, Keiron O'Shea"
author = "Keiron O'Shea"

version = "0.3.0"
release = "0.3.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
suppress_warnings = ["sphinx_autodoc_typehints.forward_reference"]

language = "en"

autodoc_member_order = "bysource"
autodoc_typehints = "description"
napoleon_google_docstring = True
napoleon_numpy_docstring = False

# -- Options for HTML output -------------------------------------------------

html_theme = "furo"
html_static_path = ["_static"]
