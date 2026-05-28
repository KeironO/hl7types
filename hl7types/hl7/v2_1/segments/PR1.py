"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: PR1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field


class PR1(BaseModel):
    """HL7 v2 PR1 segment."""

    pr1_1: List[str] = Field(
        default=...,
        validation_alias=AliasChoices(
            "pr1_1",
            "set_id_procedure",
            "PR1.1",
        ),
        serialization_alias="PR1.1",
        title="SET ID - PROCEDURE",
        description="Item #304",
    )

    pr1_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pr1_2",
            "procedure_coding_method",
            "PR1.2",
        ),
        serialization_alias="PR1.2",
        title="PROCEDURE CODING METHOD.",
        description="Item #393 | Table HL70089",
    )

    pr1_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pr1_3",
            "procedure_code",
            "PR1.3",
        ),
        serialization_alias="PR1.3",
        title="PROCEDURE CODE",
        description="Item #305 | Table HL70088",
    )

    pr1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_4",
            "procedure_description",
            "PR1.4",
        ),
        serialization_alias="PR1.4",
        title="PROCEDURE DESCRIPTION",
        description="Item #306",
    )

    pr1_5: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pr1_5",
            "procedure_date_time",
            "PR1.5",
        ),
        serialization_alias="PR1.5",
        title="PROCEDURE DATE/TIME",
        description="Item #307",
    )

    pr1_6: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pr1_6",
            "procedure_type",
            "PR1.6",
        ),
        serialization_alias="PR1.6",
        title="PROCEDURE TYPE",
        description="Item #309 | Table HL70090",
    )

    pr1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_7",
            "procedure_minutes",
            "PR1.7",
        ),
        serialization_alias="PR1.7",
        title="PROCEDURE MINUTES",
        description="Item #310",
    )

    pr1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_8",
            "anesthesiologist",
            "PR1.8",
        ),
        serialization_alias="PR1.8",
        title="ANESTHESIOLOGIST",
        description="Item #311 | Table HL70010",
    )

    pr1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_9",
            "anesthesia_code",
            "PR1.9",
        ),
        serialization_alias="PR1.9",
        title="ANESTHESIA CODE",
        description="Item #313 | Table HL70019",
    )

    pr1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_10",
            "anesthesia_minutes",
            "PR1.10",
        ),
        serialization_alias="PR1.10",
        title="ANESTHESIA MINUTES",
        description="Item #314",
    )

    pr1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_11",
            "surgeon",
            "PR1.11",
        ),
        serialization_alias="PR1.11",
        title="SURGEON",
        description="Item #315 | Table HL70010",
    )

    pr1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_12",
            "resident_code",
            "PR1.12",
        ),
        serialization_alias="PR1.12",
        title="RESIDENT CODE",
        description="Item #318 | Table HL70010",
    )

    pr1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_13",
            "consent_code",
            "PR1.13",
        ),
        serialization_alias="PR1.13",
        title="CONSENT CODE",
        description="Item #317 | Table HL70059",
    )

    model_config = {"populate_by_name": True}
