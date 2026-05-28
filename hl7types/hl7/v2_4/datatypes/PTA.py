"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PTA
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class PTA(BaseModel):
    """HL7 v2 PTA data type."""

    pta_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pta_1",
            "policy_type",
            "PTA.1",
        ),
        serialization_alias="PTA.1",
        title="policy type",
    )

    pta_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pta_2",
            "amount_class",
            "PTA.2",
        ),
        serialization_alias="PTA.2",
        title="amount class",
    )

    pta_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pta_3",
            "amount",
            "PTA.3",
        ),
        serialization_alias="PTA.3",
        title="amount",
    )

    model_config = {"populate_by_name": True}
