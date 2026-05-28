"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: OM3
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class OM3(BaseModel):
    """HL7 v2 OM3 segment."""

    om3_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_1",
            "sequence_number_test_observation_master_file",
            "OM3.1",
        ),
        serialization_alias="OM3.1",
        title="Sequence Number - Test/ Observation Master File",
        description="Item #586",
    )

    om3_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_2",
            "preferred_coding_system",
            "OM3.2",
        ),
        serialization_alias="OM3.2",
        title="Preferred Coding System",
        description="Item #636",
    )

    om3_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_3",
            "valid_coded_answers",
            "OM3.3",
        ),
        serialization_alias="OM3.3",
        title="Valid Coded \"Answers\"",
        description="Item #637",
    )

    om3_4: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_4",
            "normal_text_codes_for_categorical_observations",
            "OM3.4",
        ),
        serialization_alias="OM3.4",
        title="Normal Text/Codes for Categorical Observations",
        description="Item #638",
    )

    om3_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_5",
            "abnormal_text_codes_for_categorical_observations",
            "OM3.5",
        ),
        serialization_alias="OM3.5",
        title="Abnormal Text/Codes for Categorical Observations",
        description="Item #639",
    )

    om3_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_6",
            "critical_text_codes_for_categorical_observations",
            "OM3.6",
        ),
        serialization_alias="OM3.6",
        title="Critical Text Codes for Categorical Observations",
        description="Item #640",
    )

    om3_7: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "om3_7",
            "value_type",
            "OM3.7",
        ),
        serialization_alias="OM3.7",
        title="Value Type",
        description="Item #570 | Table HL70125",
    )

    model_config = {"populate_by_name": True}
