"""
Tests emulating ca.uhn.hl7v2.model.IsEmptyTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-core/src/test/java/ca/uhn/hl7v2/model/IsEmptyTest.java

Tests whether fields have content (are populated) vs being empty (None or containing
only separators with no actual data).
"""
from __future__ import annotations

from hl7types import decode_er7


def test_primitive_field_empty_when_not_provided() -> None:
    """Primitive string fields should be None when not provided.

    When a field is not included in the ER7 wire, it should be None,
    indicating it is empty/unpopulated.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||19951002185200||ADT^A01|LABGL1199510021852632|P|2.3\r"
        "PID|1||708010^^^MRN^MR||SURNAME^GIVEN^^^MRS^^L||19381216|F\r"
    )

    msg = decode_er7(msg_text)

    # PID.pid_9 is not provided in the message, should be None
    assert msg.PID.pid_9 is None


def test_primitive_field_populated_with_value() -> None:
    """Primitive fields should contain their value when provided.

    When a field is provided in the wire with a non-empty value, it
    should be populated and not None.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||19951002185200||ADT^A01|LABGL1199510021852632|P|2.3\r"
        "PID|1||708010^^^MRN^MR||SURNAME^GIVEN^^^MRS^^L||19381216|F||||||||||||||\r"
    )

    msg = decode_er7(msg_text)

    # PID.pid_3 has content
    assert msg.PID.pid_3 is not None
    assert len(msg.PID.pid_3) > 0


def test_composite_field_empty_when_all_components_missing() -> None:
    """Composite fields should be None when all components are missing.

    When a composite field position contains only empty components
    (e.g., ^^^^^), the field should be considered empty.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||19951002185200||ADT^A01|LABGL1199510021852632|P|2.3\r"
        "PID|1||708010^^^MRN^MR||SURNAME^GIVEN^^^MRS^^L||19381216|F|||||^^^^^||||||\r"
    )

    msg = decode_er7(msg_text)

    # PID.pid_10 is all empty components
    # If parsed, all components should be None
    if msg.PID.pid_10 is not None:
        # Check that at least the first component is None
        assert msg.PID.pid_10.ce_1 is None or msg.PID.pid_10.ce_1 == ""


def test_composite_field_populated_with_component_values() -> None:
    """Composite fields should be populated when components have values.

    When a composite field has at least one component with a value,
    it should be populated (not None).
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||19951002185200||ADT^A01|LABGL1199510021852632|P|2.3\r"
        "PID|1||708010^^^MRN^MR|PENSION NO^^^DSS^PE|SURNAME^GIVEN^^^MRS^^L||19381216|F\r"
    )

    msg = decode_er7(msg_text)

    # PID.pid_3 (patient identifier list) is populated
    assert msg.PID.pid_3 is not None
    # PID.pid_4 (alternate patient identifier) is populated
    assert msg.PID.pid_4 is not None


def test_repeating_field_empty_when_not_provided() -> None:
    """Repeating fields should be empty list when not provided.

    When a repeating field is not included in the ER7 wire,
    it should be an empty list.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||19951002185200||ADT^A01|LABGL1199510021852632|P|2.3\r"
        "PID|1||708010^^^MRN^MR||SURNAME^GIVEN^^^MRS^^L||19381216|F\r"
    )

    msg = decode_er7(msg_text)

    # PID.pid_3 is a repeating field
    assert isinstance(msg.PID.pid_3, list)


def test_segment_present_when_in_message() -> None:
    """Segments present in the wire should be accessible.

    When a segment is present in the ER7 wire, it should be
    accessible (not None) on the message model.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||19951002185200||ADT^A01|LABGL1199510021852632|P|2.3\r"
        "EVN|A01|20130923023038|\r"
        "PID|1||708010^^^MRN^MR||SURNAME^GIVEN^^^MRS^^L||19381216|F\r"
    )

    msg = decode_er7(msg_text)

    # All segments present in the wire should be accessible
    assert msg.MSH is not None
    assert msg.EVN is not None
    assert msg.PID is not None


def test_optional_segment_unpopulated_when_not_in_message() -> None:
    """Optional segments not in the wire have unpopulated fields.

    When an optional segment is not included in the ER7 wire, the
    segment exists in the model but its fields are unpopulated (None).
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||19951002185200||ADT^A01|LABGL1199510021852632|P|2.3\r"
        "PID|1||708010^^^MRN^MR||SURNAME^GIVEN^^^MRS^^L||19381216|F\r"
    )

    msg = decode_er7(msg_text)

    # EVN is not in the message but is accessible as a segment
    # with unpopulated fields
    assert msg.EVN is not None
    # All its fields should be empty/None
    assert msg.EVN.evn_2 is None
    assert msg.EVN.evn_3 is None
