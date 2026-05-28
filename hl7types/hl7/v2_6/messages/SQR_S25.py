"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: SQR_S25
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.SQR_S25_SCHEDULE import SQR_S25_SCHEDULE
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_SQR_S25_SCHEDULE = SQR_S25_SCHEDULE


class SQR_S25(BaseModel):
    """HL7 v2 SQR_S25 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        QAK (QAK): required
        SCHEDULE (Optional[List[SQR_S25_SCHEDULE]]): optional
        DSC (Optional[DSC]): optional
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

    QAK: _QAK = Field(
        default=...,
        title="QAK",
        description="Required",
    )

    SCHEDULE: list[_SQR_S25_SCHEDULE] | None = Field(
        default=None,
        title="SCHEDULE",
        description="Optional, repeating",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
