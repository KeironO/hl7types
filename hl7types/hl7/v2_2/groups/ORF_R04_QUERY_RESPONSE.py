"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ORF_R04.QUERY_RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.QRD import QRD
from ..segments.QRF import QRF

_NTE = NTE
_PID = PID
_QRD = QRD
_QRF = QRF


class ORF_R04_QUERY_RESPONSE(BaseModel):
    """HL7 v2 ORF_R04.QUERY_RESPONSE group.

    Attributes:
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        PID (Optional[PID]): optional
        NTE (Optional[List[NTE]]): optional
    """

    QRD: _QRD = Field(
        default=...,
        title="QRD",
        description="Required",
    )

    QRF: _QRF | None = Field(
        default=None,
        title="QRF",
        description="Optional",
    )

    PID: _PID | None = Field(
        default=None,
        title="PID",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
