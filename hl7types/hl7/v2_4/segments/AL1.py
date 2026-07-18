"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: AL1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE

_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class AL1(HL7Model):
    """Patient allergy information (S3.4.6).

    Attributes
    ----------
    al1_1 : CE
        AL1.1 - Set ID - AL1 (CE) R S3.4.6.1

    al1_2 : CE | None
        AL1.2 - Allergen Type Code (CE) O S3.4.7.2 | 0127 - Allergen type

    al1_3 : CE
        AL1.3 - Allergen Code/Mnemonic/Description (CE) R S3.4.7.3

    al1_4 : CE | None
        AL1.4 - Allergy Severity Code (CE) O S3.4.7.4 | 0128 - Allergy severity

    al1_5 : list[str] | None
        AL1.5 - Allergy Reaction Code (ST) O rep S3.4.7.5

    al1_6 : str | None
        AL1.6 - Identification Date (DT) O S3.4.6.6
    """

    al1_1: CE = Field(
        validation_alias=AliasChoices(
            "al1_1",
            "set_id_al1",
            "AL1.1",
        ),
        serialization_alias="AL1.1",
        title="Set ID - AL1",
        description="R | Item #00203",
    )

    al1_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_2",
            "allergen_type_code",
            "AL1.2",
        ),
        serialization_alias="AL1.2",
        title="Allergen Type Code",
        description="O | Item #00204 | Table 0127 - Allergen type",
    )

    al1_3: CE = Field(
        validation_alias=AliasChoices(
            "al1_3",
            "allergen_code_mnemonic_description",
            "AL1.3",
        ),
        serialization_alias="AL1.3",
        title="Allergen Code/Mnemonic/Description",
        description="R | Item #00205",
    )

    al1_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_4",
            "allergy_severity_code",
            "AL1.4",
        ),
        serialization_alias="AL1.4",
        title="Allergy Severity Code",
        description="O | Item #00206 | Table 0128 - Allergy severity",
    )

    al1_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_5",
            "allergy_reaction_code",
            "AL1.5",
        ),
        serialization_alias="AL1.5",
        title="Allergy Reaction Code",
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

    @field_validator("al1_6", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
