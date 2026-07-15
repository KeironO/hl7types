"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: LAN
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class LAN(HL7Model):
    """Language Detail (S15.4.3).

    Attributes
    ----------
    lan_1 : str
        LAN.1 - Set ID - LAN (SI) R S15.4.3.1

    lan_2 : CE
        LAN.2 - Language Code (CE) R S15.4.3.2 | 0296 - Primary language

    lan_3 : list[CE] | None
        LAN.3 - Language Ability Code (CE) O rep S15.4.3.3 | 0403 - Language ability

    lan_4 : CE | None
        LAN.4 - Language Proficiency Code (CE) O S15.4.3.4 | 0404 - Language proficiency
    """

    lan_1: str = Field(
        validation_alias=AliasChoices(
            "lan_1",
            "set_id_lan",
            "LAN.1",
        ),
        serialization_alias="LAN.1",
        title="Set ID - LAN",
        description="R | Item #01455 | LEN:60",
    )

    lan_2: CE = Field(
        validation_alias=AliasChoices(
            "lan_2",
            "language_code",
            "LAN.2",
        ),
        serialization_alias="LAN.2",
        title="Language Code",
        description="R | Item #01456 | Table 0296 - Primary language",
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
        description="O | Item #01457 | Table 0403 - Language ability",
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
        description="O | Item #01458 | Table 0404 - Language proficiency",
    )

    @field_validator("lan_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
