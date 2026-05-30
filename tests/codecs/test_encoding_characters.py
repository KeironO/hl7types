"""
Tests emulating ca.uhn.hl7v2.parser.EncodingCharactersTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-test/src/test/java/ca/uhn/hl7v2/parser/EncodingCharactersTest.java
"""
from __future__ import annotations

import pytest

import hl7types  # noqa: F401
from hl7types import decode_er7
from hl7types.codecs.er7.encoder import EncodingChars

# Wire string taken verbatim from EncodingCharactersTest.testValidateMSH2.
# MSH.2 is "~\&" only 3 chars instead of the required 4.
INVALID_MSH2_WIRE = (
    "MSH|~\\&|PHCN_ULTRA|2220|HSIE|2220|201106161233||ORU^R01|72313573|T|2.4|||AL|AL|AU\r\n"
    "PV1||I|^DIS^DIS^2220|||||0129296H^BRAUN^GARY|7MPH^MPH-HL7-RESULT FEED|||||||||I|^^^2220\r\n"
    "ORC|RE|^HNAM_ORDERID|11-6879530-GAS-0^PHCN_ULTRA||RE\r\n"
    "OBR|1|^HNAM_ORDERID|11-6879530-GAS-0^PHCN_ULTRA|GAS^GASES (BLOOD)|||201106161000\r\n"
    "OBX|1|FT|GAS^^LN||test value||A||||F"
)

# Same message but with a valid 4-char MSH.2, using \r\n line endings.
VALID_CRLF_WIRE = (
    "MSH|^~\\&|PHCN_ULTRA|2220|HSIE|2220|201106161233||ORU^R01|72313573|T|2.4|||AL|AL|AU\r\n"
    "PID|1||123456^^^2220^MR||Smith^John\r\n"
    "PV1||I|^DIS^DIS^2220\r\n"
    "OBR|1|^HNAM_ORDERID|11-6879530-GAS-0^PHCN_ULTRA|GAS^GASES (BLOOD)|||201106161000\r\n"
    "OBX|1|FT|GAS^^LN||test value||A||||F"
)


def test_invalid_msh2_raises() -> None:
    """A 3-char MSH.2 must raise rather than silently fall back to defaults."""
    with pytest.raises(ValueError, match="MSH.2 must be exactly 4 encoding characters"):
        decode_er7(INVALID_MSH2_WIRE)


def test_from_msh2_raises_on_short_string() -> None:
    with pytest.raises(ValueError):
        EncodingChars.from_msh2("~\\&")


def test_crlf_line_endings_accepted() -> None:
    """\\r\\n line endings (common in real-world systems) must parse without error."""
    from hl7types.hl7.v2_4.messages.ORU_R01 import ORU_R01

    msg = decode_er7(VALID_CRLF_WIRE)
    assert isinstance(msg, ORU_R01)
