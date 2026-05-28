"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORI_O24.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.IPC import IPC
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.ROL import ROL
from .ORI_O24_TIMING import ORI_O24_TIMING

_IPC = IPC
_NTE = NTE
_OBR = OBR
_ORC = ORC
_ORI_O24_TIMING = ORI_O24_TIMING
_ROL = ROL


class ORI_O24_ORDER(BaseModel):
    """HL7 v2 ORI_O24.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[ORI_O24_TIMING]]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        ROL (Optional[List[ROL]]): optional
        IPC (List[IPC]): required
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: list[_ORI_O24_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    ROL: list[_ROL] | None = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    IPC: list[_IPC] = Field(
        default=...,
        title="IPC",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
