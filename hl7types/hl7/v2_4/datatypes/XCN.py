"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: XCN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CE import CE
from .DR import DR
from .FN import FN
from .HD import HD


class XCN(BaseModel):
    """HL7 v2 XCN data type.

    Attributes
    ----------
    xcn_1 : str | None
        XCN.1 (opt) - ID number (ST) (ST)

    xcn_2 : FN | None
        XCN.2 (opt) - family name (FN)

    xcn_3 : str | None
        XCN.3 (opt) - given name (ST)

    xcn_4 : str | None
        XCN.4 (opt) - second and further given names or initials thereof (ST)

    xcn_5 : str | None
        XCN.5 (opt) - suffix (e.g., JR or III) (ST)

    xcn_6 : str | None
        XCN.6 (opt) - prefix (e.g., DR) (ST)

    xcn_7 : str | None
        XCN.7 (opt) - degree (e.g., MD) (IS)

    xcn_8 : str | None
        XCN.8 (opt) - source table (IS)

    xcn_9 : HD | None
        XCN.9 (opt) - assigning authority (HD)

    xcn_10 : str | None
        XCN.10 (opt) - name type code (ID)

    xcn_11 : str | None
        XCN.11 (opt) - identifier check digit (ST)

    xcn_12 : str | None
        XCN.12 (opt) - code identifying the check digit scheme employed (ID)

    xcn_13 : str | None
        XCN.13 (opt) - identifier type code (IS) (IS)

    xcn_14 : HD | None
        XCN.14 (opt) - assigning facility (HD)

    xcn_15 : str | None
        XCN.15 (opt) - Name Representation code (ID)

    xcn_16 : CE | None
        XCN.16 (opt) - name context (CE)

    xcn_17 : DR | None
        XCN.17 (opt) - name validity range (DR)

    xcn_18 : str | None
        XCN.18 (opt) - name assembly order (ID)
    """

    xcn_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_1",
            "id_number_st",
            "XCN.1",
        ),
        serialization_alias="XCN.1",
        title="ID number (ST)",
    )

    xcn_2: Optional[FN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_2",
            "family_name",
            "XCN.2",
        ),
        serialization_alias="XCN.2",
        title="family name",
    )

    xcn_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_3",
            "given_name",
            "XCN.3",
        ),
        serialization_alias="XCN.3",
        title="given name",
    )

    xcn_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_4",
            "second_and_further_given_names_or_initials_thereof",
            "XCN.4",
        ),
        serialization_alias="XCN.4",
        title="second and further given names or initials thereof",
    )

    xcn_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_5",
            "suffix_e_g_jr_or_iii",
            "XCN.5",
        ),
        serialization_alias="XCN.5",
        title="suffix (e.g., JR or III)",
    )

    xcn_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_6",
            "prefix_e_g_dr",
            "XCN.6",
        ),
        serialization_alias="XCN.6",
        title="prefix (e.g., DR)",
    )

    xcn_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_7",
            "degree_e_g_md",
            "XCN.7",
        ),
        serialization_alias="XCN.7",
        title="degree (e.g., MD)",
    )

    xcn_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_8",
            "source_table",
            "XCN.8",
        ),
        serialization_alias="XCN.8",
        title="source table",
    )

    xcn_9: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_9",
            "assigning_authority",
            "XCN.9",
        ),
        serialization_alias="XCN.9",
        title="assigning authority",
    )

    xcn_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_10",
            "name_type_code",
            "XCN.10",
        ),
        serialization_alias="XCN.10",
        title="name type code",
    )

    xcn_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_11",
            "identifier_check_digit",
            "XCN.11",
        ),
        serialization_alias="XCN.11",
        title="identifier check digit",
    )

    xcn_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_12",
            "code_identifying_the_check_digit_scheme_employed",
            "XCN.12",
        ),
        serialization_alias="XCN.12",
        title="code identifying the check digit scheme employed",
    )

    xcn_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_13",
            "identifier_type_code_is",
            "XCN.13",
        ),
        serialization_alias="XCN.13",
        title="identifier type code (IS)",
    )

    xcn_14: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_14",
            "assigning_facility",
            "XCN.14",
        ),
        serialization_alias="XCN.14",
        title="assigning facility",
    )

    xcn_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_15",
            "name_representation_code",
            "XCN.15",
        ),
        serialization_alias="XCN.15",
        title="Name Representation code",
    )

    xcn_16: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_16",
            "name_context",
            "XCN.16",
        ),
        serialization_alias="XCN.16",
        title="name context",
    )

    xcn_17: Optional[DR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_17",
            "name_validity_range",
            "XCN.17",
        ),
        serialization_alias="XCN.17",
        title="name validity range",
    )

    xcn_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_18",
            "name_assembly_order",
            "XCN.18",
        ),
        serialization_alias="XCN.18",
        title="name assembly order",
    )

    model_config = {"populate_by_name": True}
