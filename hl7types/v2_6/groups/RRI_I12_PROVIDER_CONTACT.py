"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RRI_I12.PROVIDER_CONTACT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTD import CTD
from ..segments.PRD import PRD

_CTD = CTD
_PRD = PRD


class RRI_I12_PROVIDER_CONTACT(BaseModel):
    """HL7 v2 RRI_I12.PROVIDER_CONTACT group.

    Attributes:
        PRD (PRD): required
        CTD (Optional[List[CTD]]): optional
    """

    PRD: _PRD = Field(
        default=...,
        title="PRD",
        description="Required",
    )

    CTD: Optional[List[_CTD]] = Field(
        default=None,
        title="CTD",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
