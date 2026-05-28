"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: LAN
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE


class LAN(BaseModel):
    """HL7 v2 LAN segment."""

    lan_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "lan_1",
            "set_id_lan",
            "LAN.1",
        ),
        serialization_alias="LAN.1",
        title="Set ID - LAN",
        description="Item #1455",
    )

    lan_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "lan_2",
            "language_code",
            "LAN.2",
        ),
        serialization_alias="LAN.2",
        title="Language Code",
        description="Item #1456 | Table HL70296",
    )

    lan_3: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "lan_3",
            "language_ability_code",
            "LAN.3",
        ),
        serialization_alias="LAN.3",
        title="Language Ability Code",
        description="Item #1457 | Table HL70403",
    )

    lan_4: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "lan_4",
            "language_proficiency_code",
            "LAN.4",
        ),
        serialization_alias="LAN.4",
        title="Language Proficiency Code",
        description="Item #1458 | Table HL70404",
    )

    model_config = {"populate_by_name": True}
