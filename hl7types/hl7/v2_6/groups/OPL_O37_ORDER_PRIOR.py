"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OPL_O37.ORDER_PRIOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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


class OPL_O37_ORDER_PRIOR(HL7Model):
    """HL7 v2 OPL_O37.ORDER_PRIOR group.

    Attributes:
        OBR (OBR): required
        ORC (Optional[ORC]): optional
        ROL (Optional[List[ROL]]): optional
        TIMING (Optional[OPL_O37_TIMING]): optional
        OBX (List[OBX]): required
    """

    OBR: _OBR = Field(
        title="OBR",
        description="Required",
    )

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    TIMING: Optional[_OPL_O37_TIMING] = Field(
        default=None,
        title="TIMING",
        description="Optional",
    )

    OBX: List[_OBX] = Field(
        min_length=1,
        title="OBX",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
