"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QBP_Q13.QBP
Type: Group
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class QBP_Q13_QBP(BaseModel):
    """HL7 v2 QBP_Q13.QBP group.

    Attributes:
        anyzsegment (Optional[Any]): optional
    """

    anyzsegment: Any | None = None

    model_config = {"populate_by_name": True}
