"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OML_O35.PRIOR_RESULT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AL1 import AL1
from .OML_O35_ORDER_PRIOR import OML_O35_ORDER_PRIOR
from .OML_O35_PATIENT_PRIOR import OML_O35_PATIENT_PRIOR
from .OML_O35_PATIENT_VISIT_PRIOR import OML_O35_PATIENT_VISIT_PRIOR

_AL1 = AL1
_OML_O35_ORDER_PRIOR = OML_O35_ORDER_PRIOR
_OML_O35_PATIENT_PRIOR = OML_O35_PATIENT_PRIOR
_OML_O35_PATIENT_VISIT_PRIOR = OML_O35_PATIENT_VISIT_PRIOR


class OML_O35_PRIOR_RESULT(BaseModel):
    """HL7 v2 OML_O35.PRIOR_RESULT group.

    Attributes:
        PATIENT_PRIOR (Optional[OML_O35_PATIENT_PRIOR]): optional
        PATIENT_VISIT_PRIOR (Optional[OML_O35_PATIENT_VISIT_PRIOR]): optional
        AL1 (Optional[List[AL1]]): optional
        ORDER_PRIOR (List[OML_O35_ORDER_PRIOR]): required
    """

    PATIENT_PRIOR: _OML_O35_PATIENT_PRIOR | None = Field(
        default=None,
        title="PATIENT_PRIOR",
        description="Optional",
    )

    PATIENT_VISIT_PRIOR: _OML_O35_PATIENT_VISIT_PRIOR | None = Field(
        default=None,
        title="PATIENT_VISIT_PRIOR",
        description="Optional",
    )

    AL1: list[_AL1] | None = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    ORDER_PRIOR: list[_OML_O35_ORDER_PRIOR] = Field(
        default=...,
        title="ORDER_PRIOR",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
