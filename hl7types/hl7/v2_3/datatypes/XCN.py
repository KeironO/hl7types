"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: XCN
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .HD import HD


class XCN(BaseModel):
    """HL7 v2 XCN data type."""

    xcn_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_1",
            "id_number_st",
            "XCN.1",
        ),
        serialization_alias="XCN.1",
        title="ID number (ST)",
    )

    xcn_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_2",
            "family_name",
            "XCN.2",
        ),
        serialization_alias="XCN.2",
        title="family name",
    )

    xcn_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_3",
            "given_name",
            "XCN.3",
        ),
        serialization_alias="XCN.3",
        title="given name",
    )

    xcn_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_4",
            "middle_initial_or_name",
            "XCN.4",
        ),
        serialization_alias="XCN.4",
        title="middle initial or name",
    )

    xcn_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_5",
            "suffix_e_g_jr_or_iii",
            "XCN.5",
        ),
        serialization_alias="XCN.5",
        title="suffix (e.g., JR or III)",
    )

    xcn_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_6",
            "prefix_e_g_dr",
            "XCN.6",
        ),
        serialization_alias="XCN.6",
        title="prefix (e.g., DR)",
    )

    xcn_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_7",
            "degree_e_g_md",
            "XCN.7",
        ),
        serialization_alias="XCN.7",
        title="degree (e.g., MD)",
    )

    xcn_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_8",
            "source_table",
            "XCN.8",
        ),
        serialization_alias="XCN.8",
        title="source table",
    )

    xcn_9: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_9",
            "assigning_authority",
            "XCN.9",
        ),
        serialization_alias="XCN.9",
        title="assigning authority",
    )

    xcn_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_10",
            "name_type",
            "XCN.10",
        ),
        serialization_alias="XCN.10",
        title="name type",
    )

    xcn_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_11",
            "identifier_check_digit",
            "XCN.11",
        ),
        serialization_alias="XCN.11",
        title="identifier check digit",
    )

    xcn_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_12",
            "code_identifying_the_check_digit_scheme_employed",
            "XCN.12",
        ),
        serialization_alias="XCN.12",
        title="code identifying the check digit scheme employed",
    )

    xcn_13: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_13",
            "identifier_type_code",
            "XCN.13",
        ),
        serialization_alias="XCN.13",
        title="identifier type code",
    )

    xcn_14: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_14",
            "assigning_facility_id",
            "XCN.14",
        ),
        serialization_alias="XCN.14",
        title="assigning facility ID",
    )

    model_config = {"populate_by_name": True}
