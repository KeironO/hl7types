"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RAR_RAR.DEFINITION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.QRD import QRD
from ..segments.QRF import QRF

from .RAR_RAR_ORDER import RAR_RAR_ORDER
from .RAR_RAR_PATIENT import RAR_RAR_PATIENT

_QRD = QRD
_QRF = QRF
_RAR_RAR_ORDER = RAR_RAR_ORDER
_RAR_RAR_PATIENT = RAR_RAR_PATIENT


class RAR_RAR_DEFINITION(HL7Model):
    """HL7 v2 RAR_RAR.DEFINITION group.

    Attributes:
        QRD (QRD): Query definition segment, required
        QRF (Optional[QRF]): Query filter segment, optional
        PATIENT (Optional[RAR_RAR_PATIENT]): optional
        ORDER (List[RAR_RAR_ORDER]): required
    """

    QRD: _QRD = Field(
        title="QRD",
        description="Query definition segment",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Query filter segment",
    )

    PATIENT: Optional[_RAR_RAR_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_RAR_RAR_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = {"populate_by_name": True}
