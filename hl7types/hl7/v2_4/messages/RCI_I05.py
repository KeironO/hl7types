"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RCI_I05
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
    """RQC/RCI - Request for patient clinical information (S11).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original Style Query Filter, optional
        PROVIDER (List[RCI_I05_PROVIDER]): required
        PID (PID): Patient identification, required
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[List[DRG]]): Diagnosis Related Group, optional
        AL1 (Optional[List[AL1]]): Patient allergy information, optional
        OBSERVATION (Optional[List[RCI_I05_OBSERVATION]]): optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="Original-Style Query Definition",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Original Style Query Filter",
    )

    PROVIDER: List[_RCI_I05_PROVIDER] = Field(
        min_length=1,
        title="PROVIDER",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient identification",
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
        description="Notes and Comments",
    )

    model_config = ConfigDict(populate_by_name=True)
