"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RSP_Q11.QUERY_RESULT_CLUSTER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.LCH import LCH
from ..segments.LOC import LOC
from ..segments.LRL import LRL
from ..segments.MFE import MFE

from .RSP_Q11_MF_LOC_DEPT import RSP_Q11_MF_LOC_DEPT

_LCH = LCH
_LOC = LOC
_LRL = LRL
_MFE = MFE
_RSP_Q11_MF_LOC_DEPT = RSP_Q11_MF_LOC_DEPT


class RSP_Q11_QUERY_RESULT_CLUSTER(HL7Model):
    """HL7 v2 RSP_Q11.QUERY_RESULT_CLUSTER group.

    Attributes:
        MFE (MFE): required
        LOC (LOC): required
        LCH (Optional[List[LCH]]): optional
        LRL (Optional[List[LRL]]): optional
        MF_LOC_DEPT (List[RSP_Q11_MF_LOC_DEPT]): required
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    LOC: _LOC = Field(
        default=...,
        title="LOC",
        description="Required",
    )

    LCH: Optional[List[_LCH]] = Field(
        default=None,
        title="LCH",
        description="Optional, repeating",
    )

    LRL: Optional[List[_LRL]] = Field(
        default=None,
        title="LRL",
        description="Optional, repeating",
    )

    MF_LOC_DEPT: List[_RSP_Q11_MF_LOC_DEPT] = Field(
        default=...,
        title="MF_LOC_DEPT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
