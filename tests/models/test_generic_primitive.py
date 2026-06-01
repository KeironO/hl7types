"""
Tests emulating ca.uhn.hl7v2.model.GenericPrimitiveTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-core/src/test/java/ca/uhn/hl7v2/model/GenericPrimitiveTest.java
"""
from __future__ import annotations

from pydantic import ValidationError
import pytest
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
    nr1 = NR(nr_1="0.1", nr_2="0.2")
    assert nr1.nr_1 == "0.1"
    assert nr1.nr_2 == "0.2"

    nr2 = NR(nr_1="1.0", nr_2="2.0")
    assert nr2.nr_1 == "1.0"
    assert nr2.nr_2 == "2.0"

    # Test with space
    with pytest.raises(ValidationError):
        nr3 = NR(nr_1=" ", nr_2="value")

    # Test with complex string
    with pytest.raises(ValidationError):
        nr4 = NR(nr_1="1234aBCDerfgkyuy", nr_2="value")


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
