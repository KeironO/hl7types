"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: SRR_S01
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH

from ..groups.SRR_S01_SCHEDULE import SRR_S01_SCHEDULE

_ERR = ERR
_MSA = MSA
_MSH = MSH
_SRR_S01_SCHEDULE = SRR_S01_SCHEDULE


class SRR_S01(HL7Model):
    """HL7 v2 SRR_S01 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        SCHEDULE (Optional[SRR_S01_SCHEDULE]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Required",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    SCHEDULE: Optional[_SRR_S01_SCHEDULE] = Field(
        default=None,
        title="SCHEDULE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
