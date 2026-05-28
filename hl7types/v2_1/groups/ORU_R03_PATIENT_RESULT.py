"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ORU_R03.PATIENT_RESULT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .ORU_R03_ORDER_OBSERVATION import ORU_R03_ORDER_OBSERVATION
from .ORU_R03_PATIENT import ORU_R03_PATIENT

_ORU_R03_ORDER_OBSERVATION = ORU_R03_ORDER_OBSERVATION
_ORU_R03_PATIENT = ORU_R03_PATIENT


class ORU_R03_PATIENT_RESULT(BaseModel):
    """HL7 v2 ORU_R03.PATIENT_RESULT group.

    Attributes:
        PATIENT (Optional[ORU_R03_PATIENT]): optional
        ORDER_OBSERVATION (List[ORU_R03_ORDER_OBSERVATION]): required
    """

    PATIENT: Optional[_ORU_R03_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER_OBSERVATION: List[_ORU_R03_ORDER_OBSERVATION] = Field(
        default=...,
        title="ORDER_OBSERVATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
