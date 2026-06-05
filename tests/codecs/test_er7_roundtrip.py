"""ER7 decode and round-trip tests for a representative ADT^A01 message.

Tests cover MSH header metadata, PID patient identity (identifier list, name,
demographics), PV1 visit information, and structural preservation through a
full encode to decode cycle.
"""
from __future__ import annotations

import pytest

from hl7types.hl7.v2_5_1.messages.ADT_A01 import ADT_A01

ADT_A01_WIRE = (
    "MSH|^~\\&|SENDING|FACILITY|RECEIVING|DEST|20240101120000||ADT^A01^ADT_A01|MSG001|P|2.5.1\r"
    "EVN|A01|20240101120000\r"
    "PID|1||123456^^^MRN^MR||Doe^John^A||19800101|M\r"
    "PV1|1|I|WARD^BED1"
)


@pytest.fixture
def decoded_adt_a01() -> ADT_A01:
    return ADT_A01.model_validate_er7(ADT_A01_WIRE)


def test_decode_adt_a01_msh_header(decoded_adt_a01: ADT_A01) -> None:
    msh = decoded_adt_a01.MSH
    assert msh.msh_3.hd_1 == "SENDING"      # type: ignore[union-attr]
    assert msh.msh_4.hd_1 == "FACILITY"     # type: ignore[union-attr]
    assert msh.msh_5.hd_1 == "RECEIVING"    # type: ignore[union-attr]
    assert msh.msh_9.msg_1 == "ADT"         # type: ignore[union-attr]
    assert msh.msh_9.msg_2 == "A01"         # type: ignore[union-attr]
    assert msh.msh_9.msg_3 == "ADT_A01"     # type: ignore[union-attr]
    assert msh.msh_10 == "MSG001"
    assert msh.msh_11.pt_1 == "P"           # type: ignore[union-attr]
    assert msh.msh_12.vid_1 == "2.5.1"      # type: ignore[union-attr]


def test_decode_adt_a01_pid_patient_identity(decoded_adt_a01: ADT_A01) -> None:
    pid = decoded_adt_a01.PID  # type: ignore[union-attr]

    identifier = pid.pid_3[0]  # type: ignore[index, union-attr]
    assert identifier.cx_1 == "123456"
    assert identifier.cx_4.hd_1 == "MRN"    # type: ignore[union-attr]
    assert identifier.cx_5 == "MR"

    name = pid.pid_5[0]  # type: ignore[index, union-attr]
    assert name.xpn_1.fn_1 == "Doe"         # type: ignore[union-attr]
    assert name.xpn_2 == "John"
    assert name.xpn_3 == "A"

    assert pid.pid_7.ts_1 == "19800101"     # type: ignore[union-attr]
    assert pid.pid_8 == "M"


def test_decode_adt_a01_pv1_visit(decoded_adt_a01: ADT_A01) -> None:
    pv1 = decoded_adt_a01.PV1  # type: ignore[union-attr]
    assert pv1.pv1_2 == "I"
    assert pv1.pv1_3.pl_1 == "WARD"         # type: ignore[union-attr]
    assert pv1.pv1_3.pl_2 == "BED1"         # type: ignore[union-attr]


def test_roundtrip_adt_a01_preserves_structured_fields(decoded_adt_a01: ADT_A01) -> None:
    msg2 = ADT_A01.model_validate_er7(decoded_adt_a01.model_dump_er7())

    assert msg2.MSH.msh_10 == "MSG001"                           # type: ignore[union-attr]
    assert msg2.MSH.msh_12.vid_1 == "2.5.1"                     # type: ignore[union-attr]

    id2 = msg2.PID.pid_3[0]                                     # type: ignore[index, union-attr]
    assert id2.cx_1 == "123456"
    assert id2.cx_4.hd_1 == "MRN"                               # type: ignore[union-attr]
    assert id2.cx_5 == "MR"

    name2 = msg2.PID.pid_5[0]                                   # type: ignore[index, union-attr]
    assert name2.xpn_1.fn_1 == "Doe"                            # type: ignore[union-attr]
    assert name2.xpn_2 == "John"

    assert msg2.PID.pid_7.ts_1 == "19800101"                    # type: ignore[union-attr]
    assert msg2.PID.pid_8 == "M"                                # type: ignore[union-attr]

    assert msg2.PV1.pv1_2 == "I"                                # type: ignore[union-attr]
    assert msg2.PV1.pv1_3.pl_1 == "WARD"                        # type: ignore[union-attr]
