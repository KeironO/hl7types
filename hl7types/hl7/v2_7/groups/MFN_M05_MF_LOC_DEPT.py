"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: MFN_M05.MF_LOC_DEPT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.LCC import LCC
from ..segments.LCH import LCH
from ..segments.LDP import LDP

_LCC = LCC
_LCH = LCH
_LDP = LDP


class MFN_M05_MF_LOC_DEPT(HL7Model):
    """HL7 v2 MFN_M05.MF_LOC_DEPT group.

    Attributes:
        LDP (LDP): Location Department, required
        LCH (Optional[List[LCH]]): Location Characteristic, optional
        LCC (Optional[List[LCC]]): Location Charge Code, optional
    """

    LDP: _LDP = Field(
        title="LDP",
        description="Location Department",
    )

    LCH: Optional[List[_LCH]] = Field(
        default=None,
        title="LCH",
        description="Location Characteristic",
    )

    LCC: Optional[List[_LCC]] = Field(
        default=None,
        title="LCC",
        description="Location Charge Code",
    )

    model_config = ConfigDict(populate_by_name=True)
