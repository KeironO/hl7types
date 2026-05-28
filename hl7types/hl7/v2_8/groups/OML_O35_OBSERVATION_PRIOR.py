"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OML_O35.OBSERVATION_PRIOR
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PRT import PRT

_NTE = NTE
_OBX = OBX
_PRT = PRT


class OML_O35_OBSERVATION_PRIOR(BaseModel):
    """HL7 v2 OML_O35.OBSERVATION_PRIOR group.

    Attributes:
        OBX (OBX): required
        PRT (Optional[List[PRT]]): optional
        NTE (Optional[List[NTE]]): optional
    """

    OBX: _OBX = Field(
        default=...,
        title="OBX",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
