"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PRA
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.PIP import PIP
from ..datatypes.PLN import PLN
from ..datatypes.SPD import SPD


class PRA(HL7Model):
    """PRA - practitioner detail segment (S8.6.3).

    Attributes
    ----------
    pra_1 : CE
        PRA.1 - Primary Key Value - PRA (CE) R S8.6.3.1

    pra_2 : list[CE] | None
        PRA.2 - Practitioner Group (CE) O rep S8.6.3.2 | 0358 - Practitioner Group

    pra_3 : list[str] | None
        PRA.3 - Practitioner Category (IS) O rep S8.6.3.3 | 0186 - Practioner Category

    pra_4 : str | None
        PRA.4 - Provider Billing (ID) O S8.6.3.4 | 0187 - Provider billing

    pra_5 : list[SPD] | None
        PRA.5 - Specialty (SPD) O rep S8.6.3.5 | 0337 - Certification Status

    pra_6 : list[PLN] | None
        PRA.6 - Practitioner ID Numbers (PLN) O rep S8.6.3.6 | 0338 - Practitioner ID number type

    pra_7 : list[PIP] | None
        PRA.7 - Privileges (PIP) O rep S8.6.3.7

    pra_8 : str | None
        PRA.8 - Date Entered Practice (DT) O S8.6.3.8
    """

    pra_1: CE = Field(
        validation_alias=AliasChoices(
            "pra_1",
            "primary_key_value_pra",
            "PRA.1",
        ),
        serialization_alias="PRA.1",
        title="Primary Key Value - PRA",
        description="R | Item #00685",
    )

    pra_2: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_2",
            "practitioner_group",
            "PRA.2",
        ),
        serialization_alias="PRA.2",
        title="Practitioner Group",
        description="O | Item #00686 | Table 0358 - Practitioner Group",
    )

    pra_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_3",
            "practitioner_category",
            "PRA.3",
        ),
        serialization_alias="PRA.3",
        title="Practitioner Category",
        description=(
            "O | Item #00687 | Table 0186 - Practioner Category | LEN:3"
        ),
    )

    pra_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_4",
            "provider_billing",
            "PRA.4",
        ),
        serialization_alias="PRA.4",
        title="Provider Billing",
        description="O | Item #00688 | Table 0187 - Provider billing | LEN:1",
    )

    pra_5: Optional[List[SPD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_5",
            "specialty",
            "PRA.5",
        ),
        serialization_alias="PRA.5",
        title="Specialty",
        description="O | Item #00689 | Table 0337 - Certification Status",
    )

    pra_6: Optional[List[PLN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_6",
            "practitioner_id_numbers",
            "PRA.6",
        ),
        serialization_alias="PRA.6",
        title="Practitioner ID Numbers",
        description=(
            "O | Item #00690 | Table 0338 - Practitioner ID number type"
        ),
    )

    pra_7: Optional[List[PIP]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_7",
            "privileges",
            "PRA.7",
        ),
        serialization_alias="PRA.7",
        title="Privileges",
        description="O | Item #00691",
    )

    pra_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_8",
            "date_entered_practice",
            "PRA.8",
        ),
        serialization_alias="PRA.8",
        title="Date Entered Practice",
        description="O | Item #01296 | LEN:8",
    )

    @field_validator("pra_8", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
