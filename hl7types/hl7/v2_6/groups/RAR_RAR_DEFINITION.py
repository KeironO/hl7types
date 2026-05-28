"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RAR_RAR.DEFINITION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.QRD import QRD
from ..segments.QRF import QRF
from .RAR_RAR_ORDER import RAR_RAR_ORDER
from .RAR_RAR_PATIENT import RAR_RAR_PATIENT

_QRD = QRD
_QRF = QRF
_RAR_RAR_ORDER = RAR_RAR_ORDER
_RAR_RAR_PATIENT = RAR_RAR_PATIENT


class RAR_RAR_DEFINITION(BaseModel):
    """HL7 v2 RAR_RAR.DEFINITION group.

    Attributes:
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        PATIENT (Optional[RAR_RAR_PATIENT]): optional
        ORDER (List[RAR_RAR_ORDER]): required
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

    PATIENT: _RAR_RAR_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_RAR_RAR_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
