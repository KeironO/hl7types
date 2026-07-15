"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: URS
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.TQ import TQ
from ..datatypes.TS import TS


class URS(HL7Model):
    """Unsolicited Selection (S5.10.5.7).

    Attributes
    ----------
    urs_1 : list[str]
        URS.1 - R/U Where Subject Definition (ST) R rep S5.10.5.7.1

    urs_2 : TS | None
        URS.2 - R/U When Data Start Date/Time (TS) O S5.10.5.7.2

    urs_3 : TS | None
        URS.3 - R/U When Data End Date/Time (TS) O S5.10.5.7.3

    urs_4 : list[str] | None
        URS.4 - R/U What User Qualifier (ST) O rep S5.10.5.7.4

    urs_5 : list[str] | None
        URS.5 - R/U Other Results Subject Definition (ST) O rep S5.10.5.7.5

    urs_6 : list[str] | None
        URS.6 - R/U Which Date/Time Qualifier (ID) O rep S5.10.5.7.6 | 0156 - Which date/time qualifier

    urs_7 : list[str] | None
        URS.7 - R/U Which Date/Time Status Qualifier (ID) O rep S5.10.5.7.7 | 0157 - Which date/time status qualifier

    urs_8 : list[str] | None
        URS.8 - R/U Date/Time Selection Qualifier (ID) O rep S5.10.5.7.8 | 0158 - Date/time selection qualifier

    urs_9 : TQ | None
        URS.9 - R/U Quantity/Timing Qualifier (TQ) O S5.10.5.7.9
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
        title="R/U When Data Start Date/Time",
        description="O | Item #00053",
    )

    urs_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_3",
            "r_u_when_data_end_date_time",
            "URS.3",
        ),
        serialization_alias="URS.3",
        title="R/U When Data End Date/Time",
        description="O | Item #00054",
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
        description="O | Item #00055 | LEN:20",
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
        description="O | Item #00056 | LEN:20",
    )

    urs_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_6",
            "r_u_which_date_time_qualifier",
            "URS.6",
        ),
        serialization_alias="URS.6",
        title="R/U Which Date/Time Qualifier",
        description=(
            "O | Item #00057 | Table 0156 - Which date/time qualifier | LEN:12"
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
        title="R/U Which Date/Time Status Qualifier",
        description=(
            "O | Item #00058 | Table 0157 - Which date/time status qualifier | "
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
        title="R/U Date/Time Selection Qualifier",
        description=(
            "O | Item #00059 | Table 0158 - Date/time selection qualifier | "
            "LEN:12"
        ),
    )

    urs_9: Optional[TQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "urs_9",
            "r_u_quantity_timing_qualifier",
            "URS.9",
        ),
        serialization_alias="URS.9",
        title="R/U Quantity/Timing Qualifier",
        description="O | Item #00695",
    )

    model_config = {"populate_by_name": True}
