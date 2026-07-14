"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MFN_M18.PAYER_MF_COVERAGE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DPS import DPS
from ..segments.MCP import MCP

_DPS = DPS
_MCP = MCP


class MFN_M18_PAYER_MF_COVERAGE(HL7Model):
    """HL7 v2 MFN_M18.PAYER_MF_COVERAGE group.

    Attributes:
        MCP (MCP): Master File Coverage, required
        DPS (Optional[List[DPS]]): Diagnosis and Procedure Code, optional
    """

    MCP: _MCP = Field(
        title="MCP",
        description="Master File Coverage",
    )

    DPS: Optional[List[_DPS]] = Field(
        default=None,
        title="DPS",
        description="Diagnosis and Procedure Code",
    )

    model_config = {"populate_by_name": True}
