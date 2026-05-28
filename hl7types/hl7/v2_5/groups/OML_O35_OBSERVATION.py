"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OML_O35.OBSERVATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.TCD import TCD

_NTE = NTE
_OBX = OBX
_TCD = TCD


class OML_O35_OBSERVATION(BaseModel):
    """HL7 v2 OML_O35.OBSERVATION group.

    Attributes:
        OBX (OBX): required
        TCD (Optional[TCD]): optional
        NTE (Optional[List[NTE]]): optional
    """

    OBX: _OBX = Field(
        default=...,
        title="OBX",
        description="Required",
    )

    TCD: _TCD | None = Field(
        default=None,
        title="TCD",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
