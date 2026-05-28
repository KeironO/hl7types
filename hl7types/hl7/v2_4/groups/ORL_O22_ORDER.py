"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORL_O22.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.ORC import ORC

from .ORL_O22_OBSERVATION_REQUEST import ORL_O22_OBSERVATION_REQUEST

_ORC = ORC
_ORL_O22_OBSERVATION_REQUEST = ORL_O22_OBSERVATION_REQUEST


class ORL_O22_ORDER(BaseModel):
    """HL7 v2 ORL_O22.ORDER group.

    Attributes:
        ORC (ORC): required
        OBSERVATION_REQUEST (Optional[ORL_O22_OBSERVATION_REQUEST]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    OBSERVATION_REQUEST: Optional[_ORL_O22_OBSERVATION_REQUEST] = Field(
        default=None,
        title="OBSERVATION_REQUEST",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
