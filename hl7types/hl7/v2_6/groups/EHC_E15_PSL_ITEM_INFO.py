"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: EHC_E15.PSL_ITEM_INFO
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ADJ import ADJ
from ..segments.PSL import PSL

_ADJ = ADJ
_PSL = PSL


class EHC_E15_PSL_ITEM_INFO(HL7Model):
    """HL7 v2 EHC_E15.PSL_ITEM_INFO group.

    Attributes:
        PSL (PSL): Product/Service Line Item, required
        ADJ (Optional[List[ADJ]]): Adjustment, optional
    """

    PSL: _PSL = Field(
        title="PSL",
        description="Product/Service Line Item",
    )

    ADJ: Optional[List[_ADJ]] = Field(
        default=None,
        title="ADJ",
        description="Adjustment",
    )

    model_config = ConfigDict(populate_by_name=True)
