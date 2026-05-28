"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: QVR_Q17.QBP
Type: Group
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class QVR_Q17_QBP(BaseModel):
    """HL7 v2 QVR_Q17.QBP group.

    Attributes:
        anyhl7segment (Optional[Any]): optional
    """

    anyhl7segment: Any | None = None

    model_config = {"populate_by_name": True}
