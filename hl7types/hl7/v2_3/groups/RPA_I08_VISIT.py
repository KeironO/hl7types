"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RPA_I08.VISIT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_NTE = NTE
_PV1 = PV1
_PV2 = PV2


class RPA_I08_VISIT(HL7Model):
    """HL7 v2 RPA_I08.VISIT group.

    Attributes:
        PV1 (PV1): Patient visit, required
        PV2 (Optional[PV2]): Patient visit - additional information, optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
    """

    PV1: _PV1 = Field(
        title="PV1",
        description="Patient visit",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Patient visit - additional information",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    model_config = ConfigDict(populate_by_name=True)
