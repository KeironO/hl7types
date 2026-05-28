"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_SPS
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CE import CE
from .TX import TX


class CM_SPS(BaseModel):
    """HL7 v2 CM_SPS data type."""

    cm_sps_1: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_sps_1",
            "specimen_source_name_or_code",
            "CM_SPS.1",
        ),
        serialization_alias="CM_SPS.1",
        title="Specimen source name or code",
    )

    cm_sps_2: TX | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_sps_2",
            "additives",
            "CM_SPS.2",
        ),
        serialization_alias="CM_SPS.2",
        title="additives",
    )

    cm_sps_3: TX | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_sps_3",
            "freetext",
            "CM_SPS.3",
        ),
        serialization_alias="CM_SPS.3",
        title="freetext",
    )

    cm_sps_4: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_sps_4",
            "body_site",
            "CM_SPS.4",
        ),
        serialization_alias="CM_SPS.4",
        title="body site",
    )

    cm_sps_5: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_sps_5",
            "site_modifier",
            "CM_SPS.5",
        ),
        serialization_alias="CM_SPS.5",
        title="site modifier",
    )

    model_config = {"populate_by_name": True}
