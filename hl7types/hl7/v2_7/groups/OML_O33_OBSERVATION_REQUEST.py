"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
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
from ..segments.TCD import TCD

from .OML_O33_OBSERVATION import OML_O33_OBSERVATION
from .OML_O33_PRIOR_RESULT import OML_O33_PRIOR_RESULT

_DG1 = DG1
_NTE = NTE
_OBR = OBR
_OML_O33_OBSERVATION = OML_O33_OBSERVATION
_OML_O33_PRIOR_RESULT = OML_O33_PRIOR_RESULT
_PRT = PRT
_TCD = TCD


class OML_O33_OBSERVATION_REQUEST(HL7Model):
    """HL7 v2 OML_O33.OBSERVATION_REQUEST group.

    Attributes:
        OBR (OBR): required
        TCD (Optional[TCD]): optional
        NTE (Optional[List[NTE]]): optional
        PRT (Optional[List[PRT]]): optional
        DG1 (Optional[List[DG1]]): optional
        OBSERVATION (Optional[List[OML_O33_OBSERVATION]]): optional
        PRIOR_RESULT (Optional[List[OML_O33_PRIOR_RESULT]]): optional
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

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    OBSERVATION: Optional[List[_OML_O33_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    PRIOR_RESULT: Optional[List[_OML_O33_PRIOR_RESULT]] = Field(
        default=None,
        title="PRIOR_RESULT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
