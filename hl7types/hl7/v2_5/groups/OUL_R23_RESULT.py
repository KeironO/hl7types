"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OUL_R23.RESULT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.SID import SID
from ..segments.TCD import TCD

_NTE = NTE
_OBX = OBX
_SID = SID
_TCD = TCD


class OUL_R23_RESULT(BaseModel):
    """HL7 v2 OUL_R23.RESULT group.

    Attributes:
        OBX (OBX): required
        TCD (Optional[TCD]): optional
        SID (Optional[List[SID]]): optional
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

    SID: list[_SID] | None = Field(
        default=None,
        title="SID",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
