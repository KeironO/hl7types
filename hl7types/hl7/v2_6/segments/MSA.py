"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: MSA
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class MSA(HL7Model):
    """Message Acknowledgment (S2.14.8).

    Attributes
    ----------
    msa_1 : str
        MSA.1 - Acknowledgment Code (ID) R S2.14.8.1 | 0008 - Acknowledgment code

    msa_2 : str
        MSA.2 - Message Control ID (ST) R S2.14.8.2

    msa_3 : str | None
        MSA.3 - Text Message (ST) O S2.14.8.3

    msa_4 : str | None
        MSA.4 - Expected Sequence Number (NM) O S2.14.8.4

    msa_6 : CNE | None
        MSA.6 - Error Condition (CNE) O S2.14.8.6 | 0357 - Message error condition codes

    msa_7 : str | None
        MSA.7 - Message Waiting Number (NM) O S2.14.8.7

    msa_8 : str | None
        MSA.8 - Message Waiting Priority (ID) O S2.14.8.8 | 0520 - Message waiting priority
    """

    msa_1: str = Field(
        validation_alias=AliasChoices(
            "msa_1",
            "acknowledgment_code",
            "MSA.1",
        ),
        serialization_alias="MSA.1",
        title="Acknowledgment Code",
        description=(
            "R | Item #00018 | Table 0008 - Acknowledgment code | LEN:2"
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
        description="R | Item #00010 | LEN:199",
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
        description="O | Item #00020",
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

    msa_6: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_6",
            "error_condition",
            "MSA.6",
        ),
        serialization_alias="MSA.6",
        title="Error Condition",
        description=(
            "O | Item #00023 | Table 0357 - Message error condition codes"
        ),
    )

    msa_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_7",
            "message_waiting_number",
            "MSA.7",
        ),
        serialization_alias="MSA.7",
        title="Message Waiting Number",
        description="O | Item #01827 | LEN:5",
    )

    msa_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_8",
            "message_waiting_priority",
            "MSA.8",
        ),
        serialization_alias="MSA.8",
        title="Message Waiting Priority",
        description=(
            "O | Item #01828 | Table 0520 - Message waiting priority | LEN:1"
        ),
    )

    @field_validator("msa_4", "msa_7", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
