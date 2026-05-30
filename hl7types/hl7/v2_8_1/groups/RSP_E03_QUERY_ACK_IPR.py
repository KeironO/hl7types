"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RSP_E03.QUERY_ACK_IPR
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model


class RSP_E03_QUERY_ACK_IPR(HL7Model):
    """HL7 v2 RSP_E03.QUERY_ACK_IPR group."""

    pass

    model_config = {"populate_by_name": True}
