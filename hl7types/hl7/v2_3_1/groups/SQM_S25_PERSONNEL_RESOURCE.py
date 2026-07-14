"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SQM_S25.PERSONNEL_RESOURCE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AIP import AIP
from ..segments.APR import APR

_AIP = AIP
_APR = APR


class SQM_S25_PERSONNEL_RESOURCE(HL7Model):
    """HL7 v2 SQM_S25.PERSONNEL_RESOURCE group.

    Attributes:
        AIP (AIP): AIP - appointment information - personnel resource segment, required
        APR (Optional[APR]): APR - appointment preferences segment, optional
    """

    AIP: _AIP = Field(
        title="AIP",
        description=(
            "AIP - appointment information - personnel resource segment"
        ),
    )

    APR: Optional[_APR] = Field(
        default=None,
        title="APR",
        description="APR - appointment preferences segment",
    )

    model_config = {"populate_by_name": True}
