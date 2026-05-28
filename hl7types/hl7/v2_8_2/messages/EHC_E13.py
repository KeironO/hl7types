"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: EHC_E13
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.EHC_E13_REQUEST import EHC_E13_REQUEST
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


class EHC_E13(BaseModel):
    """HL7 v2 EHC_E13 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[List[UAC]]): optional
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        RFI (RFI): required
        CTD (Optional[List[CTD]]): optional
        IVC (IVC): required
        PSS (PSS): required
        PSG (PSG): required
        PID (Optional[PID]): optional
        PSL (Optional[PSL]): optional
        REQUEST (List[EHC_E13_REQUEST]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: list[_UAC] | None = Field(
        default=None,
        title="UAC",
        description="Optional, repeating",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    ERR: list[_ERR] | None = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
    )

    RFI: _RFI = Field(
        default=...,
        title="RFI",
        description="Required",
    )

    CTD: list[_CTD] | None = Field(
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

    PID: _PID | None = Field(
        default=None,
        title="PID",
        description="Optional",
    )

    PSL: _PSL | None = Field(
        default=None,
        title="PSL",
        description="Optional",
    )

    REQUEST: list[_EHC_E13_REQUEST] = Field(
        default=...,
        title="REQUEST",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
