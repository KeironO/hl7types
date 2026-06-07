"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OMQ_O57.PRIOR_RESULT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1

from .OMQ_O57_ORDER_PRIOR import OMQ_O57_ORDER_PRIOR
from .OMQ_O57_PATIENT_PRIOR import OMQ_O57_PATIENT_PRIOR
from .OMQ_O57_PATIENT_VISIT_PRIOR import OMQ_O57_PATIENT_VISIT_PRIOR

_AL1 = AL1
_OMQ_O57_ORDER_PRIOR = OMQ_O57_ORDER_PRIOR
_OMQ_O57_PATIENT_PRIOR = OMQ_O57_PATIENT_PRIOR
_OMQ_O57_PATIENT_VISIT_PRIOR = OMQ_O57_PATIENT_VISIT_PRIOR


class OMQ_O57_PRIOR_RESULT(HL7Model):
    """HL7 v2 OMQ_O57.PRIOR_RESULT group.

    Attributes:
        PATIENT_PRIOR (Optional[OMQ_O57_PATIENT_PRIOR]): optional
        PATIENT_VISIT_PRIOR (Optional[OMQ_O57_PATIENT_VISIT_PRIOR]): optional
        AL1 (Optional[List[AL1]]): optional
        ORDER_PRIOR (List[OMQ_O57_ORDER_PRIOR]): required
    """

    PATIENT_PRIOR: Optional[_OMQ_O57_PATIENT_PRIOR] = Field(
        default=None,
        title="PATIENT_PRIOR",
        description="Optional",
    )

    PATIENT_VISIT_PRIOR: Optional[_OMQ_O57_PATIENT_VISIT_PRIOR] = Field(
        default=None,
        title="PATIENT_VISIT_PRIOR",
        description="Optional",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    ORDER_PRIOR: List[_OMQ_O57_ORDER_PRIOR] = Field(
        min_length=1,
        title="ORDER_PRIOR",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
