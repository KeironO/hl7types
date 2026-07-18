"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: AIL
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.PL import PL
from ..datatypes.TS import TS

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class AIL(HL7Model):
    """Appointment Information - Location Resource (S10.6.6).

    Attributes
    ----------
    ail_1 : str
        AIL.1 - Set ID - AIL (SI) R S10.6.6.1

    ail_2 : str | None
        AIL.2 - Segment Action Code (ID) C S10.6.7.2 | 0206 - Segment action code

    ail_3 : PL | None
        AIL.3 - Location Resource ID (PL) C S10.6.6.3

    ail_4 : CE
        AIL.4 - Location Type-AIL (CE) R S10.6.6.4

    ail_5 : CE | None
        AIL.5 - Location Group (CE) O S10.6.6.5

    ail_6 : TS | None
        AIL.6 - Start Date/Time (TS) C S13.4.12.3

    ail_7 : str | None
        AIL.7 - Start Date/Time Offset (NM) C S10.6.7.7

    ail_8 : CE | None
        AIL.8 - Start Date/Time Offset Units (CE) C S10.6.7.8

    ail_9 : str | None
        AIL.9 - Duration (NM) O S10.6.7.9

    ail_10 : CE | None
        AIL.10 - Duration Units (CE) O S10.6.7.10

    ail_11 : str | None
        AIL.11 - Allow Substitution Code (IS) C S10.6.7.11 | 0279 - Allow substitution codes

    ail_12 : CE | None
        AIL.12 - Filler Status Code (CE) C S10.6.7.12 | 0278 - Filler status codes
    """

    ail_1: str = Field(
        validation_alias=AliasChoices(
            "ail_1",
            "set_id_ail",
            "AIL.1",
        ),
        serialization_alias="AIL.1",
        title="Set ID - AIL",
        description="R | Item #00902 | LEN:4",
    )

    ail_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_2",
            "segment_action_code",
            "AIL.2",
        ),
        serialization_alias="AIL.2",
        title="Segment Action Code",
        description=(
            "C | Item #00763 | Table 0206 - Segment action code | LEN:3"
        ),
    )

    ail_3: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_3",
            "location_resource_id",
            "AIL.3",
        ),
        serialization_alias="AIL.3",
        title="Location Resource ID",
        description="C | Item #00903",
    )

    ail_4: CE = Field(
        validation_alias=AliasChoices(
            "ail_4",
            "location_type_ail",
            "AIL.4",
        ),
        serialization_alias="AIL.4",
        title="Location Type-AIL",
        description="R | Item #00904",
    )

    ail_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_5",
            "location_group",
            "AIL.5",
        ),
        serialization_alias="AIL.5",
        title="Location Group",
        description="O | Item #00905",
    )

    ail_6: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_6",
            "start_date_time",
            "AIL.6",
        ),
        serialization_alias="AIL.6",
        title="Start Date/Time",
        description="C | Item #01202",
    )

    ail_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_7",
            "start_date_time_offset",
            "AIL.7",
        ),
        serialization_alias="AIL.7",
        title="Start Date/Time Offset",
        description="C | Item #00891 | LEN:20",
    )

    ail_8: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_8",
            "start_date_time_offset_units",
            "AIL.8",
        ),
        serialization_alias="AIL.8",
        title="Start Date/Time Offset Units",
        description="C | Item #00892",
    )

    ail_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_9",
            "duration",
            "AIL.9",
        ),
        serialization_alias="AIL.9",
        title="Duration",
        description="O | Item #00893 | LEN:20",
    )

    ail_10: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_10",
            "duration_units",
            "AIL.10",
        ),
        serialization_alias="AIL.10",
        title="Duration Units",
        description="O | Item #00894",
    )

    ail_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_11",
            "allow_substitution_code",
            "AIL.11",
        ),
        serialization_alias="AIL.11",
        title="Allow Substitution Code",
        description=(
            "C | Item #00895 | Table 0279 - Allow substitution codes | LEN:10"
        ),
    )

    ail_12: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_12",
            "filler_status_code",
            "AIL.12",
        ),
        serialization_alias="AIL.12",
        title="Filler Status Code",
        description="C | Item #00889 | Table 0278 - Filler status codes",
    )

    @field_validator("ail_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("ail_7", "ail_9", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
