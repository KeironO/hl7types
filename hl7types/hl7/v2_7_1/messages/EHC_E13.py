"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E13
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTD import CTD
from ..segments.ERR import ERR
from ..segments.IVC import IVC
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PSG import PSG
from ..segments.PSL import PSL
from ..segments.PSS import PSS
from ..segments.RFI import RFI
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.EHC_E13_REQUEST import EHC_E13_REQUEST

_CTD = CTD
_EHC_E13_REQUEST = EHC_E13_REQUEST
_ERR = ERR
_IVC = IVC
_MSA = MSA
_MSH = MSH
_PID = PID
_PSG = PSG
_PSL = PSL
_PSS = PSS
_RFI = RFI
_SFT = SFT
_UAC = UAC


class EHC_E13(HL7Model):
    """Additional Information Response (S16.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[List[UAC]]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        RFI (RFI): Request for Information, required
        CTD (Optional[List[CTD]]): Contact Data, optional
        IVC (IVC): Invoice Segment, required
        PSS (PSS): Product/Service Section, required
        PSG (PSG): Product/Service Group, required
        PID (Optional[PID]): Patient Identification, optional
        PSL (Optional[PSL]): Product/Service Line Item, optional
        REQUEST (List[EHC_E13_REQUEST]): required
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

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Error",
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

    PSL: Optional[_PSL] = Field(
        default=None,
        title="PSL",
        description="Product/Service Line Item",
    )

    REQUEST: List[_EHC_E13_REQUEST] = Field(
        min_length=1,
        title="REQUEST",
    )

    model_config = {"populate_by_name": True}
