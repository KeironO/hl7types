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
    """HL7 v2 MSH segment.

    Attributes
    ----------
    msh_1 : str
        MSH.1 (req) - FIELD SEPARATOR (ST)

    msh_2 : str
        MSH.2 (req) - ENCODING CHARACTERS (ST)

    msh_3 : str | None
        MSH.3 (opt) - SENDING APPLICATION (ST)

    msh_4 : str | None
        MSH.4 (opt) - SENDING FACILITY (ST)

    msh_5 : str | None
        MSH.5 (opt) - RECEIVING APPLICATION (ST)

    msh_6 : str | None
        MSH.6 (opt) - RECEIVING FACILITY (ST)

    msh_7 : str | None
        MSH.7 (opt) - DATE/TIME OF MESSAGE (TS)

    msh_8 : str | None
        MSH.8 (opt) - Security (ST)

    msh_9 : str
        MSH.9 (req) - MESSAGE TYPE (ID)

    msh_10 : str
        MSH.10 (req) - MESSAGE CONTROL ID (ST)

    msh_11 : str
        MSH.11 (req) - PROCESSING ID (ID)

    msh_12 : str
        MSH.12 (req) - VERSION ID (NM)

    msh_13 : str | None
        MSH.13 (opt) - SEQUENCE NUMBER (NM)

    msh_14 : str | None
        MSH.14 (opt) - CONTINUATION POINTER (ST)
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
        description="Item #5",
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
        description="Item #509",
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
        description="Item #6",
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
        description="Item #512",
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
        description="Item #9",
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
        description="Item #513",
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
        description="Item #10",
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
        description="Item #8",
    )

    msh_9: str = Field(
        validation_alias=AliasChoices(
            "msh_9",
            "message_type",
            "MSH.9",
        ),
        serialization_alias="MSH.9",
        title="MESSAGE TYPE",
        description="Item #12 | Table HL70076",
    )

    msh_10: str = Field(
        validation_alias=AliasChoices(
            "msh_10",
            "message_control_id",
            "MSH.10",
        ),
        serialization_alias="MSH.10",
        title="MESSAGE CONTROL ID",
        description="Item #13",
    )

    msh_11: str = Field(
        validation_alias=AliasChoices(
            "msh_11",
            "processing_id",
            "MSH.11",
        ),
        serialization_alias="MSH.11",
        title="PROCESSING ID",
        description="Item #14 | Table HL70103",
    )

    msh_12: str = Field(
        validation_alias=AliasChoices(
            "msh_12",
            "version_id",
            "MSH.12",
        ),
        serialization_alias="MSH.12",
        title="VERSION ID",
        description="Item #15 | Table HL70104",
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
        description="Item #633",
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
        description="Item #699",
    )

    @field_validator("msh_12", "msh_13", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
