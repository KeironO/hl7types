"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OML_O21.OBSERVATION_REQUEST
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTD import CTD
from ..segments.DG1 import DG1
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.PRT import PRT
from ..segments.SGH import SGH
from ..segments.SGT import SGT
from ..segments.TCD import TCD

from .OML_O21_OBSERVATION import OML_O21_OBSERVATION
from .OML_O21_PRIOR_RESULT import OML_O21_PRIOR_RESULT
from .OML_O21_SPECIMEN import OML_O21_SPECIMEN

_CTD = CTD
_DG1 = DG1
_NTE = NTE
_OBR = OBR
_OML_O21_OBSERVATION = OML_O21_OBSERVATION
_OML_O21_PRIOR_RESULT = OML_O21_PRIOR_RESULT
_OML_O21_SPECIMEN = OML_O21_SPECIMEN
_PRT = PRT
_SGH = SGH
_SGT = SGT
_TCD = TCD


class OML_O21_OBSERVATION_REQUEST(BaseModel):
    """HL7 v2 OML_O21.OBSERVATION_REQUEST group.

    Attributes:
        OBR (OBR): required
        TCD (Optional[TCD]): optional
        NTE (Optional[List[NTE]]): optional
        PRT (Optional[List[PRT]]): optional
        CTD (Optional[CTD]): optional
        DG1 (Optional[List[DG1]]): optional
        OBSERVATION (Optional[List[OML_O21_OBSERVATION]]): optional
        SPECIMEN (Optional[List[OML_O21_SPECIMEN]]): optional
        SGH (Optional[SGH]): optional
        PRIOR_RESULT (Optional[List[OML_O21_PRIOR_RESULT]]): optional
        SGT (Optional[SGT]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    TCD: Optional[_TCD] = Field(
        default=None,
        title="TCD",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    OBSERVATION: Optional[List[_OML_O21_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    SPECIMEN: Optional[List[_OML_O21_SPECIMEN]] = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    SGH: Optional[_SGH] = Field(
        default=None,
        title="SGH",
        description="Optional",
    )

    PRIOR_RESULT: Optional[List[_OML_O21_PRIOR_RESULT]] = Field(
        default=None,
        title="PRIOR_RESULT",
        description="Optional, repeating",
    )

    SGT: Optional[_SGT] = Field(
        default=None,
        title="SGT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
