"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MSH
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.HD import HD
from ..datatypes.MSG import MSG
from ..datatypes.PT import PT
from ..datatypes.TS import TS
from ..datatypes.VID import VID


class MSH(BaseModel):
    """HL7 v2 MSH segment."""

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

    msh_3: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_3",
            "sending_application",
            "MSH.3",
        ),
        serialization_alias="MSH.3",
        title="Sending Application",
        description="Item #3 | Table HL70361",
    )

    msh_4: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_4",
            "sending_facility",
            "MSH.4",
        ),
        serialization_alias="MSH.4",
        title="Sending Facility",
        description="Item #4 | Table HL70362",
    )

    msh_5: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_5",
            "receiving_application",
            "MSH.5",
        ),
        serialization_alias="MSH.5",
        title="Receiving Application",
        description="Item #5 | Table HL70361",
    )

    msh_6: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_6",
            "receiving_facility",
            "MSH.6",
        ),
        serialization_alias="MSH.6",
        title="Receiving Facility",
        description="Item #6 | Table HL70362",
    )

    msh_7: TS = Field(
        default=...,
        validation_alias=AliasChoices(
            "msh_7",
            "date_time_of_message",
            "MSH.7",
        ),
        serialization_alias="MSH.7",
        title="Date/Time Of Message",
        description="Item #7",
    )

    msh_8: str | None = Field(
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

    msh_9: MSG = Field(
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

    msh_12: VID = Field(
        default=...,
        validation_alias=AliasChoices(
            "msh_12",
            "version_id",
            "MSH.12",
        ),
        serialization_alias="MSH.12",
        title="Version ID",
        description="Item #12",
    )

    msh_13: str | None = Field(
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

    msh_14: str | None = Field(
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

    msh_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_15",
            "accept_acknowledgment_type",
            "MSH.15",
        ),
        serialization_alias="MSH.15",
        title="Accept Acknowledgment Type",
        description="Item #15 | Table HL70155",
    )

    msh_16: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_16",
            "application_acknowledgment_type",
            "MSH.16",
        ),
        serialization_alias="MSH.16",
        title="Application Acknowledgment Type",
        description="Item #16 | Table HL70155",
    )

    msh_17: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_17",
            "country_code",
            "MSH.17",
        ),
        serialization_alias="MSH.17",
        title="Country Code",
        description="Item #17 | Table HL70399",
    )

    msh_18: list[str] | None = Field(
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

    msh_19: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_19",
            "principal_language_of_message",
            "MSH.19",
        ),
        serialization_alias="MSH.19",
        title="Principal Language Of Message",
        description="Item #693",
    )

    msh_20: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_20",
            "alternate_character_set_handling_scheme",
            "MSH.20",
        ),
        serialization_alias="MSH.20",
        title="Alternate Character Set Handling Scheme",
        description="Item #1317 | Table HL70356",
    )

    msh_21: list[EI] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_21",
            "message_profile_identifier",
            "MSH.21",
        ),
        serialization_alias="MSH.21",
        title="Message Profile Identifier",
        description="Item #1598",
    )

    model_config = {"populate_by_name": True}
