"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCR_I16.ROLE_PATHWAY_OBJECT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PRD import PRD
from ..segments.ROL import ROL

_PRD = PRD
_ROL = ROL


class CCR_I16_ROLE_PATHWAY_OBJECT(HL7Model):
    """HL7 v2 CCR_I16.ROLE_PATHWAY_OBJECT group.

    Attributes:
        ROL (Optional[ROL]): optional
        PRD (Optional[PRD]): optional
    """

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    PRD: Optional[_PRD] = Field(
        default=None,
        title="PRD",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
