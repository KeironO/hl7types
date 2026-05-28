"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MFN_M03.MF_TEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, Any
from pydantic import BaseModel, Field

from ..segments.MFE import MFE

_MFE = MFE


class MFN_M03_MF_TEST(BaseModel):
    """HL7 v2 MFN_M03.MF_TEST group.

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
