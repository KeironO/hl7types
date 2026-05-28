"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORN_O08.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.RQ1 import RQ1
from ..segments.RQD import RQD

_NTE = NTE
_ORC = ORC
_RQ1 = RQ1
_RQD = RQD


class ORN_O08_ORDER(BaseModel):
    """HL7 v2 ORN_O08.ORDER group.

    Attributes:
        ORC (ORC): required
        RQD (RQD): required
        RQ1 (Optional[RQ1]): optional
        NTE (Optional[List[NTE]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    RQD: _RQD = Field(
        default=...,
        title="RQD",
        description="Required",
    )

    RQ1: _RQ1 | None = Field(
        default=None,
        title="RQ1",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
