"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
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

    cwe_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_10",
            "second_alternate_identifier",
            "CWE.10",
        ),
        serialization_alias="CWE.10",
        title="Second Alternate Identifier",
    )

    cwe_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_11",
            "second_alternate_text",
            "CWE.11",
        ),
        serialization_alias="CWE.11",
        title="Second Alternate Text",
    )

    cwe_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_12",
            "name_of_second_alternate_coding_system",
            "CWE.12",
        ),
        serialization_alias="CWE.12",
        title="Name of Second Alternate Coding System",
    )

    cwe_13: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_13",
            "second_alternate_coding_system_version_id",
            "CWE.13",
        ),
        serialization_alias="CWE.13",
        title="Second Alternate Coding System Version ID",
    )

    cwe_14: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_14",
            "coding_system_oid",
            "CWE.14",
        ),
        serialization_alias="CWE.14",
        title="Coding System OID",
    )

    cwe_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_15",
            "value_set_oid",
            "CWE.15",
        ),
        serialization_alias="CWE.15",
        title="Value Set OID",
    )

    cwe_16: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_16",
            "value_set_version_id",
            "CWE.16",
        ),
        serialization_alias="CWE.16",
        title="Value Set Version ID",
    )

    cwe_17: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_17",
            "alternate_coding_system_oid",
            "CWE.17",
        ),
        serialization_alias="CWE.17",
        title="Alternate Coding System OID",
    )

    cwe_18: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_18",
            "alternate_value_set_oid",
            "CWE.18",
        ),
        serialization_alias="CWE.18",
        title="Alternate Value Set OID",
    )

    cwe_19: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_19",
            "alternate_value_set_version_id",
            "CWE.19",
        ),
        serialization_alias="CWE.19",
        title="Alternate Value Set Version ID",
    )

    cwe_20: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_20",
            "second_alternate_coding_system_oid",
            "CWE.20",
        ),
        serialization_alias="CWE.20",
        title="Second Alternate Coding System OID",
    )

    cwe_21: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_21",
            "second_alternate_value_set_oid",
            "CWE.21",
        ),
        serialization_alias="CWE.21",
        title="Second Alternate Value Set OID",
    )

    cwe_22: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cwe_22",
            "second_alternate_value_set_version_id",
            "CWE.22",
        ),
        serialization_alias="CWE.22",
        title="Second Alternate Value Set Version ID",
    )

    model_config = {"populate_by_name": True}
