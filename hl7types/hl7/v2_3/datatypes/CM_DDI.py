"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_DDI
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class CM_DDI(HL7Model):
    """HL7 v2 CM_DDI data type.

    Attributes
    ----------
    cm_ddi_1 : str | None
        CM_DDI.1 (opt) - delay days (NM)

    cm_ddi_2 : str | None
        CM_DDI.2 (opt) - amount (NM)

    cm_ddi_3 : str | None
        CM_DDI.3 (opt) - number of days (NM)
    """

    cm_ddi_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ddi_1",
            "delay_days",
            "CM_DDI.1",
        ),
        serialization_alias="CM_DDI.1",
        title="delay days",
    )

    cm_ddi_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ddi_2",
            "amount",
            "CM_DDI.2",
        ),
        serialization_alias="CM_DDI.2",
        title="amount",
    )

    cm_ddi_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ddi_3",
            "number_of_days",
            "CM_DDI.3",
        ),
        serialization_alias="CM_DDI.3",
        title="number of days",
    )

    @field_validator("cm_ddi_1", "cm_ddi_2", "cm_ddi_3", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
