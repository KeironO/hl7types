"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_ELD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CE import CE


class CM_ELD(BaseModel):
    """HL7 v2 CM_ELD data type.

    Attributes
    ----------
    cm_eld_1 : str | None
        CM_ELD.1 (opt) - segment ID (ST)

    cm_eld_2 : str | None
        CM_ELD.2 (opt) - sequence (NM)

    cm_eld_3 : str | None
        CM_ELD.3 (opt) - field position (NM)

    cm_eld_4 : CE | None
        CM_ELD.4 (opt) - code identifying error (CE)
    """

    cm_eld_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_eld_1",
            "segment_id",
            "CM_ELD.1",
        ),
        serialization_alias="CM_ELD.1",
        title="segment ID",
    )

    cm_eld_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_eld_2",
            "sequence",
            "CM_ELD.2",
        ),
        serialization_alias="CM_ELD.2",
        title="sequence",
    )

    cm_eld_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_eld_3",
            "field_position",
            "CM_ELD.3",
        ),
        serialization_alias="CM_ELD.3",
        title="field position",
    )

    cm_eld_4: Optional[CE] = Field(
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
