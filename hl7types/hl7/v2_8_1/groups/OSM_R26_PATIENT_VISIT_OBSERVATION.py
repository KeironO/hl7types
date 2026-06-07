"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OSM_R26.PATIENT_VISIT_OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.PRT import PRT

_OBX = OBX
_PRT = PRT


class OSM_R26_PATIENT_VISIT_OBSERVATION(HL7Model):
    """HL7 v2 OSM_R26.PATIENT_VISIT_OBSERVATION group.

    Attributes:
        OBX (OBX): required
        PRT (Optional[List[PRT]]): optional
    """

    OBX: _OBX = Field(
        title="OBX",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
