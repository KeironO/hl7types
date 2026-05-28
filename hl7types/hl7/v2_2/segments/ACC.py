"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ACC
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.TS import TS


class ACC(BaseModel):
    """HL7 v2 ACC segment."""

    acc_1: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_1",
            "accident_date_time",
            "ACC.1",
        ),
        serialization_alias="ACC.1",
        title="Accident date / time",
        description="Item #527",
    )

    acc_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_2",
            "accident_code",
            "ACC.2",
        ),
        serialization_alias="ACC.2",
        title="Accident code",
        description="Item #528 | Table HL70050",
    )

    acc_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_3",
            "accident_location",
            "ACC.3",
        ),
        serialization_alias="ACC.3",
        title="Accident location",
        description="Item #529",
    )

    model_config = {"populate_by_name": True}
