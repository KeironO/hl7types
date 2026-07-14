"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RCL_I06
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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

from ..groups.RCL_I06_PROVIDER import RCL_I06_PROVIDER

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


class RCL_I06(HL7Model):
    """RQC/RCL - Request/receipt of clinical data listing.

    Attributes:
        MSH (MSH): Message header segment, required
        MSA (MSA): Message acknowledgement segment, required
        QRD (QRD): Query definition segment, required
        QRF (Optional[QRF]): Query filter segment, optional
        PROVIDER (List[RCL_I06_PROVIDER]): required
        PID (PID): Patient Identification, required
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[List[DRG]]): Diagnosis Related Group, optional
        AL1 (Optional[List[AL1]]): Patient allergy information, optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        DSP (Optional[List[DSP]]): Display data segment, optional
        DSC (Optional[DSC]): Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message acknowledgement segment",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="Query definition segment",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Query filter segment",
    )

    PROVIDER: List[_RCL_I06_PROVIDER] = Field(
        min_length=1,
        title="PROVIDER",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Diagnosis",
    )

    DRG: Optional[List[_DRG]] = Field(
        default=None,
        title="DRG",
        description="Diagnosis Related Group",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Patient allergy information",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    DSP: Optional[List[_DSP]] = Field(
        default=None,
        title="DSP",
        description="Display data segment",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation pointer segment",
    )

    model_config = {"populate_by_name": True}
