"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORD_O02.ORDER_DIET
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.ODS import ODS
from ..segments.ORC import ORC

_NTE = NTE
_ODS = ODS
_ORC = ORC


class ORD_O02_ORDER_DIET(HL7Model):
    """HL7 v2 ORD_O02.ORDER_DIET group.

    Attributes:
        ORC (ORC): Common order segment, required
        ODS (Optional[List[ODS]]): Dietary orders, supplements, and preferences, optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common order segment",
    )

    ODS: Optional[List[_ODS]] = Field(
        default=None,
        title="ODS",
        description="Dietary orders, supplements, and preferences",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    model_config = {"populate_by_name": True}
