from hl7types.hl7.v2_5_1.messages.ADT_A01 import ADT_A01

ADT_A01_WIRE = (
    "MSH|^~\\&|SENDING|FACILITY|RECEIVING|DEST|20240101120000||ADT^A01^ADT_A01|MSG001|P|2.5.1\r"
    "EVN|A01|20240101120000\r"
    "PID|1||123456^^^MRN^MR||Doe^John^A||19800101|M\r"
    "PV1|1|I|WARD^BED1"
)


def test_decode_adt_a01_returns_correct_type() -> None:
    msg = ADT_A01.model_validate_er7(ADT_A01_WIRE)
    assert isinstance(msg, ADT_A01)


def test_decode_adt_a01_msh_fields() -> None:
    msg = ADT_A01.model_validate_er7(ADT_A01_WIRE)
    assert msg.MSH.msh_3.hd_1 == "SENDING"  # type: ignore[union-attr]
    assert msg.MSH.msh_12.vid_1 == "2.5.1"  # type: ignore[union-attr]


def test_decode_adt_a01_pid_name() -> None:
    msg = ADT_A01.model_validate_er7(ADT_A01_WIRE)
    name = msg.PID.pid_5[0]  # type: ignore[union-attr]
    assert name.xpn_1.fn_1 == "Doe"  # type: ignore[union-attr]
    assert name.xpn_2 == "John"


def test_roundtrip_adt_a01() -> None:
    msg = ADT_A01.model_validate_er7(ADT_A01_WIRE)
    re_encoded = msg.model_dump_er7()
    msg2 = ADT_A01.model_validate_er7(re_encoded)
    assert msg2.MSH.msh_10 == msg.MSH.msh_10  # message control ID preserved
    assert msg2.PID.pid_3[0].cx_1 == msg.PID.pid_3[0].cx_1  # type: ignore[index, union-attr]
