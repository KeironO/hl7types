"""Contract tests for required repeating fields (List[X] = Field(..., min_length=1)).

Uses ORU_R01_ORDER_OBSERVATION from v2.3, where OBSERVATION is typed as
List[ORU_R01_OBSERVATION] = Field(..., min_length=1) — required and non-empty.

The generated models use both Field(...) (required) and min_length=1 (non-empty),
so both an absent field and an empty list raise ValidationError.
"""
from __future__ import annotations

import pytest
from pydantic import ValidationError

from hl7types.hl7.v2_3.groups.ORU_R01_ORDER_OBSERVATION import ORU_R01_ORDER_OBSERVATION
from hl7types.hl7.v2_3.groups.ORU_R01_OBSERVATION import ORU_R01_OBSERVATION
from hl7types.hl7.v2_3.segments.OBR import OBR
from hl7types.hl7.v2_3.segments.OBX import OBX


@pytest.fixture
def minimal_obr() -> OBR:
    return OBR.model_construct()


@pytest.fixture
def minimal_observation() -> ORU_R01_OBSERVATION:
    return ORU_R01_OBSERVATION(OBX=OBX.model_construct())


def test_missing_observation_raises(minimal_obr: OBR) -> None:
    with pytest.raises(ValidationError, match="OBSERVATION"):
        ORU_R01_ORDER_OBSERVATION(OBR=minimal_obr)


def test_empty_list_raises(minimal_obr: OBR) -> None:
    # min_length=1 on the field means an empty list is also rejected.
    with pytest.raises(ValidationError, match="OBSERVATION"):
        ORU_R01_ORDER_OBSERVATION(OBR=minimal_obr, OBSERVATION=[])


def test_non_empty_list_accepted(
    minimal_obr: OBR,
    minimal_observation: ORU_R01_OBSERVATION,
) -> None:
    model = ORU_R01_ORDER_OBSERVATION(OBR=minimal_obr, OBSERVATION=[minimal_observation])
    assert len(model.OBSERVATION) == 1


def test_multiple_observations_preserved_in_order(minimal_obr: OBR) -> None:
    observations = [
        ORU_R01_OBSERVATION(OBX=OBX.model_construct(obx_1=str(i)))
        for i in range(3)
    ]
    model = ORU_R01_ORDER_OBSERVATION(OBR=minimal_obr, OBSERVATION=observations)
    assert [obs.OBX.obx_1 for obs in model.OBSERVATION] == ["0", "1", "2"]
