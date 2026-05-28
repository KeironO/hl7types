"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: EHC_E04.PRODUCT_SERVICE_GROUP
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PSG import PSG
from ..segments.PSL import PSL

_PSG = PSG
_PSL = PSL


class EHC_E04_PRODUCT_SERVICE_GROUP(BaseModel):
    """HL7 v2 EHC_E04.PRODUCT_SERVICE_GROUP group.

    Attributes:
        PSG (PSG): required
        PSL (Optional[List[PSL]]): optional
    """

    PSG: _PSG = Field(
        default=...,
        title="PSG",
        description="Required",
    )

    PSL: Optional[List[_PSL]] = Field(
        default=None,
        title="PSL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
