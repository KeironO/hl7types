"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CSS
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CWE import CWE


class CSS(HL7Model):
    """HL7 v2 CSS segment.

    Attributes
    ----------
    css_1 : CWE
        CSS.1 (req) - Study Scheduled Time Point (CWE)

    css_2 : str | None
        CSS.2 (opt) - Study Scheduled Patient Time Point (DTM)

    css_3 : list[CWE] | None
        CSS.3 (opt, rep) - Study Quality Control Codes (CWE)
    """

    css_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "css_1",
            "study_scheduled_time_point",
            "CSS.1",
        ),
        serialization_alias="CSS.1",
        title="Study Scheduled Time Point",
        description="Item #1055 | Table HL79999",
    )

    css_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "css_2",
            "study_scheduled_patient_time_point",
            "CSS.2",
        ),
        serialization_alias="CSS.2",
        title="Study Scheduled Patient Time Point",
        description="Item #1056",
    )

    css_3: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "css_3",
            "study_quality_control_codes",
            "CSS.3",
        ),
        serialization_alias="CSS.3",
        title="Study Quality Control Codes",
        description="Item #1057 | Table HL79999",
    )

    @field_validator("css_2", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
