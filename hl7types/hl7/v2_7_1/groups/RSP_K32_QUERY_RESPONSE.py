"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RSP_K32.QUERY_RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NK1 import NK1
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.QRI import QRI

_NK1 = NK1
_PD1 = PD1
_PID = PID
_PV1 = PV1
_PV2 = PV2
_QRI = QRI


class RSP_K32_QUERY_RESPONSE(BaseModel):
    """HL7 v2 RSP_K32.QUERY_RESPONSE group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NK1 (Optional[List[NK1]]): optional
        PV1 (PV1): required
        PV2 (Optional[PV2]): optional
        QRI (Optional[QRI]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PD1: _PD1 | None = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    NK1: list[_NK1] | None = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    PV1: _PV1 = Field(
        default=...,
        title="PV1",
        description="Required",
    )

    PV2: _PV2 | None = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    QRI: _QRI | None = Field(
        default=None,
        title="QRI",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
