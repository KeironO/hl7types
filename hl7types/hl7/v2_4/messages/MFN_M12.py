"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MFN_M12
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M12_MF_OBS_ATTRIBUTES import MFN_M12_MF_OBS_ATTRIBUTES

_MFI = MFI
_MFN_M12_MF_OBS_ATTRIBUTES = MFN_M12_MF_OBS_ATTRIBUTES
_MSH = MSH


class MFN_M12(HL7Model):
    """MFN/MFK - Master file notification message (S8).

    Attributes:
        MSH (MSH): Message Header, required
        MFI (MFI): Master File Identification, required
        MF_OBS_ATTRIBUTES (List[MFN_M12_MF_OBS_ATTRIBUTES]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Master File Identification",
    )

    MF_OBS_ATTRIBUTES: List[_MFN_M12_MF_OBS_ATTRIBUTES] = Field(
        min_length=1,
        title="MF_OBS_ATTRIBUTES",
    )

    model_config = ConfigDict(populate_by_name=True)
