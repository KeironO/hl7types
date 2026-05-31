"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PPR_PC1.CHOICE
Type: Group
"""
from __future__ import annotations

from typing import Optional, Any
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBR import OBR

_OBR = OBR


class PPR_PC1_CHOICE(HL7Model):
    """HL7 v2 PPR_PC1.CHOICE group.

    Attributes:
        OBR (Optional[OBR]): optional
        anyhl7segment (Optional[Any]): optional
    """

    OBR: Optional[_OBR] = Field(
        default=None,
        title="OBR",
        description="Optional",
    )

    anyhl7segment: Optional[Any] = None

    model_config = {"populate_by_name": True}
