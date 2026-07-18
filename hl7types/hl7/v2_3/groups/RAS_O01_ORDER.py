"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RAS_O01.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.ORC import ORC
from ..segments.RXA import RXA
from ..segments.RXR import RXR

from .RAS_O01_ENCODING import RAS_O01_ENCODING
from .RAS_O01_OBSERVATION import RAS_O01_OBSERVATION
from .RAS_O01_ORDER_DETAIL import RAS_O01_ORDER_DETAIL

_CTI = CTI
_ORC = ORC
_RAS_O01_ENCODING = RAS_O01_ENCODING
_RAS_O01_OBSERVATION = RAS_O01_OBSERVATION
_RAS_O01_ORDER_DETAIL = RAS_O01_ORDER_DETAIL
_RXA = RXA
_RXR = RXR


class RAS_O01_ORDER(HL7Model):
    """HL7 v2 RAS_O01.ORDER group.

    Attributes:
        ORC (ORC): Common order segment, required
        ORDER_DETAIL (Optional[RAS_O01_ORDER_DETAIL]): optional
        ENCODING (Optional[RAS_O01_ENCODING]): optional
        RXA (List[RXA]): Pharmacy administration segment, required
        RXR (RXR): Pharmacy route segment, required
        OBSERVATION (Optional[List[RAS_O01_OBSERVATION]]): optional
        CTI (Optional[List[CTI]]): Clinical Trial Identification, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common order segment",
    )

    ORDER_DETAIL: Optional[_RAS_O01_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
    )

    ENCODING: Optional[_RAS_O01_ENCODING] = Field(
        default=None,
        title="ENCODING",
    )

    RXA: List[_RXA] = Field(
        min_length=1,
        title="RXA",
        description="Pharmacy administration segment",
    )

    RXR: _RXR = Field(
        title="RXR",
        description="Pharmacy route segment",
    )

    OBSERVATION: Optional[List[_RAS_O01_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Clinical Trial Identification",
    )

    model_config = ConfigDict(populate_by_name=True)
