"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MA
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class MA(HL7Model):
    """HL7 v2 MA data type.

    Attributes
    ----------
    ma_1 : str | None
        MA.1 (opt) - sample 1 from channel 1 (NM)

    ma_2 : str | None
        MA.2 (opt) - sample 1 from channel 2 (NM)

    ma_3 : str | None
        MA.3 (opt) - sample 1 from channel 3 (NM)

    ma_4 : str | None
        MA.4 (opt) - sample 2 from channel 1 (NM)

    ma_5 : str | None
        MA.5 (opt) - sample 2 from channel 2 (NM)

    ma_6 : str | None
        MA.6 (opt) - sample 2 from channel 3 (NM)
    """

    ma_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ma_1",
            "sample_1_from_channel_1",
            "MA.1",
        ),
        serialization_alias="MA.1",
        title="sample 1 from channel 1",
    )

    ma_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ma_2",
            "sample_1_from_channel_2",
            "MA.2",
        ),
        serialization_alias="MA.2",
        title="sample 1 from channel 2",
    )

    ma_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ma_3",
            "sample_1_from_channel_3",
            "MA.3",
        ),
        serialization_alias="MA.3",
        title="sample 1 from channel 3",
    )

    ma_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ma_4",
            "sample_2_from_channel_1",
            "MA.4",
        ),
        serialization_alias="MA.4",
        title="sample 2 from channel 1",
    )

    ma_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ma_5",
            "sample_2_from_channel_2",
            "MA.5",
        ),
        serialization_alias="MA.5",
        title="sample 2 from channel 2",
    )

    ma_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ma_6",
            "sample_2_from_channel_3",
            "MA.6",
        ),
        serialization_alias="MA.6",
        title="sample 2 from channel 3",
    )

    @field_validator("ma_1", "ma_2", "ma_3", "ma_4", "ma_5", "ma_6", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
