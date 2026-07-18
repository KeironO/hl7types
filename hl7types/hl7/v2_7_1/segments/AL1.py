"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: AL1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE

_RE_SI = re.compile(r'\d*')


class AL1(HL7Model):
    """Patient Allergy Information (S3.4.6).

    Attributes
    ----------
    al1_1 : str
        AL1.1 - Set ID - AL1 (SI) R S3.4.6.1

    al1_2 : CWE | None
        AL1.2 - Allergen Type Code (CWE) O S3.4.6.2 | 0127 - Allergen Type

    al1_3 : CWE
        AL1.3 - Allergen Code/Mnemonic/Description (CWE) R S3.4.6.3

    al1_4 : CWE | None
        AL1.4 - Allergy Severity Code (CWE) O S3.4.6.4 | 0128 - Allergy Severity

    al1_5 : list[str] | None
        AL1.5 - Allergy Reaction Code (ST) O rep S3.4.6.5
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

    al1_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_2",
            "allergen_type_code",
            "AL1.2",
        ),
        serialization_alias="AL1.2",
        title="Allergen Type Code",
        description="O | Item #00204 | Table 0127 - Allergen Type",
    )

    al1_3: CWE = Field(
        validation_alias=AliasChoices(
            "al1_3",
            "allergen_code_mnemonic_description",
            "AL1.3",
        ),
        serialization_alias="AL1.3",
        title="Allergen Code/Mnemonic/Description",
        description="R | Item #00205",
    )

    al1_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "al1_4",
            "allergy_severity_code",
            "AL1.4",
        ),
        serialization_alias="AL1.4",
        title="Allergy Severity Code",
        description="O | Item #00206 | Table 0128 - Allergy Severity",
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
        description="O | Item #00207",
    )

    @field_validator("al1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = ConfigDict(populate_by_name=True)
