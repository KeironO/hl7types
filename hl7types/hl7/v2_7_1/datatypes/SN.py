"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: SN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class SN(HL7Model):
    """HL7 v2 SN data type.

    Attributes
    ----------
    sn_1 : str | None
        SN.1 (opt) - Comparator (ST)

    sn_2 : str | None
        SN.2 (opt) - Num1 (NM)

    sn_3 : str | None
        SN.3 (opt) - Separator/Suffix (ST)

    sn_4 : str | None
        SN.4 (opt) - Num2 (NM)
    """

    sn_1: Optional[str] = Field(
        default=None,
        max_length=2,
        validation_alias=AliasChoices(
            "sn_1",
            "comparator",
            "SN.1",
        ),
        serialization_alias="SN.1",
        title="Comparator",
    )

    sn_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sn_2",
            "num1",
            "SN.2",
        ),
        serialization_alias="SN.2",
        title="Num1",
    )

    sn_3: Optional[str] = Field(
        default=None,
        max_length=1,
        validation_alias=AliasChoices(
            "sn_3",
            "separator_suffix",
            "SN.3",
        ),
        serialization_alias="SN.3",
        title="Separator/Suffix",
    )

    sn_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sn_4",
            "num2",
            "SN.4",
        ),
        serialization_alias="SN.4",
        title="Num2",
    )

    @field_validator("sn_2", "sn_4", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
