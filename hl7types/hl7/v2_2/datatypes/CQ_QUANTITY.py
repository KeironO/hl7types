"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CQ_QUANTITY
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CQ_QUANTITY(BaseModel):
    """HL7 v2 CQ_QUANTITY data type."""

    cq_quantity_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cq_quantity_1",
            "quantity",
            "CQ_QUANTITY.1",
        ),
        serialization_alias="CQ_QUANTITY.1",
        title="quantity",
    )

    cq_quantity_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cq_quantity_2",
            "units",
            "CQ_QUANTITY.2",
        ),
        serialization_alias="CQ_QUANTITY.2",
        title="units",
    )

    model_config = {"populate_by_name": True}
