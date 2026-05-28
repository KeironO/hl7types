"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORL_O36.SPECIMEN_CONTAINER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.SAC import SAC
from .ORL_O36_ORDER import ORL_O36_ORDER

_ORL_O36_ORDER = ORL_O36_ORDER
_SAC = SAC


class ORL_O36_SPECIMEN_CONTAINER(BaseModel):
    """HL7 v2 ORL_O36.SPECIMEN_CONTAINER group.

    Attributes:
        SAC (SAC): required
        ORDER (Optional[List[ORL_O36_ORDER]]): optional
    """

    SAC: _SAC = Field(
        default=...,
        title="SAC",
        description="Required",
    )

    ORDER: list[_ORL_O36_ORDER] | None = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
