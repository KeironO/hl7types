"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: PGL_PC6.ORDER_OBSERVATION
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PRT import PRT
from ..segments.VAR import VAR

_NTE = NTE
_OBX = OBX
_PRT = PRT
_VAR = VAR


class PGL_PC6_ORDER_OBSERVATION(BaseModel):
    """HL7 v2 PGL_PC6.ORDER_OBSERVATION group.

    Attributes:
        OBX (OBX): required
        PRT (Optional[List[PRT]]): optional
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
