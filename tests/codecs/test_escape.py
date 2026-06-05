"""ER7 escape / unescape contracts: delimiter encoding, presentation-escape
preservation, and round-trip fidelity through message-level encode and decode."""
from __future__ import annotations

from pathlib import Path

import pytest

from hl7types import decode_er7
from hl7types.codecs.er7.decoder import _unescape
from hl7types.codecs.er7.encoder import DEFAULT_ENCODING, _escape

ENC = DEFAULT_ENCODING

RESOURCES = Path(__file__).parent / "resources"

# OBX.5 carries \.br\, \H\, \N\ presentation escapes and a \S\ delimiter escape.
FORMATTING_WIRE = (
    "MSH|^~\\&|PHCN_ULTRA|2220|HSIE|2220|201106161233||ORU^R01|72313573|T|2.4|||AL|AL|AU\r"
    "OBR|1|^HNAM_ORDERID|11-6879530-GAS-0^PHCN_ULTRA|GAS^GASES (BLOOD)|||201106161000\r"
    "OBX|1|FT|GAS^^LN||Biochemistry (Whole Blood Sample) - Type Venous\\.br\\\\.br\\"
    " Analysis Date : 16/06/2011\\.br\\ pCO2 : \\H\\ 117\\N\\ mmHg (35-45)"
    " (37 \\S\\o C)|||A|||F"
)


def test_escape_encodes_component_separator() -> None:
    result = _escape("GLUCOSE^1H POST 75 G GLUCOSE PO:SCNC:PT:SER/PLAS:QN", ENC)
    assert result == "GLUCOSE\\S\\1H POST 75 G GLUCOSE PO:SCNC:PT:SER/PLAS:QN"


def test_escape_passes_through_non_delimiter_hash() -> None:
    assert _escape("Truncation#escape", ENC) == "Truncation#escape"


def test_escape_preserves_existing_escape_sequences() -> None:
    assert _escape("H \\H\\ N \\N\\ ", ENC) == "H \\H\\ N \\N\\ "
    assert _escape("H \\C00FF\\ N", ENC) == "H \\C00FF\\ N"
    assert _escape("Line 1\\.br\\Line 2", ENC) == "Line 1\\.br\\Line 2"


def test_escape_encodes_bare_backslash() -> None:
    assert _escape("C:\\Users", ENC) == "C:\\E\\Users"


@pytest.mark.parametrize("escaped,expected", [
    ("\\F\\", "|"),
    ("\\S\\", "^"),
    ("\\R\\", "~"),
    ("\\T\\", "&"),
    ("\\E\\", "\\"),
], ids=["F", "S", "R", "T", "E"])
def test_unescape_delimiter_sequences(escaped: str, expected: str) -> None:
    assert _unescape(escaped, ENC) == expected


def test_unescape_preserves_presentation_escape_sequences() -> None:
    for seq in ("\\H\\", "\\N\\", "\\.br\\", "\\X0D\\", "\\C00FF\\"):
        assert _unescape(seq, ENC) == seq


def test_unescape_real_world_payload_decodes_delimiters_and_preserves_hex_escapes() -> None:
    content = (RESOURCES / "uuencoded_escaped.txt").read_text(encoding="latin-1")

    result = _unescape(content, ENC)

    assert "\\S\\" in content
    assert "\\X0D\\" in content
    assert result.count("^") > content.count("^")  # \S\ sequences decoded to ^
    assert "\\X0D\\" in result


def test_formatting_chars_roundtrip() -> None:
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
    msg = decode_er7(FORMATTING_WIRE)
    obx = msg.PATIENT_RESULT[0].ORDER_OBSERVATION[0].OBSERVATION[0].OBX  # type: ignore[index, union-attr]
    obx5_value: str = obx.obx_5[0]  # type: ignore[index, union-attr]

    assert "\\H\\" in obx5_value
    assert "\\N\\" in obx5_value
    assert "\\.br\\" in obx5_value
    assert "^o C" in obx5_value  # \S\ correctly unescaped to ^
