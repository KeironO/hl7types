"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OUL_R22
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.OUL_R22_PATIENT import OUL_R22_PATIENT
from ..groups.OUL_R22_SPECIMEN import OUL_R22_SPECIMEN

_DSC = DSC
_MSH = MSH
_NK1 = NK1
_NTE = NTE
_OUL_R22_PATIENT = OUL_R22_PATIENT
_OUL_R22_SPECIMEN = OUL_R22_SPECIMEN
_SFT = SFT
_UAC = UAC


class OUL_R22(HL7Model):
    """OUL - Unsolicited Specimen Oriented Observation Message (S7.3.10).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[NTE]): Notes and Comments, optional
        PATIENT (Optional[OUL_R22_PATIENT]): optional
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        SPECIMEN (List[OUL_R22_SPECIMEN]): required
        DSC (Optional[DSC]): Continuation Pointer, optional
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

    NTE: Optional[_NTE] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PATIENT: Optional[_OUL_R22_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of Kin / Associated Parties",
    )

    SPECIMEN: List[_OUL_R22_SPECIMEN] = Field(
        min_length=1,
        title="SPECIMEN",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = ConfigDict(populate_by_name=True)
