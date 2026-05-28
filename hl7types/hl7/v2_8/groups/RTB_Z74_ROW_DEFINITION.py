"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RTB_Z74.ROW_DEFINITION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.RDF import RDF
from ..segments.RDT import RDT

_RDF = RDF
_RDT = RDT


class RTB_Z74_ROW_DEFINITION(BaseModel):
    """HL7 v2 RTB_Z74.ROW_DEFINITION group.

    Attributes:
        RDF (RDF): required
        RDT (Optional[List[RDT]]): optional
    """

    RDF: _RDF = Field(
        default=...,
        title="RDF",
        description="Required",
    )

    RDT: list[_RDT] | None = Field(
        default=None,
        title="RDT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
