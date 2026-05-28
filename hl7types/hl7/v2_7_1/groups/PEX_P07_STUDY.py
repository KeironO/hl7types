"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PEX_P07.STUDY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CSP import CSP
from ..segments.CSR import CSR

_CSP = CSP
_CSR = CSR


class PEX_P07_STUDY(BaseModel):
    """HL7 v2 PEX_P07.STUDY group.

    Attributes:
        CSR (CSR): required
        CSP (Optional[List[CSP]]): optional
    """

    CSR: _CSR = Field(
        default=...,
        title="CSR",
        description="Required",
    )

    CSP: list[_CSP] | None = Field(
        default=None,
        title="CSP",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
