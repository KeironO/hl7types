"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MSH
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.TS import TS


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
        title="Field separator",
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
        title="Encoding characters",
        description="Item #2",
    )

    msh_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_3",
            "sending_application",
            "MSH.3",
        ),
        serialization_alias="MSH.3",
        title="Sending application",
        description="Item #3",
    )

    msh_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_4",
            "sending_facility",
            "MSH.4",
        ),
        serialization_alias="MSH.4",
        title="Sending facility",
        description="Item #4",
    )

    msh_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_5",
            "receiving_application",
            "MSH.5",
        ),
        serialization_alias="MSH.5",
        title="Receiving application",
        description="Item #5",
    )

    msh_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_6",
            "receiving_facility",
            "MSH.6",
        ),
        serialization_alias="MSH.6",
        title="Receiving facility",
        description="Item #6",
    )

    msh_7: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_7",
            "date_time_of_message",
            "MSH.7",
        ),
        serialization_alias="MSH.7",
        title="Date / Time of message",
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

    msh_9: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "msh_9",
            "message_type",
            "MSH.9",
        ),
        serialization_alias="MSH.9",
        title="Message type",
        description="Item #9 | Table HL70076",
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

    msh_11: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "msh_11",
            "processing_id",
            "MSH.11",
        ),
        serialization_alias="MSH.11",
        title="Processing ID",
        description="Item #11 | Table HL70103",
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

    msh_13: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_13",
            "sequence_number",
            "MSH.13",
        ),
        serialization_alias="MSH.13",
        title="Sequence number",
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
        title="Continuation pointer",
        description="Item #14",
    )

    msh_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_15",
            "accept_acknowledgement_type",
            "MSH.15",
        ),
        serialization_alias="MSH.15",
        title="Accept acknowledgement type",
        description="Item #15 | Table HL70155",
    )

    msh_16: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msh_16",
            "application_acknowledgement_type",
            "MSH.16",
        ),
        serialization_alias="MSH.16",
        title="Application acknowledgement type",
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
        title="Country code",
        description="Item #17",
    )

    model_config = {"populate_by_name": True}
