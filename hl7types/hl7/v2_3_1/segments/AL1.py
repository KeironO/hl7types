"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: AL1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE

_RE_SI = re.compile(r'\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class AL1(HL7Model):
    """AL1 - patient allergy information segment (S3.3.6).

    Attributes
    ----------
    al1_1 : str
        AL1.1 - Set ID - AL1 (SI) R S3.3.6.1

    al1_2 : str | None
        AL1.2 - Allergy Type (IS) O S3.3.6.2 | 0127 - Allergy type

    al1_3 : CE
        AL1.3 - Allergy Code/Mnemonic/Description (CE) R S3.3.6.3

    al1_4 : str | None
        AL1.4 - Allergy Severity (IS) O S3.3.6.4 | 0128 - Allergy severity

    al1_5 : list[str] | None
        AL1.5 - Allergy Reaction (ST) O rep S3.3.6.5

    al1_6 : str | None
        AL1.6 - Identification Date (DT) O S3.3.6.6
    """

    al1_1: str = Field(
        validation_alias=AliasChoices(
            "al1_1",
            "set_id_al1",
            "AL1.1",
        ),
        serialization_alias="AL1.1",
        title="Set ID - AL1",
        description="R | Item #00203 | LEN:4",
    )

    al1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_2",
            "allergy_type",
            "AL1.2",
        ),
        serialization_alias="AL1.2",
        title="Allergy Type",
        description="O | Item #00204 | Table 0127 - Allergy type | LEN:2",
    )

    al1_3: CE = Field(
        validation_alias=AliasChoices(
            "al1_3",
            "allergy_code_mnemonic_description",
            "AL1.3",
        ),
        serialization_alias="AL1.3",
        title="Allergy Code/Mnemonic/Description",
        description="R | Item #00205",
    )

    al1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_4",
            "allergy_severity",
            "AL1.4",
        ),
        serialization_alias="AL1.4",
        title="Allergy Severity",
        description="O | Item #00206 | Table 0128 - Allergy severity | LEN:2",
    )

    al1_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_5",
            "allergy_reaction",
            "AL1.5",
        ),
        serialization_alias="AL1.5",
        title="Allergy Reaction",
        description="O | Item #00207 | LEN:15",
    )

    al1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_6",
            "identification_date",
            "AL1.6",
        ),
        serialization_alias="AL1.6",
        title="Identification Date",
        description="O | Item #00208 | LEN:8",
    )

    @field_validator("al1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("al1_6", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
