"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: URD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class URD(HL7Model):
    """RESULTS/UPDATE DEFINITION (S5.3.5).

    Attributes
    ----------
    urd_1 : str | None
        URD.1 - R/U DATE/TIME (TS) O

    urd_2 : str | None
        URD.2 - REPORT PRIORITY (ID) O | 0109 - REPORT PRIORITY

    urd_3 : list[str]
        URD.3 - R/U WHO SUBJECT DEFINITION (ST) R rep

    urd_4 : list[str] | None
        URD.4 - R/U WHAT SUBJECT DEFINITION (ID) O rep | 0048 - WHAT SUBJECT FILTER

    urd_5 : list[str] | None
        URD.5 - R/U WHAT DEPARTMENT CODE (ST) O rep

    urd_6 : list[str] | None
        URD.6 - R/U DISPLAY/PRINT LOCATIONS (ST) O rep

    urd_7 : str | None
        URD.7 - R/U RESULTS LEVEL (ID) O | 0108 - QUERY RESULTS LEVEL
    """

    urd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_1",
            "r_u_date_time",
            "URD.1",
        ),
        serialization_alias="URD.1",
        title="R/U DATE/TIME",
        description="O | Item #00600 | LEN:19",
    )

    urd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_2",
            "report_priority",
            "URD.2",
        ),
        serialization_alias="URD.2",
        title="REPORT PRIORITY",
        description="O | Item #00601 | Table 0109 - REPORT PRIORITY | LEN:1",
    )

    urd_3: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "urd_3",
            "r_u_who_subject_definition",
            "URD.3",
        ),
        serialization_alias="URD.3",
        title="R/U WHO SUBJECT DEFINITION",
        description="R | Item #00602 | LEN:20",
    )

    urd_4: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_4",
            "r_u_what_subject_definition",
            "URD.4",
        ),
        serialization_alias="URD.4",
        title="R/U WHAT SUBJECT DEFINITION",
        description=(
            "O | Item #00603 | Table 0048 - WHAT SUBJECT FILTER | LEN:3"
        ),
    )

    urd_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_5",
            "r_u_what_department_code",
            "URD.5",
        ),
        serialization_alias="URD.5",
        title="R/U WHAT DEPARTMENT CODE",
        description="O | Item #00605 | LEN:20",
    )

    urd_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_6",
            "r_u_display_print_locations",
            "URD.6",
        ),
        serialization_alias="URD.6",
        title="R/U DISPLAY/PRINT LOCATIONS",
        description="O | Item #00607 | LEN:20",
    )

    urd_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_7",
            "r_u_results_level",
            "URD.7",
        ),
        serialization_alias="URD.7",
        title="R/U RESULTS LEVEL",
        description=(
            "O | Item #00702 | Table 0108 - QUERY RESULTS LEVEL | LEN:1"
        ),
    )

    model_config = ConfigDict(populate_by_name=True)
