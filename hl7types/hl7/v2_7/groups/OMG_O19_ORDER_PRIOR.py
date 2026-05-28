"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OMG_O19.ORDER_PRIOR
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTD import CTD
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.PRT import PRT
from .OMG_O19_OBSERVATION_PRIOR import OMG_O19_OBSERVATION_PRIOR
from .OMG_O19_TIMING_PRIOR import OMG_O19_TIMING_PRIOR

_CTD = CTD
_NTE = NTE
_OBR = OBR
_OMG_O19_OBSERVATION_PRIOR = OMG_O19_OBSERVATION_PRIOR
_OMG_O19_TIMING_PRIOR = OMG_O19_TIMING_PRIOR
_ORC = ORC
_PRT = PRT


class OMG_O19_ORDER_PRIOR(BaseModel):
    """HL7 v2 OMG_O19.ORDER_PRIOR group.

    Attributes:
        ORC (ORC): required
        OBR (OBR): required
        TIMING_PRIOR (Optional[List[OMG_O19_TIMING_PRIOR]]): optional
        NTE (Optional[List[NTE]]): optional
        PRT (Optional[List[PRT]]): optional
        CTD (Optional[CTD]): optional
        OBSERVATION_PRIOR (List[OMG_O19_OBSERVATION_PRIOR]): required
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

    TIMING_PRIOR: list[_OMG_O19_TIMING_PRIOR] | None = Field(
        default=None,
        title="TIMING_PRIOR",
        description="Optional, repeating",
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

    OBSERVATION_PRIOR: list[_OMG_O19_OBSERVATION_PRIOR] = Field(
        default=...,
        title="OBSERVATION_PRIOR",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
