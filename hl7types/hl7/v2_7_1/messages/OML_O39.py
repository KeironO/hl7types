"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OML_O39
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OML_O39_ORDER import OML_O39_ORDER
from ..groups.OML_O39_PATIENT import OML_O39_PATIENT
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSH = MSH
_NTE = NTE
_OML_O39_ORDER = OML_O39_ORDER
_OML_O39_PATIENT = OML_O39_PATIENT
_SFT = SFT
_UAC = UAC


class OML_O39(BaseModel):
    """HL7 v2 OML_O39 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OML_O39_PATIENT]): optional
        ORDER (List[OML_O39_ORDER]): required
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

    PATIENT: _OML_O39_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_OML_O39_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
