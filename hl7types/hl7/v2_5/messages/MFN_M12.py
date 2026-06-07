"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MFN_M12
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT

from ..groups.MFN_M12_MF_OBS_ATTRIBUTES import MFN_M12_MF_OBS_ATTRIBUTES

_MFI = MFI
_MFN_M12_MF_OBS_ATTRIBUTES = MFN_M12_MF_OBS_ATTRIBUTES
_MSH = MSH
_SFT = SFT


class MFN_M12(HL7Model):
    """HL7 v2 MFN_M12 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        MFI (MFI): required
        MF_OBS_ATTRIBUTES (List[MFN_M12_MF_OBS_ATTRIBUTES]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Required",
    )

    MF_OBS_ATTRIBUTES: List[_MFN_M12_MF_OBS_ATTRIBUTES] = Field(
        min_length=1,
        title="MF_OBS_ATTRIBUTES",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
