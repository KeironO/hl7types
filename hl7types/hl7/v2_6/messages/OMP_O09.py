"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OMP_O09
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

from ..groups.OMP_O09_ORDER import OMP_O09_ORDER
from ..groups.OMP_O09_PATIENT import OMP_O09_PATIENT

_MSH = MSH
_NTE = NTE
_OMP_O09_ORDER = OMP_O09_ORDER
_OMP_O09_PATIENT = OMP_O09_PATIENT
_SFT = SFT
_UAC = UAC


class OMP_O09(HL7Model):
    """OMP - Pharmacy/treatment order (S4.13.3).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[OMP_O09_PATIENT]): optional
        ORDER (List[OMP_O09_ORDER]): required
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

    PATIENT: Optional[_OMP_O09_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_OMP_O09_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
