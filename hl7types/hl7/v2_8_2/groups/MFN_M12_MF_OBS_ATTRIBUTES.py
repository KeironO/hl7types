"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MFN_M12.MF_OBS_ATTRIBUTES
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE
from ..segments.OM1 import OM1
from ..segments.PRT import PRT

from .MFN_M12_MF_OBS_OTHER_ATTRIBUTES import MFN_M12_MF_OBS_OTHER_ATTRIBUTES

_MFE = MFE
_MFN_M12_MF_OBS_OTHER_ATTRIBUTES = MFN_M12_MF_OBS_OTHER_ATTRIBUTES
_OM1 = OM1
_PRT = PRT


class MFN_M12_MF_OBS_ATTRIBUTES(HL7Model):
    """HL7 v2 MFN_M12.MF_OBS_ATTRIBUTES group.

    Attributes:
        MFE (MFE): required
        OM1 (OM1): required
        PRT (Optional[List[PRT]]): optional
        MF_OBS_OTHER_ATTRIBUTES (Optional[MFN_M12_MF_OBS_OTHER_ATTRIBUTES]): optional
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Required",
    )

    OM1: _OM1 = Field(
        title="OM1",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    MF_OBS_OTHER_ATTRIBUTES: Optional[_MFN_M12_MF_OBS_OTHER_ATTRIBUTES] = Field(
        default=None,
        title="MF_OBS_OTHER_ATTRIBUTES",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
