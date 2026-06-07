"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PRB
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.TS import TS


class PRB(HL7Model):
    """HL7 v2 PRB segment.

    Attributes
    ----------
    prb_1 : str
        PRB.1 (req) - Action Code (ID)

    prb_2 : TS
        PRB.2 (req) - Action Date/Time (TS)

    prb_3 : CE
        PRB.3 (req) - Problem ID (CE)

    prb_4 : EI
        PRB.4 (req) - Problem Instance ID (EI)

    prb_5 : EI | None
        PRB.5 (opt) - Episode of Care ID (EI)

    prb_6 : str | None
        PRB.6 (opt) - Problem List Priority (NM)

    prb_7 : TS | None
        PRB.7 (opt) - Problem Established Date/Time (TS)

    prb_8 : TS | None
        PRB.8 (opt) - Anticipated Problem Resolution Date/Time (TS)

    prb_9 : TS | None
        PRB.9 (opt) - Actual Problem Resolution Date/Time (TS)

    prb_10 : CE | None
        PRB.10 (opt) - Problem Classification (CE)

    prb_11 : list[CE] | None
        PRB.11 (opt, rep) - Problem Management Discipline (CE)

    prb_12 : CE | None
        PRB.12 (opt) - Problem Persistence (CE)

    prb_13 : CE | None
        PRB.13 (opt) - Problem Confirmation Status (CE)

    prb_14 : CE | None
        PRB.14 (opt) - Problem Life Cycle Status (CE)

    prb_15 : TS | None
        PRB.15 (opt) - Problem Life Cycle Status Date/Time (TS)

    prb_16 : TS | None
        PRB.16 (opt) - Problem Date of Onset (TS)

    prb_17 : str | None
        PRB.17 (opt) - Problem Onset Text (ST)

    prb_18 : CE | None
        PRB.18 (opt) - Problem Ranking (CE)

    prb_19 : CE | None
        PRB.19 (opt) - Certainty of Problem (CE)

    prb_20 : str | None
        PRB.20 (opt) - Probability of Problem (0-1) (NM)

    prb_21 : CE | None
        PRB.21 (opt) - Individual Awareness of Problem (CE)

    prb_22 : CE | None
        PRB.22 (opt) - Problem Prognosis (CE)

    prb_23 : CE | None
        PRB.23 (opt) - Individual Awareness of Prognosis (CE)

    prb_24 : str | None
        PRB.24 (opt) - Family/Significant Other Awareness of Problem/Prognosis (ST)

    prb_25 : CE | None
        PRB.25 (opt) - Security/Sensitivity (CE)
    """

    prb_1: str = Field(
        validation_alias=AliasChoices(
            "prb_1",
            "action_code",
            "PRB.1",
        ),
        serialization_alias="PRB.1",
        title="Action Code",
        description="Item #816 | Table HL70287",
    )

    prb_2: TS = Field(
        validation_alias=AliasChoices(
            "prb_2",
            "action_date_time",
            "PRB.2",
        ),
        serialization_alias="PRB.2",
        title="Action Date/Time",
        description="Item #817",
    )

    prb_3: CE = Field(
        validation_alias=AliasChoices(
            "prb_3",
            "problem_id",
            "PRB.3",
        ),
        serialization_alias="PRB.3",
        title="Problem ID",
        description="Item #838",
    )

    prb_4: EI = Field(
        validation_alias=AliasChoices(
            "prb_4",
            "problem_instance_id",
            "PRB.4",
        ),
        serialization_alias="PRB.4",
        title="Problem Instance ID",
        description="Item #839",
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
        description="Item #820",
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
        description="Item #841",
    )

    prb_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_7",
            "problem_established_date_time",
            "PRB.7",
        ),
        serialization_alias="PRB.7",
        title="Problem Established Date/Time",
        description="Item #842",
    )

    prb_8: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_8",
            "anticipated_problem_resolution_date_time",
            "PRB.8",
        ),
        serialization_alias="PRB.8",
        title="Anticipated Problem Resolution Date/Time",
        description="Item #843",
    )

    prb_9: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_9",
            "actual_problem_resolution_date_time",
            "PRB.9",
        ),
        serialization_alias="PRB.9",
        title="Actual Problem Resolution Date/Time",
        description="Item #844",
    )

    prb_10: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_10",
            "problem_classification",
            "PRB.10",
        ),
        serialization_alias="PRB.10",
        title="Problem Classification",
        description="Item #845",
    )

    prb_11: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_11",
            "problem_management_discipline",
            "PRB.11",
        ),
        serialization_alias="PRB.11",
        title="Problem Management Discipline",
        description="Item #846",
    )

    prb_12: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_12",
            "problem_persistence",
            "PRB.12",
        ),
        serialization_alias="PRB.12",
        title="Problem Persistence",
        description="Item #847",
    )

    prb_13: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_13",
            "problem_confirmation_status",
            "PRB.13",
        ),
        serialization_alias="PRB.13",
        title="Problem Confirmation Status",
        description="Item #848",
    )

    prb_14: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_14",
            "problem_life_cycle_status",
            "PRB.14",
        ),
        serialization_alias="PRB.14",
        title="Problem Life Cycle Status",
        description="Item #849",
    )

    prb_15: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_15",
            "problem_life_cycle_status_date_time",
            "PRB.15",
        ),
        serialization_alias="PRB.15",
        title="Problem Life Cycle Status Date/Time",
        description="Item #850",
    )

    prb_16: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_16",
            "problem_date_of_onset",
            "PRB.16",
        ),
        serialization_alias="PRB.16",
        title="Problem Date of Onset",
        description="Item #851",
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
        description="Item #852",
    )

    prb_18: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_18",
            "problem_ranking",
            "PRB.18",
        ),
        serialization_alias="PRB.18",
        title="Problem Ranking",
        description="Item #853",
    )

    prb_19: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_19",
            "certainty_of_problem",
            "PRB.19",
        ),
        serialization_alias="PRB.19",
        title="Certainty of Problem",
        description="Item #854",
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
        description="Item #855",
    )

    prb_21: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_21",
            "individual_awareness_of_problem",
            "PRB.21",
        ),
        serialization_alias="PRB.21",
        title="Individual Awareness of Problem",
        description="Item #856",
    )

    prb_22: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_22",
            "problem_prognosis",
            "PRB.22",
        ),
        serialization_alias="PRB.22",
        title="Problem Prognosis",
        description="Item #857",
    )

    prb_23: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_23",
            "individual_awareness_of_prognosis",
            "PRB.23",
        ),
        serialization_alias="PRB.23",
        title="Individual Awareness of Prognosis",
        description="Item #858",
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
        description="Item #859",
    )

    prb_25: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_25",
            "security_sensitivity",
            "PRB.25",
        ),
        serialization_alias="PRB.25",
        title="Security/Sensitivity",
        description="Item #823",
    )

    @field_validator("prb_6", "prb_20", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
