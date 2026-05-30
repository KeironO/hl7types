"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MFN_M04.MF_CDM
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CDM import CDM
from ..segments.MFE import MFE
from ..segments.PRC import PRC

_CDM = CDM
_MFE = MFE
_PRC = PRC


class MFN_M04_MF_CDM(HL7Model):
    """HL7 v2 MFN_M04.MF_CDM group.

    Attributes:
        MFE (MFE): required
        CDM (CDM): required
        PRC (Optional[List[PRC]]): optional
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    CDM: _CDM = Field(
        default=...,
        title="CDM",
        description="Required",
    )

    PRC: Optional[List[_PRC]] = Field(
        default=None,
        title="PRC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
