"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MSH
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class MSH(HL7Model):
    """MESSAGE HEADER (S2.10.1).

    Attributes
    ----------
    msh_1 : str
        MSH.1 - Field separator (ST) R S3.2.1

    msh_2 : str
        MSH.2 - Encoding characters (ST) R S3.2.2

    msh_3 : str | None
        MSH.3 - Sending application (ST) NA S3.2.3

    msh_4 : str | None
        MSH.4 - Sending facility (ST) NA S3.2.4

    msh_5 : str | None
        MSH.5 - Receiving application (ST) NA S3.2.5

    msh_6 : str | None
        MSH.6 - Receiving facility (ST) NA S3.2.6

    msh_7 : TS | None
        MSH.7 - Date / Time of message (TS) NA S3.2.7

    msh_8 : str | None
        MSH.8 - Security (ST) NA S3.2.8

    msh_9 : str
        MSH.9 - Message type (CM) R S3.2.9 | 0076 - MESSAGE TYPE

    msh_10 : str
        MSH.10 - Message Control ID (ST) R S2.10.2.2

    msh_11 : str
        MSH.11 - Processing ID (ID) R S2.10.1.11 | 0103 - PROCESSING ID

    msh_12 : str
        MSH.12 - Version ID (ID) R S2.10.1.12 | 0104 - VERSION ID

    msh_13 : str | None
        MSH.13 - Sequence number (NM) NA S2.10.1.13

    msh_14 : str | None
        MSH.14 - Continuation pointer (ST) NA S2.10.1.14

    msh_15 : str | None
        MSH.15 - Accept acknowledgement type (ID) NA S2.10.1.15 | 0155 - ACCEPT/APPLICATION ACKNOWLEDGEMENT CONDITIONS

    msh_16 : str | None
        MSH.16 - Application acknowledgement type (ID) NA S2.10.1.16 | 0155 - ACCEPT/APPLICATION ACKNOWLEDGEMENT CONDITIONS

    msh_17 : str | None
        MSH.17 - Country code (ID) NA S2.10.1.17
    """

    msh_1: str = Field(
        default="|",
        validation_alias=AliasChoices(
            "msh_1",
            "field_separator",
            "MSH.1",
        ),
        serialization_alias="MSH.1",
        title="Field separator",
        description="R | Item #00001 | LEN:1",
    )

    msh_2: str = Field(
        default="^~\\&",
        validation_alias=AliasChoices(
            "msh_2",
            "encoding_characters",
            "MSH.2",
        ),
        serialization_alias="MSH.2",
        title="Encoding characters",
        description="R | Item #00002 | LEN:4",
    )

    msh_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_3",
            "sending_application",
            "MSH.3",
        ),
        serialization_alias="MSH.3",
        title="Sending application",
        description="NA | Item #00003 | LEN:15",
    )

    msh_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_4",
            "sending_facility",
            "MSH.4",
        ),
        serialization_alias="MSH.4",
        title="Sending facility",
        description="NA | Item #00004 | LEN:20",
    )

    msh_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_5",
            "receiving_application",
            "MSH.5",
        ),
        serialization_alias="MSH.5",
        title="Receiving application",
        description="NA | Item #00005 | LEN:30",
    )

    msh_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_6",
            "receiving_facility",
            "MSH.6",
        ),
        serialization_alias="MSH.6",
        title="Receiving facility",
        description="NA | Item #00006 | LEN:30",
    )

    msh_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_7",
            "date_time_of_message",
            "MSH.7",
        ),
        serialization_alias="MSH.7",
        title="Date / Time of message",
        description="NA | Item #00007",
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
        description="NA | Item #00008 | LEN:40",
    )

    msh_9: str = Field(
        validation_alias=AliasChoices(
            "msh_9",
            "message_type",
            "MSH.9",
        ),
        serialization_alias="MSH.9",
        title="Message type",
        description="R | Item #00009 | Table 0076 - MESSAGE TYPE",
    )

    msh_10: str = Field(
        validation_alias=AliasChoices(
            "msh_10",
            "message_control_id",
            "MSH.10",
        ),
        serialization_alias="MSH.10",
        title="Message Control ID",
        description="R | Item #00010 | LEN:20",
    )

    msh_11: str = Field(
        validation_alias=AliasChoices(
            "msh_11",
            "processing_id",
            "MSH.11",
        ),
        serialization_alias="MSH.11",
        title="Processing ID",
        description="R | Item #00011 | Table 0103 - PROCESSING ID | LEN:1",
    )

    msh_12: str = Field(
        validation_alias=AliasChoices(
            "msh_12",
            "version_id",
            "MSH.12",
        ),
        serialization_alias="MSH.12",
        title="Version ID",
        description="R | Item #00012 | Table 0104 - VERSION ID | LEN:8",
    )

    msh_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_13",
            "sequence_number",
            "MSH.13",
        ),
        serialization_alias="MSH.13",
        title="Sequence number",
        description="NA | Item #00013 | LEN:15",
    )

    msh_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_14",
            "continuation_pointer",
            "MSH.14",
        ),
        serialization_alias="MSH.14",
        title="Continuation pointer",
        description="NA | Item #00014 | LEN:180",
    )

    msh_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_15",
            "accept_acknowledgement_type",
            "MSH.15",
        ),
        serialization_alias="MSH.15",
        title="Accept acknowledgement type",
        description=(
            "NA | Item #00015 | Table 0155 - ACCEPT/APPLICATION ACKNOWLEDGEMENT "
            "CONDITIONS | LEN:2"
        ),
    )

    msh_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_16",
            "application_acknowledgement_type",
            "MSH.16",
        ),
        serialization_alias="MSH.16",
        title="Application acknowledgement type",
        description=(
            "NA | Item #00016 | Table 0155 - ACCEPT/APPLICATION ACKNOWLEDGEMENT "
            "CONDITIONS | LEN:2"
        ),
    )

    msh_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_17",
            "country_code",
            "MSH.17",
        ),
        serialization_alias="MSH.17",
        title="Country code",
        description="NA | Item #00017 | LEN:2",
    )

    @field_validator("msh_13", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
