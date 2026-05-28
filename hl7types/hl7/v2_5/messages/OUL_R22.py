"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OUL_R22
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OUL_R22_PATIENT import OUL_R22_PATIENT
from ..groups.OUL_R22_SPECIMEN import OUL_R22_SPECIMEN
from ..groups.OUL_R22_VISIT import OUL_R22_VISIT
from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

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

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    NTE: _NTE | None = Field(
        default=None,
        title="NTE",
        description="Optional",
    )

    PATIENT: _OUL_R22_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    VISIT: _OUL_R22_VISIT | None = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    SPECIMEN: list[_OUL_R22_SPECIMEN] = Field(
        default=...,
        title="SPECIMEN",
        description="Required, repeating",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
