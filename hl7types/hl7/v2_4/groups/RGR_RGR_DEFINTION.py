"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RGR_RGR.DEFINTION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.QRD import QRD
from ..segments.QRF import QRF

from .RGR_RGR_ORDER import RGR_RGR_ORDER
from .RGR_RGR_PATIENT import RGR_RGR_PATIENT

_QRD = QRD
_QRF = QRF
_RGR_RGR_ORDER = RGR_RGR_ORDER
_RGR_RGR_PATIENT = RGR_RGR_PATIENT


class RGR_RGR_DEFINTION(HL7Model):
    """HL7 v2 RGR_RGR.DEFINTION group.

    Attributes:
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original Style Query Filter, optional
        PATIENT (Optional[RGR_RGR_PATIENT]): optional
        ORDER (List[RGR_RGR_ORDER]): required
    """

    QRD: _QRD = Field(
        title="QRD",
        description="Original-Style Query Definition",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Original Style Query Filter",
    )

    PATIENT: Optional[_RGR_RGR_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_RGR_RGR_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
