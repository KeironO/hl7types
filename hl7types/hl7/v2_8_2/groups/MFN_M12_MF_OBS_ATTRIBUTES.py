"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MFN_M12.MF_OBS_ATTRIBUTES
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.MFE import MFE
from ..segments.OM1 import OM1
from ..segments.PRT import PRT
from .MFN_M12_MF_OBS_OTHER_ATTRIBUTES import MFN_M12_MF_OBS_OTHER_ATTRIBUTES

_MFE = MFE
_MFN_M12_MF_OBS_OTHER_ATTRIBUTES = MFN_M12_MF_OBS_OTHER_ATTRIBUTES
_OM1 = OM1
_PRT = PRT


class MFN_M12_MF_OBS_ATTRIBUTES(BaseModel):
    """HL7 v2 MFN_M12.MF_OBS_ATTRIBUTES group.

    Attributes:
        MFE (MFE): required
        OM1 (OM1): required
        PRT (Optional[List[PRT]]): optional
        MF_OBS_OTHER_ATTRIBUTES (Optional[MFN_M12_MF_OBS_OTHER_ATTRIBUTES]): optional
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

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    MF_OBS_OTHER_ATTRIBUTES: _MFN_M12_MF_OBS_OTHER_ATTRIBUTES | None = Field(
        default=None,
        title="MF_OBS_OTHER_ATTRIBUTES",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
