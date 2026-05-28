"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORL_O41.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .ORL_O41_OBSERVATION_REQUEST import ORL_O41_OBSERVATION_REQUEST
from .ORL_O41_TIMING import ORL_O41_TIMING

_ORC = ORC
_ORL_O41_OBSERVATION_REQUEST = ORL_O41_OBSERVATION_REQUEST
_ORL_O41_TIMING = ORL_O41_TIMING
_PRT = PRT


class ORL_O41_ORDER(BaseModel):
    """HL7 v2 ORL_O41.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[List[ORL_O41_TIMING]]): optional
        OBSERVATION_REQUEST (Optional[ORL_O41_OBSERVATION_REQUEST]): optional
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

    TIMING: Optional[List[_ORL_O41_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    OBSERVATION_REQUEST: Optional[_ORL_O41_OBSERVATION_REQUEST] = Field(
        default=None,
        title="OBSERVATION_REQUEST",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
