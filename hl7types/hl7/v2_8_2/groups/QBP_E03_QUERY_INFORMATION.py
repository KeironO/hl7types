"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: QBP_E03.QUERY_INFORMATION
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model


class QBP_E03_QUERY_INFORMATION(HL7Model):
    """HL7 v2 QBP_E03.QUERY_INFORMATION group."""

    pass

    model_config = {"populate_by_name": True}
