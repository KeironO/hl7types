"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: XON
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .HD import HD


class XON(BaseModel):
    """HL7 v2 XON data type."""

    xon_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_1",
            "organization_name",
            "XON.1",
        ),
        serialization_alias="XON.1",
        title="Organization Name",
    )

    xon_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_2",
            "organization_name_type_code",
            "XON.2",
        ),
        serialization_alias="XON.2",
        title="Organization Name Type Code",
    )

    xon_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_3",
            "id_number",
            "XON.3",
        ),
        serialization_alias="XON.3",
        title="ID Number",
    )

    xon_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_4",
            "check_digit",
            "XON.4",
        ),
        serialization_alias="XON.4",
        title="Check Digit",
    )

    xon_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_5",
            "check_digit_scheme",
            "XON.5",
        ),
        serialization_alias="XON.5",
        title="Check Digit Scheme",
    )

    xon_6: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_6",
            "assigning_authority",
            "XON.6",
        ),
        serialization_alias="XON.6",
        title="Assigning Authority",
    )

    xon_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_7",
            "identifier_type_code",
            "XON.7",
        ),
        serialization_alias="XON.7",
        title="Identifier Type Code",
    )

    xon_8: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_8",
            "assigning_facility",
            "XON.8",
        ),
        serialization_alias="XON.8",
        title="Assigning Facility",
    )

    xon_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_9",
            "name_representation_code",
            "XON.9",
        ),
        serialization_alias="XON.9",
        title="Name Representation Code",
    )

    xon_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_10",
            "organization_identifier",
            "XON.10",
        ),
        serialization_alias="XON.10",
        title="Organization Identifier",
    )

    model_config = {"populate_by_name": True}
