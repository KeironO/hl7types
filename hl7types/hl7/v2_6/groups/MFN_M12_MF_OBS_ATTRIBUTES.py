"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: MFN_M12.MF_OBS_ATTRIBUTES
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE
from ..segments.OM1 import OM1
from ..segments.OM7 import OM7

_MFE = MFE
_OM1 = OM1
_OM7 = OM7


class MFN_M12_MF_OBS_ATTRIBUTES(HL7Model):
    """HL7 v2 MFN_M12.MF_OBS_ATTRIBUTES group.

    Attributes:
        MFE (MFE): required
        OM1 (OM1): required
        OM7 (Optional[OM7]): optional
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    OM1: _OM1 = Field(
        default=...,
        title="OM1",
        description="Required",
    )

    OM7: Optional[_OM7] = Field(
        default=None,
        title="OM7",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
