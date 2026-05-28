"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_RI
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CM_RI(BaseModel):
    """HL7 v2 CM_RI data type."""

    cm_ri_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ri_1",
            "repeat_pattern",
            "CM_RI.1",
        ),
        serialization_alias="CM_RI.1",
        title="repeat pattern",
    )

    cm_ri_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ri_2",
            "explicit_time_interval",
            "CM_RI.2",
        ),
        serialization_alias="CM_RI.2",
        title="explicit time interval",
    )

    model_config = {"populate_by_name": True}
