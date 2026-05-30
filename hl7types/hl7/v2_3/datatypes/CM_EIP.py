"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_EIP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .EI import EI


class CM_EIP(HL7Model):
    """HL7 v2 CM_EIP data type.

    Attributes
    ----------
    cm_eip_1 : EI | None
        CM_EIP.1 (opt) - parent´s placer order number (EI)

    cm_eip_2 : EI | None
        CM_EIP.2 (opt) - parent´s filler order number (EI)
    """

    cm_eip_1: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_eip_1",
            "parent_s_placer_order_number",
            "CM_EIP.1",
        ),
        serialization_alias="CM_EIP.1",
        title="parent´s placer order number",
    )

    cm_eip_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_eip_2",
            "parent_s_filler_order_number",
            "CM_EIP.2",
        ),
        serialization_alias="CM_EIP.2",
        title="parent´s filler order number",
    )

    model_config = {"populate_by_name": True}
