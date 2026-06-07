"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ORS_O06.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.RQ1 import RQ1
from ..segments.RQD import RQD

from .ORS_O06_TIMING import ORS_O06_TIMING

_NTE = NTE
_ORC = ORC
_ORS_O06_TIMING = ORS_O06_TIMING
_RQ1 = RQ1
_RQD = RQD


class ORS_O06_ORDER(HL7Model):
    """HL7 v2 ORS_O06.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[ORS_O06_TIMING]]): optional
        RQD (RQD): required
        RQ1 (Optional[RQ1]): optional
        NTE (Optional[List[NTE]]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    TIMING: Optional[List[_ORS_O06_TIMING]] = Field(
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
