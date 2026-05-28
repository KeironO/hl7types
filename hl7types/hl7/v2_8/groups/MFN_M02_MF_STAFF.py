"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: MFN_M02.MF_STAFF
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AFF import AFF
from ..segments.CER import CER
from ..segments.EDU import EDU
from ..segments.LAN import LAN
from ..segments.MFE import MFE
from ..segments.NTE import NTE
from ..segments.ORG import ORG
from ..segments.PRA import PRA
from ..segments.STF import STF

_AFF = AFF
_CER = CER
_EDU = EDU
_LAN = LAN
_MFE = MFE
_NTE = NTE
_ORG = ORG
_PRA = PRA
_STF = STF


class MFN_M02_MF_STAFF(BaseModel):
    """HL7 v2 MFN_M02.MF_STAFF group.

    Attributes:
        MFE (MFE): required
        STF (STF): required
        PRA (Optional[List[PRA]]): optional
        ORG (Optional[List[ORG]]): optional
        AFF (Optional[List[AFF]]): optional
        LAN (Optional[List[LAN]]): optional
        EDU (Optional[List[EDU]]): optional
        CER (Optional[List[CER]]): optional
        NTE (Optional[List[NTE]]): optional
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    STF: _STF = Field(
        default=...,
        title="STF",
        description="Required",
    )

    PRA: list[_PRA] | None = Field(
        default=None,
        title="PRA",
        description="Optional, repeating",
    )

    ORG: list[_ORG] | None = Field(
        default=None,
        title="ORG",
        description="Optional, repeating",
    )

    AFF: list[_AFF] | None = Field(
        default=None,
        title="AFF",
        description="Optional, repeating",
    )

    LAN: list[_LAN] | None = Field(
        default=None,
        title="LAN",
        description="Optional, repeating",
    )

    EDU: list[_EDU] | None = Field(
        default=None,
        title="EDU",
        description="Optional, repeating",
    )

    CER: list[_CER] | None = Field(
        default=None,
        title="CER",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
