"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MFN_M01.MF
Type: Group
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from ..segments.MFE import MFE

_MFE = MFE


class MFN_M01_MF(BaseModel):
    """HL7 v2 MFN_M01.MF group.

    Attributes:
        MFE (MFE): required
        anyhl7segment (Optional[Any]): optional
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    anyhl7segment: Any | None = None

    model_config = {"populate_by_name": True}
