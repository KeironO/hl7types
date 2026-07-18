"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ERP_R09
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERQ import ERQ
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK

_DSC = DSC
_ERQ = ERQ
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK


class ERP_R09(HL7Model):
    """Event Replay Response.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MSA (MSA): MSA - message acknowledgment segment, required
        ERR (Optional[ERR]): ERR - error segment, optional
        QAK (QAK): Query Acknowledgement, required
        ERQ (ERQ): ERQ - event replay query segment, required
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

    ERQ: _ERQ = Field(
        title="ERQ",
        description="ERQ - event replay query segment",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="DSC - Continuation pointer segment",
    )

    model_config = ConfigDict(populate_by_name=True)
