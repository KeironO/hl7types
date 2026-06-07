"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CF
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class CF(HL7Model):
    """HL7 v2 CF data type.

    Attributes
    ----------
    cf_1 : str | None
        CF.1 (opt) - Identifier (ST)

    cf_2 : str | None
        CF.2 (opt) - Formatted Text (FT)

    cf_3 : str | None
        CF.3 (opt) - Name of Coding System (ID)

    cf_4 : str | None
        CF.4 (opt) - Alternate Identifier (ST)

    cf_5 : str | None
        CF.5 (opt) - Alternate Formatted Text (FT)

    cf_6 : str | None
        CF.6 (opt) - Name of Alternate Coding System (ID)

    cf_7 : str | None
        CF.7 (opt) - Coding System Version ID (ST)

    cf_8 : str | None
        CF.8 (opt) - Alternate Coding System Version ID (ST)

    cf_9 : str | None
        CF.9 (opt) - Original Text (ST)

    cf_10 : str | None
        CF.10 (opt) - Second Alternate Identifier (ST)

    cf_11 : str | None
        CF.11 (opt) - Second Alternate Formatted Text (FT)

    cf_12 : str | None
        CF.12 (opt) - Name of Second Alternate Coding System (ID)

    cf_13 : str | None
        CF.13 (opt) - Second Alternate Coding System Version ID (ST)

    cf_14 : str | None
        CF.14 (opt) - Coding System OID (ST)

    cf_15 : str | None
        CF.15 (opt) - Value Set OID (ST)

    cf_16 : str | None
        CF.16 (opt) - Value Set Version ID (DTM)

    cf_17 : str | None
        CF.17 (opt) - Alternate Coding System OID (ST)

    cf_18 : str | None
        CF.18 (opt) - Alternate Value Set OID (ST)

    cf_19 : str | None
        CF.19 (opt) - Alternate Value Set Version ID (DTM)

    cf_20 : str | None
        CF.20 (opt) - Second Alternate Coding System OID (ST)

    cf_21 : str | None
        CF.21 (opt) - Second Alternate Value Set OID (ST)

    cf_22 : str | None
        CF.22 (opt) - Second Alternate Value Set Version ID (DTM)
    """

    cf_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_1",
            "identifier",
            "CF.1",
        ),
        serialization_alias="CF.1",
        title="Identifier",
    )

    cf_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_2",
            "formatted_text",
            "CF.2",
        ),
        serialization_alias="CF.2",
        title="Formatted Text",
    )

    cf_3: Optional[str] = Field(
        default=None,
        max_length=12,
        validation_alias=AliasChoices(
            "cf_3",
            "name_of_coding_system",
            "CF.3",
        ),
        serialization_alias="CF.3",
        title="Name of Coding System",
    )

    cf_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_4",
            "alternate_identifier",
            "CF.4",
        ),
        serialization_alias="CF.4",
        title="Alternate Identifier",
    )

    cf_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_5",
            "alternate_formatted_text",
            "CF.5",
        ),
        serialization_alias="CF.5",
        title="Alternate Formatted Text",
    )

    cf_6: Optional[str] = Field(
        default=None,
        max_length=12,
        validation_alias=AliasChoices(
            "cf_6",
            "name_of_alternate_coding_system",
            "CF.6",
        ),
        serialization_alias="CF.6",
        title="Name of Alternate Coding System",
    )

    cf_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_7",
            "coding_system_version_id",
            "CF.7",
        ),
        serialization_alias="CF.7",
        title="Coding System Version ID",
    )

    cf_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_8",
            "alternate_coding_system_version_id",
            "CF.8",
        ),
        serialization_alias="CF.8",
        title="Alternate Coding System Version ID",
    )

    cf_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_9",
            "original_text",
            "CF.9",
        ),
        serialization_alias="CF.9",
        title="Original Text",
    )

    cf_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_10",
            "second_alternate_identifier",
            "CF.10",
        ),
        serialization_alias="CF.10",
        title="Second Alternate Identifier",
    )

    cf_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_11",
            "second_alternate_formatted_text",
            "CF.11",
        ),
        serialization_alias="CF.11",
        title="Second Alternate Formatted Text",
    )

    cf_12: Optional[str] = Field(
        default=None,
        max_length=12,
        validation_alias=AliasChoices(
            "cf_12",
            "name_of_second_alternate_coding_system",
            "CF.12",
        ),
        serialization_alias="CF.12",
        title="Name of Second Alternate Coding System",
    )

    cf_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_13",
            "second_alternate_coding_system_version_id",
            "CF.13",
        ),
        serialization_alias="CF.13",
        title="Second Alternate Coding System Version ID",
    )

    cf_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_14",
            "coding_system_oid",
            "CF.14",
        ),
        serialization_alias="CF.14",
        title="Coding System OID",
    )

    cf_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_15",
            "value_set_oid",
            "CF.15",
        ),
        serialization_alias="CF.15",
        title="Value Set OID",
    )

    cf_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_16",
            "value_set_version_id",
            "CF.16",
        ),
        serialization_alias="CF.16",
        title="Value Set Version ID",
    )

    cf_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_17",
            "alternate_coding_system_oid",
            "CF.17",
        ),
        serialization_alias="CF.17",
        title="Alternate Coding System OID",
    )

    cf_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_18",
            "alternate_value_set_oid",
            "CF.18",
        ),
        serialization_alias="CF.18",
        title="Alternate Value Set OID",
    )

    cf_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_19",
            "alternate_value_set_version_id",
            "CF.19",
        ),
        serialization_alias="CF.19",
        title="Alternate Value Set Version ID",
    )

    cf_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_20",
            "second_alternate_coding_system_oid",
            "CF.20",
        ),
        serialization_alias="CF.20",
        title="Second Alternate Coding System OID",
    )

    cf_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_21",
            "second_alternate_value_set_oid",
            "CF.21",
        ),
        serialization_alias="CF.21",
        title="Second Alternate Value Set OID",
    )

    cf_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_22",
            "second_alternate_value_set_version_id",
            "CF.22",
        ),
        serialization_alias="CF.22",
        title="Second Alternate Value Set Version ID",
    )

    @field_validator("cf_16", "cf_19", "cf_22", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
