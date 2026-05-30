"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RQC_I05
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.GT1 import GT1
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.QRD import QRD
from ..segments.QRF import QRF
from ..segments.SFT import SFT

from ..groups.RQC_I05_PROVIDER import RQC_I05_PROVIDER

_GT1 = GT1
_MSH = MSH
_NK1 = NK1
_NTE = NTE
_PID = PID
_QRD = QRD
_QRF = QRF
_RQC_I05_PROVIDER = RQC_I05_PROVIDER
_SFT = SFT


class RQC_I05(HL7Model):
    """HL7 v2 RQC_I05 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        PROVIDER (List[RQC_I05_PROVIDER]): required
        PID (PID): required
        NK1 (Optional[List[NK1]]): optional
        GT1 (Optional[List[GT1]]): optional
        NTE (Optional[List[NTE]]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    QRD: _QRD = Field(
        default=...,
        title="QRD",
        description="Required",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Optional",
    )

    PROVIDER: List[_RQC_I05_PROVIDER] = Field(
        default=...,
        title="PROVIDER",
        description="Required, repeating",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
