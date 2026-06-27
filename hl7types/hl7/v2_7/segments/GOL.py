"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: GOL
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XPN import XPN


class GOL(HL7Model):
    """HL7 v2 GOL segment.

    Attributes
    ----------
    gol_1 : str
        GOL.1 (req) - Action Code (ID)

    gol_2 : str
        GOL.2 (req) - Action Date/Time (DTM)

    gol_3 : CWE
        GOL.3 (req) - Goal ID (CWE)

    gol_4 : EI
        GOL.4 (req) - Goal Instance ID (EI)

    gol_5 : EI | None
        GOL.5 (opt) - Episode of Care ID (EI)

    gol_6 : str | None
        GOL.6 (opt) - Goal List Priority (NM)

    gol_7 : str | None
        GOL.7 (opt) - Goal Established Date/Time (DTM)

    gol_8 : str | None
        GOL.8 (opt) - Expected Goal Achieve Date/Time (DTM)

    gol_9 : CWE | None
        GOL.9 (opt) - Goal Classification (CWE)

    gol_10 : CWE | None
        GOL.10 (opt) - Goal Management Discipline (CWE)

    gol_11 : CWE | None
        GOL.11 (opt) - Current Goal Review Status (CWE)

    gol_12 : str | None
        GOL.12 (opt) - Current Goal Review Date/Time (DTM)

    gol_13 : str | None
        GOL.13 (opt) - Next Goal Review Date/Time (DTM)

    gol_14 : str | None
        GOL.14 (opt) - Previous Goal Review Date/Time (DTM)

    gol_16 : CWE | None
        GOL.16 (opt) - Goal Evaluation (CWE)

    gol_17 : list[str] | None
        GOL.17 (opt, rep) - Goal Evaluation Comment (ST)

    gol_18 : CWE | None
        GOL.18 (opt) - Goal Life Cycle Status (CWE)

    gol_19 : str | None
        GOL.19 (opt) - Goal Life Cycle Status Date/Time (DTM)

    gol_20 : list[CWE] | None
        GOL.20 (opt, rep) - Goal Target Type (CWE)

    gol_21 : list[XPN] | None
        GOL.21 (opt, rep) - Goal Target Name (XPN)

    gol_22 : CNE | None
        GOL.22 (opt) - Mood Code (CNE)
    """

    gol_1: str = Field(
        validation_alias=AliasChoices(
            "gol_1",
            "action_code",
            "GOL.1",
        ),
        serialization_alias="GOL.1",
        title="Action Code",
        description="Item #816 | Table HL70287",
    )

    gol_2: str = Field(
        validation_alias=AliasChoices(
            "gol_2",
            "action_date_time",
            "GOL.2",
        ),
        serialization_alias="GOL.2",
        title="Action Date/Time",
        description="Item #817",
    )

    gol_3: CWE = Field(
        validation_alias=AliasChoices(
            "gol_3",
            "goal_id",
            "GOL.3",
        ),
        serialization_alias="GOL.3",
        title="Goal ID",
        description="Item #818",
    )

    gol_4: EI = Field(
        validation_alias=AliasChoices(
            "gol_4",
            "goal_instance_id",
            "GOL.4",
        ),
        serialization_alias="GOL.4",
        title="Goal Instance ID",
        description="Item #819",
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
        description="Item #820",
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
        description="Item #821",
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
        description="Item #822",
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
        description="Item #824",
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
        description="Item #825",
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
        description="Item #826",
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
        description="Item #827",
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
        description="Item #828",
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
        description="Item #829",
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
        description="Item #830",
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
        description="Item #832",
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
        description="Item #833",
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
        description="Item #834",
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
        description="Item #835",
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
        description="Item #836",
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
        description="Item #837",
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
        description="Item #2182 | Table HL70725",
    )

    @field_validator("gol_2", "gol_7", "gol_8", "gol_12", "gol_13", "gol_14", "gol_19", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("gol_6", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
