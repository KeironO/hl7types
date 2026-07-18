"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MSH
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.HD import HD
from ..datatypes.MSG import MSG
from ..datatypes.PT import PT
from ..datatypes.TS import TS
from ..datatypes.VID import VID

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class MSH(HL7Model):
    """Message Header (S2.15.9).

    Attributes
    ----------
    msh_1 : str
        MSH.1 - Field Separator (ST) R S2.15.9.1

    msh_2 : str
        MSH.2 - Encoding Characters (ST) R S2.15.9.2

    msh_3 : HD | None
        MSH.3 - Sending Application (HD) O S2.15.9.3 | 0361 - Application

    msh_4 : HD | None
        MSH.4 - Sending Facility (HD) O S2.15.9.4 | 0362 - Facility

    msh_5 : HD | None
        MSH.5 - Receiving Application (HD) O S2.15.9.5 | 0361 - Application

    msh_6 : HD | None
        MSH.6 - Receiving Facility (HD) O S2.15.9.6 | 0362 - Facility

    msh_7 : TS
        MSH.7 - Date/Time Of Message (TS) R S2.15.9.7

    msh_8 : str | None
        MSH.8 - Security (ST) O S2.15.9.8

    msh_9 : MSG
        MSH.9 - Message Type (MSG) R S2.15.9.9

    msh_10 : str
        MSH.10 - Message Control ID (ST) R S2.15.8.2

    msh_11 : PT
        MSH.11 - Processing ID (PT) R S2.15.9.11

    msh_12 : VID
        MSH.12 - Version ID (VID) R S2.15.9.12

    msh_13 : str | None
        MSH.13 - Sequence Number (NM) O S2.15.9.13

    msh_14 : str | None
        MSH.14 - Continuation Pointer (ST) O S2.15.4.1

    msh_15 : str | None
        MSH.15 - Accept Acknowledgment Type (ID) O S2.15.9.15 | 0155 - Accept/application acknowledgment conditions

    msh_16 : str | None
        MSH.16 - Application Acknowledgment Type (ID) O S2.15.9.16 | 0155 - Accept/application acknowledgment conditions

    msh_17 : str | None
        MSH.17 - Country Code (ID) O S2.15.9.17 | 0399 - Country code

    msh_18 : list[str] | None
        MSH.18 - Character Set (ID) O rep S2.15.9.18 | 0211 - Alternate character sets

    msh_19 : CE | None
        MSH.19 - Principal Language Of Message (CE) O S2.15.9.19

    msh_20 : str | None
        MSH.20 - Alternate Character Set Handling Scheme (ID) O S2.15.9.20 | 0356 - Alternate character set handling scheme

    msh_21 : list[EI] | None
        MSH.21 - Message Profile Identifier (EI) O rep S2.15.9.21
    """

    msh_1: str = Field(
        default="|",
        validation_alias=AliasChoices(
            "msh_1",
            "field_separator",
            "MSH.1",
        ),
        serialization_alias="MSH.1",
        title="Field Separator",
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
        title="Encoding Characters",
        description="R | Item #00002 | LEN:4",
    )

    msh_3: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_3",
            "sending_application",
            "MSH.3",
        ),
        serialization_alias="MSH.3",
        title="Sending Application",
        description="O | Item #00003 | Table 0361 - Application",
    )

    msh_4: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_4",
            "sending_facility",
            "MSH.4",
        ),
        serialization_alias="MSH.4",
        title="Sending Facility",
        description="O | Item #00004 | Table 0362 - Facility",
    )

    msh_5: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_5",
            "receiving_application",
            "MSH.5",
        ),
        serialization_alias="MSH.5",
        title="Receiving Application",
        description="O | Item #00005 | Table 0361 - Application",
    )

    msh_6: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_6",
            "receiving_facility",
            "MSH.6",
        ),
        serialization_alias="MSH.6",
        title="Receiving Facility",
        description="O | Item #00006 | Table 0362 - Facility",
    )

    msh_7: TS = Field(
        validation_alias=AliasChoices(
            "msh_7",
            "date_time_of_message",
            "MSH.7",
        ),
        serialization_alias="MSH.7",
        title="Date/Time Of Message",
        description="R | Item #00007",
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

    msh_9: MSG = Field(
        validation_alias=AliasChoices(
            "msh_9",
            "message_type",
            "MSH.9",
        ),
        serialization_alias="MSH.9",
        title="Message Type",
        description="R | Item #00009",
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

    msh_11: PT = Field(
        validation_alias=AliasChoices(
            "msh_11",
            "processing_id",
            "MSH.11",
        ),
        serialization_alias="MSH.11",
        title="Processing ID",
        description="R | Item #00011",
    )

    msh_12: VID = Field(
        validation_alias=AliasChoices(
            "msh_12",
            "version_id",
            "MSH.12",
        ),
        serialization_alias="MSH.12",
        title="Version ID",
        description="R | Item #00012",
    )

    msh_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_13",
            "sequence_number",
            "MSH.13",
        ),
        serialization_alias="MSH.13",
        title="Sequence Number",
        description="O | Item #00013 | LEN:15",
    )

    msh_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_14",
            "continuation_pointer",
            "MSH.14",
        ),
        serialization_alias="MSH.14",
        title="Continuation Pointer",
        description="O | Item #00014 | LEN:180",
    )

    msh_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_15",
            "accept_acknowledgment_type",
            "MSH.15",
        ),
        serialization_alias="MSH.15",
        title="Accept Acknowledgment Type",
        description=(
            "O | Item #00015 | Table 0155 - Accept/application acknowledgment "
            "conditions | LEN:2"
        ),
    )

    msh_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_16",
            "application_acknowledgment_type",
            "MSH.16",
        ),
        serialization_alias="MSH.16",
        title="Application Acknowledgment Type",
        description=(
            "O | Item #00016 | Table 0155 - Accept/application acknowledgment "
            "conditions | LEN:2"
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
        title="Country Code",
        description="O | Item #00017 | Table 0399 - Country code | LEN:3",
    )

    msh_18: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_18",
            "character_set",
            "MSH.18",
        ),
        serialization_alias="MSH.18",
        title="Character Set",
        description=(
            "O | Item #00692 | Table 0211 - Alternate character sets | LEN:16"
        ),
    )

    msh_19: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_19",
            "principal_language_of_message",
            "MSH.19",
        ),
        serialization_alias="MSH.19",
        title="Principal Language Of Message",
        description="O | Item #00693",
    )

    msh_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_20",
            "alternate_character_set_handling_scheme",
            "MSH.20",
        ),
        serialization_alias="MSH.20",
        title="Alternate Character Set Handling Scheme",
        description=(
            "O | Item #01317 | Table 0356 - Alternate character set handling "
            "scheme | LEN:20"
        ),
    )

    msh_21: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_21",
            "message_profile_identifier",
            "MSH.21",
        ),
        serialization_alias="MSH.21",
        title="Message Profile Identifier",
        description="O | Item #01598",
    )

    @field_validator("msh_13", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
