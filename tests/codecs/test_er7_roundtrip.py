import pytest

from hl7types.hl7.v2_5_1.messages.ADT_A01 import ADT_A01

ADT_A01_WIRE = (
    "MSH|^~\\&|SENDING|FACILITY|RECEIVING|DEST|20240101120000||ADT^A01^ADT_A01|MSG001|P|2.5.1\r"
    "EVN|A01|20240101120000\r"
    "PID|1||123456^^^MRN^MR||Doe^John^A||19800101|M\r"
    "PV1|1|I|WARD^BED1"
)


@pytest.fixture
def adt_a01() -> ADT_A01:
    return ADT_A01.model_validate_er7(ADT_A01_WIRE)


def test_decode_adt_a01_returns_correct_type(adt_a01: ADT_A01) -> None:
    assert isinstance(adt_a01, ADT_A01)


def test_decode_adt_a01_msh_fields(adt_a01: ADT_A01) -> None:
    assert adt_a01.MSH.msh_3.hd_1 == "SENDING"  # type: ignore[union-attr]
    assert adt_a01.MSH.msh_12.vid_1 == "2.5.1"  # type: ignore[union-attr]


def test_decode_adt_a01_pid_name(adt_a01: ADT_A01) -> None:
    name = adt_a01.PID.pid_5[0]  # type: ignore[union-attr]
    assert name.xpn_1.fn_1 == "Doe"  # type: ignore[union-attr]
    assert name.xpn_2 == "John"


def test_roundtrip_adt_a01(adt_a01: ADT_A01) -> None:
    re_encoded = adt_a01.model_dump_er7()
    msg2 = ADT_A01.model_validate_er7(re_encoded)
    assert msg2.MSH.msh_10 == adt_a01.MSH.msh_10  # type: ignore[union-attr]
    assert msg2.PID.pid_3[0].cx_1 == adt_a01.PID.pid_3[0].cx_1  # type: ignore[index, union-attr]
    assert msg2.PID.pid_5[0].xpn_1.fn_1 == "Doe"  # type: ignore[index, union-attr]
    assert msg2.PV1.pv1_2 == "I"  # type: ignore[union-attr]
