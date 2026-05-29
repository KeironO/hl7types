"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: CWE
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CWE(BaseModel):
    """HL7 v2 CWE data type.

    Attributes
    ----------
    cwe_1 : str | None
        CWE.1 (opt) - Identifier (ST)

    cwe_2 : str | None
        CWE.2 (opt) - Text (ST)

    cwe_3 : str | None
        CWE.3 (opt) - Name of Coding System (ID)

    cwe_4 : str | None
        CWE.4 (opt) - Alternate Identifier (ST)

    cwe_5 : str | None
        CWE.5 (opt) - Alternate Text (ST)

    cwe_6 : str | None
        CWE.6 (opt) - Name of Alternate Coding System (ID)

    cwe_7 : str | None
        CWE.7 (opt) - Coding System Version ID (ST)

    cwe_8 : str | None
        CWE.8 (opt) - Alternate Coding System Version ID (ST)

    cwe_9 : str | None
        CWE.9 (opt) - Original Text (ST)
    """

    cwe_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_1",
            "identifier",
            "CWE.1",
        ),
        serialization_alias="CWE.1",
        title="Identifier",
    )

    cwe_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_2",
            "text",
            "CWE.2",
        ),
        serialization_alias="CWE.2",
        title="Text",
    )

    cwe_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_3",
            "name_of_coding_system",
            "CWE.3",
        ),
        serialization_alias="CWE.3",
        title="Name of Coding System",
    )

    cwe_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_4",
            "alternate_identifier",
            "CWE.4",
        ),
        serialization_alias="CWE.4",
        title="Alternate Identifier",
    )

    cwe_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_5",
            "alternate_text",
            "CWE.5",
        ),
        serialization_alias="CWE.5",
        title="Alternate Text",
    )

    cwe_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_6",
            "name_of_alternate_coding_system",
            "CWE.6",
        ),
        serialization_alias="CWE.6",
        title="Name of Alternate Coding System",
    )

    cwe_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_7",
            "coding_system_version_id",
            "CWE.7",
        ),
        serialization_alias="CWE.7",
        title="Coding System Version ID",
    )

    cwe_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_8",
            "alternate_coding_system_version_id",
            "CWE.8",
        ),
        serialization_alias="CWE.8",
        title="Alternate Coding System Version ID",
    )

    cwe_9: Optional[str] = Field(
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
