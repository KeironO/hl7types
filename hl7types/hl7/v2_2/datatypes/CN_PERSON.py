"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CN_PERSON
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CN_PERSON(BaseModel):
    """HL7 v2 CN_PERSON data type.

    Attributes
    ----------
    cn_person_1 : str | None
        CN_PERSON.1 (opt) - ID number (ID)

    cn_person_2 : str | None
        CN_PERSON.2 (opt) - familiy name (ST)

    cn_person_3 : str | None
        CN_PERSON.3 (opt) - given name (ST)

    cn_person_4 : str | None
        CN_PERSON.4 (opt) - middle initial or name (ST)

    cn_person_5 : str | None
        CN_PERSON.5 (opt) - suffix (e.g. JR or III) (ST)

    cn_person_6 : str | None
        CN_PERSON.6 (opt) - prefix (e.g. DR) (ST)

    cn_person_7 : str | None
        CN_PERSON.7 (opt) - degree (e.g. MD) (ST)

    cn_person_8 : str | None
        CN_PERSON.8 (opt) - source table id (ID)
    """

    cn_person_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_person_1",
            "id_number",
            "CN_PERSON.1",
        ),
        serialization_alias="CN_PERSON.1",
        title="ID number",
    )

    cn_person_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_person_2",
            "familiy_name",
            "CN_PERSON.2",
        ),
        serialization_alias="CN_PERSON.2",
        title="familiy name",
    )

    cn_person_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_person_3",
            "given_name",
            "CN_PERSON.3",
        ),
        serialization_alias="CN_PERSON.3",
        title="given name",
    )

    cn_person_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_person_4",
            "middle_initial_or_name",
            "CN_PERSON.4",
        ),
        serialization_alias="CN_PERSON.4",
        title="middle initial or name",
    )

    cn_person_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_person_5",
            "suffix_e_g_jr_or_iii",
            "CN_PERSON.5",
        ),
        serialization_alias="CN_PERSON.5",
        title="suffix (e.g. JR or III)",
    )

    cn_person_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_person_6",
            "prefix_e_g_dr",
            "CN_PERSON.6",
        ),
        serialization_alias="CN_PERSON.6",
        title="prefix (e.g. DR)",
    )

    cn_person_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_person_7",
            "degree_e_g_md",
            "CN_PERSON.7",
        ),
        serialization_alias="CN_PERSON.7",
        title="degree (e.g. MD)",
    )

    cn_person_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_person_8",
            "source_table_id",
            "CN_PERSON.8",
        ),
        serialization_alias="CN_PERSON.8",
        title="source table id",
    )

    model_config = {"populate_by_name": True}
