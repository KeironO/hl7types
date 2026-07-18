"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RDO_O01.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

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


class RDO_O01_ORDER_DETAIL(HL7Model):
    """HL7 v2 RDO_O01.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): Pharmacy prescription order segment, required
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        RXR (List[RXR]): Pharmacy route segment, required
        COMPONENT (Optional[RDO_O01_COMPONENT]): optional
        OBSERVATION (Optional[List[RDO_O01_OBSERVATION]]): optional
    """

    RXO: _RXO = Field(
        title="RXO",
        description="Pharmacy prescription order segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Pharmacy route segment",
    )

    COMPONENT: Optional[_RDO_O01_COMPONENT] = Field(
        default=None,
        title="COMPONENT",
    )

    OBSERVATION: Optional[List[_RDO_O01_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)
