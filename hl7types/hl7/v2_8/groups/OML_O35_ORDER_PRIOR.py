"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OML_O35.ORDER_PRIOR
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.PRT import PRT
from .OML_O35_OBSERVATION_PRIOR import OML_O35_OBSERVATION_PRIOR
from .OML_O35_TIMING_PRIOR import OML_O35_TIMING_PRIOR

_NTE = NTE
_OBR = OBR
_OML_O35_OBSERVATION_PRIOR = OML_O35_OBSERVATION_PRIOR
_OML_O35_TIMING_PRIOR = OML_O35_TIMING_PRIOR
_ORC = ORC
_PRT = PRT


class OML_O35_ORDER_PRIOR(BaseModel):
    """HL7 v2 OML_O35.ORDER_PRIOR group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        TIMING_PRIOR (Optional[List[OML_O35_TIMING_PRIOR]]): optional
        OBSERVATION_PRIOR (List[OML_O35_OBSERVATION_PRIOR]): required
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    TIMING_PRIOR: list[_OML_O35_TIMING_PRIOR] | None = Field(
        default=None,
        title="TIMING_PRIOR",
        description="Optional, repeating",
    )

    OBSERVATION_PRIOR: list[_OML_O35_OBSERVATION_PRIOR] = Field(
        default=...,
        title="OBSERVATION_PRIOR",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
