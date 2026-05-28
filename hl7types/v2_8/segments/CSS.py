"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CSS
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE


class CSS(BaseModel):
    """HL7 v2 CSS segment."""

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

    model_config = {"populate_by_name": True}
