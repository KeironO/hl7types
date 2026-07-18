"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OM5
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class OM5(HL7Model):
    """Observation Batteries (Sets) (S8.8.12).

    Attributes
    ----------
    om5_1 : str | None
        OM5.1 - Sequence Number - Test/Observation Master File (NM) O S8.8.10.1

    om5_2 : list[CWE] | None
        OM5.2 - Test/Observations Included Within an Ordered Test Battery (CWE) O rep S8.8.12.2 | 9999 - no table for CE

    om5_3 : str | None
        OM5.3 - Observation ID Suffixes (ST) O S8.8.12.3
    """

    om5_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om5_1",
            "sequence_number_test_observation_master_file",
            "OM5.1",
        ),
        serialization_alias="OM5.1",
        title="Sequence Number - Test/Observation Master File",
        description="O | Item #00586",
    )

    om5_2: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om5_2",
            "test_observations_included_within_an_ordered_test_battery",
            "OM5.2",
        ),
        serialization_alias="OM5.2",
        title="Test/Observations Included Within an Ordered Test Battery",
        description="O | Item #00655 | Table 9999 - no table for CE",
    )

    om5_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om5_3",
            "observation_id_suffixes",
            "OM5.3",
        ),
        serialization_alias="OM5.3",
        title="Observation ID Suffixes",
        description="O | Item #00656",
    )

    @field_validator("om5_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
