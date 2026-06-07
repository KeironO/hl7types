"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RDT
Type: Segment
"""
from __future__ import annotations

from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.varies import varies


class RDT(HL7Model):
    """HL7 v2 RDT segment.

    Attributes
    ----------
    rdt_1 : varies
        RDT.1 (req) - Column Value (varies)
    """

    rdt_1: varies = Field(
        validation_alias=AliasChoices(
            "rdt_1",
            "column_value",
            "RDT.1",
        ),
        serialization_alias="RDT.1",
        title="Column Value",
        description="Item #703",
    )

    model_config = {"populate_by_name": True}
