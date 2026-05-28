"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OPR_O38.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .OPR_O38_ORDER import OPR_O38_ORDER

_OPR_O38_ORDER = OPR_O38_ORDER


class OPR_O38_RESPONSE(BaseModel):
    """HL7 v2 OPR_O38.RESPONSE group.

    Attributes:
        ORDER (List[OPR_O38_ORDER]): required
    """

    ORDER: List[_OPR_O38_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
