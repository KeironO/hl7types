"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ORU_R01.PATIENT_RESULT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .ORU_R01_ORDER_OBSERVATION import ORU_R01_ORDER_OBSERVATION
from .ORU_R01_PATIENT import ORU_R01_PATIENT

_ORU_R01_ORDER_OBSERVATION = ORU_R01_ORDER_OBSERVATION
_ORU_R01_PATIENT = ORU_R01_PATIENT


class ORU_R01_PATIENT_RESULT(BaseModel):
    """HL7 v2 ORU_R01.PATIENT_RESULT group.

    Attributes:
        PATIENT (Optional[ORU_R01_PATIENT]): optional
        ORDER_OBSERVATION (List[ORU_R01_ORDER_OBSERVATION]): required
    """

    PATIENT: _ORU_R01_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER_OBSERVATION: list[_ORU_R01_ORDER_OBSERVATION] = Field(
        default=...,
        title="ORDER_OBSERVATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
