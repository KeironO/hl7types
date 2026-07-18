"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
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
    """OBSERVATIONS that are calculated from other obersvations (S7.6.9).

    Attributes
    ----------
    om6_1 : str | None
        OM6.1 - Segment Type ID (ST) NA S7.6.9.1

    om6_2 : str | None
        OM6.2 - Sequence Number - Test/ Observation Master File (NM) NA S7.6.9.2

    om6_3 : str | None
        OM6.3 - Derivation Rule (TX) NA S7.6.9.3
    """

    om6_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om6_1",
            "segment_type_id",
            "OM6.1",
        ),
        serialization_alias="OM6.1",
        title="Segment Type ID",
        description="NA | Item #00585 | LEN:3",
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
        description="NA | Item #00586 | LEN:4",
    )

    om6_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om6_3",
            "derivation_rule",
            "OM6.3",
        ),
        serialization_alias="OM6.3",
        title="Derivation Rule",
        description="NA | Item #00657",
    )

    @field_validator("om6_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
