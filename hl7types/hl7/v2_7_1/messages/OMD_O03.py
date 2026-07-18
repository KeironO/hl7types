"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OMD_O03
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

from ..groups.OMD_O03_ORDER_DIET import OMD_O03_ORDER_DIET
from ..groups.OMD_O03_ORDER_TRAY import OMD_O03_ORDER_TRAY
from ..groups.OMD_O03_PATIENT import OMD_O03_PATIENT

_MSH = MSH
_NTE = NTE
_OMD_O03_ORDER_DIET = OMD_O03_ORDER_DIET
_OMD_O03_ORDER_TRAY = OMD_O03_ORDER_TRAY
_OMD_O03_PATIENT = OMD_O03_PATIENT
_SFT = SFT
_UAC = UAC


class OMD_O03(HL7Model):
    """OMD - Diet order (S4.6.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[OMD_O03_PATIENT]): optional
        ORDER_DIET (List[OMD_O03_ORDER_DIET]): required
        ORDER_TRAY (Optional[List[OMD_O03_ORDER_TRAY]]): optional
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

    PATIENT: Optional[_OMD_O03_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER_DIET: List[_OMD_O03_ORDER_DIET] = Field(
        min_length=1,
        title="ORDER_DIET",
    )

    ORDER_TRAY: Optional[List[_OMD_O03_ORDER_TRAY]] = Field(
        default=None,
        title="ORDER_TRAY",
    )

    model_config = ConfigDict(populate_by_name=True)
