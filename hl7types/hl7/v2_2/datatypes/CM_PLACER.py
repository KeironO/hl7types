"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_PLACER
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CM_PLACER(BaseModel):
    """HL7 v2 CM_PLACER data type."""

    cm_placer_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_placer_1",
            "unique_placer_id",
            "CM_PLACER.1",
        ),
        serialization_alias="CM_PLACER.1",
        title="unique placer id",
    )

    cm_placer_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_placer_2",
            "placer_application",
            "CM_PLACER.2",
        ),
        serialization_alias="CM_PLACER.2",
        title="placer application",
    )

    model_config = {"populate_by_name": True}
