"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RER_RER.DEFINITION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
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
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original Style Query Filter, optional
        PATIENT (Optional[RER_RER_PATIENT]): optional
        ORDER (List[RER_RER_ORDER]): required
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

    PATIENT: Optional[_RER_RER_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_RER_RER_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = {"populate_by_name": True}
