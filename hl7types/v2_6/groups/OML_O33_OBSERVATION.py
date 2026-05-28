"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OML_O33.OBSERVATION
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.TCD import TCD

_NTE = NTE
_OBX = OBX
_TCD = TCD


class OML_O33_OBSERVATION(BaseModel):
    """HL7 v2 OML_O33.OBSERVATION group.

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

    TCD: Optional[_TCD] = Field(
        default=None,
        title="TCD",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
