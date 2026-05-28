"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OUL_R22
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

from ..groups.OUL_R22_PATIENT import OUL_R22_PATIENT
from ..groups.OUL_R22_SPECIMEN import OUL_R22_SPECIMEN
from ..groups.OUL_R22_VISIT import OUL_R22_VISIT

_DSC = DSC
_MSH = MSH
_NTE = NTE
_OUL_R22_PATIENT = OUL_R22_PATIENT
_OUL_R22_SPECIMEN = OUL_R22_SPECIMEN
_OUL_R22_VISIT = OUL_R22_VISIT
_SFT = SFT


class OUL_R22(BaseModel):
    """HL7 v2 OUL_R22 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        NTE (Optional[NTE]): optional
        PATIENT (Optional[OUL_R22_PATIENT]): optional
        VISIT (Optional[OUL_R22_VISIT]): optional
        SPECIMEN (List[OUL_R22_SPECIMEN]): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
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

    VISIT: Optional[_OUL_R22_VISIT] = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    SPECIMEN: List[_OUL_R22_SPECIMEN] = Field(
        default=...,
        title="SPECIMEN",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
