"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: EHC_E24.PSL_ITEM_INFO
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AUT import AUT
from ..segments.PSL import PSL
from .EHC_E24_PAYER_ADJUSTMENT import EHC_E24_PAYER_ADJUSTMENT

_AUT = AUT
_EHC_E24_PAYER_ADJUSTMENT = EHC_E24_PAYER_ADJUSTMENT
_PSL = PSL


class EHC_E24_PSL_ITEM_INFO(BaseModel):
    """HL7 v2 EHC_E24.PSL_ITEM_INFO group.

    Attributes:
        PSL (PSL): required
        AUT (Optional[AUT]): optional
        PAYER_ADJUSTMENT (Optional[List[EHC_E24_PAYER_ADJUSTMENT]]): optional
    """

    PSL: _PSL = Field(
        default=...,
        title="PSL",
        description="Required",
    )

    AUT: _AUT | None = Field(
        default=None,
        title="AUT",
        description="Optional",
    )

    PAYER_ADJUSTMENT: list[_EHC_E24_PAYER_ADJUSTMENT] | None = Field(
        default=None,
        title="PAYER_ADJUSTMENT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
