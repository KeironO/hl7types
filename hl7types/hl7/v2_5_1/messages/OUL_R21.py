"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OUL_R21
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OUL_R21_ORDER_OBSERVATION import OUL_R21_ORDER_OBSERVATION
from ..groups.OUL_R21_PATIENT import OUL_R21_PATIENT
from ..groups.OUL_R21_VISIT import OUL_R21_VISIT
from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

_DSC = DSC
_MSH = MSH
_NTE = NTE
_OUL_R21_ORDER_OBSERVATION = OUL_R21_ORDER_OBSERVATION
_OUL_R21_PATIENT = OUL_R21_PATIENT
_OUL_R21_VISIT = OUL_R21_VISIT
_SFT = SFT


class OUL_R21(BaseModel):
    """HL7 v2 OUL_R21 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        NTE (Optional[NTE]): optional
        PATIENT (Optional[OUL_R21_PATIENT]): optional
        VISIT (Optional[OUL_R21_VISIT]): optional
        ORDER_OBSERVATION (List[OUL_R21_ORDER_OBSERVATION]): required
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

    PATIENT: _OUL_R21_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    VISIT: _OUL_R21_VISIT | None = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    ORDER_OBSERVATION: list[_OUL_R21_ORDER_OBSERVATION] = Field(
        default=...,
        title="ORDER_OBSERVATION",
        description="Required, repeating",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
