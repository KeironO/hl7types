"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OPL_O37.ORDER_PRIOR
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBR import OBR
from ..segments.OBX import OBX
from ..segments.ORC import ORC
from ..segments.ROL import ROL
from .OPL_O37_TIMING import OPL_O37_TIMING

_OBR = OBR
_OBX = OBX
_OPL_O37_TIMING = OPL_O37_TIMING
_ORC = ORC
_ROL = ROL


class OPL_O37_ORDER_PRIOR(BaseModel):
    """HL7 v2 OPL_O37.ORDER_PRIOR group.

    Attributes:
        OBR (OBR): required
        ORC (Optional[ORC]): optional
        ROL (Optional[List[ROL]]): optional
        TIMING (Optional[OPL_O37_TIMING]): optional
        OBX (List[OBX]): required
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    ORC: _ORC | None = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    ROL: list[_ROL] | None = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    TIMING: _OPL_O37_TIMING | None = Field(
        default=None,
        title="TIMING",
        description="Optional",
    )

    OBX: list[_OBX] = Field(
        default=...,
        title="OBX",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
