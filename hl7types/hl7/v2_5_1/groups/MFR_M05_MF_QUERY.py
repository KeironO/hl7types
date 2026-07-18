"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFR_M05.MF_QUERY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.LCC import LCC
from ..segments.LCH import LCH
from ..segments.LDP import LDP
from ..segments.LOC import LOC
from ..segments.LRL import LRL
from ..segments.MFE import MFE

_LCC = LCC
_LCH = LCH
_LDP = LDP
_LOC = LOC
_LRL = LRL
_MFE = MFE


class MFR_M05_MF_QUERY(HL7Model):
    """HL7 v2 MFR_M05.MF_QUERY group.

    Attributes:
        MFE (MFE): Master File Entry, required
        LOC (LOC): Location Identification, required
        LCH (Optional[List[LCH]]): Location Characteristic, optional
        LRL (Optional[List[LRL]]): Location Relationship, optional
        LDP (List[LDP]): Location Department, required
        LCC (Optional[List[LCC]]): Location Charge Code, optional
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

    LDP: List[_LDP] = Field(
        min_length=1,
        title="LDP",
        description="Location Department",
    )

    LCC: Optional[List[_LCC]] = Field(
        default=None,
        title="LCC",
        description="Location Charge Code",
    )

    model_config = ConfigDict(populate_by_name=True)
