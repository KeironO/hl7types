"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OMD_O03.ORDER_DIET
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC

from .OMD_O03_DIET import OMD_O03_DIET
from .OMD_O03_TIMING_DIET import OMD_O03_TIMING_DIET

_OMD_O03_DIET = OMD_O03_DIET
_OMD_O03_TIMING_DIET = OMD_O03_TIMING_DIET
_ORC = ORC


class OMD_O03_ORDER_DIET(HL7Model):
    """HL7 v2 OMD_O03.ORDER_DIET group.

    Attributes:
        ORC (ORC): required
        TIMING_DIET (Optional[List[OMD_O03_TIMING_DIET]]): optional
        DIET (Optional[OMD_O03_DIET]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING_DIET: Optional[List[_OMD_O03_TIMING_DIET]] = Field(
        default=None,
        title="TIMING_DIET",
        description="Optional, repeating",
    )

    DIET: Optional[_OMD_O03_DIET] = Field(
        default=None,
        title="DIET",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
