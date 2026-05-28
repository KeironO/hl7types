"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OML_O33.PRIOR_RESULT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.AL1 import AL1

from .OML_O33_ORDER_PRIOR import OML_O33_ORDER_PRIOR
from .OML_O33_PATIENT_PRIOR import OML_O33_PATIENT_PRIOR
from .OML_O33_PATIENT_VISIT_PRIOR import OML_O33_PATIENT_VISIT_PRIOR

_AL1 = AL1
_OML_O33_ORDER_PRIOR = OML_O33_ORDER_PRIOR
_OML_O33_PATIENT_PRIOR = OML_O33_PATIENT_PRIOR
_OML_O33_PATIENT_VISIT_PRIOR = OML_O33_PATIENT_VISIT_PRIOR


class OML_O33_PRIOR_RESULT(BaseModel):
    """HL7 v2 OML_O33.PRIOR_RESULT group.

    Attributes:
        PATIENT_PRIOR (Optional[OML_O33_PATIENT_PRIOR]): optional
        PATIENT_VISIT_PRIOR (Optional[OML_O33_PATIENT_VISIT_PRIOR]): optional
        AL1 (Optional[List[AL1]]): optional
        ORDER_PRIOR (List[OML_O33_ORDER_PRIOR]): required
    """

    PATIENT_PRIOR: Optional[_OML_O33_PATIENT_PRIOR] = Field(
        default=None,
        title="PATIENT_PRIOR",
        description="Optional",
    )

    PATIENT_VISIT_PRIOR: Optional[_OML_O33_PATIENT_VISIT_PRIOR] = Field(
        default=None,
        title="PATIENT_VISIT_PRIOR",
        description="Optional",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    ORDER_PRIOR: List[_OML_O33_ORDER_PRIOR] = Field(
        default=...,
        title="ORDER_PRIOR",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
