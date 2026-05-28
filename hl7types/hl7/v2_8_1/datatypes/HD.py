"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: HD
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class HD(BaseModel):
    """HL7 v2 HD data type."""

    hd_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "hd_1",
            "namespace_id",
            "HD.1",
        ),
        serialization_alias="HD.1",
        title="Namespace ID",
    )

    hd_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "hd_2",
            "universal_id",
            "HD.2",
        ),
        serialization_alias="HD.2",
        title="Universal ID",
    )

    hd_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "hd_3",
            "universal_id_type",
            "HD.3",
        ),
        serialization_alias="HD.3",
        title="Universal ID Type",
    )

    model_config = {"populate_by_name": True}
