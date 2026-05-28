"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RSP_K25.STAFF
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AFF import AFF
from ..segments.CER import CER
from ..segments.EDU import EDU
from ..segments.LAN import LAN
from ..segments.NK1 import NK1
from ..segments.ORG import ORG
from ..segments.PRA import PRA
from ..segments.PRT import PRT
from ..segments.ROL import ROL
from ..segments.STF import STF

_AFF = AFF
_CER = CER
_EDU = EDU
_LAN = LAN
_NK1 = NK1
_ORG = ORG
_PRA = PRA
_PRT = PRT
_ROL = ROL
_STF = STF


class RSP_K25_STAFF(BaseModel):
    """HL7 v2 RSP_K25.STAFF group.

    Attributes:
        STF (STF): required
        PRA (Optional[List[PRA]]): optional
        ORG (Optional[List[ORG]]): optional
        AFF (Optional[List[AFF]]): optional
        LAN (Optional[List[LAN]]): optional
        EDU (Optional[List[EDU]]): optional
        CER (Optional[List[CER]]): optional
        NK1 (Optional[List[NK1]]): optional
        PRT (Optional[List[PRT]]): optional
        ROL (Optional[List[ROL]]): optional
    """

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

    NK1: list[_NK1] | None = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ROL: list[_ROL] | None = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
