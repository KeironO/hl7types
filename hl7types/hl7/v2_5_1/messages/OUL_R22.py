"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OUL_R22
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

from ..groups.OUL_R22_PATIENT import OUL_R22_PATIENT
from ..groups.OUL_R22_SPECIMEN import OUL_R22_SPECIMEN
from ..groups.OUL_R22_VISIT import OUL_R22_VISIT

_DSC = DSC
_MSH = MSH
_NTE = NTE
_OUL_R22_PATIENT = OUL_R22_PATIENT
_OUL_R22_SPECIMEN = OUL_R22_SPECIMEN
_OUL_R22_VISIT = OUL_R22_VISIT
_SFT = SFT


class OUL_R22(HL7Model):
    """OUL - Unsolicited Specimen Oriented Observation Message (S7.3.2).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        NTE (Optional[NTE]): Notes and Comments, optional
        PATIENT (Optional[OUL_R22_PATIENT]): optional
        VISIT (Optional[OUL_R22_VISIT]): optional
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

    NTE: Optional[_NTE] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PATIENT: Optional[_OUL_R22_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    VISIT: Optional[_OUL_R22_VISIT] = Field(
        default=None,
        title="VISIT",
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

    model_config = {"populate_by_name": True}
