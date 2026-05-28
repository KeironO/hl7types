"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OML_O21
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OML_O21_ORDER import OML_O21_ORDER
from ..groups.OML_O21_PATIENT import OML_O21_PATIENT
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

_MSH = MSH
_NTE = NTE
_OML_O21_ORDER = OML_O21_ORDER
_OML_O21_PATIENT = OML_O21_PATIENT
_SFT = SFT


class OML_O21(BaseModel):
    """HL7 v2 OML_O21 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OML_O21_PATIENT]): optional
        ORDER (List[OML_O21_ORDER]): required
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

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: _OML_O21_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_OML_O21_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
