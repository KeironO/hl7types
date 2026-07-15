"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: LAN
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class LAN(HL7Model):
    """Language Detail (S15.4.4).

    Attributes
    ----------
    lan_1 : str
        LAN.1 - Set ID - LAN (SI) R S15.4.4.1

    lan_2 : CWE
        LAN.2 - Language Code (CWE) R S15.4.4.2 | 0296 - Primary Language

    lan_3 : list[CWE] | None
        LAN.3 - Language Ability Code (CWE) O rep S15.4.4.3 | 0403 - Language Ability

    lan_4 : CWE | None
        LAN.4 - Language Proficiency Code (CWE) O S15.4.4.4 | 0404 - Language Proficiency
    """

    lan_1: str = Field(
        validation_alias=AliasChoices(
            "lan_1",
            "set_id_lan",
            "LAN.1",
        ),
        serialization_alias="LAN.1",
        title="Set ID - LAN",
        description="R | Item #01455 | LEN:4",
    )

    lan_2: CWE = Field(
        validation_alias=AliasChoices(
            "lan_2",
            "language_code",
            "LAN.2",
        ),
        serialization_alias="LAN.2",
        title="Language Code",
        description="R | Item #01456 | Table 0296 - Primary Language",
    )

    lan_3: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "lan_3",
            "language_ability_code",
            "LAN.3",
        ),
        serialization_alias="LAN.3",
        title="Language Ability Code",
        description="O | Item #01457 | Table 0403 - Language Ability",
    )

    lan_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "lan_4",
            "language_proficiency_code",
            "LAN.4",
        ),
        serialization_alias="LAN.4",
        title="Language Proficiency Code",
        description="O | Item #01458 | Table 0404 - Language Proficiency",
    )

    @field_validator("lan_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
