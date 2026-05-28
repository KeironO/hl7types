"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OUL_R21.OBSERVATION
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.SID import SID
from ..segments.TCD import TCD

_NTE = NTE
_OBX = OBX
_SID = SID
_TCD = TCD


class OUL_R21_OBSERVATION(BaseModel):
    """HL7 v2 OUL_R21.OBSERVATION group.

    Attributes:
        OBX (Optional[OBX]): optional
        TCD (Optional[TCD]): optional
        SID (Optional[List[SID]]): optional
        NTE (Optional[List[NTE]]): optional
    """

    OBX: Optional[_OBX] = Field(
        default=None,
        title="OBX",
        description="Optional",
    )

    TCD: Optional[_TCD] = Field(
        default=None,
        title="TCD",
        description="Optional",
    )

    SID: Optional[List[_SID]] = Field(
        default=None,
        title="SID",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
