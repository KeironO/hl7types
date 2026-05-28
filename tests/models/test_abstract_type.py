"""
Tests emulating ca.uhn.hl7v2.model.AbstractTypeTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-core/src/test/java/ca/uhn/hl7v2/model/AbstractTypeTest.java

Notes:
- testToStringOnXmlMessage adapted to test message type string representation.
- XML parsing is not applicable to hl7types, which uses ER7 encoding.
"""
from __future__ import annotations

from hl7types.hl7.v2_5.messages.ADT_A01 import ADT_A01
from hl7types.hl7.v2_5.segments.MSH import MSH
from hl7types.hl7.v2_5.datatypes.MSG import MSG
from hl7types.hl7.v2_5.datatypes.HD import HD
from hl7types.hl7.v2_5.datatypes.PT import PT
from hl7types.hl7.v2_5.datatypes.VID import VID
from hl7types.hl7.v2_5.datatypes.TS import TS


def test_message_type_string_representation() -> None:
    """Message type should have a string representation containing type and trigger.

    When a message type is created, its string representation should contain
    both the message type code and the trigger event code.
    """
    msg_type = MSG(msg_1="ADT", msg_2="A01")

    # String representation should contain both components
    str_repr = str(msg_type)
    assert "ADT" in str_repr
    assert "A01" in str_repr


def test_message_type_in_msh_segment() -> None:
    """MSH segment message type should be accessible and representable.

    When an MSH segment is created with a message type, the message type
    should be accessible and have a proper string representation.
    """
    msh = MSH(
        msh_3=HD(hd_1="TEST"),
        msh_4=HD(hd_1="TEST"),
        msh_5=HD(hd_1="TEST"),
        msh_6=HD(hd_1="TEST"),
        msh_7=TS(ts_1="20050101"),
        msh_9=MSG(msg_1="ADT", msg_2="A01"),
        msh_10="MSG001",
        msh_11=PT(pt_1="T"),
        msh_12=VID(vid_1="2.5"),
    )

    # Message type should be accessible
    assert msh.msh_9 is not None
    assert msh.msh_9.msg_1 == "ADT"
    assert msh.msh_9.msg_2 == "A01"

    # String representation should contain type info
    str_repr = str(msh.msh_9)
    assert "ADT" in str_repr
    assert "A01" in str_repr


def test_message_type_model_dump() -> None:
    """Message type should serialize to ER7 format correctly.

    When a message type is serialized, it should produce the ER7 format
    with components separated by carets.
    """
    msg_type = MSG(msg_1="ADT", msg_2="A01")

    # Serialize to ER7 format
    er7 = msg_type.model_dump_er7()
    assert "ADT" in er7
    assert "A01" in er7
