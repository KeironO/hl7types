"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: EHC_E15.ADJUSTMENT_PAYEE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ADJ import ADJ
from ..segments.ROL import ROL

_ADJ = ADJ
_ROL = ROL


class EHC_E15_ADJUSTMENT_PAYEE(HL7Model):
    """HL7 v2 EHC_E15.ADJUSTMENT_PAYEE group.

    Attributes:
        ADJ (ADJ): required
        ROL (Optional[ROL]): optional
    """

    ADJ: _ADJ = Field(
        default=...,
        title="ADJ",
        description="Required",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
