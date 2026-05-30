"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: EHC_E12
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTD import CTD
from ..segments.IVC import IVC
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PSG import PSG
from ..segments.PSL import PSL
from ..segments.PSS import PSS
from ..segments.RFI import RFI
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.EHC_E12_REQUEST import EHC_E12_REQUEST

_CTD = CTD
_EHC_E12_REQUEST = EHC_E12_REQUEST
_IVC = IVC
_MSH = MSH
_PID = PID
_PSG = PSG
_PSL = PSL
_PSS = PSS
_RFI = RFI
_SFT = SFT
_UAC = UAC


class EHC_E12(HL7Model):
    """HL7 v2 EHC_E12 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[List[UAC]]): optional
        RFI (RFI): required
        CTD (Optional[List[CTD]]): optional
        IVC (IVC): required
        PSS (PSS): required
        PSG (PSG): required
        PID (Optional[PID]): optional
        PSL (Optional[List[PSL]]): optional
        REQUEST (List[EHC_E12_REQUEST]): required
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

    UAC: Optional[List[_UAC]] = Field(
        default=None,
        title="UAC",
        description="Optional, repeating",
    )

    RFI: _RFI = Field(
        default=...,
        title="RFI",
        description="Required",
    )

    CTD: Optional[List[_CTD]] = Field(
        default=None,
        title="CTD",
        description="Optional, repeating",
    )

    IVC: _IVC = Field(
        default=...,
        title="IVC",
        description="Required",
    )

    PSS: _PSS = Field(
        default=...,
        title="PSS",
        description="Required",
    )

    PSG: _PSG = Field(
        default=...,
        title="PSG",
        description="Required",
    )

    PID: Optional[_PID] = Field(
        default=None,
        title="PID",
        description="Optional",
    )

    PSL: Optional[List[_PSL]] = Field(
        default=None,
        title="PSL",
        description="Optional, repeating",
    )

    REQUEST: List[_EHC_E12_REQUEST] = Field(
        default=...,
        title="REQUEST",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
