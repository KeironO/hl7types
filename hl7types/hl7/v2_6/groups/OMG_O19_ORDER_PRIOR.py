"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OMG_O19.ORDER_PRIOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTD import CTD
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.ROL import ROL

from .OMG_O19_OBSERVATION_PRIOR import OMG_O19_OBSERVATION_PRIOR
from .OMG_O19_TIMING_PRIOR import OMG_O19_TIMING_PRIOR

_CTD = CTD
_NTE = NTE
_OBR = OBR
_OMG_O19_OBSERVATION_PRIOR = OMG_O19_OBSERVATION_PRIOR
_OMG_O19_TIMING_PRIOR = OMG_O19_TIMING_PRIOR
_ORC = ORC
_ROL = ROL


class OMG_O19_ORDER_PRIOR(BaseModel):
    """HL7 v2 OMG_O19.ORDER_PRIOR group.

    Attributes:
        ORC (Optional[ORC]): optional
        OBR (OBR): required
        TIMING_PRIOR (Optional[List[OMG_O19_TIMING_PRIOR]]): optional
        NTE (Optional[List[NTE]]): optional
        ROL (Optional[List[ROL]]): optional
        CTD (Optional[CTD]): optional
        OBSERVATION_PRIOR (List[OMG_O19_OBSERVATION_PRIOR]): required
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    TIMING_PRIOR: Optional[List[_OMG_O19_TIMING_PRIOR]] = Field(
        default=None,
        title="TIMING_PRIOR",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    OBSERVATION_PRIOR: List[_OMG_O19_OBSERVATION_PRIOR] = Field(
        default=...,
        title="OBSERVATION_PRIOR",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
