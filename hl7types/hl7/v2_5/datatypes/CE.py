"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: CE
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class CE(HL7Model):
    """HL7 v2 CE data type.

    Attributes
    ----------
    ce_1 : str | None
        CE.1 (opt) - Identifier (ST)

    ce_2 : str | None
        CE.2 (opt) - Text (ST)

    ce_3 : str | None
        CE.3 (opt) - Name of Coding System (ID)

    ce_4 : str | None
        CE.4 (opt) - Alternate Identifier (ST)

    ce_5 : str | None
        CE.5 (opt) - Alternate Text (ST)

    ce_6 : str | None
        CE.6 (opt) - Name of Alternate Coding System (ID)
    """

    ce_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ce_1",
            "identifier",
            "CE.1",
        ),
        serialization_alias="CE.1",
        title="Identifier",
    )

    ce_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ce_2",
            "text",
            "CE.2",
        ),
        serialization_alias="CE.2",
        title="Text",
    )

    ce_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ce_3",
            "name_of_coding_system",
            "CE.3",
        ),
        serialization_alias="CE.3",
        title="Name of Coding System",
    )

    ce_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ce_4",
            "alternate_identifier",
            "CE.4",
        ),
        serialization_alias="CE.4",
        title="Alternate Identifier",
    )

    ce_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ce_5",
            "alternate_text",
            "CE.5",
        ),
        serialization_alias="CE.5",
        title="Alternate Text",
    )

    ce_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ce_6",
            "name_of_alternate_coding_system",
            "CE.6",
        ),
        serialization_alias="CE.6",
        title="Name of Alternate Coding System",
    )

    model_config = {"populate_by_name": True}
