"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PLN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class PLN(HL7Model):
    """HL7 v2 PLN data type.

    Attributes
    ----------
    pln_1 : str | None
        PLN.1 (opt) - ID number (ST) (ST)

    pln_2 : str | None
        PLN.2 (opt) - type of ID number (IS) (IS)

    pln_3 : str | None
        PLN.3 (opt) - state/other qualifying info (ST)

    pln_4 : str | None
        PLN.4 (opt) - expiration date (DT)
    """

    pln_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pln_1",
            "id_number_st",
            "PLN.1",
        ),
        serialization_alias="PLN.1",
        title="ID number (ST)",
    )

    pln_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pln_2",
            "type_of_id_number_is",
            "PLN.2",
        ),
        serialization_alias="PLN.2",
        title="type of ID number (IS)",
    )

    pln_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pln_3",
            "state_other_qualifying_info",
            "PLN.3",
        ),
        serialization_alias="PLN.3",
        title="state/other qualifying info",
    )

    pln_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pln_4",
            "expiration_date",
            "PLN.4",
        ),
        serialization_alias="PLN.4",
        title="expiration date",
    )

    @field_validator("pln_4", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
