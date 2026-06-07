"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: PPG_PCG.ORDER_OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PRT import PRT
from ..segments.VAR import VAR

_NTE = NTE
_OBX = OBX
_PRT = PRT
_VAR = VAR


class PPG_PCG_ORDER_OBSERVATION(HL7Model):
    """HL7 v2 PPG_PCG.ORDER_OBSERVATION group.

    Attributes:
        OBX (OBX): required
        PRT (Optional[List[PRT]]): optional
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
    """

    OBX: _OBX = Field(
        title="OBX",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
