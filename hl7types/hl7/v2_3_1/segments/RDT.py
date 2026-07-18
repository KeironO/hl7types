"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RDT
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class RDT(HL7Model):
    """RDT - table row data segment (S2.24.19).

    Attributes
    ----------
    rdt_1 : str | None
        RDT.1 - Column Value (*) NA S2.24.19.1
    """

    rdt_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rdt_1",
            "column_value",
            "RDT.1",
        ),
        serialization_alias="RDT.1",
        title="Column Value",
        description="NA | Item #00703",
    )

    model_config = ConfigDict(populate_by_name=True)
