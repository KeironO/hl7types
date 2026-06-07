"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: DFT_P03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.FT1 import FT1
from ..segments.MSH import MSH
from ..segments.OBX import OBX
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_EVN = EVN
_FT1 = FT1
_MSH = MSH
_OBX = OBX
_PID = PID
_PV1 = PV1
_PV2 = PV2


class DFT_P03(HL7Model):
    """HL7 v2 DFT_P03 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        PID (PID): required
        PV1 (Optional[PV1]): optional
        PV2 (Optional[PV2]): optional
        OBX (Optional[List[OBX]]): optional
        FT1 (List[FT1]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Required",
    )

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    FT1: List[_FT1] = Field(
        min_length=1,
        title="FT1",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
