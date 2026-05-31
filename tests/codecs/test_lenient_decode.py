import pytest

from hl7types import decode_er7


def test_lenient_decode_warns_when_required_segment_skipped() -> None:
    from hl7types.hl7.v2_3.messages.ADT_A01 import ADT_A01

    wire = (
        "MSH|^~\\&|A|B|C|D|20010101||ADT^A01|CTRL|P|2.3\r"
        "PID|1||123456||DOE^JOHN\r"
    )

    with pytest.warns(UserWarning, match="strict=False"):
        msg = decode_er7(wire, msg_cls=ADT_A01, strict=False)

    assert msg.PV1 is not None

def test_lenient_decode_warns_when_required_segment_field_skipped() -> None:
    from hl7types.hl7.v2_3.segments.PV1 import PV1
    from hl7types.codecs.er7.decoder import decode_er7_segment

    with pytest.warns(UserWarning, match="PV1"):
        seg = decode_er7_segment("PV1|1", PV1, strict=False)

    assert seg.pv1_2 == ""
