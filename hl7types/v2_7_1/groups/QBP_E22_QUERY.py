"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: QBP_E22.QUERY
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class QBP_E22_QUERY(BaseModel):
    """HL7 v2 QBP_E22.QUERY group."""

    pass

    model_config = {"populate_by_name": True}
