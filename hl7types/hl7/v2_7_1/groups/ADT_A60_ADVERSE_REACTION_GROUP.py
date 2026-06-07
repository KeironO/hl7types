"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ADT_A60.ADVERSE_REACTION_GROUP
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.IAM import IAM
from ..segments.IAR import IAR
from ..segments.NTE import NTE

_IAM = IAM
_IAR = IAR
_NTE = NTE


class ADT_A60_ADVERSE_REACTION_GROUP(HL7Model):
    """HL7 v2 ADT_A60.ADVERSE_REACTION_GROUP group.

    Attributes:
        IAM (IAM): required
        NTE (Optional[List[NTE]]): optional
        IAR (Optional[List[IAR]]): optional
    """

    IAM: _IAM = Field(
        title="IAM",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    IAR: Optional[List[_IAR]] = Field(
        default=None,
        title="IAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
