"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORN_O02.ORDER
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

_NTE = NTE
_ORC = ORC
_RQ1 = RQ1
_RQD = RQD


class ORN_O02_ORDER(HL7Model):
    """HL7 v2 ORN_O02.ORDER group.

    Attributes:
        ORC (ORC): Common order segment, required
        RQD (RQD): Requisition detail, required
        RQ1 (Optional[RQ1]): Requisition detail-1 segment, optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common order segment",
    )

    RQD: _RQD = Field(
        title="RQD",
        description="Requisition detail",
    )

    RQ1: Optional[_RQ1] = Field(
        default=None,
        title="RQ1",
        description="Requisition detail-1 segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    model_config = {"populate_by_name": True}
