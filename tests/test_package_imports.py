"""Tests that `from hl7types.hl7.<version>.<kind> import Name` returns the
class, not the submodule (guards against the __getattr__ / IMPORT_FROM bug
where importlib.import_module sets the submodule on the parent __dict__ before
the IMPORT_FROM bytecode reads it back).
"""
from __future__ import annotations

import inspect


def test_segment_import_returns_class() -> None:
    from hl7types.hl7.v2_5_1.segments import MSH, MSA

    assert inspect.isclass(MSH), f"Expected class, got {type(MSH)}"
    assert inspect.isclass(MSA), f"Expected class, got {type(MSA)}"


def test_message_import_returns_class() -> None:
    from hl7types.hl7.v2_5_1.messages import ACK

    assert inspect.isclass(ACK), f"Expected class, got {type(ACK)}"


def test_imported_class_is_instantiable() -> None:
    from hl7types.hl7.v2_1.segments import MSH

    msh = MSH(msh_9="ACK", msh_10="1", msh_11="P", msh_12="2.1")
    assert msh.msh_9 == "ACK"


def test_repeated_import_still_returns_class() -> None:
    from hl7types.hl7.v2_5_1.segments import MSH as MSH1
    from hl7types.hl7.v2_5_1.segments import MSH as MSH2

    assert inspect.isclass(MSH1)
    assert inspect.isclass(MSH2)
    assert MSH1 is MSH2


def test_segment_import_across_versions() -> None:
    from hl7types.hl7.v2_1.segments import MSH as MSH_21
    from hl7types.hl7.v2_5_1.segments import MSH as MSH_251

    assert inspect.isclass(MSH_21), f"Expected class, got {type(MSH_21)}"
    assert inspect.isclass(MSH_251), f"Expected class, got {type(MSH_251)}"
    assert MSH_21 is not MSH_251
