"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: AL1
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class AL1(BaseModel):
    """HL7 v2 AL1 segment."""

    al1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "al1_1",
            "set_id_al1",
            "AL1.1",
        ),
        serialization_alias="AL1.1",
        title="Set ID - AL1",
        description="Item #203",
    )

    al1_2: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_2",
            "allergen_type_code",
            "AL1.2",
        ),
        serialization_alias="AL1.2",
        title="Allergen Type Code",
        description="Item #204 | Table HL70127",
    )

    al1_3: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "al1_3",
            "allergen_code_mnemonic_description",
            "AL1.3",
        ),
        serialization_alias="AL1.3",
        title="Allergen Code/Mnemonic/Description",
        description="Item #205",
    )

    al1_4: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_4",
            "allergy_severity_code",
            "AL1.4",
        ),
        serialization_alias="AL1.4",
        title="Allergy Severity Code",
        description="Item #206 | Table HL70128",
    )

    al1_5: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_5",
            "allergy_reaction_code",
            "AL1.5",
        ),
        serialization_alias="AL1.5",
        title="Allergy Reaction Code",
        description="Item #207",
    )

    al1_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_6",
            "identification_date",
            "AL1.6",
        ),
        serialization_alias="AL1.6",
        title="Identification Date",
        description="Item #208",
    )

    model_config = {"populate_by_name": True}
