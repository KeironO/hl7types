"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RQA_I08.OBSERVATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from .RQA_I08_RESULTS import RQA_I08_RESULTS

_NTE = NTE
_OBR = OBR
_RQA_I08_RESULTS = RQA_I08_RESULTS


class RQA_I08_OBSERVATION(BaseModel):
    """HL7 v2 RQA_I08.OBSERVATION group.

    Attributes:
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        RESULTS (Optional[List[RQA_I08_RESULTS]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    RESULTS: list[_RQA_I08_RESULTS] | None = Field(
        default=None,
        title="RESULTS",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
