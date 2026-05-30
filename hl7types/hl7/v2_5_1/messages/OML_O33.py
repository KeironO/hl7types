"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OML_O33
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

from ..groups.OML_O33_PATIENT import OML_O33_PATIENT
from ..groups.OML_O33_SPECIMEN import OML_O33_SPECIMEN

_MSH = MSH
_NTE = NTE
_OML_O33_PATIENT = OML_O33_PATIENT
_OML_O33_SPECIMEN = OML_O33_SPECIMEN
_SFT = SFT


class OML_O33(HL7Model):
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

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: Optional[_OML_O33_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    SPECIMEN: List[_OML_O33_SPECIMEN] = Field(
        default=...,
        title="SPECIMEN",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
