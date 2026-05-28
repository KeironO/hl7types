"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: NA
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class NA(BaseModel):
    """HL7 v2 NA data type."""

    na_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "na_1",
            "value1",
            "NA.1",
        ),
        serialization_alias="NA.1",
        title="Value1",
    )

    na_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "na_2",
            "value2",
            "NA.2",
        ),
        serialization_alias="NA.2",
        title="Value2",
    )

    na_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "na_3",
            "value3",
            "NA.3",
        ),
        serialization_alias="NA.3",
        title="Value3",
    )

    na_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "na_4",
            "value4",
            "NA.4",
        ),
        serialization_alias="NA.4",
        title="Value4",
    )

    model_config = {"populate_by_name": True}
