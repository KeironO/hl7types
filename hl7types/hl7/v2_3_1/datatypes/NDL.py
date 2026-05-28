"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: NDL
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CN import CN
from .HD import HD
from .TS import TS


class NDL(BaseModel):
    """HL7 v2 NDL data type."""

    ndl_1: Optional[CN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_1",
            "name",
            "NDL.1",
        ),
        serialization_alias="NDL.1",
        title="name",
    )

    ndl_2: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_2",
            "start_date_time",
            "NDL.2",
        ),
        serialization_alias="NDL.2",
        title="start date/time",
    )

    ndl_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_3",
            "end_date_time",
            "NDL.3",
        ),
        serialization_alias="NDL.3",
        title="end date/time",
    )

    ndl_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_4",
            "point_of_care_is",
            "NDL.4",
        ),
        serialization_alias="NDL.4",
        title="point of care (IS)",
    )

    ndl_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_5",
            "room",
            "NDL.5",
        ),
        serialization_alias="NDL.5",
        title="room",
    )

    ndl_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_6",
            "bed",
            "NDL.6",
        ),
        serialization_alias="NDL.6",
        title="bed",
    )

    ndl_7: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_7",
            "facility_hd",
            "NDL.7",
        ),
        serialization_alias="NDL.7",
        title="facility (HD)",
    )

    ndl_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_8",
            "location_status",
            "NDL.8",
        ),
        serialization_alias="NDL.8",
        title="location status",
    )

    ndl_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_9",
            "person_location_type",
            "NDL.9",
        ),
        serialization_alias="NDL.9",
        title="person location type",
    )

    ndl_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_10",
            "building",
            "NDL.10",
        ),
        serialization_alias="NDL.10",
        title="building",
    )

    ndl_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_11",
            "floor",
            "NDL.11",
        ),
        serialization_alias="NDL.11",
        title="floor",
    )

    model_config = {"populate_by_name": True}
