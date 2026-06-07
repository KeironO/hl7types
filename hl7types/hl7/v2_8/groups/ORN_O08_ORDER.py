"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORN_O08.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.PRT import PRT
from ..segments.RQ1 import RQ1
from ..segments.RQD import RQD

from .ORN_O08_TIMING import ORN_O08_TIMING

_NTE = NTE
_ORC = ORC
_ORN_O08_TIMING = ORN_O08_TIMING
_PRT = PRT
_RQ1 = RQ1
_RQD = RQD


class ORN_O08_ORDER(HL7Model):
    """HL7 v2 ORN_O08.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[List[ORN_O08_TIMING]]): optional
        RQD (RQD): required
        RQ1 (Optional[RQ1]): optional
        NTE (Optional[List[NTE]]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING: Optional[List[_ORN_O08_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    RQD: _RQD = Field(
        title="RQD",
        description="Required",
    )

    RQ1: Optional[_RQ1] = Field(
        default=None,
        title="RQ1",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
