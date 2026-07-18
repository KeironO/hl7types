"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: EHC_E12
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
    """Request Additional Information (S16.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[List[UAC]]): User Authentication Credential Segment, optional
        RFI (RFI): Request for Information, required
        CTD (Optional[List[CTD]]): Contact Data, optional
        IVC (IVC): Invoice Segment, required
        PSS (PSS): Product/Service Section, required
        PSG (PSG): Product/Service Group, required
        PID (Optional[PID]): Patient Identification, optional
        PSL (Optional[List[PSL]]): Product/Service Line Item, optional
        REQUEST (List[EHC_E12_REQUEST]): required
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

    UAC: Optional[List[_UAC]] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    RFI: _RFI = Field(
        title="RFI",
        description="Request for Information",
    )

    CTD: Optional[List[_CTD]] = Field(
        default=None,
        title="CTD",
        description="Contact Data",
    )

    IVC: _IVC = Field(
        title="IVC",
        description="Invoice Segment",
    )

    PSS: _PSS = Field(
        title="PSS",
        description="Product/Service Section",
    )

    PSG: _PSG = Field(
        title="PSG",
        description="Product/Service Group",
    )

    PID: Optional[_PID] = Field(
        default=None,
        title="PID",
        description="Patient Identification",
    )

    PSL: Optional[List[_PSL]] = Field(
        default=None,
        title="PSL",
        description="Product/Service Line Item",
    )

    REQUEST: List[_EHC_E12_REQUEST] = Field(
        min_length=1,
        title="REQUEST",
    )

    model_config = ConfigDict(populate_by_name=True)
