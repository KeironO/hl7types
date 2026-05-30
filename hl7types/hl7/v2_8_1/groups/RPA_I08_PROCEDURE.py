"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RPA_I08.PROCEDURE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PR1 import PR1

from .RPA_I08_AUTHORIZATION import RPA_I08_AUTHORIZATION

_PR1 = PR1
_RPA_I08_AUTHORIZATION = RPA_I08_AUTHORIZATION


class RPA_I08_PROCEDURE(HL7Model):
    """HL7 v2 RPA_I08.PROCEDURE group.

    Attributes:
        PR1 (PR1): required
        AUTHORIZATION (Optional[RPA_I08_AUTHORIZATION]): optional
    """

    PR1: _PR1 = Field(
        default=...,
        title="PR1",
        description="Required",
    )

    AUTHORIZATION: Optional[_RPA_I08_AUTHORIZATION] = Field(
        default=None,
        title="AUTHORIZATION",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
