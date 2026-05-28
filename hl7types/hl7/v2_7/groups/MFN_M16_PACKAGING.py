"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: MFN_M16.PACKAGING
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PCE import PCE
from ..segments.PKG import PKG

_PCE = PCE
_PKG = PKG


class MFN_M16_PACKAGING(BaseModel):
    """HL7 v2 MFN_M16.PACKAGING group.

    Attributes:
        PKG (PKG): required
        PCE (Optional[List[PCE]]): optional
    """

    PKG: _PKG = Field(
        default=...,
        title="PKG",
        description="Required",
    )

    PCE: Optional[List[_PCE]] = Field(
        default=None,
        title="PCE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
