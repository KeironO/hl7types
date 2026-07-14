"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: EHC_E24.PSL_ITEM_INFO
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ADJ import ADJ
from ..segments.AUT import AUT
from ..segments.PSL import PSL

_ADJ = ADJ
_AUT = AUT
_PSL = PSL


class EHC_E24_PSL_ITEM_INFO(HL7Model):
    """HL7 v2 EHC_E24.PSL_ITEM_INFO group.

    Attributes:
        PSL (PSL): Product/Service Line Item, required
        AUT (Optional[AUT]): Authorization Information, optional
        ADJ (Optional[List[ADJ]]): Adjustment, optional
    """

    PSL: _PSL = Field(
        title="PSL",
        description="Product/Service Line Item",
    )

    AUT: Optional[_AUT] = Field(
        default=None,
        title="AUT",
        description="Authorization Information",
    )

    ADJ: Optional[List[_ADJ]] = Field(
        default=None,
        title="ADJ",
        description="Adjustment",
    )

    model_config = {"populate_by_name": True}
