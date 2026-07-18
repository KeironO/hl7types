"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OUL_R24
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

from ..groups.OUL_R24_ORDER import OUL_R24_ORDER
from ..groups.OUL_R24_PATIENT import OUL_R24_PATIENT
from ..groups.OUL_R24_VISIT import OUL_R24_VISIT

_DSC = DSC
_MSH = MSH
_NTE = NTE
_OUL_R24_ORDER = OUL_R24_ORDER
_OUL_R24_PATIENT = OUL_R24_PATIENT
_OUL_R24_VISIT = OUL_R24_VISIT
_SFT = SFT


class OUL_R24(HL7Model):
    """OUL - Unsolicited Order Oriented Observation Message (S7.3.2).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        NTE (Optional[NTE]): Notes and Comments, optional
        PATIENT (Optional[OUL_R24_PATIENT]): optional
        VISIT (Optional[OUL_R24_VISIT]): optional
        ORDER (List[OUL_R24_ORDER]): required
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

    PATIENT: Optional[_OUL_R24_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    VISIT: Optional[_OUL_R24_VISIT] = Field(
        default=None,
        title="VISIT",
    )

    ORDER: List[_OUL_R24_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = ConfigDict(populate_by_name=True)
