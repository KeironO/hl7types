"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: QBP_Q13.QBP
Type: Group
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class QBP_Q13_QBP(BaseModel):
    """HL7 v2 QBP_Q13.QBP group.

    Attributes:
        anyhl7segment (Optional[Any]): optional
    """

    anyhl7segment: Any | None = None

    model_config = {"populate_by_name": True}
