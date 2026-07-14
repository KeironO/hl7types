"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORG_O20.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

_CTI = CTI
_NTE = NTE
_OBR = OBR
_ORC = ORC


class ORG_O20_ORDER(HL7Model):
    """HL7 v2 ORG_O20.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        OBR (Optional[OBR]): Observation Request, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        CTI (Optional[List[CTI]]): Clinical Trial Identification, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    OBR: Optional[_OBR] = Field(
        default=None,
        title="OBR",
        description="Observation Request",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Clinical Trial Identification",
    )

    model_config = {"populate_by_name": True}
