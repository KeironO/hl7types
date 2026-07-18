"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PRB
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.TS import TS

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class PRB(HL7Model):
    """Problem Detail (S12.3.2).

    Attributes
    ----------
    prb_1 : str
        PRB.1 - Action Code (ID) R S12.3.1 | 0287 - Action Code

    prb_2 : TS
        PRB.2 - Action Date/Time (TS) R S12.3.1

    prb_3 : CE
        PRB.3 - Problem ID (CE) R S12.3.2.3

    prb_4 : EI
        PRB.4 - Problem Instance ID (EI) R S12.3.2.4

    prb_5 : EI | None
        PRB.5 - Episode of Care ID (EI) O S12.3.1.5

    prb_6 : str | None
        PRB.6 - Problem List Priority (NM) O S12.3.2.6

    prb_7 : TS | None
        PRB.7 - Problem Established Date/Time (TS) O S12.3.2.7

    prb_8 : TS | None
        PRB.8 - Anticipated Problem Resolution Date/Time (TS) O S12.3.2.8

    prb_9 : TS | None
        PRB.9 - Actual Problem Resolution Date/Time (TS) O S12.3.2.9

    prb_10 : CE | None
        PRB.10 - Problem Classification (CE) O S12.3.2.10

    prb_11 : list[CE] | None
        PRB.11 - Problem Management Discipline (CE) O rep S12.3.2.11

    prb_12 : CE | None
        PRB.12 - Problem Persistence (CE) O S12.3.2.12

    prb_13 : CE | None
        PRB.13 - Problem Confirmation Status (CE) O S12.3.2.13

    prb_14 : CE | None
        PRB.14 - Problem Life Cycle Status (CE) O S12.3.2.14

    prb_15 : TS | None
        PRB.15 - Problem Life Cycle Status Date/Time (TS) O S12.3.2.15

    prb_16 : TS | None
        PRB.16 - Problem Date of Onset (TS) O S12.3.2.16

    prb_17 : str | None
        PRB.17 - Problem Onset Text (ST) O S12.3.2.17

    prb_18 : CE | None
        PRB.18 - Problem Ranking (CE) O S12.3.2.18

    prb_19 : CE | None
        PRB.19 - Certainty of Problem (CE) O S12.3.2.19

    prb_20 : str | None
        PRB.20 - Probability of Problem (0-1) (NM) O S12.3.2.20

    prb_21 : CE | None
        PRB.21 - Individual Awareness of Problem (CE) O S12.3.2.21

    prb_22 : CE | None
        PRB.22 - Problem Prognosis (CE) O S12.3.2.22

    prb_23 : CE | None
        PRB.23 - Individual Awareness of Prognosis (CE) O S12.3.2.23

    prb_24 : str | None
        PRB.24 - Family/Significant Other Awareness of Problem/Prognosis (ST) O S12.3.2.24

    prb_25 : CE | None
        PRB.25 - Security/Sensitivity (CE) O S12.3.2.25
    """

    prb_1: str = Field(
        validation_alias=AliasChoices(
            "prb_1",
            "action_code",
            "PRB.1",
        ),
        serialization_alias="PRB.1",
        title="Action Code",
        description="R | Item #00816 | Table 0287 - Action Code | LEN:2",
    )

    prb_2: TS = Field(
        validation_alias=AliasChoices(
            "prb_2",
            "action_date_time",
            "PRB.2",
        ),
        serialization_alias="PRB.2",
        title="Action Date/Time",
        description="R | Item #00817",
    )

    prb_3: CE = Field(
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

    prb_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prb_7",
            "problem_established_date_time",
            "PRB.7",
        ),
        serialization_alias="PRB.7",
        title="Problem Established Date/Time",
        description="O | Item #00842",
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
        description="O | Item #00843",
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
        description="O | Item #00844",
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
        description="O | Item #00845",
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
        description="O | Item #00846",
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
        description="O | Item #00847",
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
        description="O | Item #00848",
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
        description="O | Item #00849",
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
        description="O | Item #00850",
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
        description="O | Item #00851",
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

    prb_18: Optional[CE] = Field(
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

    prb_19: Optional[CE] = Field(
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

    prb_21: Optional[CE] = Field(
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

    prb_22: Optional[CE] = Field(
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

    prb_23: Optional[CE] = Field(
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

    prb_25: Optional[CE] = Field(
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

    @field_validator("prb_6", "prb_20", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
