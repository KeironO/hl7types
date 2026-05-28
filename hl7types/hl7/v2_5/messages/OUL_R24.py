"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OUL_R24
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OUL_R24_ORDER import OUL_R24_ORDER
from ..groups.OUL_R24_PATIENT import OUL_R24_PATIENT
from ..groups.OUL_R24_VISIT import OUL_R24_VISIT
from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

_DSC = DSC
_MSH = MSH
_NTE = NTE
_OUL_R24_ORDER = OUL_R24_ORDER
_OUL_R24_PATIENT = OUL_R24_PATIENT
_OUL_R24_VISIT = OUL_R24_VISIT
_SFT = SFT


class OUL_R24(BaseModel):
    """HL7 v2 OUL_R24 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        NTE (Optional[NTE]): optional
        PATIENT (Optional[OUL_R24_PATIENT]): optional
        VISIT (Optional[OUL_R24_VISIT]): optional
        ORDER (List[OUL_R24_ORDER]): required
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

    PATIENT: _OUL_R24_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    VISIT: _OUL_R24_VISIT | None = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    ORDER: list[_OUL_R24_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
