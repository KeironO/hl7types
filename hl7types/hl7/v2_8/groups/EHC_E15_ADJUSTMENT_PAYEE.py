"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EHC_E15.ADJUSTMENT_PAYEE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.ADJ import ADJ
from ..segments.PRT import PRT
from ..segments.ROL import ROL

_ADJ = ADJ
_PRT = PRT
_ROL = ROL


class EHC_E15_ADJUSTMENT_PAYEE(BaseModel):
    """HL7 v2 EHC_E15.ADJUSTMENT_PAYEE group.

    Attributes:
        ADJ (ADJ): required
        PRT (Optional[PRT]): optional
        ROL (Optional[ROL]): optional
    """

    ADJ: _ADJ = Field(
        default=...,
        title="ADJ",
        description="Required",
    )

    PRT: Optional[_PRT] = Field(
        default=None,
        title="PRT",
        description="Optional",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
