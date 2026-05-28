"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PTA
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE
from .MOP import MOP


class PTA(BaseModel):
    """HL7 v2 PTA data type."""

    pta_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "pta_1",
            "policy_type",
            "PTA.1",
        ),
        serialization_alias="PTA.1",
        title="Policy Type",
    )

    pta_2: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pta_2",
            "amount_class",
            "PTA.2",
        ),
        serialization_alias="PTA.2",
        title="Amount Class",
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

    model_config = {"populate_by_name": True}
