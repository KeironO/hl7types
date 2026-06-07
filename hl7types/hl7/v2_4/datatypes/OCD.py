"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OCD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
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

    @field_validator("ocd_2", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
