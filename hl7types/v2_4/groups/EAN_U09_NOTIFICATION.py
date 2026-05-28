"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: EAN_U09.NOTIFICATION
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.NDS import NDS
from ..segments.NTE import NTE

_NDS = NDS
_NTE = NTE


class EAN_U09_NOTIFICATION(BaseModel):
    """HL7 v2 EAN_U09.NOTIFICATION group.

    Attributes:
        NDS (NDS): required
        NTE (Optional[NTE]): optional
    """

    NDS: _NDS = Field(
        default=...,
        title="NDS",
        description="Required",
    )

    NTE: Optional[_NTE] = Field(
        default=None,
        title="NTE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
