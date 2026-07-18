"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE

_RE_SI = re.compile(r'\d*')


class CM1(HL7Model):
    """Clinical Study Phase Master (S8.10.3).

    Attributes
    ----------
    cm1_1 : str
        CM1.1 - CM1 - Set ID (SI) R S8.10.3.1

    cm1_2 : CE | None
        CM1.2 - Study Phase Identifier (CE) C S7.7.2

    cm1_3 : str
        CM1.3 - Description of Study Phase (ST) R S8.10.3.3
    """

    cm1_1: str = Field(
        validation_alias=AliasChoices(
            "cm1_1",
            "cm1_set_id",
            "CM1.1",
        ),
        serialization_alias="CM1.1",
        title="CM1 - Set ID",
        description="R | Item #01021 | LEN:4",
    )

    cm1_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm1_2",
            "study_phase_identifier",
            "CM1.2",
        ),
        serialization_alias="CM1.2",
        title="Study Phase Identifier",
        description="C | Item #01051",
    )

    cm1_3: str = Field(
        validation_alias=AliasChoices(
            "cm1_3",
            "description_of_study_phase",
            "CM1.3",
        ),
        serialization_alias="CM1.3",
        title="Description of Study Phase",
        description="R | Item #01023 | LEN:300",
    )

    @field_validator("cm1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = ConfigDict(populate_by_name=True)
