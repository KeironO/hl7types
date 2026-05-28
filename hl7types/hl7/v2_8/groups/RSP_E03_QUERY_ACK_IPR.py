"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_E03.QUERY_ACK_IPR
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class RSP_E03_QUERY_ACK_IPR(BaseModel):
    """HL7 v2 RSP_E03.QUERY_ACK_IPR group."""

    pass

    model_config = {"populate_by_name": True}
