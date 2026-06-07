"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OM6
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class OM6(HL7Model):
    """HL7 v2 OM6 segment.

    Attributes
    ----------
    om6_1 : str | None
        OM6.1 (opt) - Sequence Number - Test/Observation Master File (NM)

    om6_2 : str | None
        OM6.2 (opt) - Derivation Rule (TX)
    """

    om6_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om6_1",
            "sequence_number_test_observation_master_file",
            "OM6.1",
        ),
        serialization_alias="OM6.1",
        title="Sequence Number - Test/Observation Master File",
        description="Item #586",
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
        description="Item #657",
    )

    @field_validator("om6_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
