"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RGR_RGR.DEFINITION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.QRD import QRD
from ..segments.QRF import QRF

from .RGR_RGR_ORDER import RGR_RGR_ORDER
from .RGR_RGR_PATIENT import RGR_RGR_PATIENT

_QRD = QRD
_QRF = QRF
_RGR_RGR_ORDER = RGR_RGR_ORDER
_RGR_RGR_PATIENT = RGR_RGR_PATIENT


class RGR_RGR_DEFINITION(HL7Model):
    """HL7 v2 RGR_RGR.DEFINITION group.

    Attributes:
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        PATIENT (Optional[RGR_RGR_PATIENT]): optional
        ORDER (List[RGR_RGR_ORDER]): required
    """

    QRD: _QRD = Field(
        title="QRD",
        description="Required",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Optional",
    )

    PATIENT: Optional[_RGR_RGR_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_RGR_RGR_ORDER] = Field(
        min_length=1,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
