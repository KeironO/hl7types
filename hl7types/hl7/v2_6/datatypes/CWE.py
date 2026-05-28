"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: CWE
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CWE(BaseModel):
    """HL7 v2 CWE data type."""

    cwe_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_1",
            "identifier",
            "CWE.1",
        ),
        serialization_alias="CWE.1",
        title="Identifier",
    )

    cwe_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_2",
            "text",
            "CWE.2",
        ),
        serialization_alias="CWE.2",
        title="Text",
    )

    cwe_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_3",
            "name_of_coding_system",
            "CWE.3",
        ),
        serialization_alias="CWE.3",
        title="Name of Coding System",
    )

    cwe_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_4",
            "alternate_identifier",
            "CWE.4",
        ),
        serialization_alias="CWE.4",
        title="Alternate Identifier",
    )

    cwe_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_5",
            "alternate_text",
            "CWE.5",
        ),
        serialization_alias="CWE.5",
        title="Alternate Text",
    )

    cwe_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_6",
            "name_of_alternate_coding_system",
            "CWE.6",
        ),
        serialization_alias="CWE.6",
        title="Name of Alternate Coding System",
    )

    cwe_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_7",
            "coding_system_version_id",
            "CWE.7",
        ),
        serialization_alias="CWE.7",
        title="Coding System Version ID",
    )

    cwe_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_8",
            "alternate_coding_system_version_id",
            "CWE.8",
        ),
        serialization_alias="CWE.8",
        title="Alternate Coding System Version ID",
    )

    cwe_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_9",
            "original_text",
            "CWE.9",
        ),
        serialization_alias="CWE.9",
        title="Original Text",
    )

    model_config = {"populate_by_name": True}
