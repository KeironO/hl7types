"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORR_O02.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class ORR_O02_ORDER_DETAIL(BaseModel):
    """HL7 v2 ORR_O02.ORDER_DETAIL group."""

    pass

    model_config = {"populate_by_name": True}
