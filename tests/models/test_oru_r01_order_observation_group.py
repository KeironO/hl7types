"""Tests for the generated ORU_R01_ORDER_OBSERVATION group model.

Covers runtime behaviour of the Pydantic group model: required/optional fields,
the repeating OBSERVATION constraint, NTE as optional repeating, and direct
construction by field name.
"""
from __future__ import annotations

import pytest
import pydantic

from hl7types import decode_er7
from hl7types.hl7.v2_1.groups.ORU_R01_ORDER_OBSERVATION import ORU_R01_ORDER_OBSERVATION
from hl7types.hl7.v2_1.groups.ORU_R01_OBSERVATION import ORU_R01_OBSERVATION

# OBR fields 4, 7, 8, 9, 14, and 22 are required in v2.1.  All other fields
# are padded with empty strings so the pipe positions stay correct.
_OBR = "|".join([
    "OBR", "1", "", "", "CBC^CBC", "", "",
    "19950101090000", "19950101090000", "19950101090000",
    "", "", "", "", "19950101100000",
    "", "", "", "", "", "", "",
    "19950101110000",
])
assert _OBR.split("|")[0] == "OBR"
assert len(_OBR.split("|")) >= 23

_ORU_R01 = (
    "MSH|^~\\&|APP|FAC|APP2|FAC2|19950101120000||ORU^R01|MSG001|P|2.1\r"
    "PID|1||P001||DOE^JOHN||19800101|M\r"
    + _OBR + "\r"
    "OBX|1|ST|WBC^White Blood Cell||5.0|10*3/uL|4.0-11.0|N|||F\r"
)

_ORU_R01_WITH_NTE = (
    "MSH|^~\\&|APP|FAC|APP2|FAC2|19950101120000||ORU^R01|MSG002|P|2.1\r"
    "PID|1||P001||DOE^JOHN||19800101|M\r"
    + _OBR + "\r"
    "NTE|1||Fasting sample\r"
    "OBX|1|ST|WBC^White Blood Cell||5.0|10*3/uL|4.0-11.0|N|||F\r"
)


def _order_observation() -> ORU_R01_ORDER_OBSERVATION:
    """Return the first ORDER_OBSERVATION group from a decoded ORU^R01 message."""
    msg = decode_er7(_ORU_R01)
    order_obs = msg.PATIENT_RESULT[0].ORDER_OBSERVATION
    assert isinstance(order_obs, list)
    assert order_obs
    assert isinstance(order_obs[0], ORU_R01_ORDER_OBSERVATION)
    return order_obs[0]


def _order_observation_with_nte() -> ORU_R01_ORDER_OBSERVATION:
    """Return the first ORDER_OBSERVATION group from a decoded ORU^R01 with NTE."""
    return decode_er7(_ORU_R01_WITH_NTE).PATIENT_RESULT[0].ORDER_OBSERVATION[0]


def test_decoded_oru_r01_exposes_order_observation() -> None:
    """A decoded ORU^R01 message exposes at least one ORDER_OBSERVATION group."""
    msg = decode_er7(_ORU_R01)
    order_obs = msg.PATIENT_RESULT[0].ORDER_OBSERVATION
    assert isinstance(order_obs, list)
    assert len(order_obs) >= 1
    assert isinstance(order_obs[0], ORU_R01_ORDER_OBSERVATION)


def test_decoded_order_observation_obr_is_populated() -> None:
    """The decoded ORDER_OBSERVATION has a populated OBR segment."""
    oo = _order_observation()
    assert oo.OBR is not None


def test_decoded_order_observation_observation_is_nonempty_list() -> None:
    """The decoded ORDER_OBSERVATION has a non-empty OBSERVATION list."""
    oo = _order_observation()
    assert isinstance(oo.OBSERVATION, list)
    assert len(oo.OBSERVATION) >= 1


def test_decoded_order_observation_items_are_correct_type() -> None:
    """Each item in the decoded OBSERVATION list is an ORU_R01_OBSERVATION group."""
    oo = _order_observation()
    for obs in oo.OBSERVATION:
        assert isinstance(obs, ORU_R01_OBSERVATION)


def test_decoded_order_observation_nte_is_none_when_absent() -> None:
    """NTE is None when no NTE segment is present in the decoded message."""
    oo = _order_observation()
    assert oo.NTE is None


def test_direct_construction_without_orc_or_nte_succeeds() -> None:
    """Constructing ORDER_OBSERVATION with only OBR and OBSERVATION succeeds."""
    oo = _order_observation()
    grp = ORU_R01_ORDER_OBSERVATION(OBR=oo.OBR, OBSERVATION=oo.OBSERVATION)
    assert grp.OBR is not None
    assert grp.ORC is None
    assert grp.NTE is None
    assert len(grp.OBSERVATION) >= 1


def test_direct_construction_without_obr_raises() -> None:
    """Omitting OBR from direct construction raises a Pydantic ValidationError."""
    oo = _order_observation()
    with pytest.raises(pydantic.ValidationError) as exc_info:
        ORU_R01_ORDER_OBSERVATION(OBSERVATION=oo.OBSERVATION)
    missing = {e["loc"] for e in exc_info.value.errors() if e["type"] == "missing"}
    assert ("OBR",) in missing


def test_direct_construction_without_observation_raises() -> None:
    """Omitting OBSERVATION from direct construction raises a Pydantic ValidationError."""
    oo = _order_observation()
    with pytest.raises(pydantic.ValidationError) as exc_info:
        ORU_R01_ORDER_OBSERVATION(OBR=oo.OBR)
    missing = {e["loc"] for e in exc_info.value.errors() if e["type"] == "missing"}
    assert ("OBSERVATION",) in missing


def test_direct_construction_with_empty_observation_raises() -> None:
    """Supplying OBSERVATION=[] raises a Pydantic ValidationError (min_length=1)."""
    oo = _order_observation()
    with pytest.raises(pydantic.ValidationError) as exc_info:
        ORU_R01_ORDER_OBSERVATION(OBR=oo.OBR, OBSERVATION=[])
    errors = exc_info.value.errors()
    assert any(e["loc"] == ("OBSERVATION",) for e in errors)


def test_direct_construction_preserves_observation_list() -> None:
    """The supplied OBSERVATION list is preserved by equality on the constructed group."""
    oo = _order_observation()
    grp = ORU_R01_ORDER_OBSERVATION(OBR=oo.OBR, OBSERVATION=oo.OBSERVATION)
    assert grp.OBSERVATION == oo.OBSERVATION


def test_direct_construction_with_nte_populates_nte() -> None:
    """When NTE is supplied, it is stored as a list on the constructed group."""
    oo = _order_observation_with_nte()
    assert isinstance(oo.NTE, list)
    assert len(oo.NTE) >= 1
    grp = ORU_R01_ORDER_OBSERVATION(OBR=oo.OBR, OBSERVATION=oo.OBSERVATION, NTE=oo.NTE)
    assert isinstance(grp.NTE, list)
    assert grp.NTE == oo.NTE
