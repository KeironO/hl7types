"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DFT_P11.VISIT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PRT import PRT
from ..segments.PV2 import PV2
from ..segments.ROL import ROL

_PRT = PRT
_PV2 = PV2
_ROL = ROL


class DFT_P11_VISIT(HL7Model):
    """HL7 v2 DFT_P11.VISIT group.

    Attributes:
        PV2 (PV2): required
        PRT (Optional[List[PRT]]): optional
        ROL (Optional[List[ROL]]): optional
    """

    PV2: _PV2 = Field(
        default=...,
        title="PV2",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
