"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RAS_O17.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .RAS_O17_ADMINISTRATION import RAS_O17_ADMINISTRATION
from .RAS_O17_ENCODING import RAS_O17_ENCODING
from .RAS_O17_ORDER_DETAIL import RAS_O17_ORDER_DETAIL
from .RAS_O17_TIMING import RAS_O17_TIMING

_CTI = CTI
_ORC = ORC
_PRT = PRT
_RAS_O17_ADMINISTRATION = RAS_O17_ADMINISTRATION
_RAS_O17_ENCODING = RAS_O17_ENCODING
_RAS_O17_ORDER_DETAIL = RAS_O17_ORDER_DETAIL
_RAS_O17_TIMING = RAS_O17_TIMING


class RAS_O17_ORDER(HL7Model):
    """HL7 v2 RAS_O17.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[RAS_O17_TIMING]]): optional
        ORDER_DETAIL (Optional[RAS_O17_ORDER_DETAIL]): optional
        PRT (Optional[List[PRT]]): optional
        ENCODING (Optional[RAS_O17_ENCODING]): optional
        ADMINISTRATION (List[RAS_O17_ADMINISTRATION]): required
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: Optional[List[_RAS_O17_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    ORDER_DETAIL: Optional[_RAS_O17_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ENCODING: Optional[_RAS_O17_ENCODING] = Field(
        default=None,
        title="ENCODING",
        description="Optional",
    )

    ADMINISTRATION: List[_RAS_O17_ADMINISTRATION] = Field(
        default=...,
        title="ADMINISTRATION",
        description="Required, repeating",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
