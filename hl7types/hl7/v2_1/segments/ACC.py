"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ACC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class ACC(BaseModel):
    """HL7 v2 ACC segment.

    Attributes
    ----------
    acc_1 : str | None
        ACC.1 (opt) - ACCIDENT DATE/TIME (TS)

    acc_2 : str | None
        ACC.2 (opt) - ACCIDENT CODE (ID)

    acc_3 : str | None
        ACC.3 (opt) - ACCIDENT LOCATION (ST)
    """

    acc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_1",
            "accident_date_time",
            "ACC.1",
        ),
        serialization_alias="ACC.1",
        title="ACCIDENT DATE/TIME",
        description="Item #182",
    )

    acc_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_2",
            "accident_code",
            "ACC.2",
        ),
        serialization_alias="ACC.2",
        title="ACCIDENT CODE",
        description="Item #184 | Table HL70050",
    )

    acc_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_3",
            "accident_location",
            "ACC.3",
        ),
        serialization_alias="ACC.3",
        title="ACCIDENT LOCATION",
        description="Item #185",
    )

    model_config = {"populate_by_name": True}
