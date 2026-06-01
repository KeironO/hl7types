"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: VH
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class VH(HL7Model):
    """HL7 v2 VH data type.

    Attributes
    ----------
    vh_1 : str | None
        VH.1 (opt) - start day range (ID)

    vh_2 : str | None
        VH.2 (opt) - end day range (ID)

    vh_3 : str | None
        VH.3 (opt) - start hour range (TM)

    vh_4 : str | None
        VH.4 (opt) - end hour range (TM)
    """

    vh_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vh_1",
            "start_day_range",
            "VH.1",
        ),
        serialization_alias="VH.1",
        title="start day range",
    )

    vh_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vh_2",
            "end_day_range",
            "VH.2",
        ),
        serialization_alias="VH.2",
        title="end day range",
    )

    vh_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vh_3",
            "start_hour_range",
            "VH.3",
        ),
        serialization_alias="VH.3",
        title="start hour range",
    )

    vh_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vh_4",
            "end_hour_range",
            "VH.4",
        ),
        serialization_alias="VH.4",
        title="end hour range",
    )

    @field_validator("vh_3", "vh_4", mode='before')
    @classmethod
    def _validate_tm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 time")
        return v

    model_config = {"populate_by_name": True}
