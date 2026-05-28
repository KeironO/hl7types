"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_K13.ROW_DEFINITION
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.RDF import RDF
from ..segments.RDT import RDT

_RDF = RDF
_RDT = RDT


class RSP_K13_ROW_DEFINITION(BaseModel):
    """HL7 v2 RSP_K13.ROW_DEFINITION group.

    Attributes:
        RDF (RDF): required
        RDT (Optional[List[RDT]]): optional
    """

    RDF: _RDF = Field(
        default=...,
        title="RDF",
        description="Required",
    )

    RDT: Optional[List[_RDT]] = Field(
        default=None,
        title="RDT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
