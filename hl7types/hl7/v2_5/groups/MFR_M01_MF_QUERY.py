"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MFR_M01.MF_QUERY
Type: Group
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from ..segments.MFE import MFE

_MFE = MFE


class MFR_M01_MF_QUERY(BaseModel):
    """HL7 v2 MFR_M01.MF_QUERY group.

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
