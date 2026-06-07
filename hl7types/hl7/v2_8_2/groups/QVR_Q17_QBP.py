"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: QVR_Q17.QBP
Type: Group
"""
from __future__ import annotations

from typing import Optional, Any
from hl7types.hl7 import HL7Model


class QVR_Q17_QBP(HL7Model):
    """HL7 v2 QVR_Q17.QBP group.

    Attributes:
        anyhl7segment (Optional[Any]): optional
    """

    anyhl7segment: Optional[Any] = None

    model_config = {"populate_by_name": True}
