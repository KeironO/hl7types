"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MFN_M18.PAYER_MF_COVERAGE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.DPS import DPS
from ..segments.MCP import MCP

_DPS = DPS
_MCP = MCP


class MFN_M18_PAYER_MF_COVERAGE(BaseModel):
    """HL7 v2 MFN_M18.PAYER_MF_COVERAGE group.

    Attributes:
        MCP (MCP): required
        DPS (Optional[List[DPS]]): optional
    """

    MCP: _MCP = Field(
        default=...,
        title="MCP",
        description="Required",
    )

    DPS: Optional[List[_DPS]] = Field(
        default=None,
        title="DPS",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
