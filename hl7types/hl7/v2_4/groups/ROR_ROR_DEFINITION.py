"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ROR_ROR.DEFINITION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.QRD import QRD
from ..segments.QRF import QRF

from .ROR_ROR_ORDER import ROR_ROR_ORDER
from .ROR_ROR_PATIENT import ROR_ROR_PATIENT

_QRD = QRD
_QRF = QRF
_ROR_ROR_ORDER = ROR_ROR_ORDER
_ROR_ROR_PATIENT = ROR_ROR_PATIENT


class ROR_ROR_DEFINITION(HL7Model):
    """HL7 v2 ROR_ROR.DEFINITION group.

    Attributes:
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original Style Query Filter, optional
        PATIENT (Optional[ROR_ROR_PATIENT]): optional
        ORDER (List[ROR_ROR_ORDER]): required
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

    PATIENT: Optional[_ROR_ROR_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_ROR_ROR_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = {"populate_by_name": True}
