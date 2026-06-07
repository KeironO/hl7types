"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: LAN
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class LAN(HL7Model):
    """HL7 v2 LAN segment.

    Attributes
    ----------
    lan_1 : str
        LAN.1 (req) - Set ID _ LAN (SI)

    lan_2 : CE
        LAN.2 (req) - Language Code (CE)

    lan_3 : list[CE] | None
        LAN.3 (opt, rep) - Language Ability Code (CE)

    lan_4 : CE | None
        LAN.4 (opt) - Language Proficiency Code (CE)
    """

    lan_1: str = Field(
        validation_alias=AliasChoices(
            "lan_1",
            "set_id_lan",
            "LAN.1",
        ),
        serialization_alias="LAN.1",
        title="Set ID _ LAN",
        description="Item #1455",
    )

    lan_2: CE = Field(
        validation_alias=AliasChoices(
            "lan_2",
            "language_code",
            "LAN.2",
        ),
        serialization_alias="LAN.2",
        title="Language Code",
        description="Item #1456 | Table HL70296",
    )

    lan_3: Optional[List[CE]] = Field(
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

    lan_4: Optional[CE] = Field(
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

    @field_validator("lan_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
