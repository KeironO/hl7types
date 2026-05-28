"""
Tests emulating ca.uhn.hl7v2.model.GenericCompositeTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-core/src/test/java/ca/uhn/hl7v2/model/GenericCompositeTest.java
"""
from __future__ import annotations

from hl7types.hl7.v2_5.datatypes.MSG import MSG


def test_message_type_construction() -> None:
    """A message type (composite) should be constructible.

    When creating a MSG (message type) composite, it should be
    instantiable and have valid component access.
    """
    msg_type = MSG(msg_1="ADT", msg_2="A01")

    assert msg_type is not None
    assert msg_type.msg_1 == "ADT"
    assert msg_type.msg_2 == "A01"


def test_composite_component_access() -> None:
    """Composite fields should support component access.

    A composite (like MSG) should allow access to its individual
    components via field attributes.
    """
    msg_type = MSG(msg_1="ADT", msg_2="A01")

    # Access first component
    assert msg_type.msg_1 == "ADT"

    # Access second component
    assert msg_type.msg_2 == "A01"


def test_composite_with_null_components() -> None:
    """Composite fields should handle null/missing components.

    When a composite is created without all components, missing
    ones should be None.
    """
    msg_type = MSG(msg_1="ADT")

    # First component is set
    assert msg_type.msg_1 == "ADT"

    # Second component is None
    assert msg_type.msg_2 is None


def test_composite_serialisation() -> None:
    """Composite fields should serialise to ER7 format.

    When a composite is serialised, it should produce the proper
    ER7 format with components separated.
    """
    msg_type = MSG(msg_1="ADT", msg_2="A01")

    # Serialise to ER7
    er7 = msg_type.model_dump_er7()

    # Should contain both components
    assert "ADT" in er7
    assert "A01" in er7
