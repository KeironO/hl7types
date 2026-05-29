"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OM4
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.TX import TX


class OM4(BaseModel):
    """HL7 v2 OM4 segment.

    Attributes
    ----------
    om4_1 : str | None
        OM4.1 (opt) - Sequence Number - Test/Observation Master File (NM)

    om4_2 : str | None
        OM4.2 (opt) - Derived Specimen (ID)

    om4_3 : list[TX] | None
        OM4.3 (opt, rep) - Container Description (TX)

    om4_4 : list[str] | None
        OM4.4 (opt, rep) - Container Volume (NM)

    om4_5 : list[CWE] | None
        OM4.5 (opt, rep) - Container Units (CWE)

    om4_6 : CWE | None
        OM4.6 (opt) - Specimen (CWE)

    om4_7 : CWE | None
        OM4.7 (opt) - Additive (CWE)

    om4_8 : TX | None
        OM4.8 (opt) - Preparation (TX)

    om4_9 : TX | None
        OM4.9 (opt) - Special Handling Requirements (TX)

    om4_10 : CQ | None
        OM4.10 (opt) - Normal Collection Volume (CQ)

    om4_11 : CQ | None
        OM4.11 (opt) - Minimum Collection Volume (CQ)

    om4_12 : TX | None
        OM4.12 (opt) - Specimen Requirements (TX)

    om4_13 : list[str] | None
        OM4.13 (opt, rep) - Specimen Priorities (ID)

    om4_14 : CQ | None
        OM4.14 (opt) - Specimen Retention Time (CQ)

    om4_15 : list[CWE] | None
        OM4.15 (opt, rep) - Specimen Handling Code (CWE)

    om4_16 : str | None
        OM4.16 (opt) - Specimen Preference (ID)

    om4_17 : str | None
        OM4.17 (opt) - Preferred Specimen/Attribture Sequence ID (NM)

    om4_18 : list[CWE] | None
        OM4.18 (opt, rep) - Taxonomic Classification Code (CWE)
    """

    om4_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_1",
            "sequence_number_test_observation_master_file",
            "OM4.1",
        ),
        serialization_alias="OM4.1",
        title="Sequence Number - Test/Observation Master File",
        description="Item #586",
    )

    om4_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_2",
            "derived_specimen",
            "OM4.2",
        ),
        serialization_alias="OM4.2",
        title="Derived Specimen",
        description="Item #642 | Table HL70170",
    )

    om4_3: Optional[List[TX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_3",
            "container_description",
            "OM4.3",
        ),
        serialization_alias="OM4.3",
        title="Container Description",
        description="Item #643",
    )

    om4_4: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_4",
            "container_volume",
            "OM4.4",
        ),
        serialization_alias="OM4.4",
        title="Container Volume",
        description="Item #644",
    )

    om4_5: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_5",
            "container_units",
            "OM4.5",
        ),
        serialization_alias="OM4.5",
        title="Container Units",
        description="Item #645 | Table HL79999",
    )

    om4_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_6",
            "specimen",
            "OM4.6",
        ),
        serialization_alias="OM4.6",
        title="Specimen",
        description="Item #646 | Table HL79999",
    )

    om4_7: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_7",
            "additive",
            "OM4.7",
        ),
        serialization_alias="OM4.7",
        title="Additive",
        description="Item #647 | Table HL70371",
    )

    om4_8: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_8",
            "preparation",
            "OM4.8",
        ),
        serialization_alias="OM4.8",
        title="Preparation",
        description="Item #648",
    )

    om4_9: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_9",
            "special_handling_requirements",
            "OM4.9",
        ),
        serialization_alias="OM4.9",
        title="Special Handling Requirements",
        description="Item #649",
    )

    om4_10: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_10",
            "normal_collection_volume",
            "OM4.10",
        ),
        serialization_alias="OM4.10",
        title="Normal Collection Volume",
        description="Item #650",
    )

    om4_11: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_11",
            "minimum_collection_volume",
            "OM4.11",
        ),
        serialization_alias="OM4.11",
        title="Minimum Collection Volume",
        description="Item #651",
    )

    om4_12: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_12",
            "specimen_requirements",
            "OM4.12",
        ),
        serialization_alias="OM4.12",
        title="Specimen Requirements",
        description="Item #652",
    )

    om4_13: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_13",
            "specimen_priorities",
            "OM4.13",
        ),
        serialization_alias="OM4.13",
        title="Specimen Priorities",
        description="Item #653 | Table HL70027",
    )

    om4_14: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_14",
            "specimen_retention_time",
            "OM4.14",
        ),
        serialization_alias="OM4.14",
        title="Specimen Retention Time",
        description="Item #654",
    )

    om4_15: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_15",
            "specimen_handling_code",
            "OM4.15",
        ),
        serialization_alias="OM4.15",
        title="Specimen Handling Code",
        description="Item #1908 | Table HL70376",
    )

    om4_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_16",
            "specimen_preference",
            "OM4.16",
        ),
        serialization_alias="OM4.16",
        title="Specimen Preference",
        description="Item #3311 | Table HL70920",
    )

    om4_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_17",
            "preferred_specimen_attribture_sequence_id",
            "OM4.17",
        ),
        serialization_alias="OM4.17",
        title="Preferred Specimen/Attribture Sequence ID",
        description="Item #3312",
    )

    om4_18: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_18",
            "taxonomic_classification_code",
            "OM4.18",
        ),
        serialization_alias="OM4.18",
        title="Taxonomic Classification Code",
        description="Item #1539",
    )

    model_config = {"populate_by_name": True}
