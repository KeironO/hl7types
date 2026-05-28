"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CNE
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CNE(BaseModel):
    """HL7 v2 CNE data type."""

    cne_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "cne_1",
            "identifier",
            "CNE.1",
        ),
        serialization_alias="CNE.1",
        title="Identifier",
    )

    cne_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_2",
            "text",
            "CNE.2",
        ),
        serialization_alias="CNE.2",
        title="Text",
    )

    cne_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_3",
            "name_of_coding_system",
            "CNE.3",
        ),
        serialization_alias="CNE.3",
        title="Name of Coding System",
    )

    cne_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_4",
            "alternate_identifier",
            "CNE.4",
        ),
        serialization_alias="CNE.4",
        title="Alternate Identifier",
    )

    cne_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_5",
            "alternate_text",
            "CNE.5",
        ),
        serialization_alias="CNE.5",
        title="Alternate Text",
    )

    cne_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_6",
            "name_of_alternate_coding_system",
            "CNE.6",
        ),
        serialization_alias="CNE.6",
        title="Name of Alternate Coding System",
    )

    cne_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_7",
            "coding_system_version_id",
            "CNE.7",
        ),
        serialization_alias="CNE.7",
        title="Coding System Version ID",
    )

    cne_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_8",
            "alternate_coding_system_version_id",
            "CNE.8",
        ),
        serialization_alias="CNE.8",
        title="Alternate Coding System Version ID",
    )

    cne_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_9",
            "original_text",
            "CNE.9",
        ),
        serialization_alias="CNE.9",
        title="Original Text",
    )

    cne_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_10",
            "second_alternate_identifier",
            "CNE.10",
        ),
        serialization_alias="CNE.10",
        title="Second Alternate Identifier",
    )

    cne_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_11",
            "second_alternate_text",
            "CNE.11",
        ),
        serialization_alias="CNE.11",
        title="Second Alternate Text",
    )

    cne_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_12",
            "name_of_second_alternate_coding_system",
            "CNE.12",
        ),
        serialization_alias="CNE.12",
        title="Name of Second Alternate Coding System",
    )

    cne_13: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_13",
            "second_alternate_coding_system_version_id",
            "CNE.13",
        ),
        serialization_alias="CNE.13",
        title="Second Alternate Coding System Version ID",
    )

    cne_14: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_14",
            "coding_system_oid",
            "CNE.14",
        ),
        serialization_alias="CNE.14",
        title="Coding System OID",
    )

    cne_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_15",
            "value_set_oid",
            "CNE.15",
        ),
        serialization_alias="CNE.15",
        title="Value Set OID",
    )

    cne_16: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_16",
            "value_set_version_id",
            "CNE.16",
        ),
        serialization_alias="CNE.16",
        title="Value Set Version ID",
    )

    cne_17: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_17",
            "alternate_coding_system_oid",
            "CNE.17",
        ),
        serialization_alias="CNE.17",
        title="Alternate Coding System OID",
    )

    cne_18: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_18",
            "alternate_value_set_oid",
            "CNE.18",
        ),
        serialization_alias="CNE.18",
        title="Alternate Value Set OID",
    )

    cne_19: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_19",
            "alternate_value_set_version_id",
            "CNE.19",
        ),
        serialization_alias="CNE.19",
        title="Alternate Value Set Version ID",
    )

    cne_20: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_20",
            "second_alternate_coding_system_oid",
            "CNE.20",
        ),
        serialization_alias="CNE.20",
        title="Second Alternate Coding System OID",
    )

    cne_21: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_21",
            "second_alternate_value_set_oid",
            "CNE.21",
        ),
        serialization_alias="CNE.21",
        title="Second Alternate Value Set OID",
    )

    cne_22: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_22",
            "second_alternate_value_set_version_id",
            "CNE.22",
        ),
        serialization_alias="CNE.22",
        title="Second Alternate Value Set Version ID",
    )

    model_config = {"populate_by_name": True}
