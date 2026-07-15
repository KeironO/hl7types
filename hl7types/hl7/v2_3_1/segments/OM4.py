"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OM4
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CQ import CQ


class OM4(HL7Model):
    """OM4 - observations that require specimens segment (S8.7.6).

    Attributes
    ----------
    om4_1 : str | None
        OM4.1 - Sequence Number - Test/Observation Master File (NM) NA S8.7.8.1

    om4_2 : str | None
        OM4.2 - Derived Specimen (ID) NA S8.7.6.2 | 0170 - Derived specimen

    om4_3 : str | None
        OM4.3 - Container Description (TX) NA S8.7.6.3

    om4_4 : str | None
        OM4.4 - Container Volume (NM) NA S8.7.6.4

    om4_5 : CE | None
        OM4.5 - Container Units (CE) NA S8.7.6.5

    om4_6 : CE | None
        OM4.6 - Specimen (CE) NA S8.7.6.6

    om4_7 : CE | None
        OM4.7 - Additive (CE) NA S8.7.6.7

    om4_8 : str | None
        OM4.8 - Preparation (TX) NA S8.7.6.8

    om4_9 : str | None
        OM4.9 - Special Handling Requirements (TX) NA S8.7.6.9

    om4_10 : CQ | None
        OM4.10 - Normal Collection Volume (CQ) NA S8.7.6.10

    om4_11 : CQ | None
        OM4.11 - Minimum Collection Volume (CQ) NA S8.7.6.11

    om4_12 : str | None
        OM4.12 - Specimen Requirements (TX) NA S8.7.6.12

    om4_13 : list[str] | None
        OM4.13 - Specimen Priorities (ID) NA rep S8.7.6.13 | 0027 - Priority

    om4_14 : CQ | None
        OM4.14 - Specimen Retention Time (CQ) NA S8.7.6.14
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
        description="NA | Item #00586 | LEN:4",
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
        description="NA | Item #00642 | Table 0170 - Derived specimen | LEN:1",
    )

    om4_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_3",
            "container_description",
            "OM4.3",
        ),
        serialization_alias="OM4.3",
        title="Container Description",
        description="NA | Item #00643",
    )

    om4_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_4",
            "container_volume",
            "OM4.4",
        ),
        serialization_alias="OM4.4",
        title="Container Volume",
        description="NA | Item #00644 | LEN:20",
    )

    om4_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_5",
            "container_units",
            "OM4.5",
        ),
        serialization_alias="OM4.5",
        title="Container Units",
        description="NA | Item #00645",
    )

    om4_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_6",
            "specimen",
            "OM4.6",
        ),
        serialization_alias="OM4.6",
        title="Specimen",
        description="NA | Item #00646",
    )

    om4_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_7",
            "additive",
            "OM4.7",
        ),
        serialization_alias="OM4.7",
        title="Additive",
        description="NA | Item #00647",
    )

    om4_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_8",
            "preparation",
            "OM4.8",
        ),
        serialization_alias="OM4.8",
        title="Preparation",
        description="NA | Item #00648",
    )

    om4_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_9",
            "special_handling_requirements",
            "OM4.9",
        ),
        serialization_alias="OM4.9",
        title="Special Handling Requirements",
        description="NA | Item #00649",
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
        description="NA | Item #00650",
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
        description="NA | Item #00651",
    )

    om4_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_12",
            "specimen_requirements",
            "OM4.12",
        ),
        serialization_alias="OM4.12",
        title="Specimen Requirements",
        description="NA | Item #00652",
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
        description="NA | Item #00653 | Table 0027 - Priority | LEN:1",
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
        description="NA | Item #00654",
    )

    @field_validator("om4_1", "om4_4", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
