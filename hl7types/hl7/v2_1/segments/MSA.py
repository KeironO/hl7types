"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: MSA
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class MSA(BaseModel):
    """HL7 v2 MSA segment."""

    msa_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "msa_1",
            "acknowledgment_code",
            "MSA.1",
        ),
        serialization_alias="MSA.1",
        title="ACKNOWLEDGMENT CODE",
        description="Item #2 | Table HL70008",
    )

    msa_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "msa_2",
            "message_control_id",
            "MSA.2",
        ),
        serialization_alias="MSA.2",
        title="MESSAGE CONTROL ID",
        description="Item #3",
    )

    msa_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_3",
            "text_message",
            "MSA.3",
        ),
        serialization_alias="MSA.3",
        title="TEXT MESSAGE",
        description="Item #4",
    )

    msa_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_4",
            "expected_sequence_number",
            "MSA.4",
        ),
        serialization_alias="MSA.4",
        title="EXPECTED SEQUENCE NUMBER",
        description="Item #598",
    )

    msa_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_5",
            "delayed_acknowledgment_type",
            "MSA.5",
        ),
        serialization_alias="MSA.5",
        title="DELAYED ACKNOWLEDGMENT TYPE",
        description="Item #632 | Table HL70102",
    )

    model_config = {"populate_by_name": True}
