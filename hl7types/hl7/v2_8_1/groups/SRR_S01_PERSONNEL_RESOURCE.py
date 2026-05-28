"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: SRR_S01.PERSONNEL_RESOURCE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AIP import AIP
from ..segments.NTE import NTE

_AIP = AIP
_NTE = NTE


class SRR_S01_PERSONNEL_RESOURCE(BaseModel):
    """HL7 v2 SRR_S01.PERSONNEL_RESOURCE group.

    Attributes:
        AIP (AIP): required
        NTE (Optional[List[NTE]]): optional
    """

    AIP: _AIP = Field(
        default=...,
        title="AIP",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
