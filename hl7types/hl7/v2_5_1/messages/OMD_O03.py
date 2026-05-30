"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OMD_O03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

from ..groups.OMD_O03_ORDER_DIET import OMD_O03_ORDER_DIET
from ..groups.OMD_O03_ORDER_TRAY import OMD_O03_ORDER_TRAY
from ..groups.OMD_O03_PATIENT import OMD_O03_PATIENT

_MSH = MSH
_NTE = NTE
_OMD_O03_ORDER_DIET = OMD_O03_ORDER_DIET
_OMD_O03_ORDER_TRAY = OMD_O03_ORDER_TRAY
_OMD_O03_PATIENT = OMD_O03_PATIENT
_SFT = SFT


class OMD_O03(HL7Model):
    """HL7 v2 OMD_O03 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OMD_O03_PATIENT]): optional
        ORDER_DIET (List[OMD_O03_ORDER_DIET]): required
        ORDER_TRAY (Optional[List[OMD_O03_ORDER_TRAY]]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: Optional[_OMD_O03_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER_DIET: List[_OMD_O03_ORDER_DIET] = Field(
        default=...,
        title="ORDER_DIET",
        description="Required, repeating",
    )

    ORDER_TRAY: Optional[List[_OMD_O03_ORDER_TRAY]] = Field(
        default=None,
        title="ORDER_TRAY",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
