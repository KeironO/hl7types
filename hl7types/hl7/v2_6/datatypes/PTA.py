"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PTA
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from .MOP import MOP


class PTA(HL7Model):
    """HL7 v2 PTA data type.

    Attributes
    ----------
    pta_1 : str
        PTA.1 (req) - Policy Type (IS)

    pta_2 : str | None
        PTA.2 (opt) - Amount Class (IS)

    pta_3 : str | None
        PTA.3 (opt) - Money or Percentage Quantity (NM)

    pta_4 : MOP
        PTA.4 (req) - Money or Percentage (MOP)
    """

    pta_1: str = Field(
        default=...,
        max_length=5,
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
        max_length=9,
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
        max_length=16,
        validation_alias=AliasChoices(
            "pta_3",
            "money_or_percentage_quantity",
            "PTA.3",
        ),
        serialization_alias="PTA.3",
        title="Money or Percentage Quantity",
    )

    pta_4: MOP = Field(
        default=...,
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
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
