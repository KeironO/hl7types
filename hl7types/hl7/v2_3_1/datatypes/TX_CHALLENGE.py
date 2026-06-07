"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: TX_CHALLENGE
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class TX_CHALLENGE(HL7Model):
    """HL7 v2 TX_CHALLENGE data type.

    Attributes
    ----------
    tx_challenge_1 : str | None
        TX_CHALLENGE.1 (opt) - ??????????? (TX)

    tx_challenge_2 : str | None
        TX_CHALLENGE.2 (opt) - ??????????? (TX)
    """

    tx_challenge_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tx_challenge_1",
            "field_",
            "TX_CHALLENGE.1",
        ),
        serialization_alias="TX_CHALLENGE.1",
        title="???????????",
    )

    tx_challenge_2: Optional[str] = Field(
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
