"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RPA_I08.PROCEDURE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PR1 import PR1

from .RPA_I08_AUTHORIZATION_2 import RPA_I08_AUTHORIZATION_2

_PR1 = PR1
_RPA_I08_AUTHORIZATION_2 = RPA_I08_AUTHORIZATION_2


class RPA_I08_PROCEDURE(HL7Model):
    """HL7 v2 RPA_I08.PROCEDURE group.

    Attributes:
        PR1 (PR1): Procedures, required
        AUTHORIZATION_2 (Optional[RPA_I08_AUTHORIZATION_2]): optional
    """

    PR1: _PR1 = Field(
        title="PR1",
        description="Procedures",
    )

    AUTHORIZATION_2: Optional[_RPA_I08_AUTHORIZATION_2] = Field(
        default=None,
        title="AUTHORIZATION_2",
    )

    model_config = ConfigDict(populate_by_name=True)
