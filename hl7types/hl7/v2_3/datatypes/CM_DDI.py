"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_DDI
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CM_DDI(BaseModel):
    """HL7 v2 CM_DDI data type."""

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

    model_config = {"populate_by_name": True}
