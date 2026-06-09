"""ER7 pipe parsing: repeating fields and segments, malformed wires, component and
subcomponent decoding, escape handling, non-standard delimiters, and Z-segment behaviour."""
from __future__ import annotations

import pytest

import hl7types  # noqa: F401
from hl7types import decode_er7
from hl7types.hl7.v2_3.messages.ADT_A01 import ADT_A01 as ADT_A01_v23
from hl7types.hl7.v2_4.messages.ORU_R01 import ORU_R01 as ORU_R01_v24
from hl7types.hl7.v2_5.messages.ADT_A03 import ADT_A03 as ADT_A03_v25
from hl7types.hl7.v2_5.messages.ADT_A45 import ADT_A45


REPEATING_OBX5_WIRE = (
    "MSH|^~\\&|HNAM|CL|CL_RADNET|CL|20110628095233||ORU^R01|Q2301030099T1904270849|P|2.4\r"
    "PID|1||10011682^^^CL_MRN||CLABTEST^ONE\r"
    "OBR|1|3415770735^HNAM_ORDERID||CL987^MRA Head|||||||||||Rad Type&Rad Type\r"
    "OBX|1|TX|20725^ROUTINE HEMATOLOGY|H7800-4|This~Is~A~Report~~~~~||||||I|||200704021122\r"
)


def test_repeating_obx5_drops_empty_trailing_reps() -> None:
    msg = ORU_R01_v24.model_validate_er7(REPEATING_OBX5_WIRE)
    obx5 = msg.PATIENT_RESULT[0].ORDER_OBSERVATION[0].OBSERVATION[0].OBX.obx_5  # type: ignore[index, union-attr]
    # Trailing empty repetitions (~~~~~ after Report) are dropped; four non-empty values survive.
    assert obx5 == ["This", "Is", "A", "Report"]


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
def test_truncated_wire_raises_value_error(wire: str) -> None:
    with pytest.raises(ValueError):
        decode_er7(wire)


# ADT_A45 MERGE_INFO group requires MRG + PV1; only MRG is present in the wire.
MISSING_PV1_WIRE = (
    "MSH|^~\\&|4265-ADT|4265|eReferral|eReferral|201004141020||ADT^A45^ADT_A45|102416|T^|2.5^^|||NE|AL|CAN|8859/1\r"
    "EVN|A45|201004141020|\r"
    "PID|1||7010226^^^4265^MR~0000000000^^^CANON^JHN||Park^Green\r"
    "MRG|9999999^^^4265^MR\r"
    "PV1|1|I|WARD^ROOM^BED\r"
)


def test_required_last_segment_decodes() -> None:
    msg = decode_er7(MISSING_PV1_WIRE)
    assert isinstance(msg, ADT_A45)
    assert msg.PID.pid_3[0].cx_1 == "7010226"  # type: ignore[union-attr, index]
    assert msg.MERGE_INFO[0].MRG.mrg_1[0].cx_1 == "9999999"  # type: ignore[union-attr, index]
    assert msg.MERGE_INFO[0].PV1.pv1_2 == "I"


REPEATING_OBX_WIRE = (
    "MSH|^~\\&|^QueryServices||||20021011161756.297-0500||ORU^R01|1|D|2.4\r"
    "OBR|1|||CHO^CHOLESTEROL\r"
    "OBX|1|NM|Z049107^Cholesterol^L||2.30|mmol/L|||||F\r"
    "OBX|2|NM|Z049107^Cholesterol^L||3.10|mmol/L|||||F\r"
    "OBX|3|NM|Z049107^Cholesterol^L||4.50|mmol/L|||||F\r"
)


def test_repeating_obx_segments_preserve_order_and_values() -> None:
    msg = ORU_R01_v24.model_validate_er7(REPEATING_OBX_WIRE)
    obs = msg.PATIENT_RESULT[0].ORDER_OBSERVATION[0].OBSERVATION  # type: ignore[index, union-attr]
    assert [(o.OBX.obx_1, o.OBX.obx_5[0]) for o in obs] == [  # type: ignore[index, union-attr]
        ("1", "2.30"), ("2", "3.10"), ("3", "4.50"),
    ]


COMPONENTS_WIRE = (
    "MSH|^~\\&|^QueryServices||||20021011161756.297-0500||ORU^R01|1|D|2.4\r"
    "PID|||||x&y^z|\r"
    "OBR|1|||CHO^CHOLESTEROL\r"
    "OBX|1|NM|Z049107^Chol^L||2.30|mmol/L|||||F\r"
)


def test_components_subcomponent_parsing() -> None:
    msg = ORU_R01_v24.model_validate_er7(COMPONENTS_WIRE)
    name = msg.PATIENT_RESULT[0].PATIENT.PID.pid_5[0]  # type: ignore[index, union-attr]
    assert name.xpn_1.fn_1 == "x"  # type: ignore[union-attr]
    assert name.xpn_1.fn_2 == "y"  # type: ignore[union-attr]
    assert name.xpn_2 == "z"


# \T\ in PID.11 address other-designation decodes to literal &.
UNESCAPE_COMPONENTS_WIRE = (
    "MSH|^~\\&|NES|NINTENDO|AGNEW|CORNERCUBICLE|20010101000000||ADT^A04|Q123456789T123456789X123456|P|2.3\r\n"
    "EVN|A04|20010101000000|||^KOOPA^BOWSER^^^^^^^CURRENT\r\n"
    "PID|1||123456789|0123456789^AA^^JP|BROS^MARIO^^^^||19850101000000|M|||"
    "123 FAKE STREET^MARIO \\T\\ LUIGI BROS PLACE^TOADSTOOL KINGDOM^NES^A1B2C3^JP^HOME^^1234\r\n"
    "PV1|1|O\r\n"
)


def test_unescape_t_in_address() -> None:
    msg = ADT_A01_v23.model_validate_er7(UNESCAPE_COMPONENTS_WIRE)
    addr = msg.PID.pid_11[0]  # type: ignore[union-attr, index]
    assert addr.xad_2 == "MARIO & LUIGI BROS PLACE"


# Non-standard wire where ^ is the field separator and | is the component separator.
NON_PIPE_WIRE = (
    "MSH^~|\\&^HDRVTLS^552~DAYTDEV.FO-BAYPINES.MED.VA.GOV~DNS^GMRV VDEF IESIDE^200HD~"
    "HDR.MED.VA.GOV~DNS^20061006151615-0800^^ORU~R01^55253408603^T^2.4^^^AL^NE^US\r\n"
    "OBR^^^6240020~552_120.5^4500635~PAIN~99VA120.51^^^200610061445-0800^20061006144607-0800\r\n"
    "OBX^^ST^4500635~PAIN~99VA120.51^^3^~~L^^^^^W\r\n"
)


def test_non_pipe_field_separator_decodes() -> None:
    msg = decode_er7(NON_PIPE_WIRE)
    assert msg.MSH.msh_3.hd_1 == "HDRVTLS"   # type: ignore[union-attr]
    assert msg.MSH.msh_9.msg_1 == "ORU"       # type: ignore[union-attr]
    assert msg.MSH.msh_9.msg_2 == "R01"       # type: ignore[union-attr]
    assert msg.MSH.msh_10 == "55253408603"
    assert msg.MSH.msh_12.vid_1 == "2.4"      # type: ignore[union-attr]


# Empty PD1 and bare PV1 (no fields); PV1.2 (required) gets an empty-string placeholder.
EMPTY_SEGMENT_WIRE = (
    "MSH|^~\\&|1444-ADT|1444|S-ADT|SIMS|20071023160622||ADT^A03^ADT_A05|Q67084255T54052896X2|P^T|2.5|||NE|AL|CAN|8859/1\r\n"
    "EVN|A03|20071023160622\r\n"
    "PID|1||00J8804997^^^1444^MR||Aalan^Angus^^^^^L||19620404|F\r\n"
    "PD1\r\n"
    "PV1"
)


def test_empty_segment_decodes_with_placeholder() -> None:
    # Bare PV1 segment has no field data; required pv1_2 is injected as a placeholder.
    with pytest.warns(UserWarning, match=r"pv1_2"):
        msg = ADT_A03_v25.model_validate_er7(EMPTY_SEGMENT_WIRE, strict=False)
    assert isinstance(msg, ADT_A03_v25)
    # PID decoded correctly despite the subsequent empty segments.
    assert msg.PID.pid_3[0].cx_1 == "00J8804997"  # type: ignore[union-attr, index]
    # Bare PV1 segment: no field data on the wire; required pv1_2 injected as placeholder.
    assert msg.PV1.pv1_1 is None
    assert msg.PV1.pv1_2 == ""


def test_unknown_version_raises() -> None:
    wire = (
        "MSH|^~\\&|^QueryServices||||20021011161756.297-0500||ORU^R01|1|D|2.999\r"
        "OBX|1|NM|Z049107^Chol^L||2.30|mmol/L|||||F\r"
    )
    with pytest.raises(ValueError, match="Unknown message structure"):
        decode_er7(wire)


# Wire has MSH, EVN, ZZZ (non-standard), PID, PV1.
# Bug: the decoder stops at ZZZ and never reaches the real PID and PV1 that follow,
# silently returning placeholder structures with no field data.
EARLY_Z_SEGMENT_WIRE = (
    "MSH|^~\\&|IRIS|SANTER|AMB_R|SANTER|200803051508||ADT^A03^ADT_A05|263206|P|2.5\r\n"
    "EVN||200803051509||||200803031508\r\n"
    "ZZZ|aaa\r\n"
    "PID|||5520255^^^PK^PK||ZZZ^ZZZ||19830824|F\r\n"
    "PV1||I\r\n"
)


def test_early_nonstandard_segment_skips_z_and_decodes_following_segments() -> None:
    with pytest.warns(UserWarning, match=r"Skipped unknown segment 'ZZZ'"):
        msg = ADT_A03_v25.model_validate_er7(EARLY_Z_SEGMENT_WIRE)
    # ZZZ was skipped; the decoder continued and found the real PID and PV1.
    assert msg.PID.pid_3[0].cx_1 == "5520255"  # type: ignore[union-attr, index]
    assert msg.PV1.pv1_2 == "I"  # type: ignore[union-attr]
