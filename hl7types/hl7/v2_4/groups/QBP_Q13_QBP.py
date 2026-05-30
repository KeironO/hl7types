"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QBP_Q13.QBP
Type: Group
"""
from __future__ import annotations

from typing import Optional, Any
from pydantic import Field
from hl7types.hl7 import HL7Model


class QBP_Q13_QBP(HL7Model):
    """HL7 v2 QBP_Q13.QBP group.

    Attributes:
        anyzsegment (Optional[Any]): optional
    """

    anyzsegment: Optional[Any] = None

    model_config = {"populate_by_name": True}
