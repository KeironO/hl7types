"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OML_O39.OBSERVATION_REQUEST
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTD import CTD
from ..segments.DG1 import DG1
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.PRT import PRT
from ..segments.TCD import TCD
from .OML_O39_OBSERVATION import OML_O39_OBSERVATION
from .OML_O39_SPECIMEN_SHIPMENT import OML_O39_SPECIMEN_SHIPMENT

_CTD = CTD
_DG1 = DG1
_NTE = NTE
_OBR = OBR
_OML_O39_OBSERVATION = OML_O39_OBSERVATION
_OML_O39_SPECIMEN_SHIPMENT = OML_O39_SPECIMEN_SHIPMENT
_PRT = PRT
_TCD = TCD


class OML_O39_OBSERVATION_REQUEST(BaseModel):
    """HL7 v2 OML_O39.OBSERVATION_REQUEST group.

    Attributes:
        OBR (OBR): required
        TCD (Optional[TCD]): optional
        NTE (Optional[List[NTE]]): optional
        PRT (Optional[List[PRT]]): optional
        CTD (Optional[CTD]): optional
        DG1 (Optional[List[DG1]]): optional
        OBSERVATION (Optional[List[OML_O39_OBSERVATION]]): optional
        SPECIMEN_SHIPMENT (Optional[List[OML_O39_SPECIMEN_SHIPMENT]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    TCD: _TCD | None = Field(
        default=None,
        title="TCD",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    CTD: _CTD | None = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    DG1: list[_DG1] | None = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    OBSERVATION: list[_OML_O39_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    SPECIMEN_SHIPMENT: list[_OML_O39_SPECIMEN_SHIPMENT] | None = Field(
        default=None,
        title="SPECIMEN_SHIPMENT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
