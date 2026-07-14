"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCQ_I19.PROVIDER_CONTACT
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


class CCQ_I19_PROVIDER_CONTACT(HL7Model):
    """HL7 v2 CCQ_I19.PROVIDER_CONTACT group.

    Attributes:
        PRD (PRD): Provider Data, required
        CTD (Optional[List[CTD]]): Contact Data, optional
    """

    PRD: _PRD = Field(
        title="PRD",
        description="Provider Data",
    )

    CTD: Optional[List[_CTD]] = Field(
        default=None,
        title="CTD",
        description="Contact Data",
    )

    model_config = {"populate_by_name": True}
