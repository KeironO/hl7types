"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORL_O40.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.PRT import PRT
from .ORL_O40_OBSERVATION_REQUEST import ORL_O40_OBSERVATION_REQUEST
from .ORL_O40_TIMING import ORL_O40_TIMING

_ORC = ORC
_ORL_O40_OBSERVATION_REQUEST = ORL_O40_OBSERVATION_REQUEST
_ORL_O40_TIMING = ORL_O40_TIMING
_PRT = PRT


class ORL_O40_ORDER(BaseModel):
    """HL7 v2 ORL_O40.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[List[ORL_O40_TIMING]]): optional
        OBSERVATION_REQUEST (Optional[ORL_O40_OBSERVATION_REQUEST]): optional
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

    TIMING: list[_ORL_O40_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    OBSERVATION_REQUEST: _ORL_O40_OBSERVATION_REQUEST | None = Field(
        default=None,
        title="OBSERVATION_REQUEST",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
