"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RER_RER.DEFINITION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.QRD import QRD
from ..segments.QRF import QRF

from .RER_RER_ORDER import RER_RER_ORDER
from .RER_RER_PATIENT import RER_RER_PATIENT

_QRD = QRD
_QRF = QRF
_RER_RER_ORDER = RER_RER_ORDER
_RER_RER_PATIENT = RER_RER_PATIENT


class RER_RER_DEFINITION(HL7Model):
    """HL7 v2 RER_RER.DEFINITION group.

    Attributes:
        QRD (QRD): QRD - original-style query definition segment, required
        QRF (Optional[QRF]): QRF - original style query filter segment, optional
        PATIENT (Optional[RER_RER_PATIENT]): optional
        ORDER (List[RER_RER_ORDER]): required
    """

    QRD: _QRD = Field(
        title="QRD",
        description="QRD - original-style query definition segment",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="QRF - original style query filter segment",
    )

    PATIENT: Optional[_RER_RER_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_RER_RER_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
