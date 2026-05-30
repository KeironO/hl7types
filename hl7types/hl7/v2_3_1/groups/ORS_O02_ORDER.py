"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ORS_O02.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.RQD import RQD

_NTE = NTE
_ORC = ORC
_RQD = RQD


class ORS_O02_ORDER(HL7Model):
    """HL7 v2 ORS_O02.ORDER group.

    Attributes:
        ORC (ORC): required
        RQD (RQD): required
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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
