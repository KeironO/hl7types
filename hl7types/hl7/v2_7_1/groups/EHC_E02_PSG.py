"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E02.PSG
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PSG import PSG
from ..segments.PSL import PSL

_PSG = PSG
_PSL = PSL


class EHC_E02_PSG(HL7Model):
    """HL7 v2 EHC_E02.PSG group.

    Attributes:
        PSG (PSG): Product/Service Group, required
        PSL (Optional[List[PSL]]): Product/Service Line Item, optional
    """

    PSG: _PSG = Field(
        title="PSG",
        description="Product/Service Group",
    )

    PSL: Optional[List[_PSL]] = Field(
        default=None,
        title="PSL",
        description="Product/Service Line Item",
    )

    model_config = ConfigDict(populate_by_name=True)
