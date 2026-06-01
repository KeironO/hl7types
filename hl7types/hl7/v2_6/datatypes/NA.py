"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: NA
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class NA(HL7Model):
    """HL7 v2 NA data type.

    Attributes
    ----------
    na_1 : str
        NA.1 (req) - Value1 (NM)

    na_2 : str | None
        NA.2 (opt) - Value2 (NM)

    na_3 : str | None
        NA.3 (opt) - Value3 (NM)

    na_4 : str | None
        NA.4 (opt) - Value4 (NM)
    """

    na_1: str = Field(
        default=...,
        max_length=16,
        validation_alias=AliasChoices(
            "na_1",
            "value1",
            "NA.1",
        ),
        serialization_alias="NA.1",
        title="Value1",
    )

    na_2: Optional[str] = Field(
        default=None,
        max_length=16,
        validation_alias=AliasChoices(
            "na_2",
            "value2",
            "NA.2",
        ),
        serialization_alias="NA.2",
        title="Value2",
    )

    na_3: Optional[str] = Field(
        default=None,
        max_length=16,
        validation_alias=AliasChoices(
            "na_3",
            "value3",
            "NA.3",
        ),
        serialization_alias="NA.3",
        title="Value3",
    )

    na_4: Optional[str] = Field(
        default=None,
        max_length=16,
        validation_alias=AliasChoices(
            "na_4",
            "value4",
            "NA.4",
        ),
        serialization_alias="NA.4",
        title="Value4",
    )

    @field_validator("na_1", "na_2", "na_3", "na_4", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
