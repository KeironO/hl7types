"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: QVR_Q17.QBP
Type: Group
"""
from _future__ import annotations

from typing import Optional, Any
from pydantic import BaseModel, Field


class QVR_Q17_QBP(BaseModel):
    """HL7 v2 QVR_Q17.QBP group.

    Attributes:
        anyhl7segment (Optional[Any]): optional
    """

    anyhl7segment: Optional[Any] = None

    model_config = {"populate_by_name": True}
