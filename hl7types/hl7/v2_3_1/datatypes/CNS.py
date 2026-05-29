"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: CNS
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CNS(BaseModel):
    """HL7 v2 CNS data type.

    Attributes
    ----------
    cns_1 : str | None
        CNS.1 (opt) - ID number (ST) (ST)

    cns_2 : str | None
        CNS.2 (opt) - family name (ST)

    cns_3 : str | None
        CNS.3 (opt) - given name (ST)

    cns_4 : str | None
        CNS.4 (opt) - second and further given names or initials thereof (ST)

    cns_5 : str | None
        CNS.5 (opt) - suffix (e.g., JR or III) (ST)

    cns_6 : str | None
        CNS.6 (opt) - prefix (e.g., DR) (ST)

    cns_7 : str | None
        CNS.7 (opt) - degree (e.g., MD) (IS)

    cns_8 : str | None
        CNS.8 (opt) - source table (IS)

    cns_9 : str | None
        CNS.9 (opt) - assigning authority namespace ID (IS)

    cns_10 : str | None
        CNS.10 (opt) - assigning authority universal ID (ST)

    cns_11 : str | None
        CNS.11 (opt) - assigning authority universal ID type (ID)
    """

    cns_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_1",
            "id_number_st",
            "CNS.1",
        ),
        serialization_alias="CNS.1",
        title="ID number (ST)",
    )

    cns_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_2",
            "family_name",
            "CNS.2",
        ),
        serialization_alias="CNS.2",
        title="family name",
    )

    cns_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_3",
            "given_name",
            "CNS.3",
        ),
        serialization_alias="CNS.3",
        title="given name",
    )

    cns_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_4",
            "second_and_further_given_names_or_initials_thereof",
            "CNS.4",
        ),
        serialization_alias="CNS.4",
        title="second and further given names or initials thereof",
    )

    cns_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_5",
            "suffix_e_g_jr_or_iii",
            "CNS.5",
        ),
        serialization_alias="CNS.5",
        title="suffix (e.g., JR or III)",
    )

    cns_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_6",
            "prefix_e_g_dr",
            "CNS.6",
        ),
        serialization_alias="CNS.6",
        title="prefix (e.g., DR)",
    )

    cns_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_7",
            "degree_e_g_md",
            "CNS.7",
        ),
        serialization_alias="CNS.7",
        title="degree (e.g., MD)",
    )

    cns_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_8",
            "source_table",
            "CNS.8",
        ),
        serialization_alias="CNS.8",
        title="source table",
    )

    cns_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_9",
            "assigning_authority_namespace_id",
            "CNS.9",
        ),
        serialization_alias="CNS.9",
        title="assigning authority namespace ID",
    )

    cns_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_10",
            "assigning_authority_universal_id",
            "CNS.10",
        ),
        serialization_alias="CNS.10",
        title="assigning authority universal ID",
    )

    cns_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_11",
            "assigning_authority_universal_id_type",
            "CNS.11",
        ),
        serialization_alias="CNS.11",
        title="assigning authority universal ID type",
    )

    model_config = {"populate_by_name": True}
