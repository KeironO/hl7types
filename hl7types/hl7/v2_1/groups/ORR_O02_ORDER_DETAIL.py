"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ORR_O02.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .ORR_O02_CHOICE import ORR_O02_CHOICE

_ORR_O02_CHOICE = ORR_O02_CHOICE


class ORR_O02_ORDER_DETAIL(BaseModel):
    """HL7 v2 ORR_O02.ORDER_DETAIL group.

    Attributes:
        CHOICE (ORR_O02_CHOICE): required
    """

    CHOICE: _ORR_O02_CHOICE = Field(
        default=...,
        title="CHOICE",
        description="Required",
    )

    model_config = {"populate_by_name": True}
