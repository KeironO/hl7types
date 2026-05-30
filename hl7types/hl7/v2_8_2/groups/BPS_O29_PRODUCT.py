"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: BPS_O29.PRODUCT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.BPX import BPX
from ..segments.NTE import NTE

_BPX = BPX
_NTE = NTE


class BPS_O29_PRODUCT(HL7Model):
    """HL7 v2 BPS_O29.PRODUCT group.

    Attributes:
        BPX (BPX): required
        NTE (Optional[List[NTE]]): optional
    """

    BPX: _BPX = Field(
        default=...,
        title="BPX",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
