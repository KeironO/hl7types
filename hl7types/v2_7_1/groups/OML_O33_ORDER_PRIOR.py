"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OML_O33.ORDER_PRIOR
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .OML_O33_OBSERVATION_PRIOR import OML_O33_OBSERVATION_PRIOR
from .OML_O33_TIMING_PRIOR import OML_O33_TIMING_PRIOR

_NTE = NTE
_OBR = OBR
_OML_O33_OBSERVATION_PRIOR = OML_O33_OBSERVATION_PRIOR
_OML_O33_TIMING_PRIOR = OML_O33_TIMING_PRIOR
_ORC = ORC
_PRT = PRT


class OML_O33_ORDER_PRIOR(BaseModel):
    """HL7 v2 OML_O33.ORDER_PRIOR group.

    Attributes:
        ORC (ORC): required
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        PRT (Optional[List[PRT]]): optional
        TIMING_PRIOR (Optional[List[OML_O33_TIMING_PRIOR]]): optional
        OBSERVATION_PRIOR (List[OML_O33_OBSERVATION_PRIOR]): required
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
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

    TIMING_PRIOR: Optional[List[_OML_O33_TIMING_PRIOR]] = Field(
        default=None,
        title="TIMING_PRIOR",
        description="Optional, repeating",
    )

    OBSERVATION_PRIOR: List[_OML_O33_OBSERVATION_PRIOR] = Field(
        default=...,
        title="OBSERVATION_PRIOR",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
