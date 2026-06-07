"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORL_O36.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .ORL_O36_OBSERVATION_REQUEST import ORL_O36_OBSERVATION_REQUEST
from .ORL_O36_TIMING import ORL_O36_TIMING

_ORC = ORC
_ORL_O36_OBSERVATION_REQUEST = ORL_O36_OBSERVATION_REQUEST
_ORL_O36_TIMING = ORL_O36_TIMING
_PRT = PRT


class ORL_O36_ORDER(HL7Model):
    """HL7 v2 ORL_O36.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[List[ORL_O36_TIMING]]): optional
        OBSERVATION_REQUEST (Optional[ORL_O36_OBSERVATION_REQUEST]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING: Optional[List[_ORL_O36_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    OBSERVATION_REQUEST: Optional[_ORL_O36_OBSERVATION_REQUEST] = Field(
        default=None,
        title="OBSERVATION_REQUEST",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
