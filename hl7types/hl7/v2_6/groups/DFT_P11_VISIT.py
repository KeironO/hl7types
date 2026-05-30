"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: DFT_P11.VISIT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.ROL import ROL

_PV1 = PV1
_PV2 = PV2
_ROL = ROL


class DFT_P11_VISIT(HL7Model):
    """HL7 v2 DFT_P11.VISIT group.

    Attributes:
        PV1 (PV1): required
        PV2 (Optional[PV2]): optional
        ROL (Optional[List[ROL]]): optional
    """

    PV1: _PV1 = Field(
        default=...,
        title="PV1",
        description="Required",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
