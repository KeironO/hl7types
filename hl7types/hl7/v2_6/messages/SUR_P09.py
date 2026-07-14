"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: SUR_P09
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH

from ..groups.SUR_P09_FACILITY import SUR_P09_FACILITY

_MSH = MSH
_SUR_P09_FACILITY = SUR_P09_FACILITY


class SUR_P09(HL7Model):
    """SUR - Summary product experience report (S7.11.2).

    Attributes:
        MSH (MSH): Message Header, required
        FACILITY (List[SUR_P09_FACILITY]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    FACILITY: List[_SUR_P09_FACILITY] = Field(
        min_length=1,
        title="FACILITY",
    )

    model_config = {"populate_by_name": True}
