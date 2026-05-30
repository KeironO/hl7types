"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OCD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class OCD(HL7Model):
    """HL7 v2 OCD data type.

    Attributes
    ----------
    ocd_1 : str | None
        OCD.1 (opt) - occurrence code (IS)

    ocd_2 : str | None
        OCD.2 (opt) - occurrence date (DT)
    """

    ocd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ocd_1",
            "occurrence_code",
            "OCD.1",
        ),
        serialization_alias="OCD.1",
        title="occurrence code",
    )

    ocd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ocd_2",
            "occurrence_date",
            "OCD.2",
        ),
        serialization_alias="OCD.2",
        title="occurrence date",
    )

    model_config = {"populate_by_name": True}
