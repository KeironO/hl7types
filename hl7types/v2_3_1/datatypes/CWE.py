"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: CWE
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CWE(BaseModel):
    """HL7 v2 CWE data type."""

    cwe_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_1",
            "identifier",
            "CWE.1",
        ),
        serialization_alias="CWE.1",
        title="identifier",
    )

    cwe_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_2",
            "text",
            "CWE.2",
        ),
        serialization_alias="CWE.2",
        title="text",
    )

    cwe_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_3",
            "name_of_coding_system",
            "CWE.3",
        ),
        serialization_alias="CWE.3",
        title="name of coding system",
    )

    cwe_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_4",
            "alternate_identifier",
            "CWE.4",
        ),
        serialization_alias="CWE.4",
        title="alternate identifier",
    )

    cwe_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_5",
            "alternate_text",
            "CWE.5",
        ),
        serialization_alias="CWE.5",
        title="alternate text",
    )

    cwe_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_6",
            "name_of_alternate_coding_system",
            "CWE.6",
        ),
        serialization_alias="CWE.6",
        title="name of alternate coding system",
    )

    cwe_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_7",
            "coding_system_version_id",
            "CWE.7",
        ),
        serialization_alias="CWE.7",
        title="coding system version ID",
    )

    cwe_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_8",
            "alternate_coding_system_version_id",
            "CWE.8",
        ),
        serialization_alias="CWE.8",
        title="alternate coding system version ID",
    )

    cwe_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_9",
            "original_text",
            "CWE.9",
        ),
        serialization_alias="CWE.9",
        title="original text",
    )

    model_config = {"populate_by_name": True}
