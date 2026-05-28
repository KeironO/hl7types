"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RDR_RDR.DEFINITION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.QRD import QRD
from ..segments.QRF import QRF

from .RDR_RDR_ORDER import RDR_RDR_ORDER
from .RDR_RDR_PATIENT import RDR_RDR_PATIENT

_QRD = QRD
_QRF = QRF
_RDR_RDR_ORDER = RDR_RDR_ORDER
_RDR_RDR_PATIENT = RDR_RDR_PATIENT


class RDR_RDR_DEFINITION(BaseModel):
    """HL7 v2 RDR_RDR.DEFINITION group.

    Attributes:
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        PATIENT (Optional[RDR_RDR_PATIENT]): optional
        ORDER (List[RDR_RDR_ORDER]): required
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

    PATIENT: Optional[_RDR_RDR_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_RDR_RDR_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
