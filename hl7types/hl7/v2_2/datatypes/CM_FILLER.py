"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_FILLER
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CM_FILLER(BaseModel):
    """HL7 v2 CM_FILLER data type."""

    cm_filler_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_filler_1",
            "unique_filler_id",
            "CM_FILLER.1",
        ),
        serialization_alias="CM_FILLER.1",
        title="unique filler id",
    )

    cm_filler_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_filler_2",
            "filler_application_id",
            "CM_FILLER.2",
        ),
        serialization_alias="CM_FILLER.2",
        title="filler application ID",
    )

    model_config = {"populate_by_name": True}
