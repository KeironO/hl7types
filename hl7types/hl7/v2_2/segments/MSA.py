"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MSA
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class MSA(BaseModel):
    """HL7 v2 MSA segment."""

    msa_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "msa_1",
            "acknowledgement_code",
            "MSA.1",
        ),
        serialization_alias="MSA.1",
        title="Acknowledgement code",
        description="Item #18 | Table HL70008",
    )

    msa_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "msa_2",
            "message_control_id",
            "MSA.2",
        ),
        serialization_alias="MSA.2",
        title="Message Control ID",
        description="Item #10",
    )

    msa_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_3",
            "text_message",
            "MSA.3",
        ),
        serialization_alias="MSA.3",
        title="Text Message",
        description="Item #20",
    )

    msa_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_4",
            "expected_sequence_number",
            "MSA.4",
        ),
        serialization_alias="MSA.4",
        title="Expected Sequence Number",
        description="Item #21",
    )

    msa_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_5",
            "delayed_acknowledgement_type",
            "MSA.5",
        ),
        serialization_alias="MSA.5",
        title="Delayed Acknowledgement type",
        description="Item #22 | Table HL70102",
    )

    msa_6: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_6",
            "error_condition",
            "MSA.6",
        ),
        serialization_alias="MSA.6",
        title="Error Condition",
        description="Item #23",
    )

    model_config = {"populate_by_name": True}
