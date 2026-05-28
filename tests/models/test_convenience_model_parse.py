"""
Tests emulating ca.uhn.hl7v2.model.ConvenienceModelParseTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-core/src/test/java/ca/uhn/hl7v2/model/ConvenienceModelParseTest.java
"""
from __future__ import annotations

from hl7types import decode_er7


def test_message_parse_roundtrip() -> None:
    """Parse an ORU_R01 message and verify roundtrip encoding.

    When a message is parsed from ER7 and re-encoded, the result should
    match the original message structure.
    """
    msg_text = (
        "MSH|^~\\&|ULTRA|TML|OLIS|OLIS|200905011130||ORU^R01|20169838|T|2.3\r"
        "PID|||7005728^^^TML^MR||TEST^RACHEL^DIAMOND||19310313|F|||200 ANYWHERE ST^^TORONTO^ON^M6G 2T9||(416)888-8888||||||1014071185^KR\r"
        "PV1|1||OLIS||||OLIST^BLAKE^DONALD^THOR^^^^^921379^^^^OLIST\r"
        "ORC|RE||T09-100442-RET-0^^OLIS_Site_ID^ISO|||||||||OLIST^BLAKE^DONALD^THOR^^^^L^921379\r"
        "OBR|0||T09-100442-RET-0^^OLIS_Site_ID^ISO|RET^RETICULOCYTE COUNT^HL79901 literal|||200905011106|||||||200905011106||OLIST^BLAKE^DONALD^THOR^^^^L^921379||7870279|7870279|T09-100442|MOHLTC|200905011130||B7|F||1^^^200905011106^^R\r"
        "OBX|1|NM|Z114099^Erc^L||4.00|tril/L|3.90-5.60||||F|||200905011111|PMH\r"
    )

    msg = decode_er7(msg_text)

    # Verify message was parsed
    assert msg.MSH is not None
    assert msg.MSH.msh_10 == "20169838"

    # Verify roundtrip encoding contains key elements
    encoded = msg.model_dump_er7()
    assert "20169838" in encoded
    assert "PID|" in encoded
    assert "OBX|" in encoded
