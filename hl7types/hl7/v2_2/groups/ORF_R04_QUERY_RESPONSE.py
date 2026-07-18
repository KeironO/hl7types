"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ORF_R04.QUERY_RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.QRD import QRD
from ..segments.QRF import QRF

_NTE = NTE
_PID = PID
_QRD = QRD
_QRF = QRF


class ORF_R04_QUERY_RESPONSE(HL7Model):
    """HL7 v2 ORF_R04.QUERY_RESPONSE group.

    Attributes:
        QRD (QRD): QUERY DEFINITION, required
        QRF (Optional[QRF]): QUERY FILTER, optional
        PID (Optional[PID]): PATIENT IDENTIFICATION, optional
        NTE (Optional[List[NTE]]): NOTES AND COMMENTS, optional
    """

    QRD: _QRD = Field(
        title="QRD",
        description="QUERY DEFINITION",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="QUERY FILTER",
    )

    PID: Optional[_PID] = Field(
        default=None,
        title="PID",
        description="PATIENT IDENTIFICATION",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NOTES AND COMMENTS",
    )

    model_config = ConfigDict(populate_by_name=True)
