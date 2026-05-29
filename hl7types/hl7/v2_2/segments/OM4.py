"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: OM4
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.TX import TX


class OM4(BaseModel):
    """HL7 v2 OM4 segment.

    Attributes
    ----------
    om4_1 : str | None
        OM4.1 (opt) - Segment Type ID (ST)

    om4_2 : str | None
        OM4.2 (opt) - Sequence Number - Test/ Observation Master File (NM)

    om4_3 : str | None
        OM4.3 (opt) - Derived Specimen (ID)

    om4_4 : TX | None
        OM4.4 (opt) - Container Description (TX)

    om4_5 : str | None
        OM4.5 (opt) - Container Volume (NM)

    om4_6 : CE | None
        OM4.6 (opt) - Container Units (CE)

    om4_7 : CE | None
        OM4.7 (opt) - Specimen (CE)

    om4_8 : CE | None
        OM4.8 (opt) - Additive (CE)

    om4_9 : TX | None
        OM4.9 (opt) - Preparation (TX)

    om4_10 : TX | None
        OM4.10 (opt) - Special Handling Requirements (TX)

    om4_11 : str | None
        OM4.11 (opt) - Normal Collection Volume (CQ)

    om4_12 : str | None
        OM4.12 (opt) - Minimum Collection Volume (CQ)

    om4_13 : TX | None
        OM4.13 (opt) - Specimen Requirements (TX)

    om4_14 : list[str] | None
        OM4.14 (opt, rep) - Specimen Priorities (ID)

    om4_15 : str | None
        OM4.15 (opt) - Specimen Retention Time (CQ)
    """

    om4_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_1",
            "segment_type_id",
            "OM4.1",
        ),
        serialization_alias="OM4.1",
        title="Segment Type ID",
        description="Item #585",
    )

    om4_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_2",
            "sequence_number_test_observation_master_file",
            "OM4.2",
        ),
        serialization_alias="OM4.2",
        title="Sequence Number - Test/ Observation Master File",
        description="Item #586",
    )

    om4_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_3",
            "derived_specimen",
            "OM4.3",
        ),
        serialization_alias="OM4.3",
        title="Derived Specimen",
        description="Item #642 | Table HL70170",
    )

    om4_4: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_4",
            "container_description",
            "OM4.4",
        ),
        serialization_alias="OM4.4",
        title="Container Description",
        description="Item #643",
    )

    om4_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_5",
            "container_volume",
            "OM4.5",
        ),
        serialization_alias="OM4.5",
        title="Container Volume",
        description="Item #644",
    )

    om4_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_6",
            "container_units",
            "OM4.6",
        ),
        serialization_alias="OM4.6",
        title="Container Units",
        description="Item #645",
    )

    om4_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_7",
            "specimen",
            "OM4.7",
        ),
        serialization_alias="OM4.7",
        title="Specimen",
        description="Item #646",
    )

    om4_8: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_8",
            "additive",
            "OM4.8",
        ),
        serialization_alias="OM4.8",
        title="Additive",
        description="Item #647",
    )

    om4_9: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_9",
            "preparation",
            "OM4.9",
        ),
        serialization_alias="OM4.9",
        title="Preparation",
        description="Item #648",
    )

    om4_10: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_10",
            "special_handling_requirements",
            "OM4.10",
        ),
        serialization_alias="OM4.10",
        title="Special Handling Requirements",
        description="Item #649",
    )

    om4_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_11",
            "normal_collection_volume",
            "OM4.11",
        ),
        serialization_alias="OM4.11",
        title="Normal Collection Volume",
        description="Item #650",
    )

    om4_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_12",
            "minimum_collection_volume",
            "OM4.12",
        ),
        serialization_alias="OM4.12",
        title="Minimum Collection Volume",
        description="Item #651",
    )

    om4_13: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_13",
            "specimen_requirements",
            "OM4.13",
        ),
        serialization_alias="OM4.13",
        title="Specimen Requirements",
        description="Item #652",
    )

    om4_14: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_14",
            "specimen_priorities",
            "OM4.14",
        ),
        serialization_alias="OM4.14",
        title="Specimen Priorities",
        description="Item #653 | Table HL70027",
    )

    om4_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_15",
            "specimen_retention_time",
            "OM4.15",
        ),
        serialization_alias="OM4.15",
        title="Specimen Retention Time",
        description="Item #654",
    )

    model_config = {"populate_by_name": True}
