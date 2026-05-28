"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OMS_O05
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.OMS_O05_ORDER import OMS_O05_ORDER
from ..groups.OMS_O05_PATIENT import OMS_O05_PATIENT

_MSH = MSH
_NTE = NTE
_OMS_O05_ORDER = OMS_O05_ORDER
_OMS_O05_PATIENT = OMS_O05_PATIENT
_SFT = SFT
_UAC = UAC


class OMS_O05(BaseModel):
    """HL7 v2 OMS_O05 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OMS_O05_PATIENT]): optional
        ORDER (List[OMS_O05_ORDER]): required
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

    PATIENT: Optional[_OMS_O05_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_OMS_O05_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
