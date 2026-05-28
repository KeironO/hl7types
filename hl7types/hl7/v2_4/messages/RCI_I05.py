"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RCI_I05
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RCI_I05_OBSERVATION import RCI_I05_OBSERVATION
from ..groups.RCI_I05_PROVIDER import RCI_I05_PROVIDER
from ..segments.AL1 import AL1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.QRD import QRD
from ..segments.QRF import QRF

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


class RCI_I05(BaseModel):
    """HL7 v2 RCI_I05 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        PROVIDER (List[RCI_I05_PROVIDER]): required
        PID (PID): required
        DG1 (Optional[List[DG1]]): optional
        DRG (Optional[List[DRG]]): optional
        AL1 (Optional[List[AL1]]): optional
        OBSERVATION (Optional[List[RCI_I05_OBSERVATION]]): optional
        NTE (Optional[List[NTE]]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
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

    PROVIDER: list[_RCI_I05_PROVIDER] = Field(
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

    OBSERVATION: list[_RCI_I05_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
