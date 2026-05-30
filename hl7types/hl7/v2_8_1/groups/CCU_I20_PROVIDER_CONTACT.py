"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCU_I20.PROVIDER_CONTACT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTD import CTD
from ..segments.PRD import PRD

_CTD = CTD
_PRD = PRD


class CCU_I20_PROVIDER_CONTACT(HL7Model):
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

    CTD: Optional[List[_CTD]] = Field(
        default=None,
        title="CTD",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
