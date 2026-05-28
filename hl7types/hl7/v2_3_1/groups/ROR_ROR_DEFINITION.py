"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ROR_ROR.DEFINITION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.QRD import QRD
from ..segments.QRF import QRF
from .ROR_ROR_ORDER import ROR_ROR_ORDER
from .ROR_ROR_PATIENT import ROR_ROR_PATIENT

_QRD = QRD
_QRF = QRF
_ROR_ROR_ORDER = ROR_ROR_ORDER
_ROR_ROR_PATIENT = ROR_ROR_PATIENT


class ROR_ROR_DEFINITION(BaseModel):
    """HL7 v2 ROR_ROR.DEFINITION group.

    Attributes:
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        PATIENT (Optional[ROR_ROR_PATIENT]): optional
        ORDER (List[ROR_ROR_ORDER]): required
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

    PATIENT: _ROR_ROR_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_ROR_ROR_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
