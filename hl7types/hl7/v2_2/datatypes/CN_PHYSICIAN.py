"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CN_PHYSICIAN
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .AD import AD


class CN_PHYSICIAN(BaseModel):
    """HL7 v2 CN_PHYSICIAN data type."""

    cn_physician_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_physician_1",
            "physician_id",
            "CN_PHYSICIAN.1",
        ),
        serialization_alias="CN_PHYSICIAN.1",
        title="physician ID",
    )

    cn_physician_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_physician_2",
            "familiy_name",
            "CN_PHYSICIAN.2",
        ),
        serialization_alias="CN_PHYSICIAN.2",
        title="familiy name",
    )

    cn_physician_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_physician_3",
            "given_name",
            "CN_PHYSICIAN.3",
        ),
        serialization_alias="CN_PHYSICIAN.3",
        title="given name",
    )

    cn_physician_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_physician_4",
            "middle_initial_or_name",
            "CN_PHYSICIAN.4",
        ),
        serialization_alias="CN_PHYSICIAN.4",
        title="middle initial or name",
    )

    cn_physician_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_physician_5",
            "suffix_e_g_jr_or_iii",
            "CN_PHYSICIAN.5",
        ),
        serialization_alias="CN_PHYSICIAN.5",
        title="suffix (e.g. JR or III)",
    )

    cn_physician_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_physician_6",
            "prefix_e_g_dr",
            "CN_PHYSICIAN.6",
        ),
        serialization_alias="CN_PHYSICIAN.6",
        title="prefix (e.g. DR)",
    )

    cn_physician_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_physician_7",
            "degree_e_g_md",
            "CN_PHYSICIAN.7",
        ),
        serialization_alias="CN_PHYSICIAN.7",
        title="degree (e.g. MD)",
    )

    cn_physician_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_physician_8",
            "source_table_id",
            "CN_PHYSICIAN.8",
        ),
        serialization_alias="CN_PHYSICIAN.8",
        title="source table id",
    )

    cn_physician_9: AD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_physician_9",
            "adresse",
            "CN_PHYSICIAN.9",
        ),
        serialization_alias="CN_PHYSICIAN.9",
        title="Adresse",
    )

    cn_physician_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_physician_10",
            "telefon",
            "CN_PHYSICIAN.10",
        ),
        serialization_alias="CN_PHYSICIAN.10",
        title="Telefon",
    )

    cn_physician_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_physician_11",
            "faxnummer",
            "CN_PHYSICIAN.11",
        ),
        serialization_alias="CN_PHYSICIAN.11",
        title="Faxnummer",
    )

    cn_physician_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_physician_12",
            "online_nummer",
            "CN_PHYSICIAN.12",
        ),
        serialization_alias="CN_PHYSICIAN.12",
        title="Online-Nummer",
    )

    cn_physician_13: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_physician_13",
            "e_mail",
            "CN_PHYSICIAN.13",
        ),
        serialization_alias="CN_PHYSICIAN.13",
        title="E-Mail",
    )

    model_config = {"populate_by_name": True}
