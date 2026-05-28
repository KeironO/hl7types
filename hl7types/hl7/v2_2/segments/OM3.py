"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
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
            "segment_type_id",
            "OM3.1",
        ),
        serialization_alias="OM3.1",
        title="Segment Type ID",
        description="Item #585",
    )

    om3_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_2",
            "sequence_number_test_observation_master_file",
            "OM3.2",
        ),
        serialization_alias="OM3.2",
        title="Sequence Number - Test/ Observation Master File",
        description="Item #586",
    )

    om3_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_3",
            "preferred_coding_system",
            "OM3.3",
        ),
        serialization_alias="OM3.3",
        title="Preferred Coding System",
        description="Item #636",
    )

    om3_4: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_4",
            "valid_coded_answers",
            "OM3.4",
        ),
        serialization_alias="OM3.4",
        title="Valid coded answers",
        description="Item #637",
    )

    om3_5: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_5",
            "normal_test_codes_for_categorical_observations",
            "OM3.5",
        ),
        serialization_alias="OM3.5",
        title="Normal test codes for categorical observations",
        description="Item #638",
    )

    om3_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_6",
            "abnormal_test_codes_for_categorical_observations",
            "OM3.6",
        ),
        serialization_alias="OM3.6",
        title="Abnormal test codes for categorical observations",
        description="Item #639",
    )

    om3_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_7",
            "critical_test_codes_for_categorical_observations",
            "OM3.7",
        ),
        serialization_alias="OM3.7",
        title="Critical test codes for categorical observations",
        description="Item #640",
    )

    om3_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_8",
            "data_type",
            "OM3.8",
        ),
        serialization_alias="OM3.8",
        title="Data Type",
        description="Item #641",
    )

    model_config = {"populate_by_name": True}
