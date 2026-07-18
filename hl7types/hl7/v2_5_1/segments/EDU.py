"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: EDU
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CWE import CWE
from ..datatypes.DR import DR
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON

_RE_SI = re.compile(r'\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class EDU(HL7Model):
    """Educational Detail (S15.4.3).

    Attributes
    ----------
    edu_1 : str
        EDU.1 - Set ID - EDU (SI) R S15.4.3.1

    edu_2 : str | None
        EDU.2 - Academic Degree (IS) O S15.4.3.2 | 0360 - Degree/license/certificate

    edu_3 : DR | None
        EDU.3 - Academic Degree Program Date Range (DR) O S15.4.3.3

    edu_4 : DR | None
        EDU.4 - Academic Degree Program Participation Date Range (DR) O S15.4.3.4

    edu_5 : str | None
        EDU.5 - Academic Degree Granted Date (DT) O S15.4.3.5

    edu_6 : XON | None
        EDU.6 - School (XON) O S15.4.3.6

    edu_7 : CE | None
        EDU.7 - School Type Code (CE) O S15.4.3.7 | 0402 - School type

    edu_8 : XAD | None
        EDU.8 - School Address (XAD) O S15.4.3.8

    edu_9 : list[CWE] | None
        EDU.9 - Major Field of Study (CWE) O rep S15.4.3.9
    """

    edu_1: str = Field(
        validation_alias=AliasChoices(
            "edu_1",
            "set_id_edu",
            "EDU.1",
        ),
        serialization_alias="EDU.1",
        title="Set ID - EDU",
        description="R | Item #01448 | LEN:60",
    )

    edu_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "edu_2",
            "academic_degree",
            "EDU.2",
        ),
        serialization_alias="EDU.2",
        title="Academic Degree",
        description=(
            "O | Item #01449 | Table 0360 - Degree/license/certificate | LEN:10"
        ),
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
        description="O | Item #01597",
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
        description="O | Item #01450",
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
        description="O | Item #01451 | LEN:8",
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
        description="O | Item #01452",
    )

    edu_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "edu_7",
            "school_type_code",
            "EDU.7",
        ),
        serialization_alias="EDU.7",
        title="School Type Code",
        description="O | Item #01453 | Table 0402 - School type",
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
        description="O | Item #01454",
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
        description="O | Item #01885",
    )

    @field_validator("edu_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("edu_5", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
