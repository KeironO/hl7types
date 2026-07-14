"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OPL_O37.PRIOR_RESULT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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


class OPL_O37_PRIOR_RESULT(HL7Model):
    """HL7 v2 OPL_O37.PRIOR_RESULT group.

    Attributes:
        NK1 (List[NK1]): Next of Kin / Associated Parties, required
        PATIENT_PRIOR (Optional[OPL_O37_PATIENT_PRIOR]): optional
        PATIENT_VISIT_PRIOR (Optional[OPL_O37_PATIENT_VISIT_PRIOR]): optional
        AL1 (Optional[AL1]): Patient Allergy Information, optional
        ORDER_PRIOR (List[OPL_O37_ORDER_PRIOR]): required
    """

    NK1: List[_NK1] = Field(
        min_length=1,
        title="NK1",
        description="Next of Kin / Associated Parties",
    )

    PATIENT_PRIOR: Optional[_OPL_O37_PATIENT_PRIOR] = Field(
        default=None,
        title="PATIENT_PRIOR",
    )

    PATIENT_VISIT_PRIOR: Optional[_OPL_O37_PATIENT_VISIT_PRIOR] = Field(
        default=None,
        title="PATIENT_VISIT_PRIOR",
    )

    AL1: Optional[_AL1] = Field(
        default=None,
        title="AL1",
        description="Patient Allergy Information",
    )

    ORDER_PRIOR: List[_OPL_O37_ORDER_PRIOR] = Field(
        min_length=1,
        title="ORDER_PRIOR",
    )

    model_config = {"populate_by_name": True}
