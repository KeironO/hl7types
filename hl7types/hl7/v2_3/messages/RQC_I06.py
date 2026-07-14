"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RQC_I06
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

from ..groups.RQC_I06_PROVIDER import RQC_I06_PROVIDER

_GT1 = GT1
_MSH = MSH
_NK1 = NK1
_NTE = NTE
_PID = PID
_QRD = QRD
_QRF = QRF
_RQC_I06_PROVIDER = RQC_I06_PROVIDER


class RQC_I06(HL7Model):
    """RQC/RCL - Request/receipt of clinical data listing.

    Attributes:
        MSH (MSH): Message header segment, required
        QRD (QRD): Query definition segment, required
        QRF (Optional[QRF]): Query filter segment, optional
        PROVIDER (List[RQC_I06_PROVIDER]): required
        PID (PID): Patient Identification, required
        NK1 (Optional[List[NK1]]): Next of kin, optional
        GT1 (Optional[GT1]): Guarantor, optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="Query definition segment",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Query filter segment",
    )

    PROVIDER: List[_RQC_I06_PROVIDER] = Field(
        min_length=1,
        title="PROVIDER",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of kin",
    )

    GT1: Optional[_GT1] = Field(
        default=None,
        title="GT1",
        description="Guarantor",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    model_config = {"populate_by_name": True}
