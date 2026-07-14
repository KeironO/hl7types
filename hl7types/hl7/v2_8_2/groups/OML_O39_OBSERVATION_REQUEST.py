"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OML_O39.OBSERVATION_REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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


class OML_O39_OBSERVATION_REQUEST(HL7Model):
    """HL7 v2 OML_O39.OBSERVATION_REQUEST group.

    Attributes:
        OBR (OBR): Observation Request, required
        TCD (Optional[TCD]): Test Code Detail, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        CTD (Optional[CTD]): Contact Data, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        OBSERVATION (Optional[List[OML_O39_OBSERVATION]]): optional
        SPECIMEN_SHIPMENT (Optional[List[OML_O39_SPECIMEN_SHIPMENT]]): optional
    """

    OBR: _OBR = Field(
        title="OBR",
        description="Observation Request",
    )

    TCD: Optional[_TCD] = Field(
        default=None,
        title="TCD",
        description="Test Code Detail",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Contact Data",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Diagnosis",
    )

    OBSERVATION: Optional[List[_OML_O39_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    SPECIMEN_SHIPMENT: Optional[List[_OML_O39_SPECIMEN_SHIPMENT]] = Field(
        default=None,
        title="SPECIMEN_SHIPMENT",
    )

    model_config = {"populate_by_name": True}
