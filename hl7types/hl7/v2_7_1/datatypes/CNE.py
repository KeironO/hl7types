"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CNE
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class CNE(HL7Model):
    """HL7 v2 CNE data type.

    Attributes
    ----------
    cne_1 : str
        CNE.1 (req) - Identifier (ST)

    cne_2 : str | None
        CNE.2 (opt) - Text (ST)

    cne_3 : str | None
        CNE.3 (opt) - Name of Coding System (ID)

    cne_4 : str | None
        CNE.4 (opt) - Alternate Identifier (ST)

    cne_5 : str | None
        CNE.5 (opt) - Alternate Text (ST)

    cne_6 : str | None
        CNE.6 (opt) - Name of Alternate Coding System (ID)

    cne_7 : str | None
        CNE.7 (opt) - Coding System Version ID (ST)

    cne_8 : str | None
        CNE.8 (opt) - Alternate Coding System Version ID (ST)

    cne_9 : str | None
        CNE.9 (opt) - Original Text (ST)

    cne_10 : str | None
        CNE.10 (opt) - Second Alternate Identifier (ST)

    cne_11 : str | None
        CNE.11 (opt) - Second Alternate Text (ST)

    cne_12 : str | None
        CNE.12 (opt) - Name of Second Alternate Coding System (ID)

    cne_13 : str | None
        CNE.13 (opt) - Second Alternate Coding System Version ID (ST)

    cne_14 : str | None
        CNE.14 (opt) - Coding System OID (ST)

    cne_15 : str | None
        CNE.15 (opt) - Value Set OID (ST)

    cne_16 : str | None
        CNE.16 (opt) - Value Set Version ID (DTM)

    cne_17 : str | None
        CNE.17 (opt) - Alternate Coding System OID (ST)

    cne_18 : str | None
        CNE.18 (opt) - Alternate Value Set OID (ST)

    cne_19 : str | None
        CNE.19 (opt) - Alternate Value Set Version ID (DTM)

    cne_20 : str | None
        CNE.20 (opt) - Second Alternate Coding System OID (ST)

    cne_21 : str | None
        CNE.21 (opt) - Second Alternate Value Set OID (ST)

    cne_22 : str | None
        CNE.22 (opt) - Second Alternate Value Set Version ID (DTM)
    """

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

    cne_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_2",
            "text",
            "CNE.2",
        ),
        serialization_alias="CNE.2",
        title="Text",
    )

    cne_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_3",
            "name_of_coding_system",
            "CNE.3",
        ),
        serialization_alias="CNE.3",
        title="Name of Coding System",
    )

    cne_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_4",
            "alternate_identifier",
            "CNE.4",
        ),
        serialization_alias="CNE.4",
        title="Alternate Identifier",
    )

    cne_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_5",
            "alternate_text",
            "CNE.5",
        ),
        serialization_alias="CNE.5",
        title="Alternate Text",
    )

    cne_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_6",
            "name_of_alternate_coding_system",
            "CNE.6",
        ),
        serialization_alias="CNE.6",
        title="Name of Alternate Coding System",
    )

    cne_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_7",
            "coding_system_version_id",
            "CNE.7",
        ),
        serialization_alias="CNE.7",
        title="Coding System Version ID",
    )

    cne_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_8",
            "alternate_coding_system_version_id",
            "CNE.8",
        ),
        serialization_alias="CNE.8",
        title="Alternate Coding System Version ID",
    )

    cne_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_9",
            "original_text",
            "CNE.9",
        ),
        serialization_alias="CNE.9",
        title="Original Text",
    )

    cne_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_10",
            "second_alternate_identifier",
            "CNE.10",
        ),
        serialization_alias="CNE.10",
        title="Second Alternate Identifier",
    )

    cne_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_11",
            "second_alternate_text",
            "CNE.11",
        ),
        serialization_alias="CNE.11",
        title="Second Alternate Text",
    )

    cne_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_12",
            "name_of_second_alternate_coding_system",
            "CNE.12",
        ),
        serialization_alias="CNE.12",
        title="Name of Second Alternate Coding System",
    )

    cne_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_13",
            "second_alternate_coding_system_version_id",
            "CNE.13",
        ),
        serialization_alias="CNE.13",
        title="Second Alternate Coding System Version ID",
    )

    cne_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_14",
            "coding_system_oid",
            "CNE.14",
        ),
        serialization_alias="CNE.14",
        title="Coding System OID",
    )

    cne_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_15",
            "value_set_oid",
            "CNE.15",
        ),
        serialization_alias="CNE.15",
        title="Value Set OID",
    )

    cne_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_16",
            "value_set_version_id",
            "CNE.16",
        ),
        serialization_alias="CNE.16",
        title="Value Set Version ID",
    )

    cne_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_17",
            "alternate_coding_system_oid",
            "CNE.17",
        ),
        serialization_alias="CNE.17",
        title="Alternate Coding System OID",
    )

    cne_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_18",
            "alternate_value_set_oid",
            "CNE.18",
        ),
        serialization_alias="CNE.18",
        title="Alternate Value Set OID",
    )

    cne_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_19",
            "alternate_value_set_version_id",
            "CNE.19",
        ),
        serialization_alias="CNE.19",
        title="Alternate Value Set Version ID",
    )

    cne_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_20",
            "second_alternate_coding_system_oid",
            "CNE.20",
        ),
        serialization_alias="CNE.20",
        title="Second Alternate Coding System OID",
    )

    cne_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_21",
            "second_alternate_value_set_oid",
            "CNE.21",
        ),
        serialization_alias="CNE.21",
        title="Second Alternate Value Set OID",
    )

    cne_22: Optional[str] = Field(
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
