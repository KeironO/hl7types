"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MOP
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class MOP(HL7Model):
    """Money or percentage.

    Attributes
    ----------
    mop_1 : str | None
        MOP.1 (opt) - money or percentage indicator (IS)

    mop_2 : str | None
        MOP.2 (opt) - money or percentage quantity (NM)
    """

    mop_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mop_1",
            "money_or_percentage_indicator",
            "MOP.1",
        ),
        serialization_alias="MOP.1",
        title="money or percentage indicator",
    )

    mop_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mop_2",
            "money_or_percentage_quantity",
            "MOP.2",
        ),
        serialization_alias="MOP.2",
        title="money or percentage quantity",
    )

    @field_validator("mop_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
