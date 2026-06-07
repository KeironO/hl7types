"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: REF_I12.PROCEDURE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PR1 import PR1

from .REF_I12_AUTHORIZATION_CONTACT2 import REF_I12_AUTHORIZATION_CONTACT2

_PR1 = PR1
_REF_I12_AUTHORIZATION_CONTACT2 = REF_I12_AUTHORIZATION_CONTACT2


class REF_I12_PROCEDURE(HL7Model):
    """HL7 v2 REF_I12.PROCEDURE group.

    Attributes:
        PR1 (PR1): required
        AUTHORIZATION_CONTACT2 (Optional[REF_I12_AUTHORIZATION_CONTACT2]): optional
    """

    PR1: _PR1 = Field(
        title="PR1",
        description="Required",
    )

    AUTHORIZATION_CONTACT2: Optional[_REF_I12_AUTHORIZATION_CONTACT2] = Field(
        default=None,
        title="AUTHORIZATION_CONTACT2",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
