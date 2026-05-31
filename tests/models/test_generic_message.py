"""
Tests emulating ca.uhn.hl7v2.model.GenericMessageTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-core/src/test/java/ca/uhn/hl7v2/model/GenericMessageTest.java
"""
from __future__ import annotations

from hl7types import decode_er7


def test_decode_v22_message() -> None:
    """HL7 v2.2 messages should be decodable.

    A message with version 2.2 should parse successfully.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||19951002185200||ADT^A01|LABGL1199510021852632|P|2.2\r"
        "EVN|A01|19951002185200\r"
        "PID|||T12345||TEST^PATIENT^P||19601002|M||||||||||123456\r"
        "PV1||I|NER\r"
    )

    msg = decode_er7(msg_text)
    assert msg is not None
    assert msg.MSH.msh_12 == "2.2"


def test_decode_v23_message() -> None:
    """HL7 v2.3 messages should be decodable.

    A message with version 2.3 should parse successfully.
    """
    msg_text = (
        "MSH|^~\\&|ULTRA|TML|OLIS|OLIS|200905011130||ORU^R01|20169838|T|2.3\r"
        "PID|||7005728^^^TML^MR||TEST^RACHEL^DIAMOND||19310313|F|||200 ANYWHERE ST^^TORONTO^ON^M6G 2T9||(416)888-8888||||||1014071185^KR\r"
        "PV1|1|O|OLIS||||OLIST^BLAKE^DONALD^THOR^^^^^921379^^^^OLIST\r"
        "ORC|RE||T09-100442-RET-0^^OLIS_Site_ID^ISO||||^^^200905011106|||||OLIST^BLAKE^DONALD^THOR^^^^L^921379\r"
        "OBR|0||T09-100442-RET-0^^OLIS_Site_ID^ISO|RET^RETICULOCYTE COUNT^HL79901 literal|||200905011106|||||||200905011106||OLIST^BLAKE^DONALD^THOR^^^^L^921379||7870279|7870279|T09-100442|MOHLTC|200905011130||B7|F||1^^^200905011106^^R\r"
        "OBX|1|ST|RET^RETICULOCYTE COUNT^HL79901||one||||||F\r"
    )

    msg = decode_er7(msg_text)
    assert msg is not None
    assert msg.MSH.msh_12 == "2.3"


def test_decode_v24_message() -> None:
    """HL7 v2.4 messages should be decodable.

    A message with version 2.4 should parse successfully.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||20010602185200||ADT^A01|LABGL1200106021852632|P|2.4\r"
        "EVN|A01|20010602185200\r"
        "PID|||T12345||TEST^PATIENT^P||19601002|M||||||||||123456\r"
        "PV1||I|NER\r"
    )

    msg = decode_er7(msg_text)
    assert msg is not None
    assert msg.MSH.msh_12.vid_1 == "2.4"


def test_decode_v25_message() -> None:
    """HL7 v2.5 messages should be decodable.

    A message with version 2.5 should parse successfully.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||20010602185200||ADT^A01|LABGL1200106021852632|P|2.5\r"
        "EVN|A01|20010602185200\r"
        "PID|||T12345||TEST^PATIENT^P||19601002|M||||||||||123456\r"
        "PV1||I|NER\r"
    )

    msg = decode_er7(msg_text)
    assert msg is not None
    assert msg.MSH.msh_12.vid_1 == "2.5"


def test_decode_v251_message() -> None:
    """HL7 v2.5.1 messages should be decodable.

    A message with version 2.5.1 should parse successfully.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||20010602185200||ADT^A01|LABGL1200106021852632|P|2.5.1\r"
        "EVN|A01|20010602185200\r"
        "PID|||T12345||TEST^PATIENT^P||19601002|M||||||||||123456\r"
        "PV1||I|NER\r"
    )

    msg = decode_er7(msg_text)
    assert msg is not None
    assert msg.MSH.msh_12.vid_1 == "2.5.1"
