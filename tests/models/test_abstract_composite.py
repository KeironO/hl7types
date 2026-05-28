"""
Tests emulating ca.uhn.hl7v2.model.AbstractCompositeTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-core/src/test/java/ca/uhn/hl7v2/model/AbstractCompositeTest.java
"""
from __future__ import annotations

from hl7types.hl7.v2_5.messages.ORU_R01 import ORU_R01
from hl7types.hl7.v2_5.segments.MSH import MSH
from hl7types.hl7.v2_5.datatypes.MSG import MSG
from hl7types.hl7.v2_5.datatypes.HD import HD
from hl7types.hl7.v2_5.datatypes.PT import PT
from hl7types.hl7.v2_5.datatypes.VID import VID
from hl7types.hl7.v2_5.datatypes.TS import TS
from hl7types.hl7.v2_5.groups.ORU_R01_PATIENT_RESULT import ORU_R01_PATIENT_RESULT


def test_parse_null() -> None:
    """Parsing null into a composite field should set components to None.

    When a composite field (like MSG) is parsed with None, its component fields
    should be set to None rather than retaining previous values.
    """
    msh = MSH(
        msh_3=HD(hd_1="TEST"),
        msh_4=HD(hd_1="TEST"),
        msh_5=HD(hd_1="TEST"),
        msh_6=HD(hd_1="TEST"),
        msh_7=TS(ts_1="20050101"),
        msh_9=MSG(msg_1="ORU", msg_2="R01"),
        msh_10="MSG001",
        msh_11=PT(pt_1="T"),
        msh_12=VID(vid_1="2.5"),
    )

    # Message type should have content initially
    msg_type = msh.msh_9
    assert msg_type is not None
    assert msg_type.msg_1 == "ORU"
    assert msg_type.msg_2 == "R01"

    # Parse null into the message type
    msg_type_new = MSG()
    msh.msh_9 = msg_type_new

    # After parsing null, components should be None
    assert msh.msh_9.msg_1 is None
    assert msh.msh_9.msg_2 is None
