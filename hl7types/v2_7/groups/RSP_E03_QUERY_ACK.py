"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RSP_E03.QUERY_ACK
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class RSP_E03_QUERY_ACK(BaseModel):
    """HL7 v2 RSP_E03.QUERY_ACK group."""

    pass

    model_config = {"populate_by_name": True}
