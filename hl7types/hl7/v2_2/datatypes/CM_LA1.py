"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_LA1
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .AD import AD


class CM_LA1(BaseModel):
    """HL7 v2 CM_LA1 data type."""

    cm_la1_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_1",
            "dispense_deliver_to_location",
            "CM_LA1.1",
        ),
        serialization_alias="CM_LA1.1",
        title="Dispense / Deliver to Location",
    )

    cm_la1_2: Optional[AD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_2",
            "location",
            "CM_LA1.2",
        ),
        serialization_alias="CM_LA1.2",
        title="location",
    )

    model_config = {"populate_by_name": True}
