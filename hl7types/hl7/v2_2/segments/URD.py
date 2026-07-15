"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: URD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS


class URD(HL7Model):
    """RESULTS/UPDATE DEFINITION (S2.10.6).

    Attributes
    ----------
    urd_1 : TS | None
        URD.1 - R/U date / time (TS) NA S2.10.6.1

    urd_2 : str | None
        URD.2 - Report Priority (ID) NA S2.10.6.2 | 0109 - REPORT PRIORITY

    urd_3 : list[str]
        URD.3 - R/U Who Subject Definition (ST) R rep S2.10.6.3

    urd_4 : list[str] | None
        URD.4 - R/U What Subject Definition (ID) NA rep S2.10.6.4 | 0048 - WHAT SUBJECT FILTER

    urd_5 : list[str] | None
        URD.5 - R/U What Department Code (ST) NA rep S2.10.6.5

    urd_6 : list[str] | None
        URD.6 - R/U display / print locations (ST) NA rep S2.10.6.6

    urd_7 : str | None
        URD.7 - R/U Results Level (ID) NA S2.10.6.7 | 0108 - QUERY RESULTS LEVEL
    """

    urd_1: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_1",
            "r_u_date_time",
            "URD.1",
        ),
        serialization_alias="URD.1",
        title="R/U date / time",
        description="NA | Item #00045",
    )

    urd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_2",
            "report_priority",
            "URD.2",
        ),
        serialization_alias="URD.2",
        title="Report Priority",
        description="NA | Item #00046 | Table 0109 - REPORT PRIORITY | LEN:1",
    )

    urd_3: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "urd_3",
            "r_u_who_subject_definition",
            "URD.3",
        ),
        serialization_alias="URD.3",
        title="R/U Who Subject Definition",
        description="R | Item #00047 | LEN:20",
    )

    urd_4: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_4",
            "r_u_what_subject_definition",
            "URD.4",
        ),
        serialization_alias="URD.4",
        title="R/U What Subject Definition",
        description=(
            "NA | Item #00048 | Table 0048 - WHAT SUBJECT FILTER | LEN:3"
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
        title="R/U What Department Code",
        description="NA | Item #00049 | LEN:20",
    )

    urd_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_6",
            "r_u_display_print_locations",
            "URD.6",
        ),
        serialization_alias="URD.6",
        title="R/U display / print locations",
        description="NA | Item #00050 | LEN:20",
    )

    urd_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urd_7",
            "r_u_results_level",
            "URD.7",
        ),
        serialization_alias="URD.7",
        title="R/U Results Level",
        description=(
            "NA | Item #00051 | Table 0108 - QUERY RESULTS LEVEL | LEN:1"
        ),
    )

    model_config = {"populate_by_name": True}
