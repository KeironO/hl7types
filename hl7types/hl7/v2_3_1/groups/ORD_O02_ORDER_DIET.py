"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ORD_O02.ORDER_DIET
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
        ORC (ORC): ORC - common order segment, required
        ODS (Optional[List[ODS]]): ODS - dietary orders, supplements, and preferences segment, optional
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="ORC - common order segment",
    )

    ODS: Optional[List[_ODS]] = Field(
        default=None,
        title="ODS",
        description=(
            "ODS - dietary orders, supplements, and preferences segment"
        ),
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    model_config = ConfigDict(populate_by_name=True)
