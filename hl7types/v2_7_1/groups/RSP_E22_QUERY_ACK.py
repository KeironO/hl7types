"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RSP_E22.QUERY_ACK
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class RSP_E22_QUERY_ACK(BaseModel):
    """HL7 v2 RSP_E22.QUERY_ACK group."""

    pass

    model_config = {"populate_by_name": True}
