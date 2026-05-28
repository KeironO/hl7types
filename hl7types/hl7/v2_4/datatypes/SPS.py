"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: SPS
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CE import CE
from .TX import TX


class SPS(BaseModel):
    """HL7 v2 SPS data type."""

    sps_1: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_1",
            "specimen_source_name_or_code",
            "SPS.1",
        ),
        serialization_alias="SPS.1",
        title="specimen source name or code",
    )

    sps_2: TX | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_2",
            "additives",
            "SPS.2",
        ),
        serialization_alias="SPS.2",
        title="additives",
    )

    sps_3: TX | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_3",
            "freetext",
            "SPS.3",
        ),
        serialization_alias="SPS.3",
        title="freetext",
    )

    sps_4: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_4",
            "body_site",
            "SPS.4",
        ),
        serialization_alias="SPS.4",
        title="body site",
    )

    sps_5: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_5",
            "site_modifier",
            "SPS.5",
        ),
        serialization_alias="SPS.5",
        title="site modifier",
    )

    sps_6: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_6",
            "collection_modifier_method_code",
            "SPS.6",
        ),
        serialization_alias="SPS.6",
        title="collection modifier method code",
    )

    sps_7: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_7",
            "specimen_role",
            "SPS.7",
        ),
        serialization_alias="SPS.7",
        title="specimen role",
    )

    model_config = {"populate_by_name": True}
