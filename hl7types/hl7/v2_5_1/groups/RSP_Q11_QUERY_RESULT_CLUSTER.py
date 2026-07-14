"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
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
        MFE (MFE): Master File Entry, required
        LOC (LOC): Location Identification, required
        LCH (Optional[List[LCH]]): Location Characteristic, optional
        LRL (Optional[List[LRL]]): Location Relationship, optional
        MF_LOC_DEPT (List[RSP_Q11_MF_LOC_DEPT]): required
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Master File Entry",
    )

    LOC: _LOC = Field(
        title="LOC",
        description="Location Identification",
    )

    LCH: Optional[List[_LCH]] = Field(
        default=None,
        title="LCH",
        description="Location Characteristic",
    )

    LRL: Optional[List[_LRL]] = Field(
        default=None,
        title="LRL",
        description="Location Relationship",
    )

    MF_LOC_DEPT: List[_RSP_Q11_MF_LOC_DEPT] = Field(
        min_length=1,
        title="MF_LOC_DEPT",
    )

    model_config = {"populate_by_name": True}
