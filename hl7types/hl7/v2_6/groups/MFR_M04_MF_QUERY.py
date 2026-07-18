"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: MFR_M04.MF_QUERY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CDM import CDM
from ..segments.MFE import MFE
from ..segments.PRC import PRC

_CDM = CDM
_MFE = MFE
_PRC = PRC


class MFR_M04_MF_QUERY(HL7Model):
    """HL7 v2 MFR_M04.MF_QUERY group.

    Attributes:
        MFE (MFE): Master File Entry, required
        CDM (CDM): Charge Description Master, required
        PRC (Optional[List[PRC]]): Pricing, optional
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Master File Entry",
    )

    CDM: _CDM = Field(
        title="CDM",
        description="Charge Description Master",
    )

    PRC: Optional[List[_PRC]] = Field(
        default=None,
        title="PRC",
        description="Pricing",
    )

    model_config = ConfigDict(populate_by_name=True)
