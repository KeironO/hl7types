"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RAS_O17.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.ORC import ORC
from .RAS_O17_ADMINISTRATION import RAS_O17_ADMINISTRATION
from .RAS_O17_ENCODING import RAS_O17_ENCODING
from .RAS_O17_ORDER_DETAIL import RAS_O17_ORDER_DETAIL
from .RAS_O17_TIMING import RAS_O17_TIMING

_CTI = CTI
_ORC = ORC
_RAS_O17_ADMINISTRATION = RAS_O17_ADMINISTRATION
_RAS_O17_ENCODING = RAS_O17_ENCODING
_RAS_O17_ORDER_DETAIL = RAS_O17_ORDER_DETAIL
_RAS_O17_TIMING = RAS_O17_TIMING


class RAS_O17_ORDER(BaseModel):
    """HL7 v2 RAS_O17.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[RAS_O17_TIMING]]): optional
        ORDER_DETAIL (Optional[RAS_O17_ORDER_DETAIL]): optional
        ENCODING (Optional[RAS_O17_ENCODING]): optional
        ADMINISTRATION (List[RAS_O17_ADMINISTRATION]): required
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: list[_RAS_O17_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    ORDER_DETAIL: _RAS_O17_ORDER_DETAIL | None = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    ENCODING: _RAS_O17_ENCODING | None = Field(
        default=None,
        title="ENCODING",
        description="Optional",
    )

    ADMINISTRATION: list[_RAS_O17_ADMINISTRATION] = Field(
        default=...,
        title="ADMINISTRATION",
        description="Required, repeating",
    )

    CTI: list[_CTI] | None = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
