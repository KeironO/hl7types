"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
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
    """SQM/SQR - Query schedule information.

    Attributes:
        MSH (MSH): Message header segment, required
        MSA (MSA): Message acknowledgement segment, required
        ERR (Optional[ERR]): Error segment, optional
        QAK (QAK): Query Acknowledgement, required
        SCHEDULE (Optional[List[SQR_S25_SCHEDULE]]): optional
        DSC (Optional[DSC]): Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message acknowledgement segment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Error segment",
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
        description="Continuation pointer segment",
    )

    model_config = ConfigDict(populate_by_name=True)
