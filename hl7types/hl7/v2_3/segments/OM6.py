"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: OM6
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class OM6(HL7Model):
    """Observations that are calculated from other observations (S8.7.8).

    Attributes
    ----------
    om6_1 : str | None
        OM6.1 - Sequence Number - Test/ Observation Master File (NM) O S8.7.3

    om6_2 : str | None
        OM6.2 - Derivation Rule (TX) O S8.7.8.2
    """

    om6_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om6_1",
            "sequence_number_test_observation_master_file",
            "OM6.1",
        ),
        serialization_alias="OM6.1",
        title="Sequence Number - Test/ Observation Master File",
        description="O | Item #00586 | LEN:4",
    )

    om6_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om6_2",
            "derivation_rule",
            "OM6.2",
        ),
        serialization_alias="OM6.2",
        title="Derivation Rule",
        description="O | Item #00657",
    )

    @field_validator("om6_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
