"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RDT
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.varies import varies


class RDT(BaseModel):
    """HL7 v2 RDT segment.

    Attributes
    ----------
    rdt_1 : varies
        RDT.1 (req) - Column Value (varies)
    """

    rdt_1: varies = Field(
        default=...,
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
