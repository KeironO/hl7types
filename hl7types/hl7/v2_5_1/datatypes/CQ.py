"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: CQ
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CE import CE


class CQ(BaseModel):
    """HL7 v2 CQ data type.

    Attributes
    ----------
    cq_1 : str | None
        CQ.1 (opt) - Quantity (NM)

    cq_2 : CE | None
        CQ.2 (opt) - Units (CE)
    """

    cq_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cq_1",
            "quantity",
            "CQ.1",
        ),
        serialization_alias="CQ.1",
        title="Quantity",
    )

    cq_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cq_2",
            "units",
            "CQ.2",
        ),
        serialization_alias="CQ.2",
        title="Units",
    )

    model_config = {"populate_by_name": True}
