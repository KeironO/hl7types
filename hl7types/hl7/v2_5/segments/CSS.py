"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: CSS
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class CSS(HL7Model):
    """HL7 v2 CSS segment.

    Attributes
    ----------
    css_1 : CE
        CSS.1 (req) - Study Scheduled Time Point (CE)

    css_2 : TS | None
        CSS.2 (opt) - Study Scheduled Patient Time Point (TS)

    css_3 : list[CE] | None
        CSS.3 (opt, rep) - Study Quality Control Codes (CE)
    """

    css_1: CE = Field(
        validation_alias=AliasChoices(
            "css_1",
            "study_scheduled_time_point",
            "CSS.1",
        ),
        serialization_alias="CSS.1",
        title="Study Scheduled Time Point",
        description="Item #1055",
    )

    css_2: Optional[TS] = Field(
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

    css_3: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "css_3",
            "study_quality_control_codes",
            "CSS.3",
        ),
        serialization_alias="CSS.3",
        title="Study Quality Control Codes",
        description="Item #1057",
    )

    model_config = {"populate_by_name": True}
