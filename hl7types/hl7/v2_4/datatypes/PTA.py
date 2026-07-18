"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PTA
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class PTA(HL7Model):
    """Policy type (S6.4.7.29).

    Attributes
    ----------
    pta_1 : str | None
        PTA.1 (opt) - policy type (IS)

    pta_2 : str | None
        PTA.2 (opt) - amount class (IS)

    pta_3 : str | None
        PTA.3 (opt) - amount (NM)
    """

    pta_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pta_1",
            "policy_type",
            "PTA.1",
        ),
        serialization_alias="PTA.1",
        title="policy type",
    )

    pta_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pta_2",
            "amount_class",
            "PTA.2",
        ),
        serialization_alias="PTA.2",
        title="amount class",
    )

    pta_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pta_3",
            "amount",
            "PTA.3",
        ),
        serialization_alias="PTA.3",
        title="amount",
    )

    @field_validator("pta_3", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
