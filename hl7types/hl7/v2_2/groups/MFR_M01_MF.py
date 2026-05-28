"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MFR_M01.MF
Type: Group
"""
from __future__ import annotations

from typing import Optional, Any
from pydantic import BaseModel, Field

from ..segments.MFE import MFE

_MFE = MFE


class MFR_M01_MF(BaseModel):
    """HL7 v2 MFR_M01.MF group.

    Attributes:
        MFE (MFE): required
        anyzsegment (Optional[Any]): optional
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    anyzsegment: Optional[Any] = None

    model_config = {"populate_by_name": True}
