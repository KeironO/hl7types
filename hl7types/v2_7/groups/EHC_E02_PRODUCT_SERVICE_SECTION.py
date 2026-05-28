"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: EHC_E02.PRODUCT_SERVICE_SECTION
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PSS import PSS

from .EHC_E02_PSG import EHC_E02_PSG

_EHC_E02_PSG = EHC_E02_PSG
_PSS = PSS


class EHC_E02_PRODUCT_SERVICE_SECTION(BaseModel):
    """HL7 v2 EHC_E02.PRODUCT_SERVICE_SECTION group.

    Attributes:
        PSS (PSS): required
        PSG (Optional[List[EHC_E02_PSG]]): optional
    """

    PSS: _PSS = Field(
        default=...,
        title="PSS",
        description="Required",
    )

    PSG: Optional[List[_EHC_E02_PSG]] = Field(
        default=None,
        title="PSG",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
