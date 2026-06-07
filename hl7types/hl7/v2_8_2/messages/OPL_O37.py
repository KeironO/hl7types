"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OPL_O37
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PRT import PRT
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.OPL_O37_GUARANTOR import OPL_O37_GUARANTOR
from ..groups.OPL_O37_ORDER import OPL_O37_ORDER

_MSH = MSH
_NTE = NTE
_OPL_O37_GUARANTOR = OPL_O37_GUARANTOR
_OPL_O37_ORDER = OPL_O37_ORDER
_PRT = PRT
_SFT = SFT
_UAC = UAC


class OPL_O37(HL7Model):
    """HL7 v2 OPL_O37 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        PRT (List[PRT]): required
        GUARANTOR (Optional[OPL_O37_GUARANTOR]): optional
        ORDER (List[OPL_O37_ORDER]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PRT: List[_PRT] = Field(
        min_length=1,
        title="PRT",
        description="Required, repeating",
    )

    GUARANTOR: Optional[_OPL_O37_GUARANTOR] = Field(
        default=None,
        title="GUARANTOR",
        description="Optional",
    )

    ORDER: List[_OPL_O37_ORDER] = Field(
        min_length=1,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
