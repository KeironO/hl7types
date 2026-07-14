"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RDS_O13
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

from ..groups.RDS_O13_ORDER import RDS_O13_ORDER
from ..groups.RDS_O13_PATIENT import RDS_O13_PATIENT

_MSH = MSH
_NTE = NTE
_RDS_O13_ORDER = RDS_O13_ORDER
_RDS_O13_PATIENT = RDS_O13_PATIENT
_SFT = SFT


class RDS_O13(HL7Model):
    """RDS - Pharmacy/treatment dispense (S4.13.7).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[RDS_O13_PATIENT]): optional
        ORDER (List[RDS_O13_ORDER]): required
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

    PATIENT: Optional[_RDS_O13_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_RDS_O13_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = {"populate_by_name": True}
