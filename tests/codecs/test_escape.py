"""
Tests emulating ca.uhn.hl7v2.parser.EscapeTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-test/src/test/java/ca/uhn/hl7v2/parser/EscapeTest.java
"""
from __future__ import annotations

from pathlib import Path

from hl7types import decode_er7
from hl7types.codecs.er7.decoder import _unescape
from hl7types.codecs.er7.encoder import DEFAULT_ENCODING, _escape

ENC = DEFAULT_ENCODING

RESOURCES = Path(__file__).parent / "resources"

# Wire from EscapeTest.testFormattingCharacters2 (taken verbatim).
# OBX.5 contains \.br\, \H\, \N\, \S\ presentation escapes.
FORMATTING_WIRE = (
    "MSH|^~\\&|PHCN_ULTRA|2220|HSIE|2220|201106161233||ORU^R01|72313573|T|2.4|||AL|AL|AU\r"
    "OBR|1|^HNAM_ORDERID|11-6879530-GAS-0^PHCN_ULTRA|GAS^GASES (BLOOD)|||201106161000\r"
    "OBX|1|FT|GAS^^LN||Biochemistry (Whole Blood Sample) - Type Venous\\.br\\\\.br\\"
    " Analysis Date : 16/06/2011\\.br\\ pCO2 : \\H\\ 117\\N\\ mmHg (35-45)"
    " (37 \\S\\o C)|||A|||F"
)


# --- unit-level escape / unescape ---

def test_simple_escape() -> None:
    """^ in data encodes to \\S\\ (EscapeTest.testSimpleEscape)."""
    result = _escape("GLUCOSE^1H POST 75 G GLUCOSE PO:SCNC:PT:SER/PLAS:QN", ENC)
    assert result == "GLUCOSE\\S\\1H POST 75 G GLUCOSE PO:SCNC:PT:SER/PLAS:QN"


def test_truncation_escape() -> None:
    """# is not an HL7 escape character and must pass through unchanged (EscapeTest.testTruncationEscape)."""
    assert _escape("Truncation#escape", ENC) == "Truncation#escape"


def test_preserve_formatting_chars_encode() -> None:
    """\\H\\, \\N\\, \\C00FF\\, \\.br\\ are presentation escapes and must survive _escape verbatim (EscapeTest.testPreserveFormattingChars)."""
    assert _escape("H \\H\\ N \\N\\ ", ENC) == "H \\H\\ N \\N\\ "
    assert _escape("H \\C00FF\\ N", ENC) == "H \\C00FF\\ N"
    assert _escape("Line 1\\.br\\Line 2", ENC) == "Line 1\\.br\\Line 2"


def test_bare_backslash_is_escaped() -> None:
    """A backslash that is NOT part of an escape sequence must be encoded as \\E\\."""
    assert _escape("C:\\Users", ENC) == "C:\\E\\Users"


def test_unescape_known_sequences() -> None:
    assert _unescape("\\F\\", DEFAULT_ENCODING) == "|"
    assert _unescape("\\S\\", DEFAULT_ENCODING) == "^"
    assert _unescape("\\R\\", DEFAULT_ENCODING) == "~"
    assert _unescape("\\T\\", DEFAULT_ENCODING) == "&"
    assert _unescape("\\E\\", DEFAULT_ENCODING) == "\\"


def test_unescape_preserves_unknown_sequences() -> None:
    """\\H\\, \\N\\, \\.br\\, \\X0D\\ are not in the map and must pass through unchanged."""
    for seq in ("\\H\\", "\\N\\", "\\.br\\", "\\X0D\\", "\\C00FF\\"):
        assert _unescape(seq, DEFAULT_ENCODING) == seq


def test_unescape_uuencoded_real_data() -> None:
    """Real-world uuencoded payload must not raise (EscapeTest.testUnescape).

    The file contains genuine HL7 delimiter escapes (\\S\\, \\T\\, \\E\\) so the
    result is not identical to the input — the test guards against exceptions,
    not identity.
    """
    content = (RESOURCES / "uuencoded_escaped.txt").read_text(encoding="latin-1")
    result = _unescape(content, DEFAULT_ENCODING)
    assert isinstance(result, str)


# --- message-level round-trip ---

def test_formatting_chars_roundtrip() -> None:
    """Presentation escapes in OBX.5 FT data survive decode to re-encode (EscapeTest.testFormattingCharacters2)."""
    msg = decode_er7(FORMATTING_WIRE)
    encoded = msg.model_dump_er7()
    msg2 = decode_er7(encoded)

    obx1 = msg.PATIENT_RESULT[0].ORDER_OBSERVATION[0].OBSERVATION[0].OBX  # type: ignore[index, union-attr]
    obx2 = msg2.PATIENT_RESULT[0].ORDER_OBSERVATION[0].OBSERVATION[0].OBX  # type: ignore[index, union-attr]

    assert obx1.obx_5 == obx2.obx_5
    assert "\\H\\" in encoded
    assert "\\N\\" in encoded
    assert "\\.br\\" in encoded


def test_decode_preserves_presentation_escapes_but_unescapes_delimiters() -> None:
    """\\H\\, \\N\\, \\.br\\ in OBX.5 are intact after decoding; \\S\\ is correctly unescaped to ^."""
    msg = decode_er7(FORMATTING_WIRE)
    obx5_value: str = msg.PATIENT_RESULT[0].ORDER_OBSERVATION[0].OBSERVATION[0].OBX.obx_5[0]  # type: ignore[index, union-attr]

    assert "\\H\\" in obx5_value
    assert "\\N\\" in obx5_value
    assert "\\.br\\" in obx5_value
    assert "^o C" in obx5_value  # \S\ correctly unescaped to ^
