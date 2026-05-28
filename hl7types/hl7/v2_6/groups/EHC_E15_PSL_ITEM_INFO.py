"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: EHC_E15.PSL_ITEM_INFO
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ADJ import ADJ
from ..segments.PSL import PSL

_ADJ = ADJ
_PSL = PSL


class EHC_E15_PSL_ITEM_INFO(BaseModel):
    """HL7 v2 EHC_E15.PSL_ITEM_INFO group.

    Attributes:
        PSL (PSL): required
        ADJ (Optional[List[ADJ]]): optional
    """

    PSL: _PSL = Field(
        default=...,
        title="PSL",
        description="Required",
    )

    ADJ: list[_ADJ] | None = Field(
        default=None,
        title="ADJ",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
