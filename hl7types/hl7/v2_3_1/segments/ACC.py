"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ACC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class ACC(HL7Model):
    """ACC - accident segment (S6.4.9).

    Attributes
    ----------
    acc_1 : TS | None
        ACC.1 - Accident Date/Time (TS) O S6.4.9.1

    acc_2 : CE | None
        ACC.2 - Accident Code (CE) O S6.4.9.2 | 0050 - Accident Code

    acc_3 : str | None
        ACC.3 - Accident Location (ST) O S6.4.9.3

    acc_4 : CE | None
        ACC.4 - Auto Accident State (CE) O S6.4.9.4 | 0347 - Auto Accident State

    acc_5 : str | None
        ACC.5 - Accident Job Related Indicator (ID) O S6.4.9.5 | 0136 - Yes/no indicator

    acc_6 : str | None
        ACC.6 - Accident Death Indicator (ID) O S6.4.9.6 | 0136 - Yes/no indicator
    """

    acc_1: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_1",
            "accident_date_time",
            "ACC.1",
        ),
        serialization_alias="ACC.1",
        title="Accident Date/Time",
        description="O | Item #00527",
    )

    acc_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_2",
            "accident_code",
            "ACC.2",
        ),
        serialization_alias="ACC.2",
        title="Accident Code",
        description="O | Item #00528 | Table 0050 - Accident Code",
    )

    acc_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_3",
            "accident_location",
            "ACC.3",
        ),
        serialization_alias="ACC.3",
        title="Accident Location",
        description="O | Item #00529 | LEN:25",
    )

    acc_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_4",
            "auto_accident_state",
            "ACC.4",
        ),
        serialization_alias="ACC.4",
        title="Auto Accident State",
        description="O | Item #00812 | Table 0347 - Auto Accident State",
    )

    acc_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_5",
            "accident_job_related_indicator",
            "ACC.5",
        ),
        serialization_alias="ACC.5",
        title="Accident Job Related Indicator",
        description="O | Item #00813 | Table 0136 - Yes/no indicator | LEN:1",
    )

    acc_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_6",
            "accident_death_indicator",
            "ACC.6",
        ),
        serialization_alias="ACC.6",
        title="Accident Death Indicator",
        description="O | Item #00814 | Table 0136 - Yes/no indicator | LEN:12",
    )

    model_config = {"populate_by_name": True}
