"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: URS
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS


class URS(HL7Model):
    """UNSOLICITED SELECTION (S2.10.7).

    Attributes
    ----------
    urs_1 : list[str]
        URS.1 - R/U Where Subject Definition (ST) R rep S2.10.7.1

    urs_2 : TS | None
        URS.2 - R/U when data start date / time (TS) NA S2.10.7.2

    urs_3 : TS | None
        URS.3 - R/U when data end date / time (TS) NA S2.10.7.3

    urs_4 : list[str] | None
        URS.4 - R/U What User Qualifier (ST) NA rep S2.10.7.4

    urs_5 : list[str] | None
        URS.5 - R/U Other Results Subject Definition (ST) NA rep S2.10.7.5

    urs_6 : list[str] | None
        URS.6 - R/U which date / time qualifier (ID) NA rep S2.10.7.6 | 0156 - DATE/TIME QUALIFIER

    urs_7 : list[str] | None
        URS.7 - R/U which date / time status qualifier (ID) NA rep S2.10.7.7 | 0157 - WHIHC DATE/TIME STATUS QUALIFIER

    urs_8 : list[str] | None
        URS.8 - R/U date / time selection qualifier (ID) NA rep S2.10.7.8 | 0158 - DATE/TIME SELECTION QUALIFIER
    """

    urs_1: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "urs_1",
            "r_u_where_subject_definition",
            "URS.1",
        ),
        serialization_alias="URS.1",
        title="R/U Where Subject Definition",
        description="R | Item #00052 | LEN:20",
    )

    urs_2: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_2",
            "r_u_when_data_start_date_time",
            "URS.2",
        ),
        serialization_alias="URS.2",
        title="R/U when data start date / time",
        description="NA | Item #00053",
    )

    urs_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_3",
            "r_u_when_data_end_date_time",
            "URS.3",
        ),
        serialization_alias="URS.3",
        title="R/U when data end date / time",
        description="NA | Item #00054",
    )

    urs_4: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_4",
            "r_u_what_user_qualifier",
            "URS.4",
        ),
        serialization_alias="URS.4",
        title="R/U What User Qualifier",
        description="NA | Item #00055 | LEN:20",
    )

    urs_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_5",
            "r_u_other_results_subject_definition",
            "URS.5",
        ),
        serialization_alias="URS.5",
        title="R/U Other Results Subject Definition",
        description="NA | Item #00056 | LEN:20",
    )

    urs_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_6",
            "r_u_which_date_time_qualifier",
            "URS.6",
        ),
        serialization_alias="URS.6",
        title="R/U which date / time qualifier",
        description=(
            "NA | Item #00057 | Table 0156 - DATE/TIME QUALIFIER | LEN:12"
        ),
    )

    urs_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_7",
            "r_u_which_date_time_status_qualifier",
            "URS.7",
        ),
        serialization_alias="URS.7",
        title="R/U which date / time status qualifier",
        description=(
            "NA | Item #00058 | Table 0157 - WHIHC DATE/TIME STATUS QUALIFIER | "
            "LEN:12"
        ),
    )

    urs_8: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_8",
            "r_u_date_time_selection_qualifier",
            "URS.8",
        ),
        serialization_alias="URS.8",
        title="R/U date / time selection qualifier",
        description=(
            "NA | Item #00059 | Table 0158 - DATE/TIME SELECTION QUALIFIER | "
            "LEN:12"
        ),
    )

    model_config = ConfigDict(populate_by_name=True)
