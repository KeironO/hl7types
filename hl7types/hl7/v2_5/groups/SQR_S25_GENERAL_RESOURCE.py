"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SQR_S25.GENERAL_RESOURCE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AIG import AIG
from ..segments.NTE import NTE

_AIG = AIG
_NTE = NTE


class SQR_S25_GENERAL_RESOURCE(BaseModel):
    """HL7 v2 SQR_S25.GENERAL_RESOURCE group.

    Attributes:
        AIG (AIG): required
        NTE (Optional[List[NTE]]): optional
    """

    AIG: _AIG = Field(
        default=...,
        title="AIG",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
