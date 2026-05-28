"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RRE_O12.ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .RRE_O12_ENCODING import RRE_O12_ENCODING
from .RRE_O12_TIMING import RRE_O12_TIMING

_ORC = ORC
_PRT = PRT
_RRE_O12_ENCODING = RRE_O12_ENCODING
_RRE_O12_TIMING = RRE_O12_TIMING


class RRE_O12_ORDER(BaseModel):
    """HL7 v2 RRE_O12.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[List[RRE_O12_TIMING]]): optional
        ENCODING (Optional[RRE_O12_ENCODING]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING: Optional[List[_RRE_O12_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    ENCODING: Optional[_RRE_O12_ENCODING] = Field(
        default=None,
        title="ENCODING",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
