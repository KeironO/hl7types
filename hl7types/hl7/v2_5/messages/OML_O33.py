"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OML_O33
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OML_O33_PATIENT import OML_O33_PATIENT
from ..groups.OML_O33_SPECIMEN import OML_O33_SPECIMEN
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

_MSH = MSH
_NTE = NTE
_OML_O33_PATIENT = OML_O33_PATIENT
_OML_O33_SPECIMEN = OML_O33_SPECIMEN
_SFT = SFT


class OML_O33(BaseModel):
    """HL7 v2 OML_O33 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OML_O33_PATIENT]): optional
        SPECIMEN (List[OML_O33_SPECIMEN]): required
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

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: _OML_O33_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    SPECIMEN: list[_OML_O33_SPECIMEN] = Field(
        default=...,
        title="SPECIMEN",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
