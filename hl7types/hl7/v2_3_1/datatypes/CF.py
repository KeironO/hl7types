"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: CF
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class CF(HL7Model):
    """HL7 v2 CF data type.

    Attributes
    ----------
    cf_1 : str | None
        CF.1 (opt) - identifier (ST)

    cf_2 : str | None
        CF.2 (opt) - formatted text (FT)

    cf_3 : str | None
        CF.3 (opt) - name of coding system (ST)

    cf_4 : str | None
        CF.4 (opt) - alternate identifier (ST)

    cf_5 : str | None
        CF.5 (opt) - alternate formatted text (FT)

    cf_6 : str | None
        CF.6 (opt) - name of alternate coding system (ST)
    """

    cf_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_1",
            "identifier",
            "CF.1",
        ),
        serialization_alias="CF.1",
        title="identifier",
    )

    cf_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_2",
            "formatted_text",
            "CF.2",
        ),
        serialization_alias="CF.2",
        title="formatted text",
    )

    cf_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_3",
            "name_of_coding_system",
            "CF.3",
        ),
        serialization_alias="CF.3",
        title="name of coding system",
    )

    cf_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_4",
            "alternate_identifier",
            "CF.4",
        ),
        serialization_alias="CF.4",
        title="alternate identifier",
    )

    cf_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_5",
            "alternate_formatted_text",
            "CF.5",
        ),
        serialization_alias="CF.5",
        title="alternate formatted text",
    )

    cf_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_6",
            "name_of_alternate_coding_system",
            "CF.6",
        ),
        serialization_alias="CF.6",
        title="name of alternate coding system",
    )

    model_config = {"populate_by_name": True}
