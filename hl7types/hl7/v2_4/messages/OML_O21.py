"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OML_O21
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OML_O21_ORDER_GENERAL import OML_O21_ORDER_GENERAL
from ..groups.OML_O21_PATIENT import OML_O21_PATIENT
from ..segments.MSH import MSH
from ..segments.NTE import NTE

_MSH = MSH
_NTE = NTE
_OML_O21_ORDER_GENERAL = OML_O21_ORDER_GENERAL
_OML_O21_PATIENT = OML_O21_PATIENT


class OML_O21(BaseModel):
    """HL7 v2 OML_O21 message.

    Attributes:
        MSH (MSH): required
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OML_O21_PATIENT]): optional
        ORDER_GENERAL (List[OML_O21_ORDER_GENERAL]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
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

    ORDER_GENERAL: list[_OML_O21_ORDER_GENERAL] = Field(
        default=...,
        title="ORDER_GENERAL",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
