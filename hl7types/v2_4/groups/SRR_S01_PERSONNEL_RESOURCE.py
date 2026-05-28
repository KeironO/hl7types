"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: SRR_S01.PERSONNEL_RESOURCE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
