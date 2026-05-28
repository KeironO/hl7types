"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_NDL
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .TS import TS


class CM_NDL(BaseModel):
    """HL7 v2 CM_NDL data type."""

    cm_ndl_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ndl_1",
            "interpreter_technician",
            "CM_NDL.1",
        ),
        serialization_alias="CM_NDL.1",
        title="interpreter / technician",
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
            "location",
            "CM_NDL.4",
        ),
        serialization_alias="CM_NDL.4",
        title="location",
    )

    model_config = {"populate_by_name": True}
