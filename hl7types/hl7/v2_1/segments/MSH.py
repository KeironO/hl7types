"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: MSH
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class MSH(HL7Model):
    """MESSAGE HEADER (S2.5.8).

    Attributes
    ----------
    msh_1 : str
        MSH.1 - FIELD SEPARATOR (ST) R S2-46

    msh_2 : str
        MSH.2 - ENCODING CHARACTERS (ST) R

    msh_3 : str | None
        MSH.3 - SENDING APPLICATION (ST) O

    msh_4 : str | None
        MSH.4 - SENDING FACILITY (ST) O

    msh_5 : str | None
        MSH.5 - RECEIVING APPLICATION (ST) O

    msh_6 : str | None
        MSH.6 - RECEIVING FACILITY (ST) O

    msh_7 : str | None
        MSH.7 - DATE/TIME OF MESSAGE (TS) O

    msh_8 : str | None
        MSH.8 - Security (ST) O

    msh_9 : str
        MSH.9 - MESSAGE TYPE (ID) R | 0076 - MESSAGE TYPE

    msh_10 : str
        MSH.10 - MESSAGE CONTROL ID (ST) R

    msh_11 : str
        MSH.11 - PROCESSING ID (ID) R | 0103 - PROCESSING ID

    msh_12 : str
        MSH.12 - VERSION ID (NM) R | 0104 - VERSION CONTROL TABLE

    msh_13 : str | None
        MSH.13 - SEQUENCE NUMBER (NM) O

    msh_14 : str | None
        MSH.14 - CONTINUATION POINTER (ST) O
    """

    msh_1: str = Field(
        default="|",
        validation_alias=AliasChoices(
            "msh_1",
            "field_separator",
            "MSH.1",
        ),
        serialization_alias="MSH.1",
        title="FIELD SEPARATOR",
        description="R | Item #00005 | LEN:1",
    )

    msh_2: str = Field(
        default="^~\\&",
        validation_alias=AliasChoices(
            "msh_2",
            "encoding_characters",
            "MSH.2",
        ),
        serialization_alias="MSH.2",
        title="ENCODING CHARACTERS",
        description="R | Item #00509 | LEN:4",
    )

    msh_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_3",
            "sending_application",
            "MSH.3",
        ),
        serialization_alias="MSH.3",
        title="SENDING APPLICATION",
        description="O | Item #00006 | LEN:15",
    )

    msh_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_4",
            "sending_facility",
            "MSH.4",
        ),
        serialization_alias="MSH.4",
        title="SENDING FACILITY",
        description="O | Item #00512 | LEN:20",
    )

    msh_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_5",
            "receiving_application",
            "MSH.5",
        ),
        serialization_alias="MSH.5",
        title="RECEIVING APPLICATION",
        description="O | Item #00009 | LEN:15",
    )

    msh_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_6",
            "receiving_facility",
            "MSH.6",
        ),
        serialization_alias="MSH.6",
        title="RECEIVING FACILITY",
        description="O | Item #00513 | LEN:30",
    )

    msh_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_7",
            "date_time_of_message",
            "MSH.7",
        ),
        serialization_alias="MSH.7",
        title="DATE/TIME OF MESSAGE",
        description="O | Item #00010 | LEN:19",
    )

    msh_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_8",
            "security",
            "MSH.8",
        ),
        serialization_alias="MSH.8",
        title="Security",
        description="O | Item #00008 | LEN:40",
    )

    msh_9: str = Field(
        validation_alias=AliasChoices(
            "msh_9",
            "message_type",
            "MSH.9",
        ),
        serialization_alias="MSH.9",
        title="MESSAGE TYPE",
        description="R | Item #00012 | Table 0076 - MESSAGE TYPE | LEN:7",
    )

    msh_10: str = Field(
        validation_alias=AliasChoices(
            "msh_10",
            "message_control_id",
            "MSH.10",
        ),
        serialization_alias="MSH.10",
        title="MESSAGE CONTROL ID",
        description="R | Item #00013 | LEN:20",
    )

    msh_11: str = Field(
        validation_alias=AliasChoices(
            "msh_11",
            "processing_id",
            "MSH.11",
        ),
        serialization_alias="MSH.11",
        title="PROCESSING ID",
        description="R | Item #00014 | Table 0103 - PROCESSING ID | LEN:1",
    )

    msh_12: str = Field(
        validation_alias=AliasChoices(
            "msh_12",
            "version_id",
            "MSH.12",
        ),
        serialization_alias="MSH.12",
        title="VERSION ID",
        description=(
            "R | Item #00015 | Table 0104 - VERSION CONTROL TABLE | LEN:8"
        ),
    )

    msh_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_13",
            "sequence_number",
            "MSH.13",
        ),
        serialization_alias="MSH.13",
        title="SEQUENCE NUMBER",
        description="O | Item #00633 | LEN:15",
    )

    msh_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_14",
            "continuation_pointer",
            "MSH.14",
        ),
        serialization_alias="MSH.14",
        title="CONTINUATION POINTER",
        description="O | Item #00699 | LEN:180",
    )

    @field_validator("msh_12", "msh_13", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
