"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: MA
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class MA(BaseModel):
    """HL7 v2 MA data type."""

    ma_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ma_1",
            "sample_y_from_channel_1",
            "MA.1",
        ),
        serialization_alias="MA.1",
        title="Sample Y From Channel 1",
    )

    ma_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ma_2",
            "sample_y_from_channel_2",
            "MA.2",
        ),
        serialization_alias="MA.2",
        title="Sample Y From Channel 2",
    )

    ma_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ma_3",
            "sample_y_from_channel_3",
            "MA.3",
        ),
        serialization_alias="MA.3",
        title="Sample Y From Channel 3",
    )

    ma_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ma_4",
            "sample_y_from_channel_4",
            "MA.4",
        ),
        serialization_alias="MA.4",
        title="Sample Y From Channel 4",
    )

    model_config = {"populate_by_name": True}
