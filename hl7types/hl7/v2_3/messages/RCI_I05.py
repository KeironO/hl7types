"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RCI_I05
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.QRD import QRD
from ..segments.QRF import QRF

from ..groups.RCI_I05_OBSERVATION import RCI_I05_OBSERVATION
from ..groups.RCI_I05_PROVIDER import RCI_I05_PROVIDER

_AL1 = AL1
_DG1 = DG1
_DRG = DRG
_MSA = MSA
_MSH = MSH
_NTE = NTE
_PID = PID
_QRD = QRD
_QRF = QRF
_RCI_I05_OBSERVATION = RCI_I05_OBSERVATION
_RCI_I05_PROVIDER = RCI_I05_PROVIDER


class RCI_I05(HL7Model):
    """RQC/RCI - Request for patient clinical information.

    Attributes:
        MSH (MSH): Message header segment, required
        MSA (MSA): Message acknowledgement segment, required
        QRD (QRD): Query definition segment, required
        QRF (Optional[QRF]): Query filter segment, optional
        PROVIDER (List[RCI_I05_PROVIDER]): required
        PID (PID): Patient Identification, required
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[List[DRG]]): Diagnosis Related Group, optional
        AL1 (Optional[List[AL1]]): Patient allergy information, optional
        OBSERVATION (Optional[List[RCI_I05_OBSERVATION]]): optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
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

    PROVIDER: List[_RCI_I05_PROVIDER] = Field(
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

    OBSERVATION: Optional[List[_RCI_I05_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    model_config = {"populate_by_name": True}
