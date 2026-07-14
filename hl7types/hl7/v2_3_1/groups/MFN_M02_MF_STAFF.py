"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MFN_M02.MF_STAFF
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
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
        MFE (MFE): MFE - master file entry segment, required
        STF (STF): STF - staff identification segment, required
        PRA (Optional[PRA]): PRA - practitioner detail segment, optional
    """

    MFE: _MFE = Field(
        title="MFE",
        description="MFE - master file entry segment",
    )

    STF: _STF = Field(
        title="STF",
        description="STF - staff identification segment",
    )

    PRA: Optional[_PRA] = Field(
        default=None,
        title="PRA",
        description="PRA - practitioner detail segment",
    )

    model_config = {"populate_by_name": True}
