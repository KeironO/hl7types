"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PEX_P07.ASSOCIATED_PERSON
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NK1 import NK1
from ..segments.PRB import PRB

from .PEX_P07_ASSOCIATED_OBSERVATION import PEX_P07_ASSOCIATED_OBSERVATION
from .PEX_P07_ASSOCIATED_RX_ADMIN import PEX_P07_ASSOCIATED_RX_ADMIN
from .PEX_P07_ASSOCIATED_RX_ORDER import PEX_P07_ASSOCIATED_RX_ORDER

_NK1 = NK1
_PEX_P07_ASSOCIATED_OBSERVATION = PEX_P07_ASSOCIATED_OBSERVATION
_PEX_P07_ASSOCIATED_RX_ADMIN = PEX_P07_ASSOCIATED_RX_ADMIN
_PEX_P07_ASSOCIATED_RX_ORDER = PEX_P07_ASSOCIATED_RX_ORDER
_PRB = PRB


class PEX_P07_ASSOCIATED_PERSON(BaseModel):
    """HL7 v2 PEX_P07.ASSOCIATED_PERSON group.

    Attributes:
        NK1 (NK1): required
        ASSOCIATED_RX_ORDER (Optional[PEX_P07_ASSOCIATED_RX_ORDER]): optional
        ASSOCIATED_RX_ADMIN (Optional[List[PEX_P07_ASSOCIATED_RX_ADMIN]]): optional
        PRB (Optional[List[PRB]]): optional
        ASSOCIATED_OBSERVATION (Optional[List[PEX_P07_ASSOCIATED_OBSERVATION]]): optional
    """

    NK1: _NK1 = Field(
        default=...,
        title="NK1",
        description="Required",
    )

    ASSOCIATED_RX_ORDER: Optional[_PEX_P07_ASSOCIATED_RX_ORDER] = Field(
        default=None,
        title="ASSOCIATED_RX_ORDER",
        description="Optional",
    )

    ASSOCIATED_RX_ADMIN: Optional[List[_PEX_P07_ASSOCIATED_RX_ADMIN]] = Field(
        default=None,
        title="ASSOCIATED_RX_ADMIN",
        description="Optional, repeating",
    )

    PRB: Optional[List[_PRB]] = Field(
        default=None,
        title="PRB",
        description="Optional, repeating",
    )

    ASSOCIATED_OBSERVATION: Optional[List[_PEX_P07_ASSOCIATED_OBSERVATION]] = Field(
        default=None,
        title="ASSOCIATED_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
