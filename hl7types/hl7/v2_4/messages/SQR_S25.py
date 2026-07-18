"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: SQR_S25
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
    """SQM/SQR - Schedule query message and response (S10).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (QAK): Query Acknowledgment, required
        SCHEDULE (Optional[List[SQR_S25_SCHEDULE]]): optional
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    QAK: _QAK = Field(
        title="QAK",
        description="Query Acknowledgment",
    )

    SCHEDULE: Optional[List[_SQR_S25_SCHEDULE]] = Field(
        default=None,
        title="SCHEDULE",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = ConfigDict(populate_by_name=True)
