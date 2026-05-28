"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: SUR_P09
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.SUR_P09_FACILITY import SUR_P09_FACILITY
from ..segments.MSH import MSH

_MSH = MSH
_SUR_P09_FACILITY = SUR_P09_FACILITY


class SUR_P09(BaseModel):
    """HL7 v2 SUR_P09 message.

    Attributes:
        MSH (MSH): required
        FACILITY (List[SUR_P09_FACILITY]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    FACILITY: list[_SUR_P09_FACILITY] = Field(
        default=...,
        title="FACILITY",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
