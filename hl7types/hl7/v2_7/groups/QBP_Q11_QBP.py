"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: QBP_Q11.QBP
Type: Group
"""
from __future__ import annotations

from typing import Optional, Any
from pydantic import BaseModel, Field


class QBP_Q11_QBP(BaseModel):
    """HL7 v2 QBP_Q11.QBP group.

    Attributes:
        anyhl7segment (Optional[Any]): optional
    """

    anyhl7segment: Optional[Any] = None

    model_config = {"populate_by_name": True}
