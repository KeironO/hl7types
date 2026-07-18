"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: MSA
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class MSA(HL7Model):
    """MESSAGE ACKNOWLEDGMENT (S2.5.7).

    Attributes
    ----------
    msa_1 : str
        MSA.1 - ACKNOWLEDGMENT CODE (ID) R S2-45 | 0008 - ACKNOWLEDGMENT CODE

    msa_2 : str
        MSA.2 - MESSAGE CONTROL ID (ST) R

    msa_3 : str | None
        MSA.3 - TEXT MESSAGE (ST) O

    msa_4 : str | None
        MSA.4 - EXPECTED SEQUENCE NUMBER (NM) O

    msa_5 : str | None
        MSA.5 - DELAYED ACKNOWLEDGMENT TYPE (ID) O | 0102 - DELAYED ACKNOWLEDGMENT TYPE
    """

    msa_1: str = Field(
        validation_alias=AliasChoices(
            "msa_1",
            "acknowledgment_code",
            "MSA.1",
        ),
        serialization_alias="MSA.1",
        title="ACKNOWLEDGMENT CODE",
        description=(
            "R | Item #00002 | Table 0008 - ACKNOWLEDGMENT CODE | LEN:2"
        ),
    )

    msa_2: str = Field(
        validation_alias=AliasChoices(
            "msa_2",
            "message_control_id",
            "MSA.2",
        ),
        serialization_alias="MSA.2",
        title="MESSAGE CONTROL ID",
        description="R | Item #00003 | LEN:20",
    )

    msa_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_3",
            "text_message",
            "MSA.3",
        ),
        serialization_alias="MSA.3",
        title="TEXT MESSAGE",
        description="O | Item #00004 | LEN:80",
    )

    msa_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_4",
            "expected_sequence_number",
            "MSA.4",
        ),
        serialization_alias="MSA.4",
        title="EXPECTED SEQUENCE NUMBER",
        description="O | Item #00598 | LEN:15",
    )

    msa_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_5",
            "delayed_acknowledgment_type",
            "MSA.5",
        ),
        serialization_alias="MSA.5",
        title="DELAYED ACKNOWLEDGMENT TYPE",
        description=(
            "O | Item #00632 | Table 0102 - DELAYED ACKNOWLEDGMENT TYPE | LEN:1"
        ),
    )

    @field_validator("msa_4", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
