"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
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
        title="organization name",
    )

    xon_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_2",
            "organization_name_type_code",
            "XON.2",
        ),
        serialization_alias="XON.2",
        title="organization name type code",
    )

    xon_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_3",
            "id_number_nm",
            "XON.3",
        ),
        serialization_alias="XON.3",
        title="ID number (NM)",
    )

    xon_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_4",
            "check_digit",
            "XON.4",
        ),
        serialization_alias="XON.4",
        title="check digit",
    )

    xon_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_5",
            "code_identifying_the_check_digit_scheme_employed",
            "XON.5",
        ),
        serialization_alias="XON.5",
        title="code identifying the check digit scheme employed",
    )

    xon_6: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_6",
            "assigning_authority",
            "XON.6",
        ),
        serialization_alias="XON.6",
        title="assigning authority",
    )

    xon_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_7",
            "identifier_type_code",
            "XON.7",
        ),
        serialization_alias="XON.7",
        title="identifier type code",
    )

    xon_8: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xon_8",
            "assigning_facility_id",
            "XON.8",
        ),
        serialization_alias="XON.8",
        title="assigning facility ID",
    )

    model_config = {"populate_by_name": True}
