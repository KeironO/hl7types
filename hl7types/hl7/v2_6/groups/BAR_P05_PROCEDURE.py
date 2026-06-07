"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: BAR_P05.PROCEDURE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PR1 import PR1
from ..segments.ROL import ROL

_PR1 = PR1
_ROL = ROL


class BAR_P05_PROCEDURE(HL7Model):
    """HL7 v2 BAR_P05.PROCEDURE group.

    Attributes:
        PR1 (PR1): required
        ROL (Optional[List[ROL]]): optional
    """

    PR1: _PR1 = Field(
        title="PR1",
        description="Required",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
