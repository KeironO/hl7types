"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: JCC
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class JCC(HL7Model):
    """HL7 v2 JCC data type.

    Attributes
    ----------
    jcc_1 : str | None
        JCC.1 (opt) - job code (IS)

    jcc_2 : str | None
        JCC.2 (opt) - job class (IS)
    """

    jcc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "jcc_1",
            "job_code",
            "JCC.1",
        ),
        serialization_alias="JCC.1",
        title="job code",
    )

    jcc_2: Optional[str] = Field(
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
