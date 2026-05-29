"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: CNE
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CNE(BaseModel):
    """HL7 v2 CNE data type.

    Attributes
    ----------
    cne_1 : str | None
        CNE.1 (opt) - identifier (ST)

    cne_2 : str | None
        CNE.2 (opt) - text (ST)

    cne_3 : str | None
        CNE.3 (opt) - name of coding system (ST)

    cne_4 : str | None
        CNE.4 (opt) - alternate identifier (ST)

    cne_5 : str | None
        CNE.5 (opt) - alternate text (ST)

    cne_6 : str | None
        CNE.6 (opt) - name of alternate coding system (ST)

    cne_7 : str | None
        CNE.7 (opt) - coding system version ID (ST)

    cne_8 : str | None
        CNE.8 (opt) - alternate coding system version ID (ST)

    cne_9 : str | None
        CNE.9 (opt) - original text (ST)
    """

    cne_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_1",
            "identifier",
            "CNE.1",
        ),
        serialization_alias="CNE.1",
        title="identifier",
    )

    cne_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_2",
            "text",
            "CNE.2",
        ),
        serialization_alias="CNE.2",
        title="text",
    )

    cne_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_3",
            "name_of_coding_system",
            "CNE.3",
        ),
        serialization_alias="CNE.3",
        title="name of coding system",
    )

    cne_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_4",
            "alternate_identifier",
            "CNE.4",
        ),
        serialization_alias="CNE.4",
        title="alternate identifier",
    )

    cne_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_5",
            "alternate_text",
            "CNE.5",
        ),
        serialization_alias="CNE.5",
        title="alternate text",
    )

    cne_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_6",
            "name_of_alternate_coding_system",
            "CNE.6",
        ),
        serialization_alias="CNE.6",
        title="name of alternate coding system",
    )

    cne_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_7",
            "coding_system_version_id",
            "CNE.7",
        ),
        serialization_alias="CNE.7",
        title="coding system version ID",
    )

    cne_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_8",
            "alternate_coding_system_version_id",
            "CNE.8",
        ),
        serialization_alias="CNE.8",
        title="alternate coding system version ID",
    )

    cne_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_9",
            "original_text",
            "CNE.9",
        ),
        serialization_alias="CNE.9",
        title="original text",
    )

    model_config = {"populate_by_name": True}
