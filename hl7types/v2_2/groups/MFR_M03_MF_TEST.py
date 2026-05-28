"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MFR_M03.MF_TEST
Type: Group
"""
from _future__ import annotations

from typing import Optional, Any
from pydantic import BaseModel, Field

from ..segments.MFE import MFE

_MFE = MFE


class MFR_M03_MF_TEST(BaseModel):
    """HL7 v2 MFR_M03.MF_TEST group.

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
