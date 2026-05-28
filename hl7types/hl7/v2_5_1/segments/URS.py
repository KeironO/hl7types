"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: URS
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.TQ import TQ
from ..datatypes.TS import TS


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
        title="R/U Where Subject Definition",
        description="Item #52",
    )

    urs_2: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_2",
            "r_u_when_data_start_date_time",
            "URS.2",
        ),
        serialization_alias="URS.2",
        title="R/U When Data Start Date/Time",
        description="Item #53",
    )

    urs_3: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_3",
            "r_u_when_data_end_date_time",
            "URS.3",
        ),
        serialization_alias="URS.3",
        title="R/U When Data End Date/Time",
        description="Item #54",
    )

    urs_4: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_4",
            "r_u_what_user_qualifier",
            "URS.4",
        ),
        serialization_alias="URS.4",
        title="R/U What User Qualifier",
        description="Item #55",
    )

    urs_5: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_5",
            "r_u_other_results_subject_definition",
            "URS.5",
        ),
        serialization_alias="URS.5",
        title="R/U Other Results Subject Definition",
        description="Item #56",
    )

    urs_6: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_6",
            "r_u_which_date_time_qualifier",
            "URS.6",
        ),
        serialization_alias="URS.6",
        title="R/U Which Date/Time Qualifier",
        description="Item #57 | Table HL70156",
    )

    urs_7: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_7",
            "r_u_which_date_time_status_qualifier",
            "URS.7",
        ),
        serialization_alias="URS.7",
        title="R/U Which Date/Time Status Qualifier",
        description="Item #58 | Table HL70157",
    )

    urs_8: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_8",
            "r_u_date_time_selection_qualifier",
            "URS.8",
        ),
        serialization_alias="URS.8",
        title="R/U Date/Time Selection Qualifier",
        description="Item #59 | Table HL70158",
    )

    urs_9: TQ | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_9",
            "r_u_quantity_timing_qualifier",
            "URS.9",
        ),
        serialization_alias="URS.9",
        title="R/U Quantity/Timing Qualifier",
        description="Item #695",
    )

    model_config = {"populate_by_name": True}
