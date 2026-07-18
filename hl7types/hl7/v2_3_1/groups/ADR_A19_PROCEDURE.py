"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ADR_A19.PROCEDURE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PR1 import PR1
from ..segments.ROL import ROL

_PR1 = PR1
_ROL = ROL


class ADR_A19_PROCEDURE(HL7Model):
    """HL7 v2 ADR_A19.PROCEDURE group.

    Attributes:
        PR1 (PR1): PR1 - procedures segment, required
        ROL (Optional[List[ROL]]): Role, optional
    """

    PR1: _PR1 = Field(
        title="PR1",
        description="PR1 - procedures segment",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = ConfigDict(populate_by_name=True)
