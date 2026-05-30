"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: MFN_M12.MF_OBS_OTHER_ATTRIBUTES
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OM7 import OM7
from ..segments.PRT import PRT

_OM7 = OM7
_PRT = PRT


class MFN_M12_MF_OBS_OTHER_ATTRIBUTES(HL7Model):
    """HL7 v2 MFN_M12.MF_OBS_OTHER_ATTRIBUTES group.

    Attributes:
        OM7 (OM7): required
        PRT (Optional[List[PRT]]): optional
    """

    OM7: _OM7 = Field(
        default=...,
        title="OM7",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
