"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_DTN
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class CM_DTN(HL7Model):
    """Day type and number.

    Attributes
    ----------
    cm_dtn_1 : str | None
        CM_DTN.1 (opt) - day type (IS)

    cm_dtn_2 : str | None
        CM_DTN.2 (opt) - number of days (NM)
    """

    cm_dtn_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_dtn_1",
            "day_type",
            "CM_DTN.1",
        ),
        serialization_alias="CM_DTN.1",
        title="day type",
    )

    cm_dtn_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_dtn_2",
            "number_of_days",
            "CM_DTN.2",
        ),
        serialization_alias="CM_DTN.2",
        title="number of days",
    )

    @field_validator("cm_dtn_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
