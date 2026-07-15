"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PRB
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI


class PRB(HL7Model):
    """Problem Details (S12.4.2).

    Attributes
    ----------
    prb_1 : str
        PRB.1 - Action Code (ID) R S12.4.1.1 | 0287 - Problem/goal action code

    prb_2 : str
        PRB.2 - Action Date/Time (DTM) R S12.4.1.2

    prb_3 : CWE
        PRB.3 - Problem ID (CWE) R S12.4.2.3

    prb_4 : EI
        PRB.4 - Problem Instance ID (EI) R S12.4.2.4

    prb_5 : EI | None
        PRB.5 - Episode of Care ID (EI) O S12.4.1.5

    prb_6 : str | None
        PRB.6 - Problem List Priority (NM) O S12.4.2.6

    prb_7 : str | None
        PRB.7 - Problem Established Date/Time (DTM) O S12.4.2.7

    prb_8 : str | None
        PRB.8 - Anticipated Problem Resolution Date/Time (DTM) O S12.4.2.8

    prb_9 : str | None
        PRB.9 - Actual Problem Resolution Date/Time (DTM) O S12.4.2.9

    prb_10 : CWE | None
        PRB.10 - Problem Classification (CWE) O S12.4.2.10

    prb_11 : list[CWE] | None
        PRB.11 - Problem Management Discipline (CWE) O rep S12.4.2.11

    prb_12 : CWE | None
        PRB.12 - Problem Persistence (CWE) O S12.4.2.12

    prb_13 : CWE | None
        PRB.13 - Problem Confirmation Status (CWE) O S12.4.2.13

    prb_14 : CWE | None
        PRB.14 - Problem Life Cycle Status (CWE) O S12.4.2.14

    prb_15 : str | None
        PRB.15 - Problem Life Cycle Status Date/Time (DTM) O S12.4.2.15

    prb_16 : str | None
        PRB.16 - Problem Date of Onset (DTM) O S12.4.2.16

    prb_17 : str | None
        PRB.17 - Problem Onset Text (ST) O S12.4.2.17

    prb_18 : CWE | None
        PRB.18 - Problem Ranking (CWE) O S12.4.2.18

    prb_19 : CWE | None
        PRB.19 - Certainty of Problem (CWE) O S12.4.2.19

    prb_20 : str | None
        PRB.20 - Probability of Problem (0-1) (NM) O S12.4.2.20

    prb_21 : CWE | None
        PRB.21 - Individual Awareness of Problem (CWE) O S12.4.2.21

    prb_22 : CWE | None
        PRB.22 - Problem Prognosis (CWE) O S12.4.2.22

    prb_23 : CWE | None
        PRB.23 - Individual Awareness of Prognosis (CWE) O S12.4.2.23

    prb_24 : str | None
        PRB.24 - Family/Significant Other Awareness of Problem/Prognosis (ST) O S12.4.2.24

    prb_25 : CWE | None
        PRB.25 - Security/Sensitivity (CWE) O S12.4.2.25

    prb_26 : CWE | None
        PRB.26 - Problem Severity (CWE) O S12.4.2.26 | 0836 - Problem Severity

    prb_27 : CWE | None
        PRB.27 - Problem Perspective (CWE) O S12.4.2.27 | 0838 - Problem Perspective

    prb_28 : CNE | None
        PRB.28 - Mood Code (CNE) C S12.4.2.28 | 0725 - Mood Codes
    """

    prb_1: str = Field(
        validation_alias=AliasChoices(
            "prb_1",
            "action_code",
            "PRB.1",
        ),
        serialization_alias="PRB.1",
        title="Action Code",
        description=(
            "R | Item #00816 | Table 0287 - Problem/goal action code | LEN:2"
        ),
    )

    prb_2: str = Field(
        validation_alias=AliasChoices(
            "prb_2",
            "action_date_time",
            "PRB.2",
        ),
        serialization_alias="PRB.2",
        title="Action Date/Time",
        description="R | Item #00817 | LEN:24",
    )

    prb_3: CWE = Field(
        validation_alias=AliasChoices(
            "prb_3",
            "problem_id",
            "PRB.3",
        ),
        serialization_alias="PRB.3",
        title="Problem ID",
        description="R | Item #00838",
    )

    prb_4: EI = Field(
        validation_alias=AliasChoices(
            "prb_4",
            "problem_instance_id",
            "PRB.4",
        ),
        serialization_alias="PRB.4",
        title="Problem Instance ID",
        description="R | Item #00839",
    )

    prb_5: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_5",
            "episode_of_care_id",
            "PRB.5",
        ),
        serialization_alias="PRB.5",
        title="Episode of Care ID",
        description="O | Item #00820",
    )

    prb_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_6",
            "problem_list_priority",
            "PRB.6",
        ),
        serialization_alias="PRB.6",
        title="Problem List Priority",
        description="O | Item #00841 | LEN:60",
    )

    prb_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_7",
            "problem_established_date_time",
            "PRB.7",
        ),
        serialization_alias="PRB.7",
        title="Problem Established Date/Time",
        description="O | Item #00842 | LEN:24",
    )

    prb_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_8",
            "anticipated_problem_resolution_date_time",
            "PRB.8",
        ),
        serialization_alias="PRB.8",
        title="Anticipated Problem Resolution Date/Time",
        description="O | Item #00843 | LEN:24",
    )

    prb_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_9",
            "actual_problem_resolution_date_time",
            "PRB.9",
        ),
        serialization_alias="PRB.9",
        title="Actual Problem Resolution Date/Time",
        description="O | Item #00844 | LEN:24",
    )

    prb_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_10",
            "problem_classification",
            "PRB.10",
        ),
        serialization_alias="PRB.10",
        title="Problem Classification",
        description="O | Item #00845",
    )

    prb_11: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_11",
            "problem_management_discipline",
            "PRB.11",
        ),
        serialization_alias="PRB.11",
        title="Problem Management Discipline",
        description="O | Item #00846",
    )

    prb_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_12",
            "problem_persistence",
            "PRB.12",
        ),
        serialization_alias="PRB.12",
        title="Problem Persistence",
        description="O | Item #00847",
    )

    prb_13: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_13",
            "problem_confirmation_status",
            "PRB.13",
        ),
        serialization_alias="PRB.13",
        title="Problem Confirmation Status",
        description="O | Item #00848",
    )

    prb_14: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_14",
            "problem_life_cycle_status",
            "PRB.14",
        ),
        serialization_alias="PRB.14",
        title="Problem Life Cycle Status",
        description="O | Item #00849",
    )

    prb_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_15",
            "problem_life_cycle_status_date_time",
            "PRB.15",
        ),
        serialization_alias="PRB.15",
        title="Problem Life Cycle Status Date/Time",
        description="O | Item #00850 | LEN:24",
    )

    prb_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_16",
            "problem_date_of_onset",
            "PRB.16",
        ),
        serialization_alias="PRB.16",
        title="Problem Date of Onset",
        description="O | Item #00851 | LEN:24",
    )

    prb_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_17",
            "problem_onset_text",
            "PRB.17",
        ),
        serialization_alias="PRB.17",
        title="Problem Onset Text",
        description="O | Item #00852 | LEN:80",
    )

    prb_18: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_18",
            "problem_ranking",
            "PRB.18",
        ),
        serialization_alias="PRB.18",
        title="Problem Ranking",
        description="O | Item #00853",
    )

    prb_19: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_19",
            "certainty_of_problem",
            "PRB.19",
        ),
        serialization_alias="PRB.19",
        title="Certainty of Problem",
        description="O | Item #00854",
    )

    prb_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_20",
            "probability_of_problem_0_1",
            "PRB.20",
        ),
        serialization_alias="PRB.20",
        title="Probability of Problem (0-1)",
        description="O | Item #00855 | LEN:5",
    )

    prb_21: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_21",
            "individual_awareness_of_problem",
            "PRB.21",
        ),
        serialization_alias="PRB.21",
        title="Individual Awareness of Problem",
        description="O | Item #00856",
    )

    prb_22: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_22",
            "problem_prognosis",
            "PRB.22",
        ),
        serialization_alias="PRB.22",
        title="Problem Prognosis",
        description="O | Item #00857",
    )

    prb_23: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_23",
            "individual_awareness_of_prognosis",
            "PRB.23",
        ),
        serialization_alias="PRB.23",
        title="Individual Awareness of Prognosis",
        description="O | Item #00858",
    )

    prb_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_24",
            "family_significant_other_awareness_of_problem_prognosis",
            "PRB.24",
        ),
        serialization_alias="PRB.24",
        title="Family/Significant Other Awareness of Problem/Prognosis",
        description="O | Item #00859 | LEN:200",
    )

    prb_25: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_25",
            "security_sensitivity",
            "PRB.25",
        ),
        serialization_alias="PRB.25",
        title="Security/Sensitivity",
        description="O | Item #00823",
    )

    prb_26: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_26",
            "problem_severity",
            "PRB.26",
        ),
        serialization_alias="PRB.26",
        title="Problem Severity",
        description="O | Item #02234 | Table 0836 - Problem Severity",
    )

    prb_27: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_27",
            "problem_perspective",
            "PRB.27",
        ),
        serialization_alias="PRB.27",
        title="Problem Perspective",
        description="O | Item #02235 | Table 0838 - Problem Perspective",
    )

    prb_28: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_28",
            "mood_code",
            "PRB.28",
        ),
        serialization_alias="PRB.28",
        title="Mood Code",
        description="C | Item #02237 | Table 0725 - Mood Codes",
    )

    @field_validator("prb_2", "prb_7", "prb_8", "prb_9", "prb_15", "prb_16", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("prb_6", "prb_20", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
