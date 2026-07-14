"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: INU_U05
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EQU import EQU
from ..segments.INV import INV
from ..segments.MSH import MSH
from ..segments.ROL import ROL

_EQU = EQU
_INV = INV
_MSH = MSH
_ROL = ROL


class INU_U05(HL7Model):
    """INU/ACK  - Automated equipment inventory update (S13).

    Attributes:
        MSH (MSH): Message Header, required
        EQU (EQU): Equipment Detail, required
        INV (List[INV]): Inventory Detail, required
        ROL (Optional[ROL]): Role, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    EQU: _EQU = Field(
        title="EQU",
        description="Equipment Detail",
    )

    INV: List[_INV] = Field(
        min_length=1,
        title="INV",
        description="Inventory Detail",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = {"populate_by_name": True}
