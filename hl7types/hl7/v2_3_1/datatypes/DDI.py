"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: DDI
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class DDI(HL7Model):
    """HL7 v2 DDI data type.

    Attributes
    ----------
    ddi_1 : str | None
        DDI.1 (opt) - delay days (NM)

    ddi_2 : str | None
        DDI.2 (opt) - amount (NM)

    ddi_3 : str | None
        DDI.3 (opt) - number of days (NM)
    """

    ddi_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ddi_1",
            "delay_days",
            "DDI.1",
        ),
        serialization_alias="DDI.1",
        title="delay days",
    )

    ddi_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ddi_2",
            "amount",
            "DDI.2",
        ),
        serialization_alias="DDI.2",
        title="amount",
    )

    ddi_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ddi_3",
            "number_of_days",
            "DDI.3",
        ),
        serialization_alias="DDI.3",
        title="number of days",
    )

    @field_validator("ddi_1", "ddi_2", "ddi_3", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
