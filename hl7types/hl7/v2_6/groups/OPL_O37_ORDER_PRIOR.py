"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OPL_O37.ORDER_PRIOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
        OBR (OBR): Observation Request, required
        ORC (Optional[ORC]): Common Order, optional
        ROL (Optional[List[ROL]]): Role, optional
        TIMING (Optional[OPL_O37_TIMING]): optional
        OBX (List[OBX]): Observation/Result, required
    """

    OBR: _OBR = Field(
        title="OBR",
        description="Observation Request",
    )

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Common Order",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    TIMING: Optional[_OPL_O37_TIMING] = Field(
        default=None,
        title="TIMING",
    )

    OBX: List[_OBX] = Field(
        min_length=1,
        title="OBX",
        description="Observation/Result",
    )

    model_config = ConfigDict(populate_by_name=True)
