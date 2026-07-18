"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OML_O33
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
    """OML - Laboratory order for multiple orders related to a single specimen (S4.4.6).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[OML_O33_PATIENT]): optional
        SPECIMEN (List[OML_O33_SPECIMEN]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PATIENT: Optional[_OML_O33_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    SPECIMEN: List[_OML_O33_SPECIMEN] = Field(
        min_length=1,
        title="SPECIMEN",
    )

    model_config = ConfigDict(populate_by_name=True)
