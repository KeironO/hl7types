"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RRD_O14.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .RRD_O14_DISPENSE import RRD_O14_DISPENSE
from .RRD_O14_TIMING import RRD_O14_TIMING

_ORC = ORC
_PRT = PRT
_RRD_O14_DISPENSE = RRD_O14_DISPENSE
_RRD_O14_TIMING = RRD_O14_TIMING


class RRD_O14_ORDER(HL7Model):
    """HL7 v2 RRD_O14.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[List[RRD_O14_TIMING]]): optional
        DISPENSE (Optional[RRD_O14_DISPENSE]): optional
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

    TIMING: Optional[List[_RRD_O14_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    DISPENSE: Optional[_RRD_O14_DISPENSE] = Field(
        default=None,
        title="DISPENSE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
