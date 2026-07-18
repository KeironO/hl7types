"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ORS_O02.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
        ORC (ORC): ORC - common order segment, required
        RQD (RQD): RQD - requisition detail segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="ORC - common order segment",
    )

    RQD: _RQD = Field(
        title="RQD",
        description="RQD - requisition detail segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    model_config = ConfigDict(populate_by_name=True)
