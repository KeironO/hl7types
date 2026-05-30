"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_K22.QUERY_RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NK1 import NK1
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.QRI import QRI

_NK1 = NK1
_PD1 = PD1
_PID = PID
_QRI = QRI


class RSP_K22_QUERY_RESPONSE(HL7Model):
    """HL7 v2 RSP_K22.QUERY_RESPONSE group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NK1 (Optional[List[NK1]]): optional
        QRI (Optional[QRI]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    QRI: Optional[_QRI] = Field(
        default=None,
        title="QRI",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
