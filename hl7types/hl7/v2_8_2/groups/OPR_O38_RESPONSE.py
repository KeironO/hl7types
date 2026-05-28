"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OPR_O38.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .OPR_O38_ORDER import OPR_O38_ORDER

_OPR_O38_ORDER = OPR_O38_ORDER


class OPR_O38_RESPONSE(BaseModel):
    """HL7 v2 OPR_O38.RESPONSE group.

    Attributes:
        ORDER (List[OPR_O38_ORDER]): required
    """

    ORDER: list[_OPR_O38_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
