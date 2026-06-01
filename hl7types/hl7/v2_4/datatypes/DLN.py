"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: DLN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class DLN(HL7Model):
    """HL7 v2 DLN data type.

    Attributes
    ----------
    dln_1 : str | None
        DLN.1 (opt) - Driver´s License Number (ST)

    dln_2 : str | None
        DLN.2 (opt) - Issuing State, province, country (IS)

    dln_3 : str | None
        DLN.3 (opt) - expiration date (DT)
    """

    dln_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dln_1",
            "driver_s_license_number",
            "DLN.1",
        ),
        serialization_alias="DLN.1",
        title="Driver´s License Number",
    )

    dln_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dln_2",
            "issuing_state_province_country",
            "DLN.2",
        ),
        serialization_alias="DLN.2",
        title="Issuing State, province, country",
    )

    dln_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dln_3",
            "expiration_date",
            "DLN.3",
        ),
        serialization_alias="DLN.3",
        title="expiration date",
    )

    @field_validator("dln_3", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
