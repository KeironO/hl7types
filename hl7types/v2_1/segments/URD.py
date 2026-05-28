"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: URD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field


class URD(BaseModel):
    """HL7 v2 URD segment."""

    urd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_1",
            "r_u_date_time",
            "URD.1",
        ),
        serialization_alias="URD.1",
        title="R/U DATE/TIME",
        description="Item #600",
    )

    urd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_2",
            "report_priority",
            "URD.2",
        ),
        serialization_alias="URD.2",
        title="REPORT PRIORITY",
        description="Item #601 | Table HL70109",
    )

    urd_3: List[str] = Field(
        default=...,
        validation_alias=AliasChoices(
            "urd_3",
            "r_u_who_subject_definition",
            "URD.3",
        ),
        serialization_alias="URD.3",
        title="R/U WHO SUBJECT DEFINITION",
        description="Item #602",
    )

    urd_4: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_4",
            "r_u_what_subject_definition",
            "URD.4",
        ),
        serialization_alias="URD.4",
        title="R/U WHAT SUBJECT DEFINITION",
        description="Item #603 | Table HL70048",
    )

    urd_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_5",
            "r_u_what_department_code",
            "URD.5",
        ),
        serialization_alias="URD.5",
        title="R/U WHAT DEPARTMENT CODE",
        description="Item #605",
    )

    urd_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_6",
            "r_u_display_print_locations",
            "URD.6",
        ),
        serialization_alias="URD.6",
        title="R/U DISPLAY/PRINT LOCATIONS",
        description="Item #607",
    )

    urd_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_7",
            "r_u_results_level",
            "URD.7",
        ),
        serialization_alias="URD.7",
        title="R/U RESULTS LEVEL",
        description="Item #702 | Table HL70108",
    )

    model_config = {"populate_by_name": True}
