"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: BAR_P01.PROCEDURE
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


class BAR_P01_PROCEDURE(HL7Model):
    """HL7 v2 BAR_P01.PROCEDURE group.

    Attributes:
        PR1 (PR1): Procedures, required
        ROL (Optional[List[ROL]]): Role, optional
    """

    PR1: _PR1 = Field(
        title="PR1",
        description="Procedures",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = {"populate_by_name": True}
