"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OMS_O01.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.RQD import RQD

from .OMS_O01_OBSERVATION import OMS_O01_OBSERVATION

_NTE = NTE
_OMS_O01_OBSERVATION = OMS_O01_OBSERVATION
_RQD = RQD


class OMS_O01_ORDER_DETAIL(HL7Model):
    """HL7 v2 OMS_O01.ORDER_DETAIL group.

    Attributes:
        RQD (RQD): RQD - requisition detail segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        OBSERVATION (Optional[List[OMS_O01_OBSERVATION]]): optional
    """

    RQD: _RQD = Field(
        title="RQD",
        description="RQD - requisition detail segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    OBSERVATION: Optional[List[_OMS_O01_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)
