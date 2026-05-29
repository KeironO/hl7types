"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_PEN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CM_PEN(BaseModel):
    """HL7 v2 CM_PEN data type.

    Attributes
    ----------
    cm_pen_1 : str | None
        CM_PEN.1 (opt) - Penalty ID (ID)

    cm_pen_2 : str | None
        CM_PEN.2 (opt) - penalty amount (NM)
    """

    cm_pen_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pen_1",
            "penalty_id",
            "CM_PEN.1",
        ),
        serialization_alias="CM_PEN.1",
        title="Penalty ID",
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

    model_config = {"populate_by_name": True}
