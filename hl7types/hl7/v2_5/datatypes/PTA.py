"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PTA
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .MOP import MOP


class PTA(BaseModel):
    """HL7 v2 PTA data type."""

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

    model_config = {"populate_by_name": True}
