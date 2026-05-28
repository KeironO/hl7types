"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OPL_O37.PRIOR_RESULT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AL1 import AL1
from ..segments.NK1 import NK1
from .OPL_O37_ORDER_PRIOR import OPL_O37_ORDER_PRIOR
from .OPL_O37_PATIENT_PRIOR import OPL_O37_PATIENT_PRIOR
from .OPL_O37_PATIENT_VISIT_PRIOR import OPL_O37_PATIENT_VISIT_PRIOR

_AL1 = AL1
_NK1 = NK1
_OPL_O37_ORDER_PRIOR = OPL_O37_ORDER_PRIOR
_OPL_O37_PATIENT_PRIOR = OPL_O37_PATIENT_PRIOR
_OPL_O37_PATIENT_VISIT_PRIOR = OPL_O37_PATIENT_VISIT_PRIOR


class OPL_O37_PRIOR_RESULT(BaseModel):
    """HL7 v2 OPL_O37.PRIOR_RESULT group.

    Attributes:
        NK1 (List[NK1]): required
        PATIENT_PRIOR (Optional[OPL_O37_PATIENT_PRIOR]): optional
        PATIENT_VISIT_PRIOR (Optional[OPL_O37_PATIENT_VISIT_PRIOR]): optional
        AL1 (Optional[AL1]): optional
        ORDER_PRIOR (List[OPL_O37_ORDER_PRIOR]): required
    """

    NK1: list[_NK1] = Field(
        default=...,
        title="NK1",
        description="Required, repeating",
    )

    PATIENT_PRIOR: _OPL_O37_PATIENT_PRIOR | None = Field(
        default=None,
        title="PATIENT_PRIOR",
        description="Optional",
    )

    PATIENT_VISIT_PRIOR: _OPL_O37_PATIENT_VISIT_PRIOR | None = Field(
        default=None,
        title="PATIENT_VISIT_PRIOR",
        description="Optional",
    )

    AL1: _AL1 | None = Field(
        default=None,
        title="AL1",
        description="Optional",
    )

    ORDER_PRIOR: list[_OPL_O37_ORDER_PRIOR] = Field(
        default=...,
        title="ORDER_PRIOR",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
