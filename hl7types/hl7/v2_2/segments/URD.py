"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: URD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.TS import TS


class URD(BaseModel):
    """HL7 v2 URD segment.

    Attributes
    ----------
    urd_1 : TS | None
        URD.1 (opt) - R/U date / time (TS)

    urd_2 : str | None
        URD.2 (opt) - Report Priority (ID)

    urd_3 : list[str]
        URD.3 (req, rep) - R/U Who Subject Definition (ST)

    urd_4 : list[str] | None
        URD.4 (opt, rep) - R/U What Subject Definition (ID)

    urd_5 : list[str] | None
        URD.5 (opt, rep) - R/U What Department Code (ST)

    urd_6 : list[str] | None
        URD.6 (opt, rep) - R/U display / print locations (ST)

    urd_7 : str | None
        URD.7 (opt) - R/U Results Level (ID)
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
        description="Item #45",
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
        description="Item #46 | Table HL70109",
    )

    urd_3: List[str] = Field(
        default=...,
        validation_alias=AliasChoices(
            "urd_3",
            "r_u_who_subject_definition",
            "URD.3",
        ),
        serialization_alias="URD.3",
        title="R/U Who Subject Definition",
        description="Item #47",
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
        description="Item #48 | Table HL70048",
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
        description="Item #49",
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
        description="Item #50",
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
        description="Item #51 | Table HL70108",
    )

    model_config = {"populate_by_name": True}
