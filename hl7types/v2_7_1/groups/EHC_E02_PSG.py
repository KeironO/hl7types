"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E02.PSG
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PSG import PSG
from ..segments.PSL import PSL

_PSG = PSG
_PSL = PSL


class EHC_E02_PSG(BaseModel):
    """HL7 v2 EHC_E02.PSG group.

    Attributes:
        PSG (PSG): required
        PSL (Optional[List[PSL]]): optional
    """

    PSG: _PSG = Field(
        default=...,
        title="PSG",
        description="Required",
    )

    PSL: Optional[List[_PSL]] = Field(
        default=None,
        title="PSL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
