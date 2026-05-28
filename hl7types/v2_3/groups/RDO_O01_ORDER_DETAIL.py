"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RDO_O01.ORDER_DETAIL
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.RXO import RXO
from ..segments.RXR import RXR

from .RDO_O01_COMPONENT import RDO_O01_COMPONENT
from .RDO_O01_OBSERVATION import RDO_O01_OBSERVATION

_NTE = NTE
_RDO_O01_COMPONENT = RDO_O01_COMPONENT
_RDO_O01_OBSERVATION = RDO_O01_OBSERVATION
_RXO = RXO
_RXR = RXR


class RDO_O01_ORDER_DETAIL(BaseModel):
    """HL7 v2 RDO_O01.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        NTE (Optional[List[NTE]]): optional
        RXR (List[RXR]): required
        COMPONENT (Optional[RDO_O01_COMPONENT]): optional
        OBSERVATION (Optional[List[RDO_O01_OBSERVATION]]): optional
    """

    RXO: _RXO = Field(
        default=...,
        title="RXO",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    RXR: List[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    COMPONENT: Optional[_RDO_O01_COMPONENT] = Field(
        default=None,
        title="COMPONENT",
        description="Optional",
    )

    OBSERVATION: Optional[List[_RDO_O01_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
