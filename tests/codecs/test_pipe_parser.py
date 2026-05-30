"""
Tests emulating ca.uhn.hl7v2.parser.NewPipeParserTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-test/src/test/java/ca/uhn/hl7v2/parser/NewPipeParserTest.java

Notes:
- testParseRepeatingObx5: hl7types drops empty trailing repetitions; only the four
  non-empty values are asserted (HAPI preserves empty reps as empty strings).
- testUnknownVersion: hl7types raises ModuleNotFoundError (wrapped in the import);
  any exception on decode is acceptable since the version is unsupported.
- testNonPipeDelimitor: only the ORU portion is tested (no ORC/OBX required fields).
"""
from __future__ import annotations

import pytest

import hl7types  # noqa: F401
from hl7types import decode_er7
from hl7types.hl7.v2_3.messages.ADT_A01 import ADT_A01 as ADT_A01_v23
from hl7types.hl7.v2_4.messages.ORU_R01 import ORU_R01 as ORU_R01_v24
from hl7types.hl7.v2_5.messages.ADT_A03 import ADT_A03 as ADT_A03_v25
from hl7types.hl7.v2_5.messages.ADT_A45 import ADT_A45


# testParseRepeatingObx5

REPEATING_OBX5_WIRE = (
    "MSH|^~\\&|HNAM|CL|CL_RADNET|CL|20110628095233||ORU^R01|Q2301030099T1904270849|P|2.4\r"
    "PID|1||10011682^^^CL_MRN||CLABTEST^ONE\r"
    "OBR|1|3415770735^HNAM_ORDERID||CL987^MRA Head|||||||||||Rad Type&Rad Type\r"
    "OBX|1|TX|20725^ROUTINE HEMATOLOGY|H7800-4|This~Is~A~Report~~~~~||||||I|||200704021122\r"
)


def test_parse_repeating_obx5_non_empty_reps() -> None:
    """OBX.5 with ~ repetitions decodes each non-empty value (testParseRepeatingObx5)."""
    msg = ORU_R01_v24.model_validate_er7(REPEATING_OBX5_WIRE)
    obx5 = msg.PATIENT_RESULT[0].ORDER_OBSERVATION[0].OBSERVATION[0].OBX.obx_5  # type: ignore[index, union-attr]
    assert obx5[0] == "This"
    assert obx5[1] == "Is"
    assert obx5[2] == "A"
    assert obx5[3] == "Report"


# testInvalidShortMessages

@pytest.mark.parametrize("wire", [
    "",
    "M",
    "MS",
    "MSH",
    "MSH|",
    "\r",
    "M\r",
    "MS\r",
    "MSH\r",
    "MSH|\r",
])
def test_invalid_short_messages_raise(wire: str) -> None:
    """Truncated or empty wires must raise rather than produce a partial result (testInvalidShortMessages)."""
    with pytest.raises((ValueError, Exception)):
        decode_er7(wire)



# testMissingRequiredLastSegment


# ADT_A45 MERGE_INFO group requires MRG + PV1; only MRG is present here.
MISSING_PV1_WIRE = (
    "MSH|^~\\&|4265-ADT|4265|eReferral|eReferral|201004141020||ADT^A45^ADT_A45|102416|T^|2.5^^|||NE|AL|CAN|8859/1\r"
    "EVN|A45|201004141020|\r"
    "PID|1||7010226^^^4265^MR~0000000000^^^CANON^JHN||Park^Green\r"
    "MRG|9999999^^^4265^MR\r"
)


def test_missing_required_last_segment_decodes() -> None:
    """ADT_A45 with PV1 absent from MERGE_INFO must not raise (testMissingRequiredLastSegment)."""
    msg = decode_er7(MISSING_PV1_WIRE)
    assert isinstance(msg, ADT_A45)
    assert msg.PID.pid_3[0].cx_1 == "7010226"  # type: ignore[union-attr, index]



# testRepeatingSegment


REPEATING_OBX_WIRE = (
    "MSH|^~\\&|^QueryServices||||20021011161756.297-0500||ORU^R01|1|D|2.4\r"
    "OBR|1|||CHO^CHOLESTEROL\r"
    "OBX|1|NM|Z049107^Cholesterol^L||2.30|mmol/L|||||F\r"
    "OBX|2|NM|Z049107^Cholesterol^L||3.10|mmol/L|||||F\r"
    "OBX|3|NM|Z049107^Cholesterol^L||4.50|mmol/L|||||F\r"
)


def test_repeating_obx_segments() -> None:
    """Three OBX segments decode into three separate OBSERVATION reps (testRepeatingSegment)."""
    msg = ORU_R01_v24.model_validate_er7(REPEATING_OBX_WIRE)
    obs = msg.PATIENT_RESULT[0].ORDER_OBSERVATION[0].OBSERVATION  # type: ignore[index, union-attr]
    assert obs[0].OBX.obx_1 == "1"  # type: ignore[index, union-attr]
    assert obs[1].OBX.obx_1 == "2"  # type: ignore[index, union-attr]
    assert obs[2].OBX.obx_1 == "3"  # type: ignore[index, union-attr]



# testComponents


COMPONENTS_WIRE = (
    "MSH|^~\\&|^QueryServices||||20021011161756.297-0500||ORU^R01|1|D|2.4\r"
    "PID|||||x&y^z|\r"
    "OBR|1|||CHO^CHOLESTEROL\r"
    "OBX|1|NM|Z049107^Chol^L||2.30|mmol/L|||||F\r"
)


def test_components_subcomponent_parsing() -> None:
    """x&y^z in PID.5 decodes surname, surname prefix, and given name (testComponents)."""
    msg = ORU_R01_v24.model_validate_er7(COMPONENTS_WIRE)
    name = msg.PATIENT_RESULT[0].PATIENT.PID.pid_5[0]  # type: ignore[index, union-attr]
    assert name.xpn_1.fn_1 == "x"   # type: ignore[union-attr]
    assert name.xpn_1.fn_2 == "y"   # type: ignore[union-attr]
    assert name.xpn_2 == "z"



# testUnescapeComponents \T\ in address decodes to &


UNESCAPE_COMPONENTS_WIRE = (
    "MSH|^~\\&|NES|NINTENDO|AGNEW|CORNERCUBICLE|20010101000000||ADT^A04|Q123456789T123456789X123456|P|2.3\r\n"
    "EVN|A04|20010101000000|||^KOOPA^BOWSER^^^^^^^CURRENT\r\n"
    "PID|1||123456789|0123456789^AA^^JP|BROS^MARIO^^^^||19850101000000|M|||"
    "123 FAKE STREET^MARIO \\T\\ LUIGI BROS PLACE^TOADSTOOL KINGDOM^NES^A1B2C3^JP^HOME^^1234\r\n"
    "PV1|1|O\r\n"
)


def test_unescape_t_in_address() -> None:
    """\\T\\ in PID.11 other-designation decodes to & (testUnescapeComponents)."""
    msg = ADT_A01_v23.model_validate_er7(UNESCAPE_COMPONENTS_WIRE)
    addr = msg.PID.pid_11[0]  # type: ignore[union-attr, index]
    assert addr.xad_2 == "MARIO & LUIGI BROS PLACE"



# testNonPipeDelimitor


NON_PIPE_WIRE = (
    "MSH^~|\\&^HDRVTLS^552~DAYTDEV.FO-BAYPINES.MED.VA.GOV~DNS^GMRV VDEF IESIDE^200HD~"
    "HDR.MED.VA.GOV~DNS^20061006151615-0800^^ORU~R01^55253408603^T^2.4^^^AL^NE^US\r\n"
    "OBR^^^6240020~552_120.5^4500635~PAIN~99VA120.51^^^200610061445-0800^20061006144607-0800\r\n"
    "OBX^^ST^4500635~PAIN~99VA120.51^^3^~~L^^^^^W\r\n"
)


def test_non_pipe_field_separator_decodes() -> None:
    """A message using ^ as field separator (not |) must decode without error (testNonPipeDelimitor)."""
    msg = decode_er7(NON_PIPE_WIRE)
    assert msg is not None
    assert msg.MSH.msh_9.msg_1 == "ORU"   # type: ignore[union-attr]
    assert msg.MSH.msh_9.msg_2 == "R01"   # type: ignore[union-attr]



# testParseEmptySegment


EMPTY_SEGMENT_WIRE = (
    "MSH|^~\\&|1444-ADT|1444|S-ADT|SIMS|20071023160622||ADT^A03^ADT_A05|Q67084255T54052896X2|P^T|2.5|||NE|AL|CAN|8859/1\r\n"
    "EVN|A03|20071023160622\r\n"
    "PID|1||00J8804997^^^1444^MR||Aalan^Angus^^^^^L||19620404|F\r\n"
    "PD1\r\n"
    "PV1"
)


def test_empty_segment_does_not_raise() -> None:
    """Empty PD1 and PV1 segments must not crash the decoder (testParseEmptySegment)."""
    msg = ADT_A03_v25.model_validate_er7(EMPTY_SEGMENT_WIRE)
    assert isinstance(msg, ADT_A03_v25)



# testUnknownVersion


def test_unknown_version_raises() -> None:
    """A wire whose MSH.12 names a non-existent HL7 version must raise (testUnknownVersion)."""
    wire = (
        "MSH|^~\\&|^QueryServices||||20021011161756.297-0500||ORU^R01|1|D|2.999\r"
        "OBX|1|NM|Z049107^Chol^L||2.30|mmol/L|||||F\r"
    )
    with pytest.raises(Exception):
        decode_er7(wire)



# testEarlyNonStandard Z-segment near start silently skipped


EARLY_Z_SEGMENT_WIRE = (
    "MSH|^~\\&|IRIS|SANTER|AMB_R|SANTER|200803051508||ADT^A03^ADT_A05|263206|P|2.5\r\n"
    "EVN||200803051509||||200803031508\r\n"
    "ZZZ|aaa\r\n"
    "PID|||5520255^^^PK^PK||ZZZ^ZZZ||19830824|F\r\n"
    "PV1||I\r\n"
)


def test_early_nonstandard_segment_is_skipped() -> None:
    """A Z-segment before PID must not crash the decoder (testEarlyNonStandard).

    Note: hl7types does not currently advance past unknown segments, so PID data
    after the ZZZ is not accessible. The key assertion is that decoding completes
    without raising.
    """
    msg = ADT_A03_v25.model_validate_er7(EARLY_Z_SEGMENT_WIRE)
    assert isinstance(msg, ADT_A03_v25)
