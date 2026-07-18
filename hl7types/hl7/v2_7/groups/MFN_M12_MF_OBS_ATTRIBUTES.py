"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: MFN_M12.MF_OBS_ATTRIBUTES
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
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
        MFE (MFE): Master File Entry, required
        OM1 (OM1): General Segment, required
        OM7 (Optional[OM7]): Additional Basic Attributes, optional
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Master File Entry",
    )

    OM1: _OM1 = Field(
        title="OM1",
        description="General Segment",
    )

    OM7: Optional[_OM7] = Field(
        default=None,
        title="OM7",
        description="Additional Basic Attributes",
    )

    model_config = ConfigDict(populate_by_name=True)
