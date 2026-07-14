"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PEX_P07.STUDY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CSP import CSP
from ..segments.CSR import CSR

_CSP = CSP
_CSR = CSR


class PEX_P07_STUDY(HL7Model):
    """HL7 v2 PEX_P07.STUDY group.

    Attributes:
        CSR (CSR): CSR - clinical study registration segment, required
        CSP (Optional[List[CSP]]): CSP - clinical study phase segment, optional
    """

    CSR: _CSR = Field(
        title="CSR",
        description="CSR - clinical study registration segment",
    )

    CSP: Optional[List[_CSP]] = Field(
        default=None,
        title="CSP",
        description="CSP - clinical study phase segment",
    )

    model_config = {"populate_by_name": True}
