"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RCI_I05.PROVIDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTD import CTD
from ..segments.PRD import PRD

_CTD = CTD
_PRD = PRD


class RCI_I05_PROVIDER(HL7Model):
    """HL7 v2 RCI_I05.PROVIDER group.

    Attributes:
        PRD (PRD): required
        CTD (Optional[List[CTD]]): optional
    """

    PRD: _PRD = Field(
        title="PRD",
        description="Required",
    )

    CTD: Optional[List[_CTD]] = Field(
        default=None,
        title="CTD",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
