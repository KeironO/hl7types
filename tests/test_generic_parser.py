"""
Tests emulating ca.uhn.hl7v2.parser.GenericParserTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-test/src/test/java/ca/uhn/hl7v2/parser/GenericParserTest.java

Notes:
- testMessageSetAppropriatelyForParse: the XML round-trip half is not applicable (hl7types
  has no XML decoder). ADT_A31 has no dedicated model; it shares the ADT_A05 structure
  per the HL7 v2.5 spec, so ADT_A05 is used for decoding.
- testAmpersandCorrectlyParsed: marked @Ignore in HAPI due to a known bug. hl7types
  handles & -> \\T\\ correctly, so this is a positive assertion of correct behaviour.
"""
from __future__ import annotations

from hl7types import decode_er7
from hl7types.codecs.er7.encoder import _escape, DEFAULT_ENCODING as ENC
from hl7types.hl7.v2_5.messages.ADT_A05 import ADT_A05

# Wire taken verbatim from testMessageSetAppropriatelyForParse.
# ADT^A31 uses the ADT_A05 structure in v2.5.
ADT_A31_WIRE = (
    "MSH|^~\\&|||||200803051508||ADT^A31|2|P|2.5\r"
    "EVN||200803051509\r"
    "PID|||ZZZZZZ83M64Z148R^^^SSN^SSN^^20070103\r"
)

# Wire taken verbatim from testAmpersandCorrectlyParsed (Java println → \n line endings).
# OBX.5 contains a literal & which must be escaped to \T\ on re-encode.
AMPERSAND_WIRE = (
    "MSH|^~\\&|OADD||DADD||20090511130702||ORU^R01|91310000023|P|2.3||||\n"
    "PID|||2278111^^^6||CSCXBOB^LAB^||19480205|M|^^||^^, ^^|||||||||\n"
    "PV1||O|CSC^||||2499^LAST^^FIRST I MD|^||||||||||OP|35848990||||||||||||||||||||6|||||200904130000|200904140000|\n"
    "ORC|RE|59761179|M3541|||||||||2499^LAST^^FIRST I MD||||^|\n"
    "OBR|1|59761179|M3541^OADD|CR^Cell study|||200905110800||||||||^|2499^LAST^^FIRST I MD||||||||H|F||^^^^^R|^||||^^|^^||\n"
    "OBX|1|ST|CR^Cell study|1|(note)||||||F|||200905111306|MMC^Tacoma General H|7^LASTNAME^FIRSTNAME|\n"
    "OBX|2|ST|CR^Cell study|1|WBCS: Adequate in number & normal in appearance||||||F|||200905111306|MMC^Tacoma General H|7^LASTNAME^FIRSTNAME|\n"
    "OBX|3|ST|CR^Cell study|1|RBC: Occasional \"target\" cells||||||F|||200905111306|MMC^Tacoma General H|7^LASTNAME^FIRSTNAME|\n"
)


def test_parse_adt_a31_decodes() -> None:
    """ER7 decode of an ADT A31 wire must succeed (testMessageSetAppropriatelyForParse)."""
    msg = ADT_A05.model_validate_er7(ADT_A31_WIRE)
    assert isinstance(msg, ADT_A05)
    assert msg.MSH.msh_10 == "2"


def test_parse_adt_a31_pid_cx() -> None:
    """PID.3 with 7-component CX value decodes the ID and assigning authority."""
    msg = ADT_A05.model_validate_er7(ADT_A31_WIRE)
    pid3 = msg.PID.pid_3[0]  # type: ignore[union-attr]
    assert pid3.cx_1 == "ZZZZZZ83M64Z148R"
    assert pid3.cx_4.hd_1 == "SSN"  # type: ignore[union-attr]
    assert pid3.cx_5 == "SSN"


def test_ampersand_escaped_in_encode() -> None:
    """& (subcomponent separator) in data must encode to \\T\\ (testAmpersandCorrectlyParsed, @Ignore in HAPI)."""
    assert _escape("WBCS: Adequate in number & normal in appearance", ENC) == (
        "WBCS: Adequate in number \\T\\ normal in appearance"
    )


def test_ampersand_roundtrip() -> None:
    """& in OBX.5 survives decode → re-encode as \\T\\ (testAmpersandCorrectlyParsed, @Ignore in HAPI)."""
    msg = decode_er7(AMPERSAND_WIRE)
    encoded = msg.model_dump_er7()
    assert "\\T\\ normal in appearance" in encoded
    assert "number & normal" not in encoded
