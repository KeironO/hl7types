"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: SAD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class SAD(HL7Model):
    """HL7 v2 SAD data type.

    Attributes
    ----------
    sad_1 : str | None
        SAD.1 (opt) - Street or Mailing Address (ST)

    sad_2 : str | None
        SAD.2 (opt) - Street Name (ST)

    sad_3 : str | None
        SAD.3 (opt) - Dwelling Number (ST)
    """

    sad_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sad_1",
            "street_or_mailing_address",
            "SAD.1",
        ),
        serialization_alias="SAD.1",
        title="Street or Mailing Address",
    )

    sad_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sad_2",
            "street_name",
            "SAD.2",
        ),
        serialization_alias="SAD.2",
        title="Street Name",
    )

    sad_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sad_3",
            "dwelling_number",
            "SAD.3",
        ),
        serialization_alias="SAD.3",
        title="Dwelling Number",
    )

    model_config = {"populate_by_name": True}
