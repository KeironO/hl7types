"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: EHC_E24.PSL_ITEM_INFO
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AUT import AUT
from ..segments.PSL import PSL

from .EHC_E24_PAYER_ADJUSTMENT import EHC_E24_PAYER_ADJUSTMENT

_AUT = AUT
_EHC_E24_PAYER_ADJUSTMENT = EHC_E24_PAYER_ADJUSTMENT
_PSL = PSL


class EHC_E24_PSL_ITEM_INFO(HL7Model):
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

    AUT: Optional[_AUT] = Field(
        default=None,
        title="AUT",
        description="Optional",
    )

    PAYER_ADJUSTMENT: Optional[List[_EHC_E24_PAYER_ADJUSTMENT]] = Field(
        default=None,
        title="PAYER_ADJUSTMENT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
