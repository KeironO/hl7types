"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: TX_CHALLENGE
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .TX import TX


class TX_CHALLENGE(BaseModel):
    """HL7 v2 TX_CHALLENGE data type."""

    tx_challenge_1: TX | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tx_challenge_1",
            "field_",
            "TX_CHALLENGE.1",
        ),
        serialization_alias="TX_CHALLENGE.1",
        title="???????????",
    )

    tx_challenge_2: TX | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "tx_challenge_2",
            "field_",
            "TX_CHALLENGE.2",
        ),
        serialization_alias="TX_CHALLENGE.2",
        title="???????????",
    )

    model_config = {"populate_by_name": True}
