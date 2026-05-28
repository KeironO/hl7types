"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PRB
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI


class PRB(BaseModel):
    """HL7 v2 PRB segment."""

    prb_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "prb_1",
            "action_code",
            "PRB.1",
        ),
        serialization_alias="PRB.1",
        title="Action Code",
        description="Item #816 | Table HL70287",
    )

    prb_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "prb_2",
            "action_date_time",
            "PRB.2",
        ),
        serialization_alias="PRB.2",
        title="Action Date/Time",
        description="Item #817",
    )

    prb_3: CWE = Field(
        default=...,
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
        default=...,
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

    prb_7: Optional[str] = Field(
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

    prb_8: Optional[str] = Field(
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

    prb_9: Optional[str] = Field(
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

    prb_10: Optional[CWE] = Field(
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

    prb_11: Optional[List[CWE]] = Field(
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

    prb_12: Optional[CWE] = Field(
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

    prb_13: Optional[CWE] = Field(
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

    prb_14: Optional[CWE] = Field(
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

    prb_15: Optional[str] = Field(
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

    prb_16: Optional[str] = Field(
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

    prb_18: Optional[CWE] = Field(
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

    prb_19: Optional[CWE] = Field(
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

    prb_21: Optional[CWE] = Field(
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

    prb_22: Optional[CWE] = Field(
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

    prb_23: Optional[CWE] = Field(
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

    prb_25: Optional[CWE] = Field(
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

    prb_26: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_26",
            "problem_severity",
            "PRB.26",
        ),
        serialization_alias="PRB.26",
        title="Problem Severity",
        description="Item #2234 | Table HL70836",
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
        description="Item #2235 | Table HL70838",
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
        description="Item #2237 | Table HL70725",
    )

    model_config = {"populate_by_name": True}
