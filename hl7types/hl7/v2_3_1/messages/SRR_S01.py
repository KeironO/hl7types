"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SRR_S01
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
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
    """SRM/SRR - Request new appointment booking.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MSA (MSA): MSA - message acknowledgment segment, required
        ERR (Optional[ERR]): ERR - error segment, optional
        SCHEDULE (Optional[SRR_S01_SCHEDULE]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="MSA - message acknowledgment segment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="ERR - error segment",
    )

    SCHEDULE: Optional[_SRR_S01_SCHEDULE] = Field(
        default=None,
        title="SCHEDULE",
    )

    model_config = ConfigDict(populate_by_name=True)
