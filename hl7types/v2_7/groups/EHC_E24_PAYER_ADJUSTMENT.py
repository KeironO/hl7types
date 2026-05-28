"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: EHC_E24.PAYER_ADJUSTMENT
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.ADJ import ADJ

_ADJ = ADJ


class EHC_E24_PAYER_ADJUSTMENT(BaseModel):
    """HL7 v2 EHC_E24.PAYER_ADJUSTMENT group.

    Attributes:
        ADJ (ADJ): required
    """

    ADJ: _ADJ = Field(
        default=...,
        title="ADJ",
        description="Required",
    )

    model_config = {"populate_by_name": True}
