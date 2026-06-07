"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
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
from ..segments.UAC import UAC

from ..groups.RDS_O13_ORDER import RDS_O13_ORDER
from ..groups.RDS_O13_PATIENT import RDS_O13_PATIENT

_MSH = MSH
_NTE = NTE
_RDS_O13_ORDER = RDS_O13_ORDER
_RDS_O13_PATIENT = RDS_O13_PATIENT
_SFT = SFT
_UAC = UAC


class RDS_O13(HL7Model):
    """HL7 v2 RDS_O13 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[RDS_O13_PATIENT]): optional
        ORDER (List[RDS_O13_ORDER]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: Optional[_RDS_O13_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_RDS_O13_ORDER] = Field(
        min_length=1,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
