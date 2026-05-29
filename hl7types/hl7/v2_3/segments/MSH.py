"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MSH
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.HD import HD
from ..datatypes.PT import PT
from ..datatypes.TS import TS


class MSH(BaseModel):
    """HL7 v2 MSH segment.

    Attributes
    ----------
    msh_1 : str
        MSH.1 (req) - Field Separator (ST)

    msh_2 : str
        MSH.2 (req) - Encoding Characters (ST)

    msh_3 : HD | None
        MSH.3 (opt) - Sending Application (HD)

    msh_4 : HD | None
        MSH.4 (opt) - Sending Facility (HD)

    msh_5 : HD | None
        MSH.5 (opt) - Receiving Application (HD)

    msh_6 : HD | None
        MSH.6 (opt) - Receiving Facility (HD)

    msh_7 : TS | None
        MSH.7 (opt) - Date / Time of Message (TS)

    msh_8 : str | None
        MSH.8 (opt) - Security (ST)

    msh_9 : str
        MSH.9 (req) - Message Type (CM)

    msh_10 : str
        MSH.10 (req) - Message Control ID (ST)

    msh_11 : PT
        MSH.11 (req) - Processing ID (PT)

    msh_12 : str
        MSH.12 (req) - Version ID (ID)

    msh_13 : str | None
        MSH.13 (opt) - Sequence Number (NM)

    msh_14 : str | None
        MSH.14 (opt) - Continuation Pointer (ST)

    msh_15 : str | None
        MSH.15 (opt) - Accept Acknowledgement Type (ID)

    msh_16 : str | None
        MSH.16 (opt) - Application Acknowledgement Type (ID)

    msh_17 : str | None
        MSH.17 (opt) - Country Code (ID)

    msh_18 : str | None
        MSH.18 (opt) - Character Set (ID)

    msh_19 : CE | None
        MSH.19 (opt) - Principal Language of Message (CE)
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
        description="Item #1",
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
        description="Item #2",
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
        description="Item #3",
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
        description="Item #4",
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
        description="Item #5",
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
        description="Item #6",
    )

    msh_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_7",
            "date_time_of_message",
            "MSH.7",
        ),
        serialization_alias="MSH.7",
        title="Date / Time of Message",
        description="Item #7",
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
        default=...,
        validation_alias=AliasChoices(
            "msh_9",
            "message_type",
            "MSH.9",
        ),
        serialization_alias="MSH.9",
        title="Message Type",
        description="Item #9",
    )

    msh_10: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "msh_10",
            "message_control_id",
            "MSH.10",
        ),
        serialization_alias="MSH.10",
        title="Message Control ID",
        description="Item #10",
    )

    msh_11: PT = Field(
        default=...,
        validation_alias=AliasChoices(
            "msh_11",
            "processing_id",
            "MSH.11",
        ),
        serialization_alias="MSH.11",
        title="Processing ID",
        description="Item #11",
    )

    msh_12: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "msh_12",
            "version_id",
            "MSH.12",
        ),
        serialization_alias="MSH.12",
        title="Version ID",
        description="Item #12 | Table HL70104",
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
        description="Item #13",
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
        description="Item #14",
    )

    msh_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_15",
            "accept_acknowledgement_type",
            "MSH.15",
        ),
        serialization_alias="MSH.15",
        title="Accept Acknowledgement Type",
        description="Item #15 | Table HL70155",
    )

    msh_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_16",
            "application_acknowledgement_type",
            "MSH.16",
        ),
        serialization_alias="MSH.16",
        title="Application Acknowledgement Type",
        description="Item #16 | Table HL70155",
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
        description="Item #17",
    )

    msh_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_18",
            "character_set",
            "MSH.18",
        ),
        serialization_alias="MSH.18",
        title="Character Set",
        description="Item #692 | Table HL70211",
    )

    msh_19: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_19",
            "principal_language_of_message",
            "MSH.19",
        ),
        serialization_alias="MSH.19",
        title="Principal Language of Message",
        description="Item #693",
    )

    model_config = {"populate_by_name": True}
