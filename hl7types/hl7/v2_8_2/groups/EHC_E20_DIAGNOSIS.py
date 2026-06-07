"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: EHC_E20.DIAGNOSIS
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DG1 import DG1
from ..segments.NTE import NTE

_DG1 = DG1
_NTE = NTE


class EHC_E20_DIAGNOSIS(HL7Model):
    """HL7 v2 EHC_E20.DIAGNOSIS group.

    Attributes:
        DG1 (DG1): required
        NTE (Optional[List[NTE]]): optional
    """

    DG1: _DG1 = Field(
        title="DG1",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
