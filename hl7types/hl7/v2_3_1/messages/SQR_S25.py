"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SQR_S25
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK

from ..groups.SQR_S25_SCHEDULE import SQR_S25_SCHEDULE

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_SQR_S25_SCHEDULE = SQR_S25_SCHEDULE


class SQR_S25(HL7Model):
    """SQM/SQR - Schedule query message and response.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MSA (MSA): MSA - message acknowledgment segment, required
        ERR (Optional[ERR]): ERR - error segment, optional
        QAK (QAK): Query Acknowledgement, required
        SCHEDULE (Optional[List[SQR_S25_SCHEDULE]]): optional
        DSC (Optional[DSC]): DSC - Continuation pointer segment, optional
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

    QAK: _QAK = Field(
        title="QAK",
        description="Query Acknowledgement",
    )

    SCHEDULE: Optional[List[_SQR_S25_SCHEDULE]] = Field(
        default=None,
        title="SCHEDULE",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="DSC - Continuation pointer segment",
    )

    model_config = {"populate_by_name": True}
