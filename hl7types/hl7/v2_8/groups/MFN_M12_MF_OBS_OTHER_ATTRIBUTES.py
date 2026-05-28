"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: MFN_M12.MF_OBS_OTHER_ATTRIBUTES
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OM7 import OM7
from ..segments.PRT import PRT

_OM7 = OM7
_PRT = PRT


class MFN_M12_MF_OBS_OTHER_ATTRIBUTES(BaseModel):
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

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
