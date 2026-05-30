"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: EIP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .EI import EI


class EIP(HL7Model):
    """HL7 v2 EIP data type.

    Attributes
    ----------
    eip_1 : EI | None
        EIP.1 (opt) - Placer Assigned Identifier (EI)

    eip_2 : EI | None
        EIP.2 (opt) - Filler Assigned Identifier (EI)
    """

    eip_1: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "eip_1",
            "placer_assigned_identifier",
            "EIP.1",
        ),
        serialization_alias="EIP.1",
        title="Placer Assigned Identifier",
    )

    eip_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "eip_2",
            "filler_assigned_identifier",
            "EIP.2",
        ),
        serialization_alias="EIP.2",
        title="Filler Assigned Identifier",
    )

    model_config = {"populate_by_name": True}
