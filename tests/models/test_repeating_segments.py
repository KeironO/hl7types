"""Tests for messages containing multiple instances of repeating segments."""
from __future__ import annotations

from hl7types import decode_er7

_MSG = (
    "MSH|^~\\&|NES|NINTENDO|AGNEW|CORNERCUBICLE|20010101000000||ADT^A01|Q123|P|2.3\r"
    "EVN|A01|20010101000000\r"
    "PID|1||123456789||BROS^MARIO^^^^||19850101000000|M\r"
    "NK1|1|BROS^LUIGI^^^^|BRO^Brother\r"
    "NK1|2|TOAD^TOADSTOOL^^^^|FND^Friend\r"
    "NK1|3|PEACH^PRINCESS^^^^|FND^Friend\r"
    "PV1|1|I|WARD^ROOM^BED\r"
    "DG1|1|I10|J06.9^Acute upper respiratory infection^ICD10|||A\r"
    "DG1|2|I10|Z87.39^Personal history^ICD10|||A\r"
)


def test_multiple_nk1_segments_parsed() -> None:
    msg = decode_er7(_MSG)
    assert msg.NK1 is not None
    assert len(msg.NK1) == 3


def test_nk1_segment_order_preserved() -> None:
    msg = decode_er7(_MSG)
    names = [nk1.nk1_2[0].xpn_1 for nk1 in msg.NK1]  # type: ignore[union-attr, index]
    assert names == ["BROS", "TOAD", "PEACH"]


def test_nk1_relationship_field() -> None:
    msg = decode_er7(_MSG)
    assert msg.NK1[0].nk1_3.ce_1 == "BRO"  # type: ignore[union-attr, index]
    assert msg.NK1[1].nk1_3.ce_1 == "FND"  # type: ignore[union-attr, index]


def test_multiple_dg1_segments_parsed() -> None:
    msg = decode_er7(_MSG)
    assert msg.DG1 is not None
    assert len(msg.DG1) == 2


def test_dg1_diagnosis_codes() -> None:
    msg = decode_er7(_MSG)
    codes = [dg1.dg1_3.ce_1 for dg1 in msg.DG1]  # type: ignore[union-attr, index]
    assert codes == ["J06.9", "Z87.39"]


def test_repeating_segments_roundtrip() -> None:
    msg = decode_er7(_MSG)
    encoded = msg.model_dump_er7()
    msg2 = decode_er7(encoded)

    assert len(msg2.NK1) == len(msg.NK1)  # type: ignore[arg-type]
    assert len(msg2.DG1) == len(msg.DG1)  # type: ignore[arg-type]

    for orig, reparsed in zip(msg.NK1, msg2.NK1):  # type: ignore[union-attr]
        assert orig.nk1_1 == reparsed.nk1_1

    for orig, reparsed in zip(msg.DG1, msg2.DG1):  # type: ignore[union-attr]
        assert orig.dg1_3.ce_1 == reparsed.dg1_3.ce_1  # type: ignore[union-attr]
