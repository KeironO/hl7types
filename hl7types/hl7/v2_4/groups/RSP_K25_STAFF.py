"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_K25.STAFF
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AFF import AFF
from ..segments.EDU import EDU
from ..segments.LAN import LAN
from ..segments.ORG import ORG
from ..segments.PRA import PRA
from ..segments.STF import STF

_AFF = AFF
_EDU = EDU
_LAN = LAN
_ORG = ORG
_PRA = PRA
_STF = STF


class RSP_K25_STAFF(HL7Model):
    """HL7 v2 RSP_K25.STAFF group.

    Attributes:
        STF (STF): required
        PRA (Optional[PRA]): optional
        ORG (Optional[List[ORG]]): optional
        AFF (Optional[List[AFF]]): optional
        LAN (Optional[List[LAN]]): optional
        EDU (Optional[List[EDU]]): optional
    """

    STF: _STF = Field(
        title="STF",
        description="Required",
    )

    PRA: Optional[_PRA] = Field(
        default=None,
        title="PRA",
        description="Optional",
    )

    ORG: Optional[List[_ORG]] = Field(
        default=None,
        title="ORG",
        description="Optional, repeating",
    )

    AFF: Optional[List[_AFF]] = Field(
        default=None,
        title="AFF",
        description="Optional, repeating",
    )

    LAN: Optional[List[_LAN]] = Field(
        default=None,
        title="LAN",
        description="Optional, repeating",
    )

    EDU: Optional[List[_EDU]] = Field(
        default=None,
        title="EDU",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
