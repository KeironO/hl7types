"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: EAR_U08.COMMAND_RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ECD import ECD
from ..segments.ECR import ECR
from ..segments.SAC import SAC

_ECD = ECD
_ECR = ECR
_SAC = SAC


class EAR_U08_COMMAND_RESPONSE(HL7Model):
    """HL7 v2 EAR_U08.COMMAND_RESPONSE group.

    Attributes:
        ECD (ECD): required
        SAC (Optional[SAC]): optional
        ECR (ECR): required
    """

    ECD: _ECD = Field(
        default=...,
        title="ECD",
        description="Required",
    )

    SAC: Optional[_SAC] = Field(
        default=None,
        title="SAC",
        description="Optional",
    )

    ECR: _ECR = Field(
        default=...,
        title="ECR",
        description="Required",
    )

    model_config = {"populate_by_name": True}
