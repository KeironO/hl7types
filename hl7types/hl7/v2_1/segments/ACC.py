"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ACC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class ACC(HL7Model):
    """ACCIDENT.

    Attributes
    ----------
    acc_1 : str | None
        ACC.1 - ACCIDENT DATE/TIME (TS) O S6-3

    acc_2 : str | None
        ACC.2 - ACCIDENT CODE (ID) O | 0050 - ACCIDENT CODE

    acc_3 : str | None
        ACC.3 - ACCIDENT LOCATION (ST) O
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
        description="O | Item #00182 | LEN:19",
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
        description="O | Item #00184 | Table 0050 - ACCIDENT CODE | LEN:2",
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
        description="O | Item #00185 | LEN:25",
    )

    model_config = ConfigDict(populate_by_name=True)
