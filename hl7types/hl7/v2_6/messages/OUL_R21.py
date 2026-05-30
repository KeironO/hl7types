"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OUL_R21
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

from ..groups.OUL_R21_ORDER_OBSERVATION import OUL_R21_ORDER_OBSERVATION
from ..groups.OUL_R21_PATIENT import OUL_R21_PATIENT

_DSC = DSC
_MSH = MSH
_NTE = NTE
_OUL_R21_ORDER_OBSERVATION = OUL_R21_ORDER_OBSERVATION
_OUL_R21_PATIENT = OUL_R21_PATIENT
_SFT = SFT


class OUL_R21(HL7Model):
    """HL7 v2 OUL_R21 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        NTE (Optional[NTE]): optional
        PATIENT (Optional[OUL_R21_PATIENT]): optional
        ORDER_OBSERVATION (List[OUL_R21_ORDER_OBSERVATION]): required
        DSC (Optional[DSC]): optional
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

    NTE: Optional[_NTE] = Field(
        default=None,
        title="NTE",
        description="Optional",
    )

    PATIENT: Optional[_OUL_R21_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER_OBSERVATION: List[_OUL_R21_ORDER_OBSERVATION] = Field(
        default=...,
        title="ORDER_OBSERVATION",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
