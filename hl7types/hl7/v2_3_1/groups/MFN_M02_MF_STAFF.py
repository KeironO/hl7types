"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MFN_M02.MF_STAFF
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.MFE import MFE
from ..segments.PRA import PRA
from ..segments.STF import STF

_MFE = MFE
_PRA = PRA
_STF = STF


class MFN_M02_MF_STAFF(BaseModel):
    """HL7 v2 MFN_M02.MF_STAFF group.

    Attributes:
        MFE (MFE): required
        STF (STF): required
        PRA (Optional[PRA]): optional
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    STF: _STF = Field(
        default=...,
        title="STF",
        description="Required",
    )

    PRA: _PRA | None = Field(
        default=None,
        title="PRA",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
