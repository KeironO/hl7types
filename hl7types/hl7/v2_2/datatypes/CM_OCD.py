"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_OCD
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class CM_OCD(HL7Model):
    """Occurence.

    Attributes
    ----------
    cm_ocd_1 : str | None
        CM_OCD.1 (opt) - occurrence code (ID)

    cm_ocd_2 : str | None
        CM_OCD.2 (opt) - occurrence date (DT)
    """

    cm_ocd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ocd_1",
            "occurrence_code",
            "CM_OCD.1",
        ),
        serialization_alias="CM_OCD.1",
        title="occurrence code",
    )

    cm_ocd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ocd_2",
            "occurrence_date",
            "CM_OCD.2",
        ),
        serialization_alias="CM_OCD.2",
        title="occurrence date",
    )

    @field_validator("cm_ocd_2", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
