"""Tests for trigger-event to message structure resolution when MSH-9.3 is absent."""

from __future__ import annotations

import pytest

from hl7types import decode_er7
from hl7types.hl7.v2_3.messages.ADT_A01 import ADT_A01 as ADT_A01_v23
from hl7types.hl7.v2_5.messages.ADT_A01 import ADT_A01

MSH_V25 = "MSH|^~\\&|SEND|FAC|RECV|FAC2|20010101120000||{msh9}|CTRL001|P|2.5\r"
MSH_V23 = "MSH|^~\\&|SEND|FAC|RECV|FAC2|20010101120000||{msh9}|CTRL001|P|2.3\r"
EVN = "EVN|A01|20010101120000\r"
PID = "PID|1||123456^^^MRN||DOE^JOHN\r"
PV1 = "PV1|1|I\r"


def _make_v25(trigger: str) -> str:
    return MSH_V25.format(msh9=f"ADT^{trigger}") + EVN + PID + PV1


def _make_v23(trigger: str) -> str:
    return MSH_V23.format(msh9=f"ADT^{trigger}") + EVN + PID + PV1


def test_explicit_msh9_3_still_works() -> None:
    wire = MSH_V25.format(msh9="ADT^A01^ADT_A01") + EVN + PID + PV1
    result = decode_er7(wire)
    assert isinstance(result, ADT_A01)


def test_a01_without_msh9_3_resolves_directly() -> None:
    assert isinstance(decode_er7(_make_v25("A01")), ADT_A01)


def test_a04_without_msh9_3_resolves_to_adt_a01() -> None:
    assert isinstance(decode_er7(_make_v25("A04")), ADT_A01)


def test_a08_without_msh9_3_resolves_to_adt_a01() -> None:
    assert isinstance(decode_er7(_make_v25("A08")), ADT_A01)


def test_a13_without_msh9_3_resolves_to_adt_a01() -> None:
    assert isinstance(decode_er7(_make_v25("A13")), ADT_A01)


def test_unknown_trigger_still_raises() -> None:
    wire = MSH_V25.format(msh9="ADT^ZZZZ") + EVN + PID + PV1
    with pytest.raises(ValueError, match="Unknown message structure"):
        decode_er7(wire)


# v2.3, aliases are implemented as thin wrapper modules rather than an event map,
# so ADT_A04 resolves to the ADT_A01 class while the raw MSH-9 is preserved.

def test_v23_a04_resolves_to_adt_a01() -> None:
    result = decode_er7(_make_v23("A04"))
    assert isinstance(result, ADT_A01_v23)


def test_v23_a04_msh9_preserves_original_trigger() -> None:
    result = decode_er7(_make_v23("A04"))
    assert isinstance(result, ADT_A01_v23)
    assert result.MSH.msh_9 == "ADT^A04"
