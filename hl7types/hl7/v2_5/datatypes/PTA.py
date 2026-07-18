"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PTA
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from .MOP import MOP

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class PTA(HL7Model):
    """Policy type and amount (S2.A.58).

    Attributes
    ----------
    pta_1 : str | None
        PTA.1 (opt) - Policy Type (IS)

    pta_2 : str | None
        PTA.2 (opt) - Amount Class (IS)

    pta_3 : str | None
        PTA.3 (opt) - Money or Percentage Quantity (NM)

    pta_4 : MOP | None
        PTA.4 (opt) - Money or Percentage (MOP)
    """

    pta_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pta_1",
            "policy_type",
            "PTA.1",
        ),
        serialization_alias="PTA.1",
        title="Policy Type",
    )

    pta_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pta_2",
            "amount_class",
            "PTA.2",
        ),
        serialization_alias="PTA.2",
        title="Amount Class",
    )

    pta_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pta_3",
            "money_or_percentage_quantity",
            "PTA.3",
        ),
        serialization_alias="PTA.3",
        title="Money or Percentage Quantity",
    )

    pta_4: Optional[MOP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pta_4",
            "money_or_percentage",
            "PTA.4",
        ),
        serialization_alias="PTA.4",
        title="Money or Percentage",
    )

    @field_validator("pta_3", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
