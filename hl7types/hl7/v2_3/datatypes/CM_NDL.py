"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_NDL
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CN import CN
from .HD import HD
from .TS import TS


class CM_NDL(BaseModel):
    """HL7 v2 CM_NDL data type."""

    cm_ndl_1: CN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ndl_1",
            "name",
            "CM_NDL.1",
        ),
        serialization_alias="CM_NDL.1",
        title="name",
    )

    cm_ndl_2: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ndl_2",
            "start_date_time",
            "CM_NDL.2",
        ),
        serialization_alias="CM_NDL.2",
        title="start date/time",
    )

    cm_ndl_3: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ndl_3",
            "end_date_time",
            "CM_NDL.3",
        ),
        serialization_alias="CM_NDL.3",
        title="end date/time",
    )

    cm_ndl_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ndl_4",
            "point_of_care_is",
            "CM_NDL.4",
        ),
        serialization_alias="CM_NDL.4",
        title="point of care (IS)",
    )

    cm_ndl_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ndl_5",
            "room",
            "CM_NDL.5",
        ),
        serialization_alias="CM_NDL.5",
        title="room",
    )

    cm_ndl_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ndl_6",
            "bed",
            "CM_NDL.6",
        ),
        serialization_alias="CM_NDL.6",
        title="bed",
    )

    cm_ndl_7: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ndl_7",
            "facility_hd",
            "CM_NDL.7",
        ),
        serialization_alias="CM_NDL.7",
        title="facility (HD)",
    )

    cm_ndl_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ndl_8",
            "location_status",
            "CM_NDL.8",
        ),
        serialization_alias="CM_NDL.8",
        title="location status",
    )

    cm_ndl_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ndl_9",
            "person_location_type",
            "CM_NDL.9",
        ),
        serialization_alias="CM_NDL.9",
        title="person location type",
    )

    cm_ndl_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ndl_10",
            "building",
            "CM_NDL.10",
        ),
        serialization_alias="CM_NDL.10",
        title="building",
    )

    cm_ndl_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ndl_11",
            "floor",
            "CM_NDL.11",
        ),
        serialization_alias="CM_NDL.11",
        title="floor",
    )

    model_config = {"populate_by_name": True}
