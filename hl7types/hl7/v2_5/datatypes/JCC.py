"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: JCC
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .TX import TX


class JCC(BaseModel):
    """HL7 v2 JCC data type."""

    jcc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "jcc_1",
            "job_code",
            "JCC.1",
        ),
        serialization_alias="JCC.1",
        title="Job Code",
    )

    jcc_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "jcc_2",
            "job_class",
            "JCC.2",
        ),
        serialization_alias="JCC.2",
        title="Job Class",
    )

    jcc_3: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "jcc_3",
            "job_description_text",
            "JCC.3",
        ),
        serialization_alias="JCC.3",
        title="Job Description Text",
    )

    model_config = {"populate_by_name": True}
