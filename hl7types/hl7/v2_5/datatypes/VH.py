"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: VH
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class VH(BaseModel):
    """HL7 v2 VH data type."""

    vh_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "vh_1",
            "start_day_range",
            "VH.1",
        ),
        serialization_alias="VH.1",
        title="Start Day Range",
    )

    vh_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "vh_2",
            "end_day_range",
            "VH.2",
        ),
        serialization_alias="VH.2",
        title="End Day Range",
    )

    vh_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "vh_3",
            "start_hour_range",
            "VH.3",
        ),
        serialization_alias="VH.3",
        title="Start Hour Range",
    )

    vh_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "vh_4",
            "end_hour_range",
            "VH.4",
        ),
        serialization_alias="VH.4",
        title="End Hour Range",
    )

    model_config = {"populate_by_name": True}
