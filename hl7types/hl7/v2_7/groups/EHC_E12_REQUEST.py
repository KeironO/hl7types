"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: EHC_E12.REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTD import CTD
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.OBX import OBX

_CTD = CTD
_NTE = NTE
_OBR = OBR
_OBX = OBX


class EHC_E12_REQUEST(BaseModel):
    """HL7 v2 EHC_E12.REQUEST group.

    Attributes:
        CTD (Optional[CTD]): optional
        OBR (OBR): required
        NTE (Optional[NTE]): optional
        OBX (Optional[List[OBX]]): optional
    """

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: Optional[_NTE] = Field(
        default=None,
        title="NTE",
        description="Optional",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
