"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: AL1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class AL1(HL7Model):
    """Patient Allergy Information (S3.4.6).

    Attributes
    ----------
    al1_1 : str
        AL1.1 (req) - Set ID - AL1 (SI) S3.4.6.1

    al1_2 : CE | None
        AL1.2 (opt) - Allergen Type Code (CE) S3.4.6.2 | 0127 - Allergen Type

    al1_3 : CE
        AL1.3 (req) - Allergen Code/Mnemonic/Description (CE) S3.4.6.3

    al1_4 : CE | None
        AL1.4 (opt) - Allergy Severity Code (CE) S3.4.6.4 | 0128 - Allergy Severity

    al1_5 : list[str] | None
        AL1.5 (opt, rep) - Allergy Reaction Code (ST) S3.4.6.5

    al1_6 : str | None
        AL1.6 (opt) - Identification Date (DT) S3.4.6.6
    """

    al1_1: str = Field(
        validation_alias=AliasChoices(
            "al1_1",
            "set_id_al1",
            "AL1.1",
        ),
        serialization_alias="AL1.1",
        title="Set ID - AL1",
        description="Item #203",
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
        description="Item #204 | Table HL70127",
    )

    al1_3: CE = Field(
        validation_alias=AliasChoices(
            "al1_3",
            "allergen_code_mnemonic_description",
            "AL1.3",
        ),
        serialization_alias="AL1.3",
        title="Allergen Code/Mnemonic/Description",
        description="Item #205",
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
        description="Item #206 | Table HL70128",
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
        description="Item #207",
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
        description="Item #208",
    )

    @field_validator("al1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("al1_6", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
