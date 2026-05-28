"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: QBP_E03.QUERY_INFORMATION
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class QBP_E03_QUERY_INFORMATION(BaseModel):
    """HL7 v2 QBP_E03.QUERY_INFORMATION group."""

    pass

    model_config = {"populate_by_name": True}
