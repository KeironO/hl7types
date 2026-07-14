"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OML_O33.OBSERVATION_REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DG1 import DG1
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.PRT import PRT
from ..segments.SGH import SGH
from ..segments.SGT import SGT
from ..segments.TCD import TCD

from .OML_O33_OBSERVATION import OML_O33_OBSERVATION
from .OML_O33_PRIOR_RESULT import OML_O33_PRIOR_RESULT

_DG1 = DG1
_NTE = NTE
_OBR = OBR
_OML_O33_OBSERVATION = OML_O33_OBSERVATION
_OML_O33_PRIOR_RESULT = OML_O33_PRIOR_RESULT
_PRT = PRT
_SGH = SGH
_SGT = SGT
_TCD = TCD


class OML_O33_OBSERVATION_REQUEST(HL7Model):
    """HL7 v2 OML_O33.OBSERVATION_REQUEST group.

    Attributes:
        OBR (OBR): Observation Request, required
        TCD (Optional[TCD]): Test Code Detail, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        OBSERVATION (Optional[List[OML_O33_OBSERVATION]]): optional
        SGH (Optional[SGH]): Segment Group Header, optional
        PRIOR_RESULT (Optional[List[OML_O33_PRIOR_RESULT]]): optional
        SGT (Optional[SGT]): Segment Group Trailer, optional
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

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Diagnosis",
    )

    OBSERVATION: Optional[List[_OML_O33_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    SGH: Optional[_SGH] = Field(
        default=None,
        title="SGH",
        description="Segment Group Header",
    )

    PRIOR_RESULT: Optional[List[_OML_O33_PRIOR_RESULT]] = Field(
        default=None,
        title="PRIOR_RESULT",
    )

    SGT: Optional[_SGT] = Field(
        default=None,
        title="SGT",
        description="Segment Group Trailer",
    )

    model_config = {"populate_by_name": True}
