"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: AL1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CWE import CWE


class AL1(HL7Model):
    """HL7 v2 AL1 segment.

    Attributes
    ----------
    al1_1 : str
        AL1.1 (req) - Set ID - AL1 (SI)

    al1_2 : CWE | None
        AL1.2 (opt) - Allergen Type Code (CWE)

    al1_3 : CWE
        AL1.3 (req) - Allergen Code/Mnemonic/Description (CWE)

    al1_4 : CWE | None
        AL1.4 (opt) - Allergy Severity Code (CWE)

    al1_5 : list[str] | None
        AL1.5 (opt, rep) - Allergy Reaction Code (ST)
    """

    al1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "al1_1",
            "set_id_al1",
            "AL1.1",
        ),
        serialization_alias="AL1.1",
        title="Set ID - AL1",
        description="Item #203",
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
        description="Item #204 | Table HL70127",
    )

    al1_3: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "al1_3",
            "allergen_code_mnemonic_description",
            "AL1.3",
        ),
        serialization_alias="AL1.3",
        title="Allergen Code/Mnemonic/Description",
        description="Item #205",
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

    @field_validator("al1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
