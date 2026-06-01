"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_PLN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class CM_PLN(HL7Model):
    """HL7 v2 CM_PLN data type.

    Attributes
    ----------
    cm_pln_1 : str | None
        CM_PLN.1 (opt) - ID number (ST)

    cm_pln_2 : str | None
        CM_PLN.2 (opt) - type of ID number (IS) (IS)

    cm_pln_3 : str | None
        CM_PLN.3 (opt) - state/other qualifying info (ST)

    cm_pln_4 : str | None
        CM_PLN.4 (opt) - expiration date (DT)
    """

    cm_pln_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pln_1",
            "id_number",
            "CM_PLN.1",
        ),
        serialization_alias="CM_PLN.1",
        title="ID number",
    )

    cm_pln_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pln_2",
            "type_of_id_number_is",
            "CM_PLN.2",
        ),
        serialization_alias="CM_PLN.2",
        title="type of ID number (IS)",
    )

    cm_pln_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pln_3",
            "state_other_qualifying_info",
            "CM_PLN.3",
        ),
        serialization_alias="CM_PLN.3",
        title="state/other qualifying info",
    )

    cm_pln_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pln_4",
            "expiration_date",
            "CM_PLN.4",
        ),
        serialization_alias="CM_PLN.4",
        title="expiration date",
    )

    @field_validator("cm_pln_4", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
