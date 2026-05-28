"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RRA_O02.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from .RRA_O02_ADMINISTRATION import RRA_O02_ADMINISTRATION

_ORC = ORC
_RRA_O02_ADMINISTRATION = RRA_O02_ADMINISTRATION


class RRA_O02_ORDER(BaseModel):
    """HL7 v2 RRA_O02.ORDER group.

    Attributes:
        ORC (ORC): required
        ADMINISTRATION (Optional[List[RRA_O02_ADMINISTRATION]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ADMINISTRATION: list[_RRA_O02_ADMINISTRATION] | None = Field(
        default=None,
        title="ADMINISTRATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
