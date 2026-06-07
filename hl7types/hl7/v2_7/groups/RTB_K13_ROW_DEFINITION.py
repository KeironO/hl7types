"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RTB_K13.ROW_DEFINITION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RDF import RDF
from ..segments.RDT import RDT

_RDF = RDF
_RDT = RDT


class RTB_K13_ROW_DEFINITION(HL7Model):
    """HL7 v2 RTB_K13.ROW_DEFINITION group.

    Attributes:
        RDF (RDF): required
        RDT (Optional[List[RDT]]): optional
    """

    RDF: _RDF = Field(
        title="RDF",
        description="Required",
    )

    RDT: Optional[List[_RDT]] = Field(
        default=None,
        title="RDT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
