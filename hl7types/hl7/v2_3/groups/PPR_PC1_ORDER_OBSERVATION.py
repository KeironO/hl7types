"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PPR_PC1.ORDER_OBSERVATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.VAR import VAR

_NTE = NTE
_OBX = OBX
_VAR = VAR


class PPR_PC1_ORDER_OBSERVATION(BaseModel):
    """HL7 v2 PPR_PC1.ORDER_OBSERVATION group.

    Attributes:
        OBX (OBX): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
    """

    OBX: _OBX = Field(
        default=...,
        title="OBX",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VAR: list[_VAR] | None = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
