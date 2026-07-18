"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OPL_O37
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PRT import PRT
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.OPL_O37_GUARANTOR import OPL_O37_GUARANTOR
from ..groups.OPL_O37_ORDER import OPL_O37_ORDER

_MSH = MSH
_NTE = NTE
_OPL_O37_GUARANTOR = OPL_O37_GUARANTOR
_OPL_O37_ORDER = OPL_O37_ORDER
_PRT = PRT
_SFT = SFT
_UAC = UAC


class OPL_O37(HL7Model):
    """OPL - Population/Location-Based Laboratory Order Message (S4.4.16).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PRT (List[PRT]): Participation Information, required
        GUARANTOR (Optional[OPL_O37_GUARANTOR]): optional
        ORDER (List[OPL_O37_ORDER]): required
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

    PRT: List[_PRT] = Field(
        min_length=1,
        title="PRT",
        description="Participation Information",
    )

    GUARANTOR: Optional[_OPL_O37_GUARANTOR] = Field(
        default=None,
        title="GUARANTOR",
    )

    ORDER: List[_OPL_O37_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
