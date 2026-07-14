"""
sphinx extension that generates HL7 reference pages by parsing the generated
source files with the AST.
"""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from pathlib import Path

from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)

_PKG_ROOT = Path(__file__).parent.parent.parent / "hl7types" / "hl7"
_VERSIONS = sorted(p.name for p in _PKG_ROOT.iterdir() if p.is_dir() and p.name.startswith("v"))
_CATEGORIES = ("messages", "segments", "datatypes", "groups")

_CATEGORY_TITLES = {
    "messages": "Messages",
    "segments": "Segments",
    "datatypes": "Data Types",
    "groups": "Groups",
}

# All known HL7 type names across all versions, built once at module load so
# that _type_rst() can decide whether to emit a :ref: or plain text.
_ALL_HL7_NAMES: set[str] = set()


def _collect_hl7_names() -> None:
    for ver_dir in _PKG_ROOT.iterdir():
        if not ver_dir.name.startswith("v"):
            continue
        for cat in _CATEGORIES:
            cat_dir = ver_dir / cat
            if cat_dir.is_dir():
                for p in cat_dir.glob("*.py"):
                    if p.stem != "__init__":
                        _ALL_HL7_NAMES.add(p.stem)


_collect_hl7_names()

# Matches bare HL7 type names in annotation strings, including the underscore-
# prefixed local aliases used in generated message/group files (_MSH, _NK1 …).
_TYPE_NAME_RE = re.compile(r"_?([A-Z][A-Z0-9_]*)")


@dataclass
class FieldInfo:
    name: str
    alias: str  # serialization_alias, e.g. "MSH.3"
    annotation: str  # raw AST-unparsed annotation string
    required: bool
    title: str
    description: str


def _human_version(ver: str) -> str:
    return ver[1:].replace("_", ".")


def _ref_label(version: str, cls_name: str) -> str:
    return f"hl7-{version}-{cls_name}"


def _type_rst(annotation: str, version: str) -> str:
    """
    Turn an annotation string into rst.  HL7 type names found inside the
    annotation are replaced with :ref: links; everything else is left as-is.
    """

    def replace(m: re.Match) -> str:
        name = m.group(1)
        if name in _ALL_HL7_NAMES:
            label = _ref_label(version, name)
            return f":ref:`{name} <{label}>`"
        return name

    return _TYPE_NAME_RE.sub(replace, annotation)


def _parse_alias_file(path: Path) -> tuple[str, str] | None:
    """Return (alias_name, canonical_name) if the file is a thin alias module."""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except SyntaxError:
        return None
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.names:
            alias = node.names[0]
            if alias.asname and alias.name != alias.asname:
                return alias.asname, alias.name
    return None


def _parse_file(path: Path) -> tuple[str, str, list[FieldInfo]] | None:
    """
    Parse one generated .py file and return (class_name, summary, fields).
    Returns None if the file has no suitable class.
    """
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except SyntaxError:
        return None

    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef):
            continue

        cls_name = node.name
        summary = (ast.get_docstring(node) or "").splitlines()[0].strip()

        fields: list[FieldInfo] = []
        for stmt in node.body:
            if not isinstance(stmt, ast.AnnAssign):
                continue
            if not isinstance(stmt.target, ast.Name):
                continue
            fname = stmt.target.id
            if fname == "model_config":
                continue
            if not isinstance(stmt.value, ast.Call):
                continue

            annotation = ast.unparse(stmt.annotation)
            kwargs = {kw.arg: kw.value for kw in stmt.value.keywords}

            required = "default" not in kwargs and not stmt.value.args

            def _str(key: str) -> str:
                n = kwargs.get(key)
                return n.value if isinstance(n, ast.Constant) and isinstance(n.value, str) else ""

            fields.append(
                FieldInfo(
                    name=fname,
                    alias=_str("serialization_alias"),
                    annotation=annotation,
                    required=required,
                    title=_str("title"),
                    description=_str("description"),
                )
            )

        if fields:
            return cls_name, summary, fields

        # Subclass with no own fields (e.g. ADT_A04(ADT_A01)) — follow base class.
        if node.bases:
            base_name = ast.unparse(node.bases[0])
            base_path = path.parent / f"{base_name}.py"
            if base_path.exists():
                base = _parse_file(base_path)
                if base is not None:
                    _, _, inherited = base
                    return cls_name, summary, inherited

    return None


def _class_to_rst(
    cls_name: str, summary: str, fields: list[FieldInfo], version: str, category: str
) -> list[str]:
    label = _ref_label(version, cls_name)
    module = f"hl7types.hl7.{version}.{category}.{cls_name}"
    heading = f"{cls_name} {summary}" if summary else cls_name
    lines = [
        f".. _{label}:",
        "",
        heading,
        "~" * len(heading),
        "",
        f".. py:class:: {module}.{cls_name}",
        "   :noindex:",
        "",
    ]

    show_alias = any(fi.alias for fi in fields)
    header = ["   * - Field"]
    if show_alias:
        header.append("     - HL7")
    header += ["     - Type", "     - Required", "     - Description"]

    lines += [".. list-table::", "   :header-rows: 1", "   :widths: auto", ""] + header
    for fi in fields:
        req = "required" if fi.required else "optional"
        desc = fi.description or fi.title or ""
        type_cell = _type_rst(fi.annotation, version)
        row = [f"   * - ``{fi.name}``"]
        if show_alias:
            row.append(f"     - {fi.alias}")
        row += [f"     - {type_cell}", f"     - {req}", f"     - {desc}"]
        lines += row
    lines.append("")
    return lines


def _alias_to_rst(alias: str, canonical: str, version: str) -> list[str]:
    label = _ref_label(version, alias)
    canonical_ref = f":ref:`{canonical} <{_ref_label(version, canonical)}>`"
    return [
        f".. _{label}:",
        "",
        alias,
        "~" * len(alias),
        "",
        f"Alias for {canonical_ref}.",
        "",
    ]


def _generate_category_page(version: str, category: str, out_dir: Path) -> Path | None:
    cat_dir = _PKG_ROOT / version / category
    if not cat_dir.is_dir():
        return None

    paths = sorted(p for p in cat_dir.glob("*.py") if p.stem != "__init__")
    out_path = out_dir / f"{version}_{category}.rst"

    if out_path.exists():
        out_mtime = out_path.stat().st_mtime
        if all(p.stat().st_mtime < out_mtime for p in paths):
            return out_path

    ver_human = _human_version(version)
    cat_title = _CATEGORY_TITLES.get(category, category.title())
    title = f"v{ver_human} {cat_title}"
    lines: list[str] = [title, "=" * len(title), ""]

    print(f"  hl7_autodoc: {version}/{category} ({len(paths)} files)", flush=True)
    for p in paths:
        result = _parse_file(p)
        if result is not None:
            cls_name, summary, fields = result
            lines += _class_to_rst(cls_name, summary, fields, version, category)
            continue
        alias_result = _parse_alias_file(p)
        if alias_result is not None:
            alias, canonical = alias_result
            lines += _alias_to_rst(alias, canonical, version)

    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


def _generate_version_index(version: str, out_dir: Path, generated_cats: list[str]) -> None:
    ver_human = _human_version(version)
    title = f"HL7 v{ver_human}"
    lines = [title, "=" * len(title), "", ".. toctree::", "   :maxdepth: 1", ""]
    for cat in generated_cats:
        lines.append(f"   {version}_{cat}")
    lines.append("")
    (out_dir / f"{version}.rst").write_text("\n".join(lines), encoding="utf-8")


def _generate_all(app: Sphinx) -> None:
    out_dir = Path(app.srcdir) / "hl7"
    out_dir.mkdir(exist_ok=True)

    print(f"hl7_autodoc: generating pages for {len(_VERSIONS)} versions (AST mode)...", flush=True)
    version_list: list[str] = []
    for version in _VERSIONS:
        print(f"hl7_autodoc: {version}", flush=True)
        generated: list[str] = []
        for category in _CATEGORIES:
            p = _generate_category_page(version, category, out_dir)
            if p is not None:
                generated.append(category)
        if generated:
            _generate_version_index(version, out_dir, generated)
            version_list.append(version)

    title = "HL7 Reference"
    lines = [title, "=" * len(title), "", ".. toctree::", "   :maxdepth: 1", ""]
    for ver in version_list:
        lines.append(f"   hl7/{ver}")
    lines.append("")
    (Path(app.srcdir) / "hl7_reference.rst").write_text("\n".join(lines), encoding="utf-8")
    print(f"hl7_autodoc: done: {len(version_list)} versions written", flush=True)


def setup(app: Sphinx) -> dict:
    app.connect("builder-inited", _generate_all)
    return {"version": "1.0", "parallel_read_safe": True}
