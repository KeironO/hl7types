"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCI_I22.MEDICATION_ADMINISTRATION_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXA import RXA
from ..segments.RXR import RXR

from .CCI_I22_MEDICATION_ADMINISTRATION_OBSERVATION import CCI_I22_MEDICATION_ADMINISTRATION_OBSERVATION

_CCI_I22_MEDICATION_ADMINISTRATION_OBSERVATION = CCI_I22_MEDICATION_ADMINISTRATION_OBSERVATION
_RXA = RXA
_RXR = RXR


class CCI_I22_MEDICATION_ADMINISTRATION_DETAIL(HL7Model):
    """HL7 v2 CCI_I22.MEDICATION_ADMINISTRATION_DETAIL group.

    Attributes:
        RXA (List[RXA]): required
        RXR (RXR): required
        MEDICATION_ADMINISTRATION_OBSERVATION (Optional[List[CCI_I22_MEDICATION_ADMINISTRATION_OBSERVATION]]): optional
    """

    RXA: List[_RXA] = Field(
        min_length=1,
        title="RXA",
        description="Required, repeating",
    )

    RXR: _RXR = Field(
        title="RXR",
        description="Required",
    )

    MEDICATION_ADMINISTRATION_OBSERVATION: Optional[List[_CCI_I22_MEDICATION_ADMINISTRATION_OBSERVATION]] = Field(
        default=None,
        title="MEDICATION_ADMINISTRATION_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
