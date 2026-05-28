"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OMI_O23
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OMI_O23_ORDER import OMI_O23_ORDER
from ..groups.OMI_O23_PATIENT import OMI_O23_PATIENT
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSH = MSH
_NTE = NTE
_OMI_O23_ORDER = OMI_O23_ORDER
_OMI_O23_PATIENT = OMI_O23_PATIENT
_SFT = SFT
_UAC = UAC


class OMI_O23(BaseModel):
    """HL7 v2 OMI_O23 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OMI_O23_PATIENT]): optional
        ORDER (List[OMI_O23_ORDER]): required
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

    PATIENT: _OMI_O23_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_OMI_O23_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
