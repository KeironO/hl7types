"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OM5
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class OM5(BaseModel):
    """HL7 v2 OM5 segment."""

    om5_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om5_1",
            "sequence_number_test_observation_master_file",
            "OM5.1",
        ),
        serialization_alias="OM5.1",
        title="Sequence Number - Test/ Observation Master File",
        description="Item #586",
    )

    om5_2: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om5_2",
            "test_observations_included_within_an_ordered_test_battery",
            "OM5.2",
        ),
        serialization_alias="OM5.2",
        title="Test/Observations Included within an Ordered Test Battery",
        description="Item #655 | Table HL79999",
    )

    om5_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om5_3",
            "observation_id_suffixes",
            "OM5.3",
        ),
        serialization_alias="OM5.3",
        title="Observation ID Suffixes",
        description="Item #656",
    )

    model_config = {"populate_by_name": True}
