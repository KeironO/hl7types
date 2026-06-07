"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SSR_U04.SPECIMEN_CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SAC import SAC
from ..segments.SPM import SPM

_SAC = SAC
_SPM = SPM


class SSR_U04_SPECIMEN_CONTAINER(HL7Model):
    """HL7 v2 SSR_U04.SPECIMEN_CONTAINER group.

    Attributes:
        SAC (SAC): required
        SPM (Optional[List[SPM]]): optional
    """

    SAC: _SAC = Field(
        title="SAC",
        description="Required",
    )

    SPM: Optional[List[_SPM]] = Field(
        default=None,
        title="SPM",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
