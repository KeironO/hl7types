"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: OMN_O01.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.RQ1 import RQ1
from ..segments.RQD import RQD

from .OMN_O01_OBSERVATION import OMN_O01_OBSERVATION

_NTE = NTE
_OMN_O01_OBSERVATION = OMN_O01_OBSERVATION
_RQ1 = RQ1
_RQD = RQD


class OMN_O01_ORDER_DETAIL(HL7Model):
    """HL7 v2 OMN_O01.ORDER_DETAIL group.

    Attributes:
        RQD (RQD): Requisition detail, required
        RQ1 (Optional[RQ1]): Requisition detail-1 segment, optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        OBSERVATION (Optional[List[OMN_O01_OBSERVATION]]): optional
    """

    RQD: _RQD = Field(
        title="RQD",
        description="Requisition detail",
    )

    RQ1: Optional[_RQ1] = Field(
        default=None,
        title="RQ1",
        description="Requisition detail-1 segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    OBSERVATION: Optional[List[_OMN_O01_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    model_config = {"populate_by_name": True}
