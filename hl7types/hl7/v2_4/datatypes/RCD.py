"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RCD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class RCD(BaseModel):
    """HL7 v2 RCD data type."""

    rcd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcd_1",
            "segment_field_name",
            "RCD.1",
        ),
        serialization_alias="RCD.1",
        title="segment field name",
    )

    rcd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcd_2",
            "hl7_date_type",
            "RCD.2",
        ),
        serialization_alias="RCD.2",
        title="HL7 date type",
    )

    rcd_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcd_3",
            "maximum_column_width",
            "RCD.3",
        ),
        serialization_alias="RCD.3",
        title="maximum column width",
    )

    model_config = {"populate_by_name": True}
