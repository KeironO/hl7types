"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CM2
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class CM2(HL7Model):
    """HL7 v2 CM2 segment.

    Attributes
    ----------
    cm2_1 : str | None
        CM2.1 (opt) - Set ID- CM2 (SI)

    cm2_2 : CWE
        CM2.2 (req) - Scheduled Time Point (CWE)

    cm2_3 : str | None
        CM2.3 (opt) - Description of Time Point (ST)

    cm2_4 : list[CWE] | None
        CM2.4 (req, rep) - Events Scheduled This Time Point (CWE) [optional: CWE has no required components]
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
        description="Item #1024",
    )

    cm2_2: CWE = Field(
        validation_alias=AliasChoices(
            "cm2_2",
            "scheduled_time_point",
            "CM2.2",
        ),
        serialization_alias="CM2.2",
        title="Scheduled Time Point",
        description="Item #1025",
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
        description="Item #1026",
    )

    cm2_4: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm2_4",
            "events_scheduled_this_time_point",
            "CM2.4",
        ),
        serialization_alias="CM2.4",
        title="Events Scheduled This Time Point",
        description="Item #1027",
    )

    @field_validator("cm2_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
