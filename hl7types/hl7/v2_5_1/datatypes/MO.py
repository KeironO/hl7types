"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MO
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class MO(HL7Model):
    """Money (S2.A.1.41).

    Attributes
    ----------
    mo_1 : str | None
        MO.1 (opt) - Quantity (NM)

    mo_2 : str | None
        MO.2 (opt) - Denomination (ID)
    """

    mo_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mo_1",
            "quantity",
            "MO.1",
        ),
        serialization_alias="MO.1",
        title="Quantity",
    )

    mo_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mo_2",
            "denomination",
            "MO.2",
        ),
        serialization_alias="MO.2",
        title="Denomination",
    )

    @field_validator("mo_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
