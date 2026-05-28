"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ACC
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
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
        title="Accident Date/Time",
        description="Item #527",
    )

    acc_2: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_2",
            "accident_code",
            "ACC.2",
        ),
        serialization_alias="ACC.2",
        title="Accident Code",
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
        title="Accident Location",
        description="Item #529",
    )

    acc_4: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_4",
            "auto_accident_state",
            "ACC.4",
        ),
        serialization_alias="ACC.4",
        title="Auto Accident State",
        description="Item #812 | Table HL70347",
    )

    acc_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_5",
            "accident_job_related_indicator",
            "ACC.5",
        ),
        serialization_alias="ACC.5",
        title="Accident Job Related Indicator",
        description="Item #813 | Table HL70136",
    )

    acc_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_6",
            "accident_death_indicator",
            "ACC.6",
        ),
        serialization_alias="ACC.6",
        title="Accident Death Indicator",
        description="Item #814 | Table HL70136",
    )

    model_config = {"populate_by_name": True}
