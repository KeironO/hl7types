"""ER7 parsing of ADT^A31 (sharing the ADT_A05 structure), CX identifier decoding,
and ampersand escape / unescape round-trip contracts."""
from __future__ import annotations

import pytest

from hl7types import decode_er7
from hl7types.codecs.er7.decoder import _unescape
from hl7types.codecs.er7.encoder import DEFAULT_ENCODING, _escape
from hl7types.hl7.v2_5.messages.ADT_A05 import ADT_A05

ENC = DEFAULT_ENCODING

# From testMessageSetAppropriatelyForParse. v2.5 ADT^A31 reuses the ADT_A05 structure.
ADT_A31_WIRE = (
    "MSH|^~\\&|||||200803051508||ADT^A31|2|P|2.5\r"
    "EVN||200803051509\r"
    "PID|||ZZZZZZ83M64Z148R^^^SSN^SSN^^20070103\r"
)

# From testAmpersandCorrectlyParsed (marked @Ignore in HAPI due to a known bug there).
# OBX.5 of OBX segment 2 contains a literal & that must encode as \T\ and decode back.
AMPERSAND_WIRE = (
    "MSH|^~\\&|OADD||DADD||20090511130702||ORU^R01|91310000023|P|2.3\n"
    "PID|||2278111^^^6||CSCXBOB^LAB^||19480205|M|^^||^^, ^^|||||||||\n"
    "PV1||O|CSC^||||2499^LAST^^FIRST I MD|^||||||||||OP|35848990||||||||||||||||||||6|||||200904130000|200904140000|\n"
    "ORC|RE|59761179|M3541||||^^^200905110800|||||2499^LAST^^FIRST I MD||||^|\n"
    "OBR|1|59761179|M3541^OADD|CR^Cell study|||200905110800||||||||^|2499^LAST^^FIRST I MD||||||||H|F||^^^^^R|^||||^^|^^||\n"
    "OBX|1|ST|CR^Cell study|1|(note)||||||F|||200905111306|MMC^Tacoma General H|7^LASTNAME^FIRSTNAME|\n"
    "OBX|2|ST|CR^Cell study|1|WBCS: Adequate in number & normal in appearance||||||F|||200905111306|MMC^Tacoma General H|7^LASTNAME^FIRSTNAME|\n"
    "OBX|3|ST|CR^Cell study|1|RBC: Occasional \"target\" cells||||||F|||200905111306|MMC^Tacoma General H|7^LASTNAME^FIRSTNAME|\n"
)


def test_adt_a31_decodes_using_adt_a05_structure() -> None:
    # ADT_A31_WIRE has no PV1; lenient mode injects a placeholder and warns.
    with pytest.warns(UserWarning, match=r"PV1"):
        msg = ADT_A05.model_validate_er7(ADT_A31_WIRE)
    assert isinstance(msg, ADT_A05)
    assert msg.MSH.msh_9.msg_1 == "ADT"    # type: ignore[union-attr]
    assert msg.MSH.msh_9.msg_2 == "A31"    # type: ignore[union-attr]
    assert msg.MSH.msh_10 == "2"
    assert msg.MSH.msh_11.pt_1 == "P"      # type: ignore[union-attr]
    assert msg.MSH.msh_12.vid_1 == "2.5"   # type: ignore[union-attr]


def test_parse_adt_a31_pid_cx() -> None:
    with pytest.warns(UserWarning, match=r"PV1"):
        msg = ADT_A05.model_validate_er7(ADT_A31_WIRE)
    pid3 = msg.PID.pid_3[0]  # type: ignore[union-attr]
    assert pid3.cx_1 == "ZZZZZZ83M64Z148R"
    assert pid3.cx_4.hd_1 == "SSN"  # type: ignore[union-attr]
    assert pid3.cx_5 == "SSN"


def test_ampersand_escaped_in_encode() -> None:
    assert _escape("WBCS: Adequate in number & normal in appearance", ENC) == (
        "WBCS: Adequate in number \\T\\ normal in appearance"
    )


def test_ampersand_escape_decodes_to_literal_ampersand() -> None:
    assert _unescape(r"number \T\ normal", ENC) == "number & normal"


def test_ampersand_roundtrip() -> None:
    msg = decode_er7(AMPERSAND_WIRE)
    # v2.3 ORU_R01 group path: RESPONSE > ORDER_OBSERVATION > OBSERVATION
    obx2 = msg.RESPONSE[0].ORDER_OBSERVATION[0].OBSERVATION[1].OBX  # type: ignore[index, union-attr]
    assert obx2.obx_5[0] == "WBCS: Adequate in number & normal in appearance"  # type: ignore[index, union-attr]

    encoded = msg.model_dump_er7()
    assert "\\T\\ normal in appearance" in encoded
    assert "number & normal" not in encoded
