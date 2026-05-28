"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OUL_R22.RESULT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PRT import PRT
from ..segments.SID import SID
from ..segments.TCD import TCD

_NTE = NTE
_OBX = OBX
_PRT = PRT
_SID = SID
_TCD = TCD


class OUL_R22_RESULT(BaseModel):
    """HL7 v2 OUL_R22.RESULT group.

    Attributes:
        OBX (OBX): required
        PRT (Optional[List[PRT]]): optional
        TCD (Optional[TCD]): optional
        SID (Optional[List[SID]]): optional
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
