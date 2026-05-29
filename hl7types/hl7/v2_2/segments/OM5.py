"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: OM5
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class OM5(BaseModel):
    """HL7 v2 OM5 segment.

    Attributes
    ----------
    om5_1 : str | None
        OM5.1 (opt) - Segment Type ID (ST)

    om5_2 : str | None
        OM5.2 (opt) - Sequence Number - Test/ Observation Master File (NM)

    om5_3 : list[CE] | None
        OM5.3 (opt, rep) - Tests / observations included within an ordered test battery (CE)

    om5_4 : str | None
        OM5.4 (opt) - Observation ID Suffixes (ST)
    """

    om5_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om5_1",
            "segment_type_id",
            "OM5.1",
        ),
        serialization_alias="OM5.1",
        title="Segment Type ID",
        description="Item #585",
    )

    om5_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om5_2",
            "sequence_number_test_observation_master_file",
            "OM5.2",
        ),
        serialization_alias="OM5.2",
        title="Sequence Number - Test/ Observation Master File",
        description="Item #586",
    )

    om5_3: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om5_3",
            "tests_observations_included_within_an_ordered_test_battery",
            "OM5.3",
        ),
        serialization_alias="OM5.3",
        title="Tests / observations included within an ordered test battery",
        description="Item #655",
    )

    om5_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om5_4",
            "observation_id_suffixes",
            "OM5.4",
        ),
        serialization_alias="OM5.4",
        title="Observation ID Suffixes",
        description="Item #656",
    )

    model_config = {"populate_by_name": True}
