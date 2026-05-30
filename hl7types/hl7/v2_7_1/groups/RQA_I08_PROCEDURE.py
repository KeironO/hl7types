"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RQA_I08.PROCEDURE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PR1 import PR1

from .RQA_I08_AUTHORIZATION import RQA_I08_AUTHORIZATION

_PR1 = PR1
_RQA_I08_AUTHORIZATION = RQA_I08_AUTHORIZATION


class RQA_I08_PROCEDURE(HL7Model):
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

    AUTHORIZATION: Optional[_RQA_I08_AUTHORIZATION] = Field(
        default=None,
        title="AUTHORIZATION",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
