"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: MFN_M17.MF_DRG
Type: Group
"""
from __future__ import annotations

from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DMI import DMI
from ..segments.MFE import MFE

_DMI = DMI
_MFE = MFE


class MFN_M17_MF_DRG(HL7Model):
    """HL7 v2 MFN_M17.MF_DRG group.

    Attributes:
        MFE (MFE): Master File Entry, required
        DMI (DMI): DRG Master File Information, required
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Master File Entry",
    )

    DMI: _DMI = Field(
        title="DMI",
        description="DRG Master File Information",
    )

    model_config = ConfigDict(populate_by_name=True)
