"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: MFN_M17.MF_DRG
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DMI import DMI
from ..segments.MFE import MFE

_DMI = DMI
_MFE = MFE


class MFN_M17_MF_DRG(BaseModel):
    """HL7 v2 MFN_M17.MF_DRG group.

    Attributes:
        MFE (MFE): required
        DMI (DMI): required
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    DMI: _DMI = Field(
        default=...,
        title="DMI",
        description="Required",
    )

    model_config = {"populate_by_name": True}
