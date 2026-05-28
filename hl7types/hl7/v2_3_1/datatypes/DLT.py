"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: DLT
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .NR import NR


class DLT(BaseModel):
    """HL7 v2 DLT data type."""

    dlt_1: NR | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dlt_1",
            "range",
            "DLT.1",
        ),
        serialization_alias="DLT.1",
        title="Range",
    )

    dlt_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dlt_2",
            "numeric_threshold",
            "DLT.2",
        ),
        serialization_alias="DLT.2",
        title="numeric threshold",
    )

    dlt_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dlt_3",
            "change_computation",
            "DLT.3",
        ),
        serialization_alias="DLT.3",
        title="change computation",
    )

    dlt_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dlt_4",
            "length_of_time_days",
            "DLT.4",
        ),
        serialization_alias="DLT.4",
        title="length of time-days",
    )

    model_config = {"populate_by_name": True}
