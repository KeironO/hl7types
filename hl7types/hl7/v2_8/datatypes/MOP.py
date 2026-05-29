"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: MOP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class MOP(BaseModel):
    """HL7 v2 MOP data type.

    Attributes
    ----------
    mop_1 : str
        MOP.1 (req) - Money or Percentage Indicator (ID)

    mop_2 : str
        MOP.2 (req) - Money or Percentage Quantity (NM)

    mop_3 : str | None
        MOP.3 (opt) - Monetary  Denomination (ID)
    """

    mop_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "mop_1",
            "money_or_percentage_indicator",
            "MOP.1",
        ),
        serialization_alias="MOP.1",
        title="Money or Percentage Indicator",
    )

    mop_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "mop_2",
            "money_or_percentage_quantity",
            "MOP.2",
        ),
        serialization_alias="MOP.2",
        title="Money or Percentage Quantity",
    )

    mop_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mop_3",
            "monetary_denomination",
            "MOP.3",
        ),
        serialization_alias="MOP.3",
        title="Monetary  Denomination",
    )

    model_config = {"populate_by_name": True}
