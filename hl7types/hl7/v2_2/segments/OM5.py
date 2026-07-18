"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: OM5
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class OM5(HL7Model):
    """OBSERVATION BATTERIES (S7.6.8).

    Attributes
    ----------
    om5_1 : str | None
        OM5.1 - Segment Type ID (ST) NA S7.6.9.1

    om5_2 : str | None
        OM5.2 - Sequence Number - Test/ Observation Master File (NM) NA S7.6.9.2

    om5_3 : list[CE] | None
        OM5.3 - Tests / observations included within an ordered test battery (CE) NA rep S7.6.8.3

    om5_4 : str | None
        OM5.4 - Observation ID Suffixes (ST) NA S7.6.8.4
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
        description="NA | Item #00585 | LEN:3",
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
        description="NA | Item #00586 | LEN:4",
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
        description="NA | Item #00655",
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
        description="NA | Item #00656 | LEN:200",
    )

    @field_validator("om5_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
