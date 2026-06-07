"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OUL_R22
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.OUL_R22_PATIENT import OUL_R22_PATIENT
from ..groups.OUL_R22_SPECIMEN import OUL_R22_SPECIMEN

_DSC = DSC
_MSH = MSH
_NK1 = NK1
_NTE = NTE
_OUL_R22_PATIENT = OUL_R22_PATIENT
_OUL_R22_SPECIMEN = OUL_R22_SPECIMEN
_SFT = SFT
_UAC = UAC


class OUL_R22(HL7Model):
    """HL7 v2 OUL_R22 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[NTE]): optional
        PATIENT (Optional[OUL_R22_PATIENT]): optional
        NK1 (Optional[List[NK1]]): optional
        SPECIMEN (List[OUL_R22_SPECIMEN]): required
        DSC (Optional[DSC]): optional
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

    NTE: Optional[_NTE] = Field(
        default=None,
        title="NTE",
        description="Optional",
    )

    PATIENT: Optional[_OUL_R22_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    SPECIMEN: List[_OUL_R22_SPECIMEN] = Field(
        min_length=1,
        title="SPECIMEN",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
