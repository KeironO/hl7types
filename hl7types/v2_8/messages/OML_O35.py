"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OML_O35
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.OML_O35_PATIENT import OML_O35_PATIENT
from ..groups.OML_O35_SPECIMEN import OML_O35_SPECIMEN

_MSH = MSH
_NTE = NTE
_OML_O35_PATIENT = OML_O35_PATIENT
_OML_O35_SPECIMEN = OML_O35_SPECIMEN
_SFT = SFT
_UAC = UAC


class OML_O35(BaseModel):
    """HL7 v2 OML_O35 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OML_O35_PATIENT]): optional
        SPECIMEN (List[OML_O35_SPECIMEN]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: Optional[_OML_O35_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    SPECIMEN: List[_OML_O35_SPECIMEN] = Field(
        default=...,
        title="SPECIMEN",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
