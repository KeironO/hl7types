"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MSA
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class MSA(HL7Model):
    """Message acknowledgement segment (S2.24.2).

    Attributes
    ----------
    msa_1 : str
        MSA.1 - Acknowledgement code (ID) R S2.24.2.1 | 0008 - Acknowledgement Code

    msa_2 : str
        MSA.2 - Message Control ID (ST) R S2.24.1

    msa_3 : str | None
        MSA.3 - Text Message (ST) O S2.24.2.3

    msa_4 : str | None
        MSA.4 - Expected Sequence Number (NM) O S2.24.2.4

    msa_5 : str | None
        MSA.5 - Delayed Acknowledgement Type (ID) O S2.24.2.5 | 0102 - Delayed Acknowledgement Type

    msa_6 : CE | None
        MSA.6 - Error Condition (CE) O S2.24.2.6
    """

    msa_1: str = Field(
        validation_alias=AliasChoices(
            "msa_1",
            "acknowledgement_code",
            "MSA.1",
        ),
        serialization_alias="MSA.1",
        title="Acknowledgement code",
        description=(
            "R | Item #00018 | Table 0008 - Acknowledgement Code | LEN:2"
        ),
    )

    msa_2: str = Field(
        validation_alias=AliasChoices(
            "msa_2",
            "message_control_id",
            "MSA.2",
        ),
        serialization_alias="MSA.2",
        title="Message Control ID",
        description="R | Item #00010 | LEN:20",
    )

    msa_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_3",
            "text_message",
            "MSA.3",
        ),
        serialization_alias="MSA.3",
        title="Text Message",
        description="O | Item #00020 | LEN:80",
    )

    msa_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_4",
            "expected_sequence_number",
            "MSA.4",
        ),
        serialization_alias="MSA.4",
        title="Expected Sequence Number",
        description="O | Item #00021 | LEN:15",
    )

    msa_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_5",
            "delayed_acknowledgement_type",
            "MSA.5",
        ),
        serialization_alias="MSA.5",
        title="Delayed Acknowledgement Type",
        description=(
            "O | Item #00022 | Table 0102 - Delayed Acknowledgement Type | LEN:1"
        ),
    )

    msa_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_6",
            "error_condition",
            "MSA.6",
        ),
        serialization_alias="MSA.6",
        title="Error Condition",
        description="O | Item #00023",
    )

    @field_validator("msa_4", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
