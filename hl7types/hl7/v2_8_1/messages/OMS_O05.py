"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OMS_O05
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OMS_O05_ORDER import OMS_O05_ORDER
from ..groups.OMS_O05_PATIENT import OMS_O05_PATIENT
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

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

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: _OMS_O05_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_OMS_O05_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
