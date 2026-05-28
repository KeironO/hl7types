"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORU_R01.PATIENT_RESULT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
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

    PATIENT: Optional[_ORU_R01_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER_OBSERVATION: List[_ORU_R01_ORDER_OBSERVATION] = Field(
        default=...,
        title="ORDER_OBSERVATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
