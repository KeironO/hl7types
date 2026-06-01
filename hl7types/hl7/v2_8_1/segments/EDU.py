"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: EDU
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CWE import CWE
from ..datatypes.DR import DR
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON


class EDU(HL7Model):
    """HL7 v2 EDU segment.

    Attributes
    ----------
    edu_1 : str
        EDU.1 (req) - Set ID - EDU (SI)

    edu_2 : CWE | None
        EDU.2 (opt) - Academic Degree (CWE)

    edu_3 : DR | None
        EDU.3 (opt) - Academic Degree Program Date Range (DR)

    edu_4 : DR | None
        EDU.4 (opt) - Academic Degree Program Participation Date Range (DR)

    edu_5 : str | None
        EDU.5 (opt) - Academic Degree Granted Date (DT)

    edu_6 : XON | None
        EDU.6 (opt) - School (XON)

    edu_7 : CWE | None
        EDU.7 (opt) - School Type Code (CWE)

    edu_8 : XAD | None
        EDU.8 (opt) - School Address (XAD)

    edu_9 : list[CWE] | None
        EDU.9 (opt, rep) - Major Field of Study (CWE)
    """

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

    edu_2: Optional[CWE] = Field(
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

    edu_3: Optional[DR] = Field(
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

    edu_4: Optional[DR] = Field(
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

    edu_5: Optional[str] = Field(
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

    edu_6: Optional[XON] = Field(
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

    edu_7: Optional[CWE] = Field(
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

    edu_8: Optional[XAD] = Field(
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

    edu_9: Optional[List[CWE]] = Field(
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

    @field_validator("edu_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("edu_5", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
