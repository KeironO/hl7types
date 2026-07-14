"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OPL_O37.ORDER_PRIOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .OPL_O37_OBSERVATION_RESULT_GROUP import OPL_O37_OBSERVATION_RESULT_GROUP
from .OPL_O37_TIMING import OPL_O37_TIMING

_OBR = OBR
_OPL_O37_OBSERVATION_RESULT_GROUP = OPL_O37_OBSERVATION_RESULT_GROUP
_OPL_O37_TIMING = OPL_O37_TIMING
_ORC = ORC
_PRT = PRT


class OPL_O37_ORDER_PRIOR(HL7Model):
    """HL7 v2 OPL_O37.ORDER_PRIOR group.

    Attributes:
        OBR (OBR): Observation Request, required
        ORC (Optional[ORC]): Common Order, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        TIMING (Optional[OPL_O37_TIMING]): optional
        OBSERVATION_RESULT_GROUP (List[OPL_O37_OBSERVATION_RESULT_GROUP]): required
    """

    OBR: _OBR = Field(
        title="OBR",
        description="Observation Request",
    )

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Common Order",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    TIMING: Optional[_OPL_O37_TIMING] = Field(
        default=None,
        title="TIMING",
    )

    OBSERVATION_RESULT_GROUP: List[_OPL_O37_OBSERVATION_RESULT_GROUP] = Field(
        min_length=1,
        title="OBSERVATION_RESULT_GROUP",
    )

    model_config = {"populate_by_name": True}
