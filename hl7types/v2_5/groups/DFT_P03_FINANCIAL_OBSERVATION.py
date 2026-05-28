"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: DFT_P03.FINANCIAL_OBSERVATION
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX

_NTE = NTE
_OBX = OBX


class DFT_P03_FINANCIAL_OBSERVATION(BaseModel):
    """HL7 v2 DFT_P03.FINANCIAL_OBSERVATION group.

    Attributes:
        OBX (OBX): required
        NTE (Optional[List[NTE]]): optional
    """

    OBX: _OBX = Field(
        default=...,
        title="OBX",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
