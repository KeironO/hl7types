"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
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
        RDF (RDF): Table Row Definition, required
        RDT (Optional[List[RDT]]): Table Row Data, optional
    """

    RDF: _RDF = Field(
        title="RDF",
        description="Table Row Definition",
    )

    RDT: Optional[List[_RDT]] = Field(
        default=None,
        title="RDT",
        description="Table Row Data",
    )

    model_config = {"populate_by_name": True}
