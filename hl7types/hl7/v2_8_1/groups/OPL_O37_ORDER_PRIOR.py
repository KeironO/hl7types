"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OPL_O37.ORDER_PRIOR
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

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


class OPL_O37_ORDER_PRIOR(BaseModel):
    """HL7 v2 OPL_O37.ORDER_PRIOR group.

    Attributes:
        OBR (OBR): required
        ORC (Optional[ORC]): optional
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[OPL_O37_TIMING]): optional
        OBSERVATION_RESULT_GROUP (List[OPL_O37_OBSERVATION_RESULT_GROUP]): required
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    ORC: _ORC | None = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING: _OPL_O37_TIMING | None = Field(
        default=None,
        title="TIMING",
        description="Optional",
    )

    OBSERVATION_RESULT_GROUP: list[_OPL_O37_OBSERVATION_RESULT_GROUP] = Field(
        default=...,
        title="OBSERVATION_RESULT_GROUP",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
