"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ORD_O04.ORDER_DIET
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.ODS import ODS
from ..segments.ORC import ORC

from .ORD_O04_TIMING_DIET import ORD_O04_TIMING_DIET

_NTE = NTE
_ODS = ODS
_ORC = ORC
_ORD_O04_TIMING_DIET = ORD_O04_TIMING_DIET


class ORD_O04_ORDER_DIET(HL7Model):
    """HL7 v2 ORD_O04.ORDER_DIET group.

    Attributes:
        ORC (ORC): Common Order, required
        TIMING_DIET (Optional[List[ORD_O04_TIMING_DIET]]): optional
        ODS (Optional[List[ODS]]): Dietary Orders, Supplements, and Preferences, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    TIMING_DIET: Optional[List[_ORD_O04_TIMING_DIET]] = Field(
        default=None,
        title="TIMING_DIET",
    )

    ODS: Optional[List[_ODS]] = Field(
        default=None,
        title="ODS",
        description="Dietary Orders, Supplements, and Preferences",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}
