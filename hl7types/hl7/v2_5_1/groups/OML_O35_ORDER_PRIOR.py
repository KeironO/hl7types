"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OML_O35.ORDER_PRIOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .OML_O35_OBSERVATION_PRIOR import OML_O35_OBSERVATION_PRIOR
from .OML_O35_TIMING_PRIOR import OML_O35_TIMING_PRIOR

_NTE = NTE
_OBR = OBR
_OML_O35_OBSERVATION_PRIOR = OML_O35_OBSERVATION_PRIOR
_OML_O35_TIMING_PRIOR = OML_O35_TIMING_PRIOR
_ORC = ORC


class OML_O35_ORDER_PRIOR(HL7Model):
    """HL7 v2 OML_O35.ORDER_PRIOR group.

    Attributes:
        ORC (Optional[ORC]): Common Order, optional
        OBR (OBR): Observation Request, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        TIMING_PRIOR (Optional[List[OML_O35_TIMING_PRIOR]]): optional
        OBSERVATION_PRIOR (List[OML_O35_OBSERVATION_PRIOR]): required
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Common Order",
    )

    OBR: _OBR = Field(
        title="OBR",
        description="Observation Request",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    TIMING_PRIOR: Optional[List[_OML_O35_TIMING_PRIOR]] = Field(
        default=None,
        title="TIMING_PRIOR",
    )

    OBSERVATION_PRIOR: List[_OML_O35_OBSERVATION_PRIOR] = Field(
        min_length=1,
        title="OBSERVATION_PRIOR",
    )

    model_config = ConfigDict(populate_by_name=True)
