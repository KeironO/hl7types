"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORN_O08.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.RQ1 import RQ1
from ..segments.RQD import RQD

_NTE = NTE
_ORC = ORC
_RQ1 = RQ1
_RQD = RQD


class ORN_O08_ORDER(HL7Model):
    """HL7 v2 ORN_O08.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        RQD (RQD): Requisition Detail, required
        RQ1 (Optional[RQ1]): Requisition Detail-1, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    RQD: _RQD = Field(
        title="RQD",
        description="Requisition Detail",
    )

    RQ1: Optional[_RQ1] = Field(
        default=None,
        title="RQ1",
        description="Requisition Detail-1",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = ConfigDict(populate_by_name=True)
