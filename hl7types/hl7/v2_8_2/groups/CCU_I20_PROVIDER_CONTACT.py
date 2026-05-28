"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCU_I20.PROVIDER_CONTACT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTD import CTD
from ..segments.PRD import PRD

_CTD = CTD
_PRD = PRD


class CCU_I20_PROVIDER_CONTACT(BaseModel):
    """HL7 v2 CCU_I20.PROVIDER_CONTACT group.

    Attributes:
        PRD (PRD): required
        CTD (Optional[List[CTD]]): optional
    """

    PRD: _PRD = Field(
        default=...,
        title="PRD",
        description="Required",
    )

    CTD: list[_CTD] | None = Field(
        default=None,
        title="CTD",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
