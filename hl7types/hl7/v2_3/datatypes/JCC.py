"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: JCC
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class JCC(BaseModel):
    """HL7 v2 JCC data type."""

    jcc_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "jcc_1",
            "job_code",
            "JCC.1",
        ),
        serialization_alias="JCC.1",
        title="job code",
    )

    jcc_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "jcc_2",
            "job_class",
            "JCC.2",
        ),
        serialization_alias="JCC.2",
        title="job class",
    )

    model_config = {"populate_by_name": True}
