"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PPV_PCA.CHOICE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBR import OBR
from ..segments.RXO import RXO

_OBR = OBR
_RXO = RXO


class PPV_PCA_CHOICE(HL7Model):
    """HL7 v2 PPV_PCA.CHOICE group.

    Attributes:
        OBR (Optional[OBR]): optional
        RXO (Optional[RXO]): optional
    """

    OBR: Optional[_OBR] = Field(
        default=None,
        title="OBR",
        description="Optional",
    )

    RXO: Optional[_RXO] = Field(
        default=None,
        title="RXO",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
