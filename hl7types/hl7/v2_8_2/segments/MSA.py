"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MSA
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class MSA(BaseModel):
    """HL7 v2 MSA segment.

    Attributes
    ----------
    msa_1 : str
        MSA.1 (req) - Acknowledgment Code (ID)

    msa_2 : str
        MSA.2 (req) - Message Control ID (ST)

    msa_4 : str | None
        MSA.4 (opt) - Expected Sequence Number (NM)

    msa_7 : str | None
        MSA.7 (opt) - Message Waiting Number (NM)

    msa_8 : str | None
        MSA.8 (opt) - Message Waiting Priority (ID)
    """

    msa_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "msa_1",
            "acknowledgment_code",
            "MSA.1",
        ),
        serialization_alias="MSA.1",
        title="Acknowledgment Code",
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

    msa_4: Optional[str] = Field(
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

    msa_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_7",
            "message_waiting_number",
            "MSA.7",
        ),
        serialization_alias="MSA.7",
        title="Message Waiting Number",
        description="Item #1827",
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
        description="Item #1828 | Table HL70520",
    )

    model_config = {"populate_by_name": True}
