"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ADT_A61
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.ROL import ROL

_EVN = EVN
_MSH = MSH
_PD1 = PD1
_PID = PID
_PV1 = PV1
_PV2 = PV2
_ROL = ROL


class ADT_A61(HL7Model):
    """HL7 v2 ADT_A61 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PV1 (PV1): required
        ROL (Optional[List[ROL]]): optional
        PV2 (Optional[PV2]): optional
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

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="Required",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
