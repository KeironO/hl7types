"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: XCN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .FN import FN
from .HD import HD


class XCN(HL7Model):
    """HL7 v2 XCN data type.

    Attributes
    ----------
    xcn_1 : str | None
        XCN.1 (opt) - ID number (ST) (ST)

    xcn_2 : FN | None
        XCN.2 (opt) - family+last name (FN)

    xcn_3 : str | None
        XCN.3 (opt) - given name (ST)

    xcn_4 : str | None
        XCN.4 (opt) - middle initial or name (ST)

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
        XCN.13 (opt) - identifier type code (IS)

    xcn_14 : HD | None
        XCN.14 (opt) - assigning facility (HD)

    xcn_15 : str | None
        XCN.15 (opt) - Name Representation code (ID)
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
            "family_last_name",
            "XCN.2",
        ),
        serialization_alias="XCN.2",
        title="family+last name",
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
            "middle_initial_or_name",
            "XCN.4",
        ),
        serialization_alias="XCN.4",
        title="middle initial or name",
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
            "identifier_type_code",
            "XCN.13",
        ),
        serialization_alias="XCN.13",
        title="identifier type code",
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

    model_config = {"populate_by_name": True}
