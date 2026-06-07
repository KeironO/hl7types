"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
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
        JCC.1 (opt) - Job Code (IS)

    jcc_2 : str | None
        JCC.2 (opt) - Job Class (IS)

    jcc_3 : str | None
        JCC.3 (opt) - Job Description Text (TX)
    """

    jcc_1: Optional[str] = Field(
        default=None,
        max_length=20,
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
        max_length=20,
        validation_alias=AliasChoices(
            "jcc_2",
            "job_class",
            "JCC.2",
        ),
        serialization_alias="JCC.2",
        title="Job Class",
    )

    jcc_3: Optional[str] = Field(
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
