"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RPI_I01.PROVIDER
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


class RPI_I01_PROVIDER(HL7Model):
    """HL7 v2 RPI_I01.PROVIDER group.

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
