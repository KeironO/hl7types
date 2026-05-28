"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RCL_I06
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RCL_I06_PROVIDER import RCL_I06_PROVIDER
from ..segments.AL1 import AL1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.DSC import DSC
from ..segments.DSP import DSP
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.QRD import QRD
from ..segments.QRF import QRF
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_AL1 = AL1
_DG1 = DG1
_DRG = DRG
_DSC = DSC
_DSP = DSP
_MSA = MSA
_MSH = MSH
_NTE = NTE
_PID = PID
_QRD = QRD
_QRF = QRF
_RCL_I06_PROVIDER = RCL_I06_PROVIDER
_SFT = SFT
_UAC = UAC


class RCL_I06(BaseModel):
    """HL7 v2 RCL_I06 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MSA (MSA): required
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        PROVIDER (List[RCL_I06_PROVIDER]): required
        PID (PID): required
        DG1 (Optional[List[DG1]]): optional
        DRG (Optional[List[DRG]]): optional
        AL1 (Optional[List[AL1]]): optional
        NTE (Optional[List[NTE]]): optional
        DSP (Optional[List[DSP]]): optional
        DSC (Optional[DSC]): optional
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

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    QRD: _QRD = Field(
        default=...,
        title="QRD",
        description="Required",
    )

    QRF: _QRF | None = Field(
        default=None,
        title="QRF",
        description="Optional",
    )

    PROVIDER: list[_RCL_I06_PROVIDER] = Field(
        default=...,
        title="PROVIDER",
        description="Required, repeating",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    DG1: list[_DG1] | None = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    DRG: list[_DRG] | None = Field(
        default=None,
        title="DRG",
        description="Optional, repeating",
    )

    AL1: list[_AL1] | None = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    DSP: list[_DSP] | None = Field(
        default=None,
        title="DSP",
        description="Optional, repeating",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
