"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OMG_O19.PRIOR_RESULT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.AL1 import AL1

from .OMG_O19_ORDER_PRIOR import OMG_O19_ORDER_PRIOR
from .OMG_O19_PATIENT_PRIOR import OMG_O19_PATIENT_PRIOR
from .OMG_O19_PATIENT_VISIT_PRIOR import OMG_O19_PATIENT_VISIT_PRIOR

_AL1 = AL1
_OMG_O19_ORDER_PRIOR = OMG_O19_ORDER_PRIOR
_OMG_O19_PATIENT_PRIOR = OMG_O19_PATIENT_PRIOR
_OMG_O19_PATIENT_VISIT_PRIOR = OMG_O19_PATIENT_VISIT_PRIOR


class OMG_O19_PRIOR_RESULT(BaseModel):
    """HL7 v2 OMG_O19.PRIOR_RESULT group.

    Attributes:
        PATIENT_PRIOR (Optional[OMG_O19_PATIENT_PRIOR]): optional
        PATIENT_VISIT_PRIOR (Optional[OMG_O19_PATIENT_VISIT_PRIOR]): optional
        AL1 (Optional[List[AL1]]): optional
        ORDER_PRIOR (List[OMG_O19_ORDER_PRIOR]): required
    """

    PATIENT_PRIOR: Optional[_OMG_O19_PATIENT_PRIOR] = Field(
        default=None,
        title="PATIENT_PRIOR",
        description="Optional",
    )

    PATIENT_VISIT_PRIOR: Optional[_OMG_O19_PATIENT_VISIT_PRIOR] = Field(
        default=None,
        title="PATIENT_VISIT_PRIOR",
        description="Optional",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    ORDER_PRIOR: List[_OMG_O19_ORDER_PRIOR] = Field(
        default=...,
        title="ORDER_PRIOR",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
