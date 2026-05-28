"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_ELD
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CE import CE


class CM_ELD(BaseModel):
    """HL7 v2 CM_ELD data type."""

    cm_eld_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_eld_1",
            "segment_id",
            "CM_ELD.1",
        ),
        serialization_alias="CM_ELD.1",
        title="segment ID",
    )

    cm_eld_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_eld_2",
            "sequence",
            "CM_ELD.2",
        ),
        serialization_alias="CM_ELD.2",
        title="sequence",
    )

    cm_eld_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_eld_3",
            "field_position",
            "CM_ELD.3",
        ),
        serialization_alias="CM_ELD.3",
        title="field position",
    )

    cm_eld_4: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_eld_4",
            "code_identifying_error",
            "CM_ELD.4",
        ),
        serialization_alias="CM_ELD.4",
        title="code identifying error",
    )

    model_config = {"populate_by_name": True}
