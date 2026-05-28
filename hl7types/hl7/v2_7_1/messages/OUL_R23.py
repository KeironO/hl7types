"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OUL_R23
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OUL_R23_PATIENT import OUL_R23_PATIENT
from ..groups.OUL_R23_SPECIMEN import OUL_R23_SPECIMEN
from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_DSC = DSC
_MSH = MSH
_NK1 = NK1
_NTE = NTE
_OUL_R23_PATIENT = OUL_R23_PATIENT
_OUL_R23_SPECIMEN = OUL_R23_SPECIMEN
_SFT = SFT
_UAC = UAC


class OUL_R23(BaseModel):
    """HL7 v2 OUL_R23 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[NTE]): optional
        PATIENT (Optional[OUL_R23_PATIENT]): optional
        NK1 (Optional[List[NK1]]): optional
        SPECIMEN (List[OUL_R23_SPECIMEN]): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    NTE: _NTE | None = Field(
        default=None,
        title="NTE",
        description="Optional",
    )

    PATIENT: _OUL_R23_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    NK1: list[_NK1] | None = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    SPECIMEN: list[_OUL_R23_SPECIMEN] = Field(
        default=...,
        title="SPECIMEN",
        description="Required, repeating",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
