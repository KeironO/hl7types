"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: BTS_O31.PRODUCT_STATUS
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.BTX import BTX
from ..segments.NTE import NTE

_BTX = BTX
_NTE = NTE


class BTS_O31_PRODUCT_STATUS(HL7Model):
    """HL7 v2 BTS_O31.PRODUCT_STATUS group.

    Attributes:
        BTX (BTX): Blood Product Transfusion/Disposition, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    BTX: _BTX = Field(
        title="BTX",
        description="Blood Product Transfusion/Disposition",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}
