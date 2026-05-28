"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: AIL
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.PL import PL


class AIL(BaseModel):
    """HL7 v2 AIL segment."""

    ail_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ail_1",
            "set_id_ail",
            "AIL.1",
        ),
        serialization_alias="AIL.1",
        title="Set ID - AIL",
        description="Item #902",
    )

    ail_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_2",
            "segment_action_code",
            "AIL.2",
        ),
        serialization_alias="AIL.2",
        title="Segment Action Code",
        description="Item #763 | Table HL70206",
    )

    ail_3: list[PL] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_3",
            "location_resource_id",
            "AIL.3",
        ),
        serialization_alias="AIL.3",
        title="Location Resource ID",
        description="Item #903",
    )

    ail_4: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_4",
            "location_type_ail",
            "AIL.4",
        ),
        serialization_alias="AIL.4",
        title="Location Type - AIL",
        description="Item #904 | Table HL70305",
    )

    ail_5: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_5",
            "location_group",
            "AIL.5",
        ),
        serialization_alias="AIL.5",
        title="Location Group",
        description="Item #905",
    )

    ail_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_6",
            "start_date_time",
            "AIL.6",
        ),
        serialization_alias="AIL.6",
        title="Start Date/Time",
        description="Item #1202",
    )

    ail_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_7",
            "start_date_time_offset",
            "AIL.7",
        ),
        serialization_alias="AIL.7",
        title="Start Date/Time Offset",
        description="Item #891",
    )

    ail_8: CNE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_8",
            "start_date_time_offset_units",
            "AIL.8",
        ),
        serialization_alias="AIL.8",
        title="Start Date/Time Offset Units",
        description="Item #892",
    )

    ail_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_9",
            "duration",
            "AIL.9",
        ),
        serialization_alias="AIL.9",
        title="Duration",
        description="Item #893",
    )

    ail_10: CNE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_10",
            "duration_units",
            "AIL.10",
        ),
        serialization_alias="AIL.10",
        title="Duration Units",
        description="Item #894",
    )

    ail_11: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_11",
            "allow_substitution_code",
            "AIL.11",
        ),
        serialization_alias="AIL.11",
        title="Allow Substitution Code",
        description="Item #895 | Table HL70279",
    )

    ail_12: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_12",
            "filler_status_code",
            "AIL.12",
        ),
        serialization_alias="AIL.12",
        title="Filler Status Code",
        description="Item #889 | Table HL70278",
    )

    model_config = {"populate_by_name": True}
