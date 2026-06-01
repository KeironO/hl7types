"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_PEN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class CM_PEN(HL7Model):
    """HL7 v2 CM_PEN data type.

    Attributes
    ----------
    cm_pen_1 : str | None
        CM_PEN.1 (opt) - penalty type (IS)

    cm_pen_2 : str | None
        CM_PEN.2 (opt) - penalty amount (NM)
    """

    cm_pen_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pen_1",
            "penalty_type",
            "CM_PEN.1",
        ),
        serialization_alias="CM_PEN.1",
        title="penalty type",
    )

    cm_pen_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pen_2",
            "penalty_amount",
            "CM_PEN.2",
        ),
        serialization_alias="CM_PEN.2",
        title="penalty amount",
    )

    @field_validator("cm_pen_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
