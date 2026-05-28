"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RRA_O18.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from .RRA_O18_ADMINISTRATION import RRA_O18_ADMINISTRATION

_ORC = ORC
_RRA_O18_ADMINISTRATION = RRA_O18_ADMINISTRATION


class RRA_O18_ORDER(BaseModel):
    """HL7 v2 RRA_O18.ORDER group.

    Attributes:
        ORC (ORC): required
        ADMINISTRATION (Optional[RRA_O18_ADMINISTRATION]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ADMINISTRATION: _RRA_O18_ADMINISTRATION | None = Field(
        default=None,
        title="ADMINISTRATION",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
