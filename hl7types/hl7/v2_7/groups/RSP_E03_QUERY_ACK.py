"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RSP_E03.QUERY_ACK
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class RSP_E03_QUERY_ACK(BaseModel):
    """HL7 v2 RSP_E03.QUERY_ACK group."""

    pass

    model_config = {"populate_by_name": True}
