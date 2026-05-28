"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MFN_M04.MF_CDM
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CDM import CDM
from ..segments.MFE import MFE
from ..segments.NTE import NTE
from ..segments.PRC import PRC

_CDM = CDM
_MFE = MFE
_NTE = NTE
_PRC = PRC


class MFN_M04_MF_CDM(BaseModel):
    """HL7 v2 MFN_M04.MF_CDM group.

    Attributes:
        MFE (MFE): required
        NTE (Optional[List[NTE]]): optional
        CDM (CDM): required
        PRC (Optional[List[PRC]]): optional
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    CDM: _CDM = Field(
        default=...,
        title="CDM",
        description="Required",
    )

    PRC: list[_PRC] | None = Field(
        default=None,
        title="PRC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
