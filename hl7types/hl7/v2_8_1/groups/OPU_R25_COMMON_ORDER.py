"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OPU_R25.COMMON_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC
from ..segments.PRT import PRT

_ORC = ORC
_PRT = PRT


class OPU_R25_COMMON_ORDER(HL7Model):
    """HL7 v2 OPU_R25.COMMON_ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
