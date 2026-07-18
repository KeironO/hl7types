"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RRE_O12.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC

from .RRE_O12_ENCODING import RRE_O12_ENCODING
from .RRE_O12_TIMING import RRE_O12_TIMING

_ORC = ORC
_RRE_O12_ENCODING = RRE_O12_ENCODING
_RRE_O12_TIMING = RRE_O12_TIMING


class RRE_O12_ORDER(HL7Model):
    """HL7 v2 RRE_O12.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        TIMING (Optional[List[RRE_O12_TIMING]]): optional
        ENCODING (Optional[RRE_O12_ENCODING]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    TIMING: Optional[List[_RRE_O12_TIMING]] = Field(
        default=None,
        title="TIMING",
    )

    ENCODING: Optional[_RRE_O12_ENCODING] = Field(
        default=None,
        title="ENCODING",
    )

    model_config = ConfigDict(populate_by_name=True)
