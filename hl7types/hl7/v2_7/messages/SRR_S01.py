"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: SRR_S01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.SRR_S01_SCHEDULE import SRR_S01_SCHEDULE
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH

_ERR = ERR
_MSA = MSA
_MSH = MSH
_SRR_S01_SCHEDULE = SRR_S01_SCHEDULE


class SRR_S01(BaseModel):
    """HL7 v2 SRR_S01 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        SCHEDULE (Optional[SRR_S01_SCHEDULE]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    ERR: list[_ERR] | None = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
    )

    SCHEDULE: _SRR_S01_SCHEDULE | None = Field(
        default=None,
        title="SCHEDULE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
