"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OMS_O01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.OMS_O01_ORDER import OMS_O01_ORDER
from ..groups.OMS_O01_PATIENT import OMS_O01_PATIENT

_MSH = MSH
_NTE = NTE
_OMS_O01_ORDER = OMS_O01_ORDER
_OMS_O01_PATIENT = OMS_O01_PATIENT


class OMS_O01(HL7Model):
    """HL7 v2 OMS_O01 message.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        PATIENT (Optional[OMS_O01_PATIENT]): optional
        ORDER (List[OMS_O01_ORDER]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    PATIENT: Optional[_OMS_O01_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_OMS_O01_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
