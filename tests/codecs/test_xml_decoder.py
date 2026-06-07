from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

import pytest
from pydantic import ValidationError

from hl7types import decode_er7, decode_xml, encode_xml
from hl7types.codecs.xml.decoder import (
    _build_alias_map,
    _extract_truncation,
    _group_xml_tag,
    _is_segment_cls,
    _unwrap,
    decode_xml_segment,
)
from hl7types.hl7.v2_5_1.messages.ACK import ACK
from hl7types.hl7.v2_5_1.messages.ADT_A01 import ADT_A01
from hl7types.hl7.v2_5_1.segments.MSA import MSA
from hl7types.hl7.v2_5_1.segments.MSH import MSH


ACK_WIRE = (
    "MSH|^~\\&|SEND|FAC|RECV|FAC|20240101120000||ACK|MSG001|P|2.5.1\r"
    "MSA|AA|MSG001\r"
)

ADT_A01_WIRE = (
    "MSH|^~\\&|SENDING|FACILITY|RECEIVING|DEST|20240101120000||ADT^A01^ADT_A01|MSG001|P|2.5.1\r"
    "EVN|A01|20240101120000\r"
    "PID|1||123456^^^MRN^MR||Doe^John^A||19800101|M\r"
    "NK1|1|Smith^Jane|SPO|555-1234\r"
    "NK1|2|Smith^Bob|FTH|555-5678\r"
    "PV1|1|I|WARD^BED1\r"
    "AL1|1|DA|PENICILLIN|SEV|RASH\r"
    "DG1|1|ICD10|J18.9^PNEUMONIA|||A\r"
    "PR1|1||88.72^EEG^I9C||20240101120000\r"
    "IN1|1|PLAN-A|INS-001|BLUE CROSS\r"
    "IN2|MEMBER-001\r"
)


@pytest.fixture
def ack_xml() -> str:
    return encode_xml(decode_er7(ACK_WIRE))


@pytest.fixture
def adt_xml() -> str:
    return encode_xml(decode_er7(ADT_A01_WIRE, msg_cls=ADT_A01, strict=False))


def test_optional_returns_inner() -> None:
    inner, is_list = _unwrap(typing.Optional[str])
    assert inner is str
    assert is_list is False


def test_list_returns_inner_and_is_list() -> None:
    inner, is_list = _unwrap(typing.List[str])
    assert inner is str
    assert is_list is True


def test_optional_list_unwraps_both() -> None:
    inner, is_list = _unwrap(typing.Optional[typing.List[str]])
    assert inner is str
    assert is_list is True


def test_bare_type_unchanged() -> None:
    inner, is_list = _unwrap(str)
    assert inner is str
    assert is_list is False


def test_union_with_multiple_non_none_returns_original() -> None:
    ann = typing.Union[str, int]
    result, is_list = _unwrap(ann)
    assert is_list is False
    assert result is ann


def test_true_for_segment() -> None:
    assert _is_segment_cls(MSH) is True


def test_false_for_group() -> None:
    from hl7types.hl7.v2_5_1.groups.ADT_A01_PROCEDURE import ADT_A01_PROCEDURE
    assert _is_segment_cls(ADT_A01_PROCEDURE) is False


def test_false_for_non_model() -> None:
    assert _is_segment_cls(str) is False


def test_false_for_non_class() -> None:
    assert _is_segment_cls(42) is False  # type: ignore[arg-type]


def test_last_underscore_becomes_dot() -> None:
    class ADT_A01_PROCEDURE:
        pass
    assert _group_xml_tag(ADT_A01_PROCEDURE) == "ADT_A01.PROCEDURE"


def test_no_underscore_returns_name() -> None:
    class NOUNDER:
        pass
    assert _group_xml_tag(NOUNDER) == "NOUNDER"


def test_segment_aliases_present() -> None:
    am = _build_alias_map(MSA)
    assert "MSA.1" in am
    assert "MSA.2" in am


def test_group_alias_map_is_empty() -> None:
    from hl7types.hl7.v2_5_1.groups.ADT_A01_PROCEDURE import ADT_A01_PROCEDURE
    assert _build_alias_map(ADT_A01_PROCEDURE) == {}


def test_returns_empty_for_four_char_msh2() -> None:
    xml = (
        '<ACK xmlns="urn:hl7-org:v2xml">'
        "<MSH><MSH.2>^~\\&amp;</MSH.2><MSH.12><VID.1>2.5.1</VID.1></MSH.12></MSH>"
        "</ACK>"
    )
    root = ET.fromstring(xml)
    assert _extract_truncation(root) == ""


def test_returns_truncation_char_for_v27() -> None:
    xml = (
        '<ACK xmlns="urn:hl7-org:v2xml">'
        "<MSH><MSH.2>^~\\&amp;#</MSH.2><MSH.12><VID.1>2.7</VID.1></MSH.12></MSH>"
        "</ACK>"
    )
    root = ET.fromstring(xml)
    assert _extract_truncation(root) == "#"


def test_returns_empty_when_no_msh() -> None:
    root = ET.fromstring('<ACK xmlns="urn:hl7-org:v2xml"/>')
    assert _extract_truncation(root) == ""


def test_returns_empty_for_five_char_msh2_below_v27() -> None:
    xml = (
        '<ACK xmlns="urn:hl7-org:v2xml">'
        "<MSH><MSH.2>^~\\&amp;#</MSH.2><MSH.12><VID.1>2.5</VID.1></MSH.12></MSH>"
        "</ACK>"
    )
    root = ET.fromstring(xml)
    assert _extract_truncation(root) == ""


def test_scalar_fields() -> None:
    elem = ET.fromstring("<MSA><MSA.1>AA</MSA.1><MSA.2>MSG001</MSA.2></MSA>")
    seg = decode_xml_segment(elem, MSA)
    assert seg.msa_1 == "AA"
    assert seg.msa_2 == "MSG001"


def test_composite_field() -> None:
    elem = ET.fromstring(
        "<MSH>"
        "<MSH.1>|</MSH.1><MSH.2>^~\\&amp;</MSH.2>"
        "<MSH.3><HD.1>SEND</HD.1></MSH.3>"
        "<MSH.9><MSG.1>ACK</MSG.1></MSH.9>"
        "<MSH.10>001</MSH.10>"
        "<MSH.11><PT.1>P</PT.1></MSH.11>"
        "<MSH.12><VID.1>2.5.1</VID.1></MSH.12>"
        "<MSH.7><TS.1>20240101</TS.1></MSH.7>"
        "</MSH>"
    )
    seg = decode_xml_segment(elem, MSH)
    assert seg.msh_3.hd_1 == "SEND"  # type: ignore[union-attr]
    assert seg.msh_9.msg_1 == "ACK"  # type: ignore[union-attr]


def test_repeating_field() -> None:
    from hl7types.hl7.v2_5_1.segments.PID import PID
    elem = ET.fromstring(
        "<PID>"
        "<PID.3><CX.1>ID1</CX.1></PID.3>"
        "<PID.3><CX.1>ID2</CX.1></PID.3>"
        "</PID>"
    )
    seg = decode_xml_segment(elem, PID, strict=False)
    assert seg.pid_3[0].cx_1 == "ID1"  # type: ignore[index, union-attr]
    assert seg.pid_3[1].cx_1 == "ID2"  # type: ignore[index, union-attr]


def test_unknown_tags_ignored() -> None:
    elem = ET.fromstring(
        "<MSA><MSA.1>AA</MSA.1><MSA.2>MSG001</MSA.2><UNKNOWN>X</UNKNOWN></MSA>"
    )
    seg = decode_xml_segment(elem, MSA)
    assert seg.msa_1 == "AA"


def test_msh_field_separator_injected() -> None:
    elem = ET.fromstring(
        "<MSH>"
        "<MSH.2>^~\\&amp;</MSH.2>"
        "<MSH.9><MSG.1>ACK</MSG.1></MSH.9>"
        "<MSH.10>001</MSH.10>"
        "<MSH.11><PT.1>P</PT.1></MSH.11>"
        "<MSH.12><VID.1>2.5.1</VID.1></MSH.12>"
        "<MSH.7><TS.1>20240101</TS.1></MSH.7>"
        "</MSH>"
    )
    seg = decode_xml_segment(elem, MSH)
    assert seg.msh_1 == "|"


def test_lenient_injects_placeholder_and_warns() -> None:
    elem = ET.fromstring("<MSA><MSA.1>AA</MSA.1></MSA>")
    with pytest.warns(UserWarning, match=r"msa_2.*strict=False"):
        seg = decode_xml_segment(elem, MSA, strict=False)
    assert seg.msa_1 == "AA"
    assert seg.msa_2 == ""


def test_strict_raises_on_missing_required_field() -> None:
    elem = ET.fromstring("<MSA><MSA.1>AA</MSA.1></MSA>")
    with pytest.raises(ValidationError):
        decode_xml_segment(elem, MSA, strict=True)


def test_truncation_char_stripped_from_scalar() -> None:
    elem = ET.fromstring("<MSA><MSA.1>AA</MSA.1><MSA.2>MSG001#</MSA.2></MSA>")
    seg = decode_xml_segment(elem, MSA, truncation="#")
    assert seg.msa_2 == "MSG001"


def test_truncation_not_stripped_from_encoding_chars_field() -> None:
    from hl7types.hl7.v2_7.segments.MSH import MSH as MSH27
    elem = ET.fromstring(
        "<MSH>"
        "<MSH.2>^~\\&amp;#</MSH.2>"
        "<MSH.9><MSG.1>ACK</MSG.1><MSG.2>A01</MSG.2><MSG.3>ACK</MSG.3></MSH.9>"
        "<MSH.10>001</MSH.10>"
        "<MSH.11><PT.1>P</PT.1></MSH.11>"
        "<MSH.12><VID.1>2.7</VID.1></MSH.12>"
        "<MSH.7>20240101120000</MSH.7>"
        "</MSH>"
    )
    seg = decode_xml_segment(elem, MSH27, strict=True, truncation="#")
    assert seg.msh_2 == "^~\\&#"


def test_empty_string_raises() -> None:
    with pytest.raises(ValueError, match="Empty"):
        decode_xml("")


def test_invalid_xml_raises() -> None:
    with pytest.raises(ValueError, match="Invalid XML"):
        decode_xml("<unclosed")


def test_no_msh_without_msg_cls_raises() -> None:
    with pytest.raises(ValueError, match="Cannot auto-detect"):
        decode_xml("<MSA><MSA.1>AA</MSA.1><MSA.2>001</MSA.2></MSA>")


def test_missing_msh9_raises() -> None:
    xml = (
        '<ACK xmlns="urn:hl7-org:v2xml">'
        "<MSH><MSH.12><VID.1>2.5.1</VID.1></MSH.12></MSH>"
        "</ACK>"
    )
    with pytest.raises(ValueError, match="MSH.9"):
        decode_xml(xml)


def test_missing_msh12_raises() -> None:
    xml = (
        '<ACK xmlns="urn:hl7-org:v2xml">'
        "<MSH><MSH.9><MSG.1>ACK</MSG.1></MSH.9></MSH>"
        "</ACK>"
    )
    with pytest.raises(ValueError, match="MSH.12"):
        decode_xml(xml)


def test_unknown_message_structure_raises() -> None:
    xml = (
        '<ZUNK xmlns="urn:hl7-org:v2xml">'
        "<MSH>"
        "<MSH.9><MSG.1>ZUNK</MSG.1></MSH.9>"
        "<MSH.12><VID.1>2.5.1</VID.1></MSH.12>"
        "</MSH>"
        "</ZUNK>"
    )
    with pytest.raises(ValueError, match="Unknown message structure"):
        decode_xml(xml)


def test_auto_detects_message_class(ack_xml: str) -> None:
    msg = decode_xml(ack_xml)
    assert isinstance(msg, ACK)


def test_explicit_msg_cls(ack_xml: str) -> None:
    msg = decode_xml(ack_xml, msg_cls=ACK)
    assert isinstance(msg, ACK)


def test_msh_scalar_fields(ack_xml: str) -> None:
    msg = decode_xml(ack_xml)
    assert msg.MSH.msh_10 == "MSG001"


def test_msh_composite_fields(ack_xml: str) -> None:
    msg = decode_xml(ack_xml)
    assert msg.MSH.msh_3.hd_1 == "SEND"    # type: ignore[union-attr]
    assert msg.MSH.msh_5.hd_1 == "RECV"    # type: ignore[union-attr]
    assert msg.MSH.msh_9.msg_1 == "ACK"    # type: ignore[union-attr]
    assert msg.MSH.msh_12.vid_1 == "2.5.1" # type: ignore[union-attr]


def test_msa_fields(ack_xml: str) -> None:
    msg = decode_xml(ack_xml)
    assert msg.MSA.msa_1 == "AA"
    assert msg.MSA.msa_2 == "MSG001"


def test_namespaced_xml_accepted(ack_xml: str) -> None:
    assert 'xmlns="urn:hl7-org:v2xml"' in ack_xml
    msg = decode_xml(ack_xml)
    assert msg.MSA.msa_1 == "AA"


def test_bare_xml_accepted(ack_xml: str) -> None:
    bare = ack_xml.replace(' xmlns="urn:hl7-org:v2xml"', "")
    msg = decode_xml(bare, msg_cls=ACK)
    assert msg.MSA.msa_1 == "AA"


def test_strict_missing_msa_raises() -> None:
    # Build XML with MSA omitted directly so we can test decode_xml strict behaviour.
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<ACK xmlns="urn:hl7-org:v2xml">'
        "<MSH>"
        "<MSH.1>|</MSH.1><MSH.2>^~\\&amp;</MSH.2>"
        "<MSH.3><HD.1>SEND</HD.1></MSH.3>"
        "<MSH.9><MSG.1>ACK</MSG.1></MSH.9>"
        "<MSH.10>MSG001</MSH.10>"
        "<MSH.11><PT.1>P</PT.1></MSH.11>"
        "<MSH.12><VID.1>2.5.1</VID.1></MSH.12>"
        "<MSH.7><TS.1>20240101120000</TS.1></MSH.7>"
        "</MSH>"
        "</ACK>"
    )
    with pytest.raises(ValidationError):
        decode_xml(xml, msg_cls=ACK, strict=True)


def test_lenient_missing_msa_warns_and_injects_placeholder() -> None:
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<ACK xmlns="urn:hl7-org:v2xml">'
        "<MSH>"
        "<MSH.1>|</MSH.1><MSH.2>^~\\&amp;</MSH.2>"
        "<MSH.3><HD.1>SEND</HD.1></MSH.3>"
        "<MSH.9><MSG.1>ACK</MSG.1></MSH.9>"
        "<MSH.10>MSG001</MSH.10>"
        "<MSH.11><PT.1>P</PT.1></MSH.11>"
        "<MSH.12><VID.1>2.5.1</VID.1></MSH.12>"
        "<MSH.7><TS.1>20240101120000</TS.1></MSH.7>"
        "</MSH>"
        "</ACK>"
    )
    with pytest.warns(UserWarning, match=r"MSA.*strict=False"):
        msg = decode_xml(xml, msg_cls=ACK, strict=False)
    assert msg.MSA.model_fields_set == set()


def test_auto_detects_adt_a01_class(adt_xml: str) -> None:
    msg = decode_xml(adt_xml, strict=False)
    assert isinstance(msg, ADT_A01)


def test_pid_nested_composite(adt_xml: str) -> None:
    msg = decode_xml(adt_xml, strict=False)
    name = msg.PID.pid_5[0]             # type: ignore[index, union-attr]
    assert name.xpn_1.fn_1 == "Doe"    # type: ignore[union-attr]
    assert name.xpn_2 == "John"
    assert name.xpn_3 == "A"


def test_pid_demographics(adt_xml: str) -> None:
    msg = decode_xml(adt_xml, strict=False)
    assert msg.PID.pid_8 == "M"         # type: ignore[union-attr]


def test_repeating_nk1_segments(adt_xml: str) -> None:
    msg = decode_xml(adt_xml, strict=False)
    assert len(msg.NK1) == 2                            # type: ignore[arg-type]
    assert msg.NK1[0].nk1_2[0].xpn_2 == "Jane"        # type: ignore[index, union-attr]
    assert msg.NK1[1].nk1_2[0].xpn_2 == "Bob"         # type: ignore[index, union-attr]


def test_pv1_fields(adt_xml: str) -> None:
    msg = decode_xml(adt_xml, strict=False)
    assert msg.PV1.pv1_2 == "I"         # type: ignore[union-attr]


def test_repeating_al1_segments(adt_xml: str) -> None:
    msg = decode_xml(adt_xml, strict=False)
    assert len(msg.AL1) == 1                                # type: ignore[arg-type]
    assert msg.AL1[0].al1_3.ce_1 == "PENICILLIN"           # type: ignore[index, union-attr]


def test_dg1_segment(adt_xml: str) -> None:
    msg = decode_xml(adt_xml, strict=False)
    assert msg.DG1[0].dg1_3.ce_1 == "J18.9"               # type: ignore[index, union-attr]


def test_procedure_group(adt_xml: str) -> None:
    msg = decode_xml(adt_xml, strict=False)
    assert len(msg.PROCEDURE) == 1                          # type: ignore[arg-type]
    assert msg.PROCEDURE[0].PR1.pr1_3.ce_1 == "88.72"      # type: ignore[index, union-attr]


def test_insurance_group(adt_xml: str) -> None:
    msg = decode_xml(adt_xml, strict=False)
    assert len(msg.INSURANCE) == 1                                  # type: ignore[arg-type]
    assert msg.INSURANCE[0].IN1.in1_4[0].xon_1 == "BLUE CROSS"     # type: ignore[index, union-attr]


def test_insurance_group_in2(adt_xml: str) -> None:
    msg = decode_xml(adt_xml, strict=False)
    assert msg.INSURANCE[0].IN2.in2_1[0].cx_1 == "MEMBER-001"      # type: ignore[index, union-attr]


def test_ack_roundtrip() -> None:
    original = decode_er7(ACK_WIRE)
    msg = decode_xml(encode_xml(original))

    assert msg.MSH.msh_10 == original.MSH.msh_10
    assert msg.MSH.msh_3.hd_1 == original.MSH.msh_3.hd_1   # type: ignore[union-attr]
    assert msg.MSH.msh_12.vid_1 == original.MSH.msh_12.vid_1 # type: ignore[union-attr]
    assert msg.MSA.msa_1 == original.MSA.msa_1
    assert msg.MSA.msa_2 == original.MSA.msa_2


def test_adt_a01_roundtrip() -> None:
    original = decode_er7(ADT_A01_WIRE, msg_cls=ADT_A01, strict=False)
    msg = decode_xml(encode_xml(original), strict=False)

    assert msg.MSH.msh_10 == original.MSH.msh_10
    assert msg.PID.pid_5[0].xpn_1.fn_1 == original.PID.pid_5[0].xpn_1.fn_1    # type: ignore[index, union-attr]
    assert msg.PID.pid_8 == original.PID.pid_8                                  # type: ignore[union-attr]
    assert msg.PV1.pv1_2 == original.PV1.pv1_2                                 # type: ignore[union-attr]
    assert len(msg.NK1) == len(original.NK1)                                    # type: ignore[arg-type]
    assert len(msg.PROCEDURE) == len(original.PROCEDURE)                        # type: ignore[arg-type]
    assert len(msg.INSURANCE) == len(original.INSURANCE)                        # type: ignore[arg-type]


TRUNCATION_27_WIRE = (
    "MSH|^~\\&#|SEND|FAC|RECV|FAC|20240101120000||ADT^A01^ADT_A01|MSG001|P|2.7\r"
    "EVN|A01|20240101120000\r"
    "PID|1||12345^^^FAC^MR||Smith#\r"
    "PV1|1|I\r"
)


@pytest.fixture
def adt27_xml() -> str:
    from hl7types.hl7.v2_7.messages.ADT_A01 import ADT_A01 as ADT_A01_27
    msg = decode_er7(TRUNCATION_27_WIRE, msg_cls=ADT_A01_27)
    return encode_xml(msg)


def test_msh2_preserved_with_truncation_char(adt27_xml: str) -> None:
    msg = decode_xml(adt27_xml, strict=False)
    assert msg.MSH.msh_2 == "^~\\&#"


def test_truncation_stripped_from_field_value(adt27_xml: str) -> None:
    import re
    xml_with_trunc = re.sub(r"<FN\.1>Smith</FN\.1>", "<FN.1>Smith#</FN.1>", adt27_xml)
    msg = decode_xml(xml_with_trunc, strict=False)
    assert msg.PID.pid_5[0].xpn_1.fn_1 == "Smith"  # type: ignore[index, union-attr]


def test_no_truncation_in_pre_v27_message(ack_xml: str) -> None:
    assert _extract_truncation(ET.fromstring(ack_xml)) == ""
