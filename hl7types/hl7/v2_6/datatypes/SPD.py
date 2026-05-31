"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: SPD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class SPD(HL7Model):
    """HL7 v2 SPD data type.

    Attributes
    ----------
    spd_1 : str
        SPD.1 (req) - Specialty Name (ST)

    spd_2 : str | None
        SPD.2 (opt) - Governing Board (ST)

    spd_3 : str | None
        SPD.3 (opt) - Eligible or Certified (ID)

    spd_4 : str | None
        SPD.4 (opt) - Date of Certification (DT)
    """

    spd_1: str = Field(
        default=...,
        max_length=50,
        validation_alias=AliasChoices(
            "spd_1",
            "specialty_name",
            "SPD.1",
        ),
        serialization_alias="SPD.1",
        title="Specialty Name",
    )

    spd_2: Optional[str] = Field(
        default=None,
        max_length=50,
        validation_alias=AliasChoices(
            "spd_2",
            "governing_board",
            "SPD.2",
        ),
        serialization_alias="SPD.2",
        title="Governing Board",
    )

    spd_3: Optional[str] = Field(
        default=None,
        max_length=1,
        validation_alias=AliasChoices(
            "spd_3",
            "eligible_or_certified",
            "SPD.3",
        ),
        serialization_alias="SPD.3",
        title="Eligible or Certified",
    )

    spd_4: Optional[str] = Field(
        default=None,
        max_length=8,
        validation_alias=AliasChoices(
            "spd_4",
            "date_of_certification",
            "SPD.4",
        ),
        serialization_alias="SPD.4",
        title="Date of Certification",
    )

    model_config = {"populate_by_name": True}
