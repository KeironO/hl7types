"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: GOL
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XPN import XPN

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class GOL(HL7Model):
    """Goal Detail (S12.4.1).

    Attributes
    ----------
    gol_1 : str
        GOL.1 - Action Code (ID) R S4.A.9.2 | 0206 - Segment Action Code

    gol_2 : str
        GOL.2 - Action Date/Time (DTM) R S12.4.1.2

    gol_3 : CWE
        GOL.3 - Goal ID (CWE) R S12.4.1.3

    gol_4 : EI
        GOL.4 - Goal Instance ID (EI) R S12.4.1.4

    gol_5 : EI | None
        GOL.5 - Episode of Care ID (EI) O S12.4.1.5

    gol_6 : str | None
        GOL.6 - Goal List Priority (NM) O S12.4.1.6

    gol_7 : str | None
        GOL.7 - Goal Established Date/Time (DTM) O S12.4.1.7

    gol_8 : str | None
        GOL.8 - Expected Goal Achieve Date/Time (DTM) O S12.4.1.8

    gol_9 : CWE | None
        GOL.9 - Goal Classification (CWE) O S12.4.1.9

    gol_10 : CWE | None
        GOL.10 - Goal Management Discipline (CWE) O S12.4.1.10

    gol_11 : CWE | None
        GOL.11 - Current Goal Review Status (CWE) O S12.4.1.11

    gol_12 : str | None
        GOL.12 - Current Goal Review Date/Time (DTM) O S12.4.1.12

    gol_13 : str | None
        GOL.13 - Next Goal Review Date/Time (DTM) O S12.4.1.13

    gol_14 : str | None
        GOL.14 - Previous Goal Review Date/Time (DTM) O S12.4.1.14

    gol_16 : CWE | None
        GOL.16 - Goal Evaluation (CWE) O S12.4.1.16

    gol_17 : list[str] | None
        GOL.17 - Goal Evaluation Comment (ST) O rep S12.4.1.17

    gol_18 : CWE | None
        GOL.18 - Goal Life Cycle Status (CWE) O S12.4.1.18

    gol_19 : str | None
        GOL.19 - Goal Life Cycle Status Date/Time (DTM) O S12.4.1.19

    gol_20 : list[CWE] | None
        GOL.20 - Goal Target Type (CWE) O rep S12.4.1.20

    gol_21 : list[XPN] | None
        GOL.21 - Goal Target Name (XPN) O rep S12.4.1.21

    gol_22 : CNE | None
        GOL.22 - Mood Code (CNE) C S12.4.1.22 | 0725 - Mood Codes
    """

    gol_1: str = Field(
        validation_alias=AliasChoices(
            "gol_1",
            "action_code",
            "GOL.1",
        ),
        serialization_alias="GOL.1",
        title="Action Code",
        description="R | Item #00816 | Table 0206 - Segment Action Code",
    )

    gol_2: str = Field(
        validation_alias=AliasChoices(
            "gol_2",
            "action_date_time",
            "GOL.2",
        ),
        serialization_alias="GOL.2",
        title="Action Date/Time",
        description="R | Item #00817",
    )

    gol_3: CWE = Field(
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
        description="O | Item #00821",
    )

    gol_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_7",
            "goal_established_date_time",
            "GOL.7",
        ),
        serialization_alias="GOL.7",
        title="Goal Established Date/Time",
        description="O | Item #00822",
    )

    gol_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_8",
            "expected_goal_achieve_date_time",
            "GOL.8",
        ),
        serialization_alias="GOL.8",
        title="Expected Goal Achieve Date/Time",
        description="O | Item #00824",
    )

    gol_9: Optional[CWE] = Field(
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

    gol_10: Optional[CWE] = Field(
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

    gol_11: Optional[CWE] = Field(
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

    gol_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_12",
            "current_goal_review_date_time",
            "GOL.12",
        ),
        serialization_alias="GOL.12",
        title="Current Goal Review Date/Time",
        description="O | Item #00828",
    )

    gol_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_13",
            "next_goal_review_date_time",
            "GOL.13",
        ),
        serialization_alias="GOL.13",
        title="Next Goal Review Date/Time",
        description="O | Item #00829",
    )

    gol_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_14",
            "previous_goal_review_date_time",
            "GOL.14",
        ),
        serialization_alias="GOL.14",
        title="Previous Goal Review Date/Time",
        description="O | Item #00830",
    )

    gol_16: Optional[CWE] = Field(
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
        description="O | Item #00833",
    )

    gol_18: Optional[CWE] = Field(
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

    gol_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_19",
            "goal_life_cycle_status_date_time",
            "GOL.19",
        ),
        serialization_alias="GOL.19",
        title="Goal Life Cycle Status Date/Time",
        description="O | Item #00835",
    )

    gol_20: Optional[List[CWE]] = Field(
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

    gol_22: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gol_22",
            "mood_code",
            "GOL.22",
        ),
        serialization_alias="GOL.22",
        title="Mood Code",
        description="C | Item #02182 | Table 0725 - Mood Codes",
    )

    @field_validator("gol_2", "gol_7", "gol_8", "gol_12", "gol_13", "gol_14", "gol_19", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("gol_6", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
