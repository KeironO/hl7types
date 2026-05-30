from typing import Optional

import pytest
from pydantic import Field

from hl7types import HL7Registry, decode_er7
from hl7types.hl7 import HL7Model
from hl7types.hl7.v2_5_1.datatypes.HD import HD
from hl7types.hl7.v2_5_1.datatypes.MSG import MSG
from hl7types.hl7.v2_5_1.datatypes.PT import PT
from hl7types.hl7.v2_5_1.datatypes.TS import TS
from hl7types.hl7.v2_5_1.datatypes.VID import VID
from hl7types.hl7.v2_5_1.segments.MSA import MSA
from hl7types.hl7.v2_5_1.segments.MSH import MSH

_MSH = MSH
_MSA = MSA

_WIRE = (
    "MSH|^~\\&|WPAS||SEND||20260101120000||ACK|MSG000002|P|2.5.1\r"
    "MSA|AA|MSG000001\r"
    "ZWCC|WPAS|20260101120000\r"
)


class ZWCC(HL7Model):
    zwcc_1: Optional[str] = Field(None, serialization_alias="ZWCC.1")
    zwcc_2: Optional[str] = Field(None, serialization_alias="ZWCC.2")


_ZWCC = ZWCC


class WCCACKMessage(HL7Model):
    MSH: _MSH
    MSA: _MSA
    ZWCC: Optional[_ZWCC] = None


def _make_registry() -> HL7Registry:
    r = HL7Registry()
    r.register_segment("ZWCC", ZWCC)
    r.register_message("2.5.1", "ACK", WCCACKMessage)
    return r


# HL7Registry unit tests

def test_register_and_get_segment():
    r = HL7Registry()
    r.register_segment("ZWCC", ZWCC)
    assert r.get_segment("ZWCC") is ZWCC


def test_get_segment_returns_none_for_unknown():
    r = HL7Registry()
    assert r.get_segment("ZWCC") is None


def test_register_and_get_message():
    r = HL7Registry()
    r.register_message("2.5.1", "ACK", WCCACKMessage)
    assert r.get_message("2.5.1", "ACK") is WCCACKMessage


def test_get_message_returns_none_for_unknown():
    r = HL7Registry()
    assert r.get_message("2.5.1", "ACK") is None


@pytest.mark.parametrize("seg_name", ["MSH", "FHS", "BHS"])
def test_protected_segments_raise(seg_name: str):
    r = HL7Registry()
    with pytest.raises(ValueError, match="delimiter-definition segment"):
        r.register_segment(seg_name, ZWCC)


def test_registries_are_isolated():
    r1 = HL7Registry()
    r2 = HL7Registry()
    r1.register_segment("ZWCC", ZWCC)
    assert r1.get_segment("ZWCC") is ZWCC
    assert r2.get_segment("ZWCC") is None


# decode_er7 integration with registry


def test_decode_with_custom_message_class():
    r = _make_registry()
    msg = decode_er7(_WIRE, registry=r, strict=True)
    assert isinstance(msg, WCCACKMessage)
    assert msg.ZWCC is not None
    assert msg.ZWCC.zwcc_1 == "WPAS"
    assert msg.ZWCC.zwcc_2 == "20260101120000"


def test_decode_explicit_msg_cls_with_custom_segment():
    r = HL7Registry()
    r.register_segment("ZWCC", ZWCC)
    msg = decode_er7(_WIRE, msg_cls=WCCACKMessage, registry=r, strict=True)
    assert isinstance(msg, WCCACKMessage)
    assert msg.ZWCC is not None
    assert msg.ZWCC.zwcc_1 == "WPAS"


def test_decode_without_registry_drops_z_segment():
    # Without a registry or explicit msg_cls the decoder falls back to the
    # generated ACK model, which has no ZWCC field the segment is silently
    # ignored rather than raising.
    from hl7types.hl7.v2_5_1.messages.ACK import ACK

    msg = decode_er7(_WIRE, msg_cls=ACK, strict=True)
    assert not hasattr(msg, "ZWCC")


def test_decode_msa_still_populated():
    r = _make_registry()
    msg = decode_er7(_WIRE, registry=r, strict=True)
    assert msg.MSA.msa_1 == "AA"
    assert msg.MSA.msa_2 == "MSG000001"


def test_construct_and_encode_with_custom_segment():
    msh = MSH(
        msh_3=HD(hd_1="WPAS"),
        msh_5=HD(hd_1="SEND"),
        msh_7=TS(ts_1="20260101120000"),
        msh_9=MSG(msg_1="ACK"),
        msh_10="MSG000002",
        msh_11=PT(pt_1="P"),
        msh_12=VID(vid_1="2.5.1"),
    )
    msa = MSA(msa_1="AA", msa_2="MSG000001")
    zwcc = ZWCC(zwcc_1="WPAS", zwcc_2="20260101120000")
    msg = WCCACKMessage(MSH=msh, MSA=msa, ZWCC=zwcc)

    er7 = msg.model_dump_er7()
    lines = [l for l in er7.splitlines() if l]
    assert any(l.startswith("ZWCC|") for l in lines)
    zwcc_line = next(l for l in lines if l.startswith("ZWCC|"))
    assert zwcc_line == "ZWCC|WPAS|20260101120000"
