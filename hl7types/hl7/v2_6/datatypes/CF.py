"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: CF
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .FT import FT


class CF(HL7Model):
    """HL7 v2 CF data type.

    Attributes
    ----------
    cf_1 : str | None
        CF.1 (opt) - Identifier (ST)

    cf_2 : FT | None
        CF.2 (opt) - Formatted Text (FT)

    cf_3 : str | None
        CF.3 (opt) - Name of Coding System (ID)

    cf_4 : str | None
        CF.4 (opt) - Alternate Identifier (ST)

    cf_5 : FT | None
        CF.5 (opt) - Alternate Formatted Text (FT)

    cf_6 : str | None
        CF.6 (opt) - Name of Alternate Coding System (ID)
    """

    cf_1: Optional[str] = Field(
        default=None,
        max_length=20,
        validation_alias=AliasChoices(
            "cf_1",
            "identifier",
            "CF.1",
        ),
        serialization_alias="CF.1",
        title="Identifier",
    )

    cf_2: Optional[FT] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_2",
            "formatted_text",
            "CF.2",
        ),
        serialization_alias="CF.2",
        title="Formatted Text",
    )

    cf_3: Optional[str] = Field(
        default=None,
        max_length=20,
        validation_alias=AliasChoices(
            "cf_3",
            "name_of_coding_system",
            "CF.3",
        ),
        serialization_alias="CF.3",
        title="Name of Coding System",
    )

    cf_4: Optional[str] = Field(
        default=None,
        max_length=20,
        validation_alias=AliasChoices(
            "cf_4",
            "alternate_identifier",
            "CF.4",
        ),
        serialization_alias="CF.4",
        title="Alternate Identifier",
    )

    cf_5: Optional[FT] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_5",
            "alternate_formatted_text",
            "CF.5",
        ),
        serialization_alias="CF.5",
        title="Alternate Formatted Text",
    )

    cf_6: Optional[str] = Field(
        default=None,
        max_length=20,
        validation_alias=AliasChoices(
            "cf_6",
            "name_of_alternate_coding_system",
            "CF.6",
        ),
        serialization_alias="CF.6",
        title="Name of Alternate Coding System",
    )

    model_config = {"populate_by_name": True}
