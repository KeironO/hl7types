"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_K22.QUERY_RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.QRI import QRI

_PD1 = PD1
_PID = PID
_QRI = QRI


class RSP_K22_QUERY_RESPONSE(BaseModel):
    """HL7 v2 RSP_K22.QUERY_RESPONSE group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
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

    QRI: _QRI | None = Field(
        default=None,
        title="QRI",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
