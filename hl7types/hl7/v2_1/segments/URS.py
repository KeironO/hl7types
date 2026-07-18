"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: URS
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class URS(HL7Model):
    """UNSOLICITED SELECTION (S5.3.6).

    Attributes
    ----------
    urs_1 : list[str]
        URS.1 - R/U WHERE SUBJECT DEFINITION (ST) R rep

    urs_2 : str | None
        URS.2 - R/U WHEN DATA START DATE/TIME (TS) O

    urs_3 : str | None
        URS.3 - R/U WHEN DATA END DATE/TIME (TS) O

    urs_4 : list[str] | None
        URS.4 - R/U WHAT USER QUALIFIER (ST) O rep

    urs_5 : list[str] | None
        URS.5 - R/U OTHER RESULTS SUBJECT DEFINI (ST) O rep
    """

    urs_1: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "urs_1",
            "r_u_where_subject_definition",
            "URS.1",
        ),
        serialization_alias="URS.1",
        title="R/U WHERE SUBJECT DEFINITION",
        description="R | Item #00608 | LEN:20",
    )

    urs_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_2",
            "r_u_when_data_start_date_time",
            "URS.2",
        ),
        serialization_alias="URS.2",
        title="R/U WHEN DATA START DATE/TIME",
        description="O | Item #00609 | LEN:19",
    )

    urs_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_3",
            "r_u_when_data_end_date_time",
            "URS.3",
        ),
        serialization_alias="URS.3",
        title="R/U WHEN DATA END DATE/TIME",
        description="O | Item #00610 | LEN:19",
    )

    urs_4: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_4",
            "r_u_what_user_qualifier",
            "URS.4",
        ),
        serialization_alias="URS.4",
        title="R/U WHAT USER QUALIFIER",
        description="O | Item #00611 | LEN:20",
    )

    urs_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_5",
            "r_u_other_results_subject_defini",
            "URS.5",
        ),
        serialization_alias="URS.5",
        title="R/U OTHER RESULTS SUBJECT DEFINI",
        description="O | Item #00612 | LEN:20",
    )

    model_config = ConfigDict(populate_by_name=True)
