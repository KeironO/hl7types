"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: URS
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class URS(BaseModel):
    """HL7 v2 URS segment."""

    urs_1: list[str] = Field(
        default=...,
        validation_alias=AliasChoices(
            "urs_1",
            "r_u_where_subject_definition",
            "URS.1",
        ),
        serialization_alias="URS.1",
        title="R/U WHERE SUBJECT DEFINITION",
        description="Item #608",
    )

    urs_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_2",
            "r_u_when_data_start_date_time",
            "URS.2",
        ),
        serialization_alias="URS.2",
        title="R/U WHEN DATA START DATE/TIME",
        description="Item #609",
    )

    urs_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_3",
            "r_u_when_data_end_date_time",
            "URS.3",
        ),
        serialization_alias="URS.3",
        title="R/U WHEN DATA END DATE/TIME",
        description="Item #610",
    )

    urs_4: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_4",
            "r_u_what_user_qualifier",
            "URS.4",
        ),
        serialization_alias="URS.4",
        title="R/U WHAT USER QUALIFIER",
        description="Item #611",
    )

    urs_5: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_5",
            "r_u_other_results_subject_defini",
            "URS.5",
        ),
        serialization_alias="URS.5",
        title="R/U OTHER RESULTS SUBJECT DEFINI",
        description="Item #612",
    )

    model_config = {"populate_by_name": True}
