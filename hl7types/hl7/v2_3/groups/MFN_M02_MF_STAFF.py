"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFN_M02.MF_STAFF
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE
from ..segments.PRA import PRA
from ..segments.STF import STF

_MFE = MFE
_PRA = PRA
_STF = STF


class MFN_M02_MF_STAFF(HL7Model):
    """HL7 v2 MFN_M02.MF_STAFF group.

    Attributes:
        MFE (MFE): Master file entry segment, required
        STF (STF): Staff identification segment, required
        PRA (Optional[PRA]): Practitioner detail segment, optional
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Master file entry segment",
    )

    STF: _STF = Field(
        title="STF",
        description="Staff identification segment",
    )

    PRA: Optional[_PRA] = Field(
        default=None,
        title="PRA",
        description="Practitioner detail segment",
    )

    model_config = ConfigDict(populate_by_name=True)
