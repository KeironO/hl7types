"""
Tests emulating ca.uhn.hl7v2.parser.CanonicalModelClassFactoryTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-test/src/test/java/ca/uhn/hl7v2/parser/CanonicalModelClassFactoryTest.java
"""
from __future__ import annotations

from hl7types import decode_er7
from hl7types.hl7.v2_5.messages.ADT_A45 import ADT_A45

# Wire string taken verbatim from CanonicalModelClassFactoryTest.testAckVersion.
# MSH.9 uses the 3-component form (ADT^A45^ADT_A45) and PID.3 carries three
# patient identifier repetitions separated by ~.
ADT_A45_WIRE = (
    "MSH|^~\\&|4265-ADT|4265|eReferral|eReferral|201004141020||ADT^A45^ADT_A45|102416|T^|2.5^^|||NE|AL|CAN|8859/1\r"
    "EVN|A45|201004141020|\r"
    "PID|1||7010226^^^4265^MR~0000000000^^^CANON^JHN^^^^^^GP~1736465^^^4265^VN||Park^Green^^^MS.^^L||19890812|F\r"
    "MRG|9999999^^^4265^MR\r"
    "PV1|1|I"
)


def test_ack_version_correct_type() -> None:
    msg = decode_er7(ADT_A45_WIRE)
    assert isinstance(msg, ADT_A45)


def test_ack_version_pid3_repetitions() -> None:
    """PID.3 carries three ~ -separated identifiers; all should decode."""
    msg = decode_er7(ADT_A45_WIRE)
    assert len(msg.PID.pid_3) == 3  # type: ignore[union-attr]
    assert msg.PID.pid_3[0].cx_1 == "7010226"  # type: ignore[union-attr]
    assert msg.PID.pid_3[1].cx_1 == "0000000000"  # type: ignore[union-attr]
    assert msg.PID.pid_3[2].cx_1 == "1736465"  # type: ignore[union-attr]


def test_ack_version_pid3_identifier_types() -> None:
    msg = decode_er7(ADT_A45_WIRE)
    assert msg.PID.pid_3[0].cx_5 == "MR"  # type: ignore[union-attr]
    assert msg.PID.pid_3[1].cx_5 == "JHN"  # type: ignore[union-attr]
    assert msg.PID.pid_3[2].cx_5 == "VN"  # type: ignore[union-attr]


def test_ack_version_msh9_three_component() -> None:
    """MSH.9 in the 3-component form should decode message type and trigger name."""
    msg = decode_er7(ADT_A45_WIRE)
    assert msg.MSH.msh_9.msg_1 == "ADT"  # type: ignore[union-attr]
    assert msg.MSH.msh_9.msg_2 == "A45"  # type: ignore[union-attr]
