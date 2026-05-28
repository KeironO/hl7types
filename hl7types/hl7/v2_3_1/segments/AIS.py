"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: AIS
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class AIS(BaseModel):
    """HL7 v2 AIS segment."""

    ais_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ais_1",
            "set_id_ais",
            "AIS.1",
        ),
        serialization_alias="AIS.1",
        title="Set ID - AIS",
        description="Item #890",
    )

    ais_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_2",
            "segment_action_code",
            "AIS.2",
        ),
        serialization_alias="AIS.2",
        title="Segment Action Code",
        description="Item #763 | Table HL70206",
    )

    ais_3: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "ais_3",
            "universal_service_id",
            "AIS.3",
        ),
        serialization_alias="AIS.3",
        title="Universal Service ID",
        description="Item #238",
    )

    ais_4: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_4",
            "start_date_time",
            "AIS.4",
        ),
        serialization_alias="AIS.4",
        title="Start Date/Time",
        description="Item #1202",
    )

    ais_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_5",
            "start_date_time_offset",
            "AIS.5",
        ),
        serialization_alias="AIS.5",
        title="Start Date/Time Offset",
        description="Item #891",
    )

    ais_6: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_6",
            "start_date_time_offset_units",
            "AIS.6",
        ),
        serialization_alias="AIS.6",
        title="Start Date/Time Offset Units",
        description="Item #892",
    )

    ais_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_7",
            "duration",
            "AIS.7",
        ),
        serialization_alias="AIS.7",
        title="Duration",
        description="Item #893",
    )

    ais_8: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_8",
            "duration_units",
            "AIS.8",
        ),
        serialization_alias="AIS.8",
        title="Duration Units",
        description="Item #894",
    )

    ais_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_9",
            "allow_substitution_code",
            "AIS.9",
        ),
        serialization_alias="AIS.9",
        title="Allow Substitution Code",
        description="Item #895 | Table HL70279",
    )

    ais_10: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_10",
            "filler_status_code",
            "AIS.10",
        ),
        serialization_alias="AIS.10",
        title="Filler Status Code",
        description="Item #889 | Table HL70278",
    )

    model_config = {"populate_by_name": True}
