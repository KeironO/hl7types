"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RER_RER.DEFINITION
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.QRD import QRD
from ..segments.QRF import QRF

from .RER_RER_ORDER import RER_RER_ORDER
from .RER_RER_PATIENT import RER_RER_PATIENT

_QRD = QRD
_QRF = QRF
_RER_RER_ORDER = RER_RER_ORDER
_RER_RER_PATIENT = RER_RER_PATIENT


class RER_RER_DEFINITION(BaseModel):
    """HL7 v2 RER_RER.DEFINITION group.

    Attributes:
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        PATIENT (Optional[RER_RER_PATIENT]): optional
        ORDER (List[RER_RER_ORDER]): required
    """

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

    PATIENT: Optional[_RER_RER_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_RER_RER_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
