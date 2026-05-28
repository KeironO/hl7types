"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OML_O21.ORDER_GENERAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .OML_O21_CONTAINER_1 import OML_O21_CONTAINER_1
from .OML_O21_ORDER import OML_O21_ORDER

_OML_O21_CONTAINER_1 = OML_O21_CONTAINER_1
_OML_O21_ORDER = OML_O21_ORDER


class OML_O21_ORDER_GENERAL(BaseModel):
    """HL7 v2 OML_O21.ORDER_GENERAL group.

    Attributes:
        CONTAINER_1 (Optional[OML_O21_CONTAINER_1]): optional
        ORDER (List[OML_O21_ORDER]): required
    """

    CONTAINER_1: Optional[_OML_O21_CONTAINER_1] = Field(
        default=None,
        title="CONTAINER_1",
        description="Optional",
    )

    ORDER: List[_OML_O21_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
