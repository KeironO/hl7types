"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_GROUP_ID
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CM_GROUP_ID(BaseModel):
    """HL7 v2 CM_GROUP_ID data type."""

    cm_group_id_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_group_id_1",
            "unique_group_id",
            "CM_GROUP_ID.1",
        ),
        serialization_alias="CM_GROUP_ID.1",
        title="unique group id",
    )

    cm_group_id_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_group_id_2",
            "placer_application_id",
            "CM_GROUP_ID.2",
        ),
        serialization_alias="CM_GROUP_ID.2",
        title="placer application id",
    )

    model_config = {"populate_by_name": True}
