"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SUR_P09
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH

from ..groups.SUR_P09_FACILITY import SUR_P09_FACILITY

_MSH = MSH
_SUR_P09_FACILITY = SUR_P09_FACILITY


class SUR_P09(HL7Model):
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

    FACILITY: List[_SUR_P09_FACILITY] = Field(
        default=...,
        title="FACILITY",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
