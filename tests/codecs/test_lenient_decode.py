"""Lenient ER7 decoding (strict=False): missing required segments and fields are
tolerated, placeholder values are injected, and a UserWarning is emitted.

Strict-mode companions (missing segment/field raises) live in test_strict_decoding.py.
"""
from __future__ import annotations

import pytest

from hl7types import decode_er7
from hl7types.codecs.er7.decoder import decode_er7_segment
from hl7types.hl7.v2_3.messages.ADT_A01 import ADT_A01
from hl7types.hl7.v2_3.segments.PV1 import PV1

# ADT^A01 wire omitting the required EVN and PV1 segments.
_WIRE_MISSING_PV1 = (
    "MSH|^~\\&|A|B|C|D|20010101||ADT^A01|CTRL|P|2.3\r"
    "PID|1||123456||DOE^JOHN\r"
)


def test_missing_required_segment_still_decodes_and_warns() -> None:
    with pytest.warns(UserWarning, match=r"PV1.*strict=False"):
        msg = decode_er7(_WIRE_MISSING_PV1, msg_cls=ADT_A01, strict=False)

    # Supplied segments decode correctly.
    assert msg.MSH.msh_10 == "CTRL"
    assert msg.PID.pid_5.xpn_1 == "DOE"
    assert msg.PID.pid_5.xpn_2 == "JOHN"

    # Missing PV1 is injected as an all-None placeholder.
    assert msg.PV1 is not None
    assert msg.PV1.model_fields_set == set()
    assert msg.PV1.pv1_1 is None


def test_missing_required_segment_field_still_decodes_and_warns() -> None:
    with pytest.warns(UserWarning, match=r"PV1.*pv1_2"):
        seg = decode_er7_segment("PV1|1", PV1, strict=False)

    # pv1_1 (Set ID ; optional) was supplied on the wire.
    assert seg.pv1_1 == "1"
    # pv1_2 (Patient Class ; required) was injected as an empty string.
    assert seg.pv1_2 == ""
