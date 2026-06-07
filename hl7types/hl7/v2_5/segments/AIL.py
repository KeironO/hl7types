"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: AIL
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.PL import PL
from ..datatypes.TS import TS


class AIL(HL7Model):
    """HL7 v2 AIL segment.

    Attributes
    ----------
    ail_1 : str
        AIL.1 (req) - Set ID - AIL (SI)

    ail_2 : str | None
        AIL.2 (opt) - Segment Action Code (ID)

    ail_3 : list[PL] | None
        AIL.3 (opt, rep) - Location Resource ID (PL)

    ail_4 : CE | None
        AIL.4 (opt) - Location Type-AIL (CE)

    ail_5 : CE | None
        AIL.5 (opt) - Location Group (CE)

    ail_6 : TS | None
        AIL.6 (opt) - Start Date/Time (TS)

    ail_7 : str | None
        AIL.7 (opt) - Start Date/Time Offset (NM)

    ail_8 : CE | None
        AIL.8 (opt) - Start Date/Time Offset Units (CE)

    ail_9 : str | None
        AIL.9 (opt) - Duration (NM)

    ail_10 : CE | None
        AIL.10 (opt) - Duration Units (CE)

    ail_11 : str | None
        AIL.11 (opt) - Allow Substitution Code (IS)

    ail_12 : CE | None
        AIL.12 (opt) - Filler Status Code (CE)
    """

    ail_1: str = Field(
        validation_alias=AliasChoices(
            "ail_1",
            "set_id_ail",
            "AIL.1",
        ),
        serialization_alias="AIL.1",
        title="Set ID - AIL",
        description="Item #902",
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
        description="Item #763 | Table HL70206",
    )

    ail_3: Optional[List[PL]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_3",
            "location_resource_id",
            "AIL.3",
        ),
        serialization_alias="AIL.3",
        title="Location Resource ID",
        description="Item #903",
    )

    ail_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_4",
            "location_type_ail",
            "AIL.4",
        ),
        serialization_alias="AIL.4",
        title="Location Type-AIL",
        description="Item #904 | Table HL70305",
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
        description="Item #905",
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
        description="Item #1202",
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
        description="Item #891",
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
        description="Item #892",
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
        description="Item #893",
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
        description="Item #894",
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
        description="Item #895 | Table HL70279",
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
        description="Item #889 | Table HL70278",
    )

    @field_validator("ail_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("ail_7", "ail_9", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
