"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OMQ_O57.ORDER_PRIOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTD import CTD
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .OMQ_O57_OBSERVATION_PRIOR import OMQ_O57_OBSERVATION_PRIOR
from .OMQ_O57_TIMING_PRIOR import OMQ_O57_TIMING_PRIOR

_CTD = CTD
_NTE = NTE
_OBR = OBR
_OMQ_O57_OBSERVATION_PRIOR = OMQ_O57_OBSERVATION_PRIOR
_OMQ_O57_TIMING_PRIOR = OMQ_O57_TIMING_PRIOR
_ORC = ORC
_PRT = PRT


class OMQ_O57_ORDER_PRIOR(HL7Model):
    """HL7 v2 OMQ_O57.ORDER_PRIOR group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        OBR (OBR): required
        TIMING_PRIOR (Optional[List[OMQ_O57_TIMING_PRIOR]]): optional
        NTE (Optional[List[NTE]]): optional
        CTD (Optional[CTD]): optional
        OBSERVATION_PRIOR (List[OMQ_O57_OBSERVATION_PRIOR]): required
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    TIMING_PRIOR: Optional[List[_OMQ_O57_TIMING_PRIOR]] = Field(
        default=None,
        title="TIMING_PRIOR",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    OBSERVATION_PRIOR: List[_OMQ_O57_OBSERVATION_PRIOR] = Field(
        default=...,
        title="OBSERVATION_PRIOR",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
