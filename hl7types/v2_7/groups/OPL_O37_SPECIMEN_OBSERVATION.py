"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OPL_O37.SPECIMEN_OBSERVATION
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.PRT import PRT

_OBX = OBX
_PRT = PRT


class OPL_O37_SPECIMEN_OBSERVATION(BaseModel):
    """HL7 v2 OPL_O37.SPECIMEN_OBSERVATION group.

    Attributes:
        OBX (OBX): required
        PRT (Optional[List[PRT]]): optional
    """

    OBX: _OBX = Field(
        default=...,
        title="OBX",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
