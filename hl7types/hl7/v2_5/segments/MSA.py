"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MSA
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class MSA(HL7Model):
    """HL7 v2 MSA segment.

    Attributes
    ----------
    msa_1 : str
        MSA.1 (req) - Acknowledgment Code (ID)

    msa_2 : str
        MSA.2 (req) - Message Control ID (ST)

    msa_3 : str | None
        MSA.3 (opt) - Text Message (ST)

    msa_4 : str | None
        MSA.4 (opt) - Expected Sequence Number (NM)

    msa_5 : str | None
        MSA.5 (opt) - Delayed Acknowledgment Type (ID)

    msa_6 : CE | None
        MSA.6 (opt) - Error Condition (CE)
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

    msa_3: Optional[str] = Field(
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

    msa_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_5",
            "delayed_acknowledgment_type",
            "MSA.5",
        ),
        serialization_alias="MSA.5",
        title="Delayed Acknowledgment Type",
        description="Item #22",
    )

    msa_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msa_6",
            "error_condition",
            "MSA.6",
        ),
        serialization_alias="MSA.6",
        title="Error Condition",
        description="Item #23 | Table HL70357",
    )

    model_config = {"populate_by_name": True}
