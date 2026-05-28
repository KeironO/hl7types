"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_Z86.COMMON_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ORC import ORC

from .RSP_Z86_ADMINISTRATION import RSP_Z86_ADMINISTRATION
from .RSP_Z86_DISPENSE import RSP_Z86_DISPENSE
from .RSP_Z86_ENCODED_ORDER import RSP_Z86_ENCODED_ORDER
from .RSP_Z86_GIVE import RSP_Z86_GIVE
from .RSP_Z86_OBSERVATION import RSP_Z86_OBSERVATION
from .RSP_Z86_ORDER_DETAIL import RSP_Z86_ORDER_DETAIL
from .RSP_Z86_TIMING import RSP_Z86_TIMING

_ORC = ORC
_RSP_Z86_ADMINISTRATION = RSP_Z86_ADMINISTRATION
_RSP_Z86_DISPENSE = RSP_Z86_DISPENSE
_RSP_Z86_ENCODED_ORDER = RSP_Z86_ENCODED_ORDER
_RSP_Z86_GIVE = RSP_Z86_GIVE
_RSP_Z86_OBSERVATION = RSP_Z86_OBSERVATION
_RSP_Z86_ORDER_DETAIL = RSP_Z86_ORDER_DETAIL
_RSP_Z86_TIMING = RSP_Z86_TIMING


class RSP_Z86_COMMON_ORDER(BaseModel):
    """HL7 v2 RSP_Z86.COMMON_ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[RSP_Z86_TIMING]]): optional
        ORDER_DETAIL (Optional[RSP_Z86_ORDER_DETAIL]): optional
        ENCODED_ORDER (Optional[RSP_Z86_ENCODED_ORDER]): optional
        DISPENSE (Optional[RSP_Z86_DISPENSE]): optional
        GIVE (Optional[RSP_Z86_GIVE]): optional
        ADMINISTRATION (Optional[RSP_Z86_ADMINISTRATION]): optional
        OBSERVATION (List[RSP_Z86_OBSERVATION]): required
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: Optional[List[_RSP_Z86_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    ORDER_DETAIL: Optional[_RSP_Z86_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    ENCODED_ORDER: Optional[_RSP_Z86_ENCODED_ORDER] = Field(
        default=None,
        title="ENCODED_ORDER",
        description="Optional",
    )

    DISPENSE: Optional[_RSP_Z86_DISPENSE] = Field(
        default=None,
        title="DISPENSE",
        description="Optional",
    )

    GIVE: Optional[_RSP_Z86_GIVE] = Field(
        default=None,
        title="GIVE",
        description="Optional",
    )

    ADMINISTRATION: Optional[_RSP_Z86_ADMINISTRATION] = Field(
        default=None,
        title="ADMINISTRATION",
        description="Optional",
    )

    OBSERVATION: List[_RSP_Z86_OBSERVATION] = Field(
        default=...,
        title="OBSERVATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
