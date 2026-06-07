"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: DPR_O48.DONATION_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR

_NTE = NTE
_OBR = OBR


class DPR_O48_DONATION_ORDER(HL7Model):
    """HL7 v2 DPR_O48.DONATION_ORDER group.

    Attributes:
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
    """

    OBR: _OBR = Field(
        title="OBR",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
