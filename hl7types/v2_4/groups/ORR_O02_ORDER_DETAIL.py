"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORR_O02.ORDER_DETAIL
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class ORR_O02_ORDER_DETAIL(BaseModel):
    """HL7 v2 ORR_O02.ORDER_DETAIL group."""

    pass

    model_config = {"populate_by_name": True}
