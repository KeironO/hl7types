"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OML_O39
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.OML_O39_ORDER import OML_O39_ORDER
from ..groups.OML_O39_PATIENT import OML_O39_PATIENT

_MSH = MSH
_NTE = NTE
_OML_O39_ORDER = OML_O39_ORDER
_OML_O39_PATIENT = OML_O39_PATIENT
_SFT = SFT
_UAC = UAC


class OML_O39(HL7Model):
    """Specimen shipment centric laboratory order (S4.4.10).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[OML_O39_PATIENT]): optional
        ORDER (List[OML_O39_ORDER]): required
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

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PATIENT: Optional[_OML_O39_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_OML_O39_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
