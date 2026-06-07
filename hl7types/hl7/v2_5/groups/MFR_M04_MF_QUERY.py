"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MFR_M04.MF_QUERY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CDM import CDM
from ..segments.LCH import LCH
from ..segments.MFE import MFE
from ..segments.PRC import PRC

_CDM = CDM
_LCH = LCH
_MFE = MFE
_PRC = PRC


class MFR_M04_MF_QUERY(HL7Model):
    """HL7 v2 MFR_M04.MF_QUERY group.

    Attributes:
        MFE (MFE): required
        CDM (CDM): required
        LCH (Optional[List[LCH]]): optional
        PRC (Optional[List[PRC]]): optional
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Required",
    )

    CDM: _CDM = Field(
        title="CDM",
        description="Required",
    )

    LCH: Optional[List[_LCH]] = Field(
        default=None,
        title="LCH",
        description="Optional, repeating",
    )

    PRC: Optional[List[_PRC]] = Field(
        default=None,
        title="PRC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
