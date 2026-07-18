"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: GOL
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.TQ import TQ
from ..datatypes.TS import TS
from ..datatypes.XPN import XPN

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class GOL(HL7Model):
    """Goal Detail (S12.3.1).

    Attributes
    ----------
    gol_1 : str
        GOL.1 - Action Code (ID) R S12.3.1 | 0287 - Action Code

    gol_2 : TS
        GOL.2 - Action Date/Time (TS) R S12.3.1

    gol_3 : CE
        GOL.3 - Goal ID (CE) R S12.3.1.3

    gol_4 : EI
        GOL.4 - Goal Instance ID (EI) R S12.3.1.4

    gol_5 : EI | None
        GOL.5 - Episode of Care ID (EI) O S12.3.1.5

    gol_6 : str | None
        GOL.6 - Goal List Priority (NM) O S12.3.1.6

    gol_7 : TS | None
        GOL.7 - Goal Established Date/Time (TS) NA S12.3.1.7

    gol_8 : TS | None
        GOL.8 - Expected Goal Achievement Date/Time (TS) NA S12.3.1.8

    gol_9 : CE | None
        GOL.9 - Goal Classification (CE) O S12.3.1.9

    gol_10 : CE | None
        GOL.10 - Goal Management Discipline (CE) O S12.3.1.10

    gol_11 : CE | None
        GOL.11 - Current Goal Review Status (CE) O S12.3.1.11

    gol_12 : TS | None
        GOL.12 - Current Goal Review Date/Time (TS) NA S12.3.1.12

    gol_13 : TS | None
        GOL.13 - Next Goal Review Date/Time (TS) NA S12.3.1.13

    gol_14 : TS | None
        GOL.14 - Previous Goal Review Date/Time (TS) NA S12.3.1.14

    gol_15 : TQ | None
        GOL.15 - Goal Review Interval (TQ) O S12.3.1.15

    gol_16 : CE | None
        GOL.16 - Goal Evaluation (CE) O S12.3.1.16

    gol_17 : list[str] | None
        GOL.17 - Goal Evaluation Comment (ST) O rep S12.3.1.17

    gol_18 : CE | None
        GOL.18 - Goal Life Cycle Status (CE) O S12.3.1.18

    gol_19 : TS | None
        GOL.19 - Goal Life Cycle Status Date/Time (TS) NA S12.3.1.19

    gol_20 : list[CE] | None
        GOL.20 - Goal Target Type (CE) O rep S12.3.1.20

    gol_21 : list[XPN] | None
        GOL.21 - Goal Target Name (XPN) O rep S12.3.1.21
    """

    gol_1: str = Field(
        validation_alias=AliasChoices(
            "gol_1",
            "action_code",
            "GOL.1",
        ),
        serialization_alias="GOL.1",
        title="Action Code",
        description="R | Item #00816 | Table 0287 - Action Code | LEN:2",
    )

    gol_2: TS = Field(
        validation_alias=AliasChoices(
            "gol_2",
            "action_date_time",
            "GOL.2",
        ),
        serialization_alias="GOL.2",
        title="Action Date/Time",
        description="R | Item #00817",
    )

    gol_3: CE = Field(
        validation_alias=AliasChoices(
            "gol_3",
            "goal_id",
            "GOL.3",
        ),
        serialization_alias="GOL.3",
        title="Goal ID",
        description="R | Item #00818",
    )

    gol_4: EI = Field(
        validation_alias=AliasChoices(
            "gol_4",
            "goal_instance_id",
            "GOL.4",
        ),
        serialization_alias="GOL.4",
        title="Goal Instance ID",
        description="R | Item #00819",
    )

    gol_5: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_5",
            "episode_of_care_id",
            "GOL.5",
        ),
        serialization_alias="GOL.5",
        title="Episode of Care ID",
        description="O | Item #00820",
    )

    gol_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_6",
            "goal_list_priority",
            "GOL.6",
        ),
        serialization_alias="GOL.6",
        title="Goal List Priority",
        description="O | Item #00821 | LEN:60",
    )

    gol_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_7",
            "goal_established_date_time",
            "GOL.7",
        ),
        serialization_alias="GOL.7",
        title="Goal Established Date/Time",
        description="NA | Item #00822",
    )

    gol_8: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_8",
            "expected_goal_achievement_date_time",
            "GOL.8",
        ),
        serialization_alias="GOL.8",
        title="Expected Goal Achievement Date/Time",
        description="NA | Item #00824",
    )

    gol_9: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_9",
            "goal_classification",
            "GOL.9",
        ),
        serialization_alias="GOL.9",
        title="Goal Classification",
        description="O | Item #00825",
    )

    gol_10: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_10",
            "goal_management_discipline",
            "GOL.10",
        ),
        serialization_alias="GOL.10",
        title="Goal Management Discipline",
        description="O | Item #00826",
    )

    gol_11: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_11",
            "current_goal_review_status",
            "GOL.11",
        ),
        serialization_alias="GOL.11",
        title="Current Goal Review Status",
        description="O | Item #00827",
    )

    gol_12: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_12",
            "current_goal_review_date_time",
            "GOL.12",
        ),
        serialization_alias="GOL.12",
        title="Current Goal Review Date/Time",
        description="NA | Item #00828",
    )

    gol_13: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_13",
            "next_goal_review_date_time",
            "GOL.13",
        ),
        serialization_alias="GOL.13",
        title="Next Goal Review Date/Time",
        description="NA | Item #00829",
    )

    gol_14: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_14",
            "previous_goal_review_date_time",
            "GOL.14",
        ),
        serialization_alias="GOL.14",
        title="Previous Goal Review Date/Time",
        description="NA | Item #00830",
    )

    gol_15: Optional[TQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_15",
            "goal_review_interval",
            "GOL.15",
        ),
        serialization_alias="GOL.15",
        title="Goal Review Interval",
        description="O | Item #00831",
    )

    gol_16: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_16",
            "goal_evaluation",
            "GOL.16",
        ),
        serialization_alias="GOL.16",
        title="Goal Evaluation",
        description="O | Item #00832",
    )

    gol_17: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_17",
            "goal_evaluation_comment",
            "GOL.17",
        ),
        serialization_alias="GOL.17",
        title="Goal Evaluation Comment",
        description="O | Item #00833 | LEN:300",
    )

    gol_18: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_18",
            "goal_life_cycle_status",
            "GOL.18",
        ),
        serialization_alias="GOL.18",
        title="Goal Life Cycle Status",
        description="O | Item #00834",
    )

    gol_19: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_19",
            "goal_life_cycle_status_date_time",
            "GOL.19",
        ),
        serialization_alias="GOL.19",
        title="Goal Life Cycle Status Date/Time",
        description="NA | Item #00835",
    )

    gol_20: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_20",
            "goal_target_type",
            "GOL.20",
        ),
        serialization_alias="GOL.20",
        title="Goal Target Type",
        description="O | Item #00836",
    )

    gol_21: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_21",
            "goal_target_name",
            "GOL.21",
        ),
        serialization_alias="GOL.21",
        title="Goal Target Name",
        description="O | Item #00837",
    )

    @field_validator("gol_6", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
