"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: NK1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_SI = re.compile(r'\d*')


class NK1(HL7Model):
    """NEXT OF KIN (S6.3.6).

    Attributes
    ----------
    nk1_1 : str
        NK1.1 - SET ID - NEXT OF KIN (SI) R S3-23, 6-15

    nk1_2 : str | None
        NK1.2 - NEXT OF KIN NAME (PN) O

    nk1_3 : str | None
        NK1.3 - NEXT OF KIN RELATIONSHIP (ST) O | 0063 - RELATIONSHIP

    nk1_4 : str | None
        NK1.4 - NEXT OF KIN - ADDRESS (AD) O

    nk1_5 : list[str] | None
        NK1.5 - NEXT OF KIN - PHONE NUMBER (TN) O rep
    """

    nk1_1: str = Field(
        validation_alias=AliasChoices(
            "nk1_1",
            "set_id_next_of_kin",
            "NK1.1",
        ),
        serialization_alias="NK1.1",
        title="SET ID - NEXT OF KIN",
        description="R | Item #00712 | LEN:4",
    )

    nk1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_2",
            "next_of_kin_name",
            "NK1.2",
        ),
        serialization_alias="NK1.2",
        title="NEXT OF KIN NAME",
        description="O | Item #00048 | LEN:48",
    )

    nk1_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_3",
            "next_of_kin_relationship",
            "NK1.3",
        ),
        serialization_alias="NK1.3",
        title="NEXT OF KIN RELATIONSHIP",
        description="O | Item #00047 | Table 0063 - RELATIONSHIP | LEN:15",
    )

    nk1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_4",
            "next_of_kin_address",
            "NK1.4",
        ),
        serialization_alias="NK1.4",
        title="NEXT OF KIN - ADDRESS",
        description="O | Item #00225 | LEN:106",
    )

    nk1_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_5",
            "next_of_kin_phone_number",
            "NK1.5",
        ),
        serialization_alias="NK1.5",
        title="NEXT OF KIN - PHONE NUMBER",
        description="O | Item #00230 | LEN:40",
    )

    @field_validator("nk1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = ConfigDict(populate_by_name=True)
