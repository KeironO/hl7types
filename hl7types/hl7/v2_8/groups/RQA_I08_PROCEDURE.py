"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RQA_I08.PROCEDURE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PR1 import PR1
from .RQA_I08_AUTHORIZATION import RQA_I08_AUTHORIZATION

_PR1 = PR1
_RQA_I08_AUTHORIZATION = RQA_I08_AUTHORIZATION


class RQA_I08_PROCEDURE(BaseModel):
    """HL7 v2 RQA_I08.PROCEDURE group.

    Attributes:
        PR1 (PR1): required
        AUTHORIZATION (Optional[RQA_I08_AUTHORIZATION]): optional
    """

    PR1: _PR1 = Field(
        default=...,
        title="PR1",
        description="Required",
    )

    AUTHORIZATION: _RQA_I08_AUTHORIZATION | None = Field(
        default=None,
        title="AUTHORIZATION",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
