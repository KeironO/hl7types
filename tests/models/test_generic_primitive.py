"""
Tests emulating ca.uhn.hl7v2.model.GenericPrimitiveTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-core/src/test/java/ca/uhn/hl7v2/model/GenericPrimitiveTest.java
"""
from __future__ import annotations

from hl7types.hl7.v2_5.datatypes.NR import NR


def test_composite_with_primitive_components() -> None:
    """Composite fields with primitive components should be constructible.

    When creating a composite type like NR (numeric range) that contains
    primitive string components, it should be instantiatable.
    """
    nr = NR(nr_1="100", nr_2="200")

    assert nr is not None
    assert nr.nr_1 == "100"
    assert nr.nr_2 == "200"


def test_composite_with_null_components() -> None:
    """Composite fields should handle None/null component values.

    When a composite is created without all components, missing ones
    should be None.
    """
    nr = NR(nr_1="100")

    assert nr.nr_1 == "100"
    assert nr.nr_2 is None


def test_primitive_component_set_get() -> None:
    """Primitive components in composites should support set/get operations.

    When setting values on primitive components, they should be retrievable.
    """
    # Test with simple values
    nr1 = NR(nr_1="AAAA", nr_2="BBBB")
    assert nr1.nr_1 == "AAAA"
    assert nr1.nr_2 == "BBBB"

    # Test with empty string
    nr2 = NR(nr_1="", nr_2="value")
    assert nr2.nr_1 == ""
    assert nr2.nr_2 == "value"

    # Test with space
    nr3 = NR(nr_1=" ", nr_2="value")
    assert nr3.nr_1 == " "

    # Test with complex string
    nr4 = NR(nr_1="1234aBCDerfgkyuy", nr_2="value")
    assert nr4.nr_1 == "1234aBCDerfgkyuy"


def test_composite_serialisation() -> None:
    """Composite fields should serialise to ER7 format correctly.

    When a composite is serialised, it should produce the ER7 format.
    """
    nr = NR(nr_1="100", nr_2="200")

    # Serialise to ER7
    er7 = nr.model_dump_er7()

    # Should contain both components
    assert "100" in er7
    assert "200" in er7
