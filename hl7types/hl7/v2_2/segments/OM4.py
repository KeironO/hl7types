"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: OM4
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class OM4(HL7Model):
    """OBSERVATION that require specimens (S7.6.7).

    Attributes
    ----------
    om4_1 : str | None
        OM4.1 - Segment Type ID (ST) NA S7.6.9.1

    om4_2 : str | None
        OM4.2 - Sequence Number - Test/ Observation Master File (NM) NA S7.6.9.2

    om4_3 : str | None
        OM4.3 - Derived Specimen (ID) NA S7.6.7.3 | 0170 - DERIVED SPECIMEN

    om4_4 : str | None
        OM4.4 - Container Description (TX) NA S7.6.7.4

    om4_5 : str | None
        OM4.5 - Container Volume (NM) NA S7.6.7.5

    om4_6 : CE | None
        OM4.6 - Container Units (CE) O S7.6.7.6

    om4_7 : CE | None
        OM4.7 - Specimen (CE) NA S7.6.7.7

    om4_8 : CE | None
        OM4.8 - Additive (CE) NA S7.6.7.8

    om4_9 : str | None
        OM4.9 - Preparation (TX) NA S7.6.7.9

    om4_10 : str | None
        OM4.10 - Special Handling Requirements (TX) NA S7.6.7.10

    om4_11 : str | None
        OM4.11 - Normal Collection Volume (CQ) NA S7.6.7.11

    om4_12 : str | None
        OM4.12 - Minimum Collection Volume (CQ) NA S7.6.7.12

    om4_13 : str | None
        OM4.13 - Specimen Requirements (TX) NA S7.6.7.13

    om4_14 : list[str] | None
        OM4.14 - Specimen Priorities (ID) NA rep S7.6.7.14 | 0027 - PRIORITY (COMPONENT 6 QTY/TIMING[735])

    om4_15 : str | None
        OM4.15 - Specimen Retention Time (CQ) NA S7.6.7.15
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
        description="NA | Item #00585 | LEN:3",
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
        description="NA | Item #00586 | LEN:4",
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
        description="NA | Item #00642 | Table 0170 - DERIVED SPECIMEN | LEN:1",
    )

    om4_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_4",
            "container_description",
            "OM4.4",
        ),
        serialization_alias="OM4.4",
        title="Container Description",
        description="NA | Item #00643",
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
        description="NA | Item #00644 | LEN:20",
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
        description="O | Item #00645",
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
        description="NA | Item #00646",
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
        description="NA | Item #00647",
    )

    om4_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_9",
            "preparation",
            "OM4.9",
        ),
        serialization_alias="OM4.9",
        title="Preparation",
        description="NA | Item #00648",
    )

    om4_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_10",
            "special_handling_requirements",
            "OM4.10",
        ),
        serialization_alias="OM4.10",
        title="Special Handling Requirements",
        description="NA | Item #00649",
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
        description="NA | Item #00650",
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
        description="NA | Item #00651",
    )

    om4_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_13",
            "specimen_requirements",
            "OM4.13",
        ),
        serialization_alias="OM4.13",
        title="Specimen Requirements",
        description="NA | Item #00652",
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
        description=(
            "NA | Item #00653 | Table 0027 - PRIORITY (COMPONENT 6 "
            "QTY/TIMING[735]) | LEN:60"
        ),
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
        description="NA | Item #00654",
    )

    @field_validator("om4_2", "om4_5", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
