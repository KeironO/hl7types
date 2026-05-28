"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: EIP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .EI import EI


class EIP(BaseModel):
    """HL7 v2 EIP data type."""

    eip_1: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "eip_1",
            "parent_s_placer_order_number",
            "EIP.1",
        ),
        serialization_alias="EIP.1",
        title="parent´s placer order number",
    )

    eip_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "eip_2",
            "parent_s_filler_order_number",
            "EIP.2",
        ),
        serialization_alias="EIP.2",
        title="parent´s filler order number",
    )

    model_config = {"populate_by_name": True}
