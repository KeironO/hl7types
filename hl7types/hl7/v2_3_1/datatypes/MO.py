"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MO
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class MO(HL7Model):
    """HL7 v2 MO data type.

    Attributes
    ----------
    mo_1 : str | None
        MO.1 (opt) - quantity (NM)

    mo_2 : str | None
        MO.2 (opt) - denomination (ID)
    """

    mo_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mo_1",
            "quantity",
            "MO.1",
        ),
        serialization_alias="MO.1",
        title="quantity",
    )

    mo_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mo_2",
            "denomination",
            "MO.2",
        ),
        serialization_alias="MO.2",
        title="denomination",
    )

    @field_validator("mo_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
