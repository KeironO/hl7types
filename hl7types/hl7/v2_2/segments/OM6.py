"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: OM6
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.TX import TX


class OM6(BaseModel):
    """HL7 v2 OM6 segment."""

    om6_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om6_1",
            "segment_type_id",
            "OM6.1",
        ),
        serialization_alias="OM6.1",
        title="Segment Type ID",
        description="Item #585",
    )

    om6_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om6_2",
            "sequence_number_test_observation_master_file",
            "OM6.2",
        ),
        serialization_alias="OM6.2",
        title="Sequence Number - Test/ Observation Master File",
        description="Item #586",
    )

    om6_3: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om6_3",
            "derivation_rule",
            "OM6.3",
        ),
        serialization_alias="OM6.3",
        title="Derivation Rule",
        description="Item #657",
    )

    model_config = {"populate_by_name": True}
