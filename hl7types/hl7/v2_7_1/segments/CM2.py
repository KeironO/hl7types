"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CM2
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE

_RE_SI = re.compile(r'\d*')


class CM2(HL7Model):
    """Clinical Study Schedule Master (S8.11.4).

    Attributes
    ----------
    cm2_1 : str | None
        CM2.1 - Set ID- CM2 (SI) O S8.11.4.1

    cm2_2 : CWE
        CM2.2 - Scheduled Time Point (CWE) R S8.11.4.2

    cm2_3 : str | None
        CM2.3 - Description of Time Point (ST) O S8.11.4.3

    cm2_4 : list[CWE]
        CM2.4 - Events Scheduled This Time Point (CWE) R rep S8.11.4.4
    """

    cm2_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm2_1",
            "set_id_cm2",
            "CM2.1",
        ),
        serialization_alias="CM2.1",
        title="Set ID- CM2",
        description="O | Item #01024 | LEN:4",
    )

    cm2_2: CWE = Field(
        validation_alias=AliasChoices(
            "cm2_2",
            "scheduled_time_point",
            "CM2.2",
        ),
        serialization_alias="CM2.2",
        title="Scheduled Time Point",
        description="R | Item #01025",
    )

    cm2_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm2_3",
            "description_of_time_point",
            "CM2.3",
        ),
        serialization_alias="CM2.3",
        title="Description of Time Point",
        description="O | Item #01026",
    )

    cm2_4: List[CWE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "cm2_4",
            "events_scheduled_this_time_point",
            "CM2.4",
        ),
        serialization_alias="CM2.4",
        title="Events Scheduled This Time Point",
        description="R | Item #01027",
    )

    @field_validator("cm2_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = ConfigDict(populate_by_name=True)
