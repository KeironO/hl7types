"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORL_O43.SPECIMEN_CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.SAC import SAC

from .ORL_O43_ORDER import ORL_O43_ORDER

_ORL_O43_ORDER = ORL_O43_ORDER
_SAC = SAC


class ORL_O43_SPECIMEN_CONTAINER(BaseModel):
    """HL7 v2 ORL_O43.SPECIMEN_CONTAINER group.

    Attributes:
        SAC (SAC): required
        ORDER (Optional[List[ORL_O43_ORDER]]): optional
    """

    SAC: _SAC = Field(
        default=...,
        title="SAC",
        description="Required",
    )

    ORDER: Optional[List[_ORL_O43_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
