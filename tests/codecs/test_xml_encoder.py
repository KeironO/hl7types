"""Tests for hl7types.codecs.xml.encoder."""
from __future__ import annotations

import typing
from xml.etree import ElementTree as ET

import pytest
from pydantic import BaseModel

from hl7types import decode_er7, encode_xml
from hl7types.codecs.xml.encoder import (
    _field_pos,
    _group_xml_tag,
    _is_model,
    _is_segment_cls,
    _unwrap,
)


_ACK_WIRE = (
    "MSH|^~\\&|SEND|FAC|RECV|FAC|20240101120000||ACK|MSG001|P|2.5.1\r"
    "MSA|AA|MSG001\r"
)

_ADT_A01_WIRE = (
    "MSH|^~\\&|SEND|FAC|RECV|FAC|20240101120000||ADT^A01|MSG002|P|2.5.1\r"
    "EVN|A01|20240101120000\r"
    "PID|1||12345||DOE^JOHN\r"
    "PV1|1|I\r"
    "PR1|1||88.72^EEG^I9C||20240101120000\r"
)


def test_group_xml_tag_converts_last_underscore():
    class ADT_A01_PROCEDURE:
        pass
    assert _group_xml_tag(ADT_A01_PROCEDURE) == "ADT_A01.PROCEDURE"


def test_group_xml_tag_no_underscore_returns_name():
    class NOUNDER:
        pass
    assert _group_xml_tag(NOUNDER) == "NOUNDER"


def test_field_pos_with_dot():
    assert _field_pos("MSH.9") == 9


def test_field_pos_multi_digit():
    assert _field_pos("PID.12") == 12


def test_field_pos_no_dot():
    assert _field_pos("MSH") == 0


def test_field_pos_non_digit_suffix():
    assert _field_pos("foo.bar") == 0

def test_unwrap_optional_returns_inner():
    inner, is_list = _unwrap(typing.Optional[str])
    assert inner is str
    assert is_list is False


def test_unwrap_list_returns_inner_and_is_list():
    inner, is_list = _unwrap(typing.List[str])
    assert inner is str
    assert is_list is True


def test_unwrap_bare_type_unchanged():
    inner, is_list = _unwrap(str)
    assert inner is str
    assert is_list is False


def test_unwrap_optional_list():
    inner, is_list = _unwrap(typing.Optional[typing.List[str]])
    assert inner is str
    assert is_list is True

def test_is_model_true_for_basemodel_subclass():
    class MyModel(BaseModel):
        pass
    assert _is_model(MyModel) is True


def test_is_model_false_for_plain_class():
    assert _is_model(str) is False


def test_is_model_false_for_non_class():
    assert _is_model(42) is False

def test_is_segment_cls_true_for_segment():
    from hl7types.hl7.v2_5_1.segments.MSH import MSH
    assert _is_segment_cls(MSH.model_construct()) is True


def test_is_segment_cls_false_for_group():
    from hl7types.hl7.v2_5_1.groups.ADT_A01_PROCEDURE import ADT_A01_PROCEDURE
    assert _is_segment_cls(ADT_A01_PROCEDURE.model_construct()) is False



def test_encode_xml_segment_has_xml_declaration():
    from hl7types.hl7.v2_5_1.segments.MSA import MSA
    xml = encode_xml(MSA(msa_1="AA", msa_2="MSG001"))
    assert xml.startswith('<?xml version="1.0" encoding="UTF-8"?>')


def test_encode_xml_segment_root_tag_is_class_name():
    from hl7types.hl7.v2_5_1.segments.MSA import MSA
    xml = encode_xml(MSA(msa_1="AA", msa_2="MSG001"))
    root = ET.fromstring(xml[xml.index("<MSA"):])
    assert root.tag == "{urn:hl7-org:v2xml}MSA"


def test_encode_xml_segment_field_values():
    from hl7types.hl7.v2_5_1.segments.MSA import MSA
    xml = encode_xml(MSA(msa_1="AA", msa_2="MSG001"))
    root = ET.fromstring(xml[xml.index("<MSA"):])
    ns = "urn:hl7-org:v2xml"
    assert root.find(f"{{{ns}}}MSA.1").text == "AA"
    assert root.find(f"{{{ns}}}MSA.2").text == "MSG001"


def test_encode_xml_segment_excludes_none_fields():
    from hl7types.hl7.v2_5_1.segments.MSA import MSA
    xml = encode_xml(MSA(msa_1="AA", msa_2="MSG001"))
    assert "MSA.3" not in xml


def test_encode_xml_segment_nested_composite():
    from hl7types.hl7.v2_5_1.segments.MSH import MSH
    from hl7types.hl7.v2_5_1.datatypes.HD import HD
    from hl7types.hl7.v2_5_1.datatypes.MSG import MSG
    from hl7types.hl7.v2_5_1.datatypes.PT import PT
    from hl7types.hl7.v2_5_1.datatypes.TS import TS
    from hl7types.hl7.v2_5_1.datatypes.VID import VID
    msh = MSH(
        msh_3=HD(hd_1="SEND"),
        msh_5=HD(hd_1="RECV"),
        msh_7=TS(ts_1="20240101120000"),
        msh_9=MSG(msg_1="ACK"),
        msh_10="MSG001",
        msh_11=PT(pt_1="P"),
        msh_12=VID(vid_1="2.5.1"),
    )
    xml = encode_xml(msh)
    assert "<HD.1>SEND</HD.1>" in xml
    assert "<MSG.1>ACK</MSG.1>" in xml


def test_encode_xml_message_root_tag():
    msg = decode_er7(_ACK_WIRE)
    xml = encode_xml(msg)
    root = ET.fromstring(xml[xml.index("<ACK"):])
    assert root.tag == "{urn:hl7-org:v2xml}ACK"


def test_encode_xml_message_contains_segments():
    msg = decode_er7(_ACK_WIRE)
    xml = encode_xml(msg)
    assert "<MSH>" in xml
    assert "<MSA>" in xml


def test_encode_xml_message_msa_values():
    msg = decode_er7(_ACK_WIRE)
    xml = encode_xml(msg)
    assert "<MSA.1>AA</MSA.1>" in xml
    assert "<MSA.2>MSG001</MSA.2>" in xml


def test_encode_xml_message_default_namespace():
    msg = decode_er7(_ACK_WIRE)
    xml = encode_xml(msg)
    assert 'xmlns="urn:hl7-org:v2xml"' in xml


def test_encode_xml_message_custom_namespace():
    msg = decode_er7(_ACK_WIRE)
    xml = encode_xml(msg, namespace="urn:custom:ns")
    assert 'xmlns="urn:custom:ns"' in xml


def test_encode_xml_pretty_false_no_indentation():
    msg = decode_er7(_ACK_WIRE)
    xml = encode_xml(msg, pretty=False)
    assert "\n    " not in xml


def test_encode_xml_pretty_true_has_indentation():
    msg = decode_er7(_ACK_WIRE)
    xml = encode_xml(msg, pretty=True)
    assert "\n    " in xml


def test_encode_xml_message_with_group_uses_dot_tag():
    from hl7types.hl7.v2_5_1.messages.ADT_A01 import ADT_A01
    msg = decode_er7(_ADT_A01_WIRE, msg_cls=ADT_A01)
    xml = encode_xml(msg)
    assert "<ADT_A01.PROCEDURE>" in xml


def test_encode_xml_message_group_contains_segment():
    from hl7types.hl7.v2_5_1.messages.ADT_A01 import ADT_A01
    msg = decode_er7(_ADT_A01_WIRE, msg_cls=ADT_A01)
    xml = encode_xml(msg)
    assert "<PR1>" in xml
