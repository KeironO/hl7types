"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OPU_R25.PATIENT_VISIT_OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PRT import PRT

_NTE = NTE
_OBX = OBX
_PRT = PRT


class OPU_R25_PATIENT_VISIT_OBSERVATION(HL7Model):
    """HL7 v2 OPU_R25.PATIENT_VISIT_OBSERVATION group.

    Attributes:
        OBX (OBX): required
        NTE (Optional[List[NTE]]): optional
        PRT (Optional[List[PRT]]): optional
    """

    OBX: _OBX = Field(
        default=...,
        title="OBX",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
