"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RCD
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class RCD(BaseModel):
    """HL7 v2 RCD data type."""

    rcd_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcd_1",
            "segment_field_name",
            "RCD.1",
        ),
        serialization_alias="RCD.1",
        title="Segment Field Name",
    )

    rcd_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcd_2",
            "hl7_data_type",
            "RCD.2",
        ),
        serialization_alias="RCD.2",
        title="HL7 Data Type",
    )

    rcd_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rcd_3",
            "maximum_column_width",
            "RCD.3",
        ),
        serialization_alias="RCD.3",
        title="Maximum Column Width",
    )

    model_config = {"populate_by_name": True}
