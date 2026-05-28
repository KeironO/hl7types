"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: EDU
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.CWE import CWE
from ..datatypes.DR import DR
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON


class EDU(BaseModel):
    """HL7 v2 EDU segment."""

    edu_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "edu_1",
            "set_id_edu",
            "EDU.1",
        ),
        serialization_alias="EDU.1",
        title="Set ID - EDU",
        description="Item #1448",
    )

    edu_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "edu_2",
            "academic_degree",
            "EDU.2",
        ),
        serialization_alias="EDU.2",
        title="Academic Degree",
        description="Item #1449 | Table HL70360",
    )

    edu_3: DR | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "edu_3",
            "academic_degree_program_date_range",
            "EDU.3",
        ),
        serialization_alias="EDU.3",
        title="Academic Degree Program Date Range",
        description="Item #1597",
    )

    edu_4: DR | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "edu_4",
            "academic_degree_program_participation_date_range",
            "EDU.4",
        ),
        serialization_alias="EDU.4",
        title="Academic Degree Program Participation Date Range",
        description="Item #1450",
    )

    edu_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "edu_5",
            "academic_degree_granted_date",
            "EDU.5",
        ),
        serialization_alias="EDU.5",
        title="Academic Degree Granted Date",
        description="Item #1451",
    )

    edu_6: XON | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "edu_6",
            "school",
            "EDU.6",
        ),
        serialization_alias="EDU.6",
        title="School",
        description="Item #1452",
    )

    edu_7: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "edu_7",
            "school_type_code",
            "EDU.7",
        ),
        serialization_alias="EDU.7",
        title="School Type Code",
        description="Item #1453 | Table HL70402",
    )

    edu_8: XAD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "edu_8",
            "school_address",
            "EDU.8",
        ),
        serialization_alias="EDU.8",
        title="School Address",
        description="Item #1454",
    )

    edu_9: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "edu_9",
            "major_field_of_study",
            "EDU.9",
        ),
        serialization_alias="EDU.9",
        title="Major Field of Study",
        description="Item #1885",
    )

    model_config = {"populate_by_name": True}
