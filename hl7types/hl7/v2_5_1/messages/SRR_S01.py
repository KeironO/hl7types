"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: SRR_S01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
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
    """SRM/SRR - Request new appointment booking (S10.3).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        SCHEDULE (Optional[SRR_S01_SCHEDULE]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    SCHEDULE: Optional[_SRR_S01_SCHEDULE] = Field(
        default=None,
        title="SCHEDULE",
    )

    model_config = {"populate_by_name": True}
