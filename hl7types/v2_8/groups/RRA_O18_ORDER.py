"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RRA_O18.ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .RRA_O18_ADMINISTRATION import RRA_O18_ADMINISTRATION
from .RRA_O18_TIMING import RRA_O18_TIMING

_ORC = ORC
_PRT = PRT
_RRA_O18_ADMINISTRATION = RRA_O18_ADMINISTRATION
_RRA_O18_TIMING = RRA_O18_TIMING


class RRA_O18_ORDER(BaseModel):
    """HL7 v2 RRA_O18.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[List[RRA_O18_TIMING]]): optional
        ADMINISTRATION (Optional[RRA_O18_ADMINISTRATION]): optional
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

    TIMING: Optional[List[_RRA_O18_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    ADMINISTRATION: Optional[_RRA_O18_ADMINISTRATION] = Field(
        default=None,
        title="ADMINISTRATION",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
