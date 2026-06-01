"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: MA
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class MA(HL7Model):
    """HL7 v2 MA data type.

    Attributes
    ----------
    ma_1 : str | None
        MA.1 (opt) - Sample Y From Channel 1 (NM)

    ma_2 : str | None
        MA.2 (opt) - Sample Y From Channel 2 (NM)

    ma_3 : str | None
        MA.3 (opt) - Sample Y From Channel 3 (NM)

    ma_4 : str | None
        MA.4 (opt) - Sample Y From Channel 4 (NM)
    """

    ma_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ma_1",
            "sample_y_from_channel_1",
            "MA.1",
        ),
        serialization_alias="MA.1",
        title="Sample Y From Channel 1",
    )

    ma_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ma_2",
            "sample_y_from_channel_2",
            "MA.2",
        ),
        serialization_alias="MA.2",
        title="Sample Y From Channel 2",
    )

    ma_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ma_3",
            "sample_y_from_channel_3",
            "MA.3",
        ),
        serialization_alias="MA.3",
        title="Sample Y From Channel 3",
    )

    ma_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ma_4",
            "sample_y_from_channel_4",
            "MA.4",
        ),
        serialization_alias="MA.4",
        title="Sample Y From Channel 4",
    )

    @field_validator("ma_1", "ma_2", "ma_3", "ma_4", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
